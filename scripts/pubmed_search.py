"""
pubmed_search.py
----------------
Search PubMed for clinical literature and save results to a CSV file.

This script uses the NCBI E-utilities API — it is free and does not require
an account or API key for basic use (up to 3 requests per second).

HOW TO USE:
    1. Install the required library (one-time setup):
           pip install requests

    2. Run the script from your terminal:
           python pubmed_search.py

    3. When prompted, enter your search terms — e.g.:
           osimertinib renal impairment
           palbociclib hepatic dosing
           EGFR mutation NSCLC first line

    4. Results are printed to the screen and saved to a CSV file
       named after your search term (e.g. osimertinib_renal_impairment.csv)

WHAT YOU GET:
    - PubMed ID (PMID) — use this to look up the full article on pubmed.ncbi.nlm.nih.gov
    - Title
    - Authors
    - Journal name
    - Publication year
    - Abstract (if available)
"""

# --- IMPORTS ---
# 'requests' lets us make calls to the PubMed API over the internet
import requests

# 'csv' lets us write results to a spreadsheet-style file
import csv

# 'time' lets us pause between API calls so we don't overwhelm the server
import time

# 'os' lets us work with file paths
import os


# --- SETTINGS ---
# You can change these values to adjust how the script behaves

# How many results to return per search (max 10,000 — keep it reasonable)
MAX_RESULTS = 20

# Where to save the output CSV files (current folder by default)
OUTPUT_FOLDER = "."

# PubMed API base URLs — these are fixed and should not need changing
ESEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EFETCH_URL  = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


# --- FUNCTIONS ---

def search_pubmed(search_term, max_results=MAX_RESULTS):
    """
    Step 1: Search PubMed for a term and get back a list of article IDs (PMIDs).

    PubMed works in two steps:
      - First, you search and get a list of IDs
      - Then, you fetch the details for those IDs

    This function does the first step.
    """

    print(f"\nSearching PubMed for: '{search_term}'...")

    # Build the search request
    # 'params' is a dictionary of options we send to the API
    params = {
        "db": "pubmed",          # Which database to search
        "term": search_term,     # The search query
        "retmax": max_results,   # Maximum number of results to return
        "retmode": "json",       # Return results in JSON format (easier to read in Python)
        "sort": "relevance",     # Sort by relevance (most relevant first)
    }

    # Send the search request and get the response
    response = requests.get(ESEARCH_URL, params=params)

    # Check if the request was successful (status code 200 = OK)
    if response.status_code != 200:
        print(f"Error: Could not reach PubMed. Status code: {response.status_code}")
        return []

    # Convert the response from JSON format into a Python dictionary
    data = response.json()

    # Extract the list of article IDs from the response
    id_list = data["esearchresult"]["idlist"]

    print(f"Found {len(id_list)} articles.")
    return id_list


def fetch_article_details(pmid_list):
    """
    Step 2: Fetch the full details (title, authors, abstract, etc.)
    for a list of PubMed IDs (PMIDs).
    """

    if not pmid_list:
        print("No articles to fetch.")
        return []

    print(f"Fetching details for {len(pmid_list)} articles...")

    # Join the list of IDs into a comma-separated string (required by the API)
    ids_string = ",".join(pmid_list)

    # Build the fetch request
    params = {
        "db": "pubmed",
        "id": ids_string,
        "retmode": "xml",   # Fetch in XML format — gives us the most detail
        "rettype": "abstract",
    }

    # Pause for 0.5 seconds — good practice to avoid overwhelming the API
    time.sleep(0.5)

    # Send the request
    response = requests.get(EFETCH_URL, params=params)

    if response.status_code != 200:
        print(f"Error: Could not fetch article details. Status code: {response.status_code}")
        return []

    # Parse the XML response using Python's built-in XML parser
    # We import it here because it's only needed in this function
    import xml.etree.ElementTree as ET
    root = ET.fromstring(response.content)

    # --- Extract data from each article ---
    articles = []

    for article in root.findall(".//PubmedArticle"):

        # Helper function: safely extract text from an XML element
        # Returns empty string if the element doesn't exist
        def get_text(element, path):
            node = element.find(path)
            return node.text.strip() if node is not None and node.text else ""

        # Extract PMID
        pmid = get_text(article, ".//PMID")

        # Extract title
        title = get_text(article, ".//ArticleTitle")

        # Extract journal name
        journal = get_text(article, ".//Journal/Title")

        # Extract publication year
        year = get_text(article, ".//PubDate/Year")
        if not year:
            # Some articles use MedlineDate instead of Year
            year = get_text(article, ".//PubDate/MedlineDate")

        # Extract authors — loop through all author entries and combine them
        authors = []
        for author in article.findall(".//Author"):
            last  = get_text(author, "LastName")
            first = get_text(author, "ForeName")
            if last:
                authors.append(f"{last} {first}".strip())

        # Format author list: show first 3 authors, then "et al." if there are more
        if len(authors) > 3:
            author_string = ", ".join(authors[:3]) + " et al."
        else:
            author_string = ", ".join(authors)

        # Extract abstract text
        # Abstracts can have multiple sections (e.g. Background, Methods, Results)
        abstract_parts = []
        for abstract_text in article.findall(".//AbstractText"):
            label = abstract_text.get("Label", "")  # e.g. "BACKGROUND", "RESULTS"
            text  = abstract_text.text or ""
            if label:
                abstract_parts.append(f"{label}: {text}")
            else:
                abstract_parts.append(text)

        abstract = " ".join(abstract_parts).strip()

        # Build the PubMed URL for this article
        pubmed_url = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""

        # Add this article's data to our list
        articles.append({
            "PMID":     pmid,
            "Title":    title,
            "Authors":  author_string,
            "Journal":  journal,
            "Year":     year,
            "Abstract": abstract,
            "URL":      pubmed_url,
        })

    return articles


def save_to_csv(articles, search_term):
    """
    Save the list of articles to a CSV file.
    The filename is based on the search term (spaces replaced with underscores).
    """

    if not articles:
        print("No articles to save.")
        return

    # Create a safe filename from the search term
    # Replace spaces with underscores, remove special characters
    safe_term = "".join(c if c.isalnum() or c == "_" else "_" for c in search_term.replace(" ", "_"))
    filename = os.path.join(OUTPUT_FOLDER, f"pubmed_{safe_term}.csv")

    # Write the articles to CSV
    # 'newline=""' prevents extra blank lines on Windows
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:

        # Define the column headers
        fieldnames = ["PMID", "Title", "Authors", "Journal", "Year", "Abstract", "URL"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()          # Write the header row
        writer.writerows(articles)    # Write all article rows

    print(f"\nResults saved to: {filename}")
    return filename


def print_summary(articles):
    """
    Print a readable summary of results to the screen.
    """
    print("\n" + "="*70)
    print(f"SEARCH RESULTS ({len(articles)} articles)")
    print("="*70)

    for i, article in enumerate(articles, start=1):
        print(f"\n[{i}] {article['Title']}")
        print(f"    Authors:  {article['Authors']}")
        print(f"    Journal:  {article['Journal']} ({article['Year']})")
        print(f"    PMID:     {article['PMID']}")
        print(f"    URL:      {article['URL']}")

        # Show a short preview of the abstract (first 200 characters)
        if article["Abstract"]:
            preview = article["Abstract"][:200]
            if len(article["Abstract"]) > 200:
                preview += "..."
            print(f"    Abstract: {preview}")


# --- MAIN PROGRAM ---
# This block runs when you execute the script directly

if __name__ == "__main__":

    print("="*70)
    print("PubMed Literature Search Tool")
    print("For Medical Information use — results require human review")
    print("="*70)

    # Ask the user to enter a search term
    search_term = input("\nEnter search terms (e.g. 'osimertinib renal impairment'): ").strip()

    # Don't proceed if the user entered nothing
    if not search_term:
        print("No search term entered. Exiting.")
        exit()

    # Ask how many results to return
    max_input = input(f"How many results? (press Enter for default {MAX_RESULTS}): ").strip()
    if max_input.isdigit():
        max_results = int(max_input)
    else:
        max_results = MAX_RESULTS

    # Step 1: Search PubMed and get PMIDs
    pmid_list = search_pubmed(search_term, max_results)

    if not pmid_list:
        print("No results found. Try different search terms.")
        exit()

    # Step 2: Fetch article details
    articles = fetch_article_details(pmid_list)

    if not articles:
        print("Could not retrieve article details.")
        exit()

    # Step 3: Display results on screen
    print_summary(articles)

    # Step 4: Save to CSV
    save_to_csv(articles, search_term)

    print("\nDone. Open the CSV file in Excel to review your results.")
