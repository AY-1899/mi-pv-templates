"""
case_tracker.py
---------------
A simple command-line tool for tracking Medical Information inquiry cases.

Cases are stored in a CSV file (mi_cases.csv) that you can also open in Excel.
No database or internet connection required — everything stays on your computer.

HOW TO USE:
    Run from your terminal:
        python case_tracker.py

    You will see a menu with the following options:
        1 — Log a new case
        2 — View all open cases
        3 — View all cases (including closed)
        4 — Update an existing case
        5 — Export a summary report
        6 — Exit

CASE FIELDS:
    - Case ID         : Auto-generated (MI-0001, MI-0002, etc.)
    - Date received   : Today's date (auto-filled, can be changed)
    - Reporter type   : HCP / Patient / Caregiver / Other
    - Product         : Drug name
    - Query topic     : Brief description of the inquiry
    - Category        : Standard / 2nd-line / Off-label / AE related / Compassionate use
    - AE flag         : Yes / No / Possible
    - Status          : Open / In progress / Closed
    - Assigned to     : Your name or initials
    - Notes           : Free text for updates
    - Date closed     : Filled when status is set to Closed
"""

# --- IMPORTS ---
import csv          # For reading and writing the CSV case log
import os           # For checking if the file exists
from datetime import date   # For auto-filling today's date


# --- SETTINGS ---
# Name of the file where cases are stored
CASE_FILE = "mi_cases.csv"

# Column headers for the CSV file — these define the structure of each case record
FIELDS = [
    "Case ID",
    "Date Received",
    "Reporter Type",
    "Product",
    "Query Topic",
    "Category",
    "AE Flag",
    "Status",
    "Assigned To",
    "Notes",
    "Date Closed",
]

# Valid options for certain fields — helps keep data consistent
REPORTER_TYPES = ["HCP", "Patient", "Caregiver", "Other"]
CATEGORIES     = ["Standard", "2nd-line", "Off-label", "AE related", "Compassionate use"]
AE_FLAGS       = ["No", "Yes", "Possible"]
STATUSES       = ["Open", "In progress", "Closed"]


# --- HELPER FUNCTIONS ---

def load_cases():
    """
    Load all cases from the CSV file.
    Returns a list of dictionaries — one dictionary per case.
    If the file doesn't exist yet, returns an empty list.
    """
    if not os.path.exists(CASE_FILE):
        return []

    cases = []
    with open(CASE_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cases.append(dict(row))
    return cases


def save_cases(cases):
    """
    Save the full list of cases back to the CSV file.
    This overwrites the existing file — so we always write the complete list.
    """
    with open(CASE_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(cases)


def generate_case_id(cases):
    """
    Generate the next Case ID in sequence (MI-0001, MI-0002, etc.)
    Looks at existing cases to find the highest number used so far.
    """
    if not cases:
        return "MI-0001"

    # Extract the numeric part from each existing Case ID
    numbers = []
    for case in cases:
        case_id = case.get("Case ID", "")
        if case_id.startswith("MI-") and case_id[3:].isdigit():
            numbers.append(int(case_id[3:]))

    # Next ID is one higher than the current maximum
    next_number = max(numbers) + 1 if numbers else 1
    return f"MI-{next_number:04d}"   # Format as 4 digits with leading zeros


def ask_choice(prompt, options):
    """
    Ask the user to choose from a numbered list of options.
    Keeps asking until a valid choice is made.
    Returns the chosen option as a string.
    """
    print(f"\n{prompt}")
    for i, option in enumerate(options, start=1):
        print(f"  {i}. {option}")

    while True:
        choice = input("Enter number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print(f"  Please enter a number between 1 and {len(options)}.")


def ask_text(prompt, default=""):
    """
    Ask the user to enter free text.
    If a default value is provided, it is shown and used if the user presses Enter.
    """
    if default:
        user_input = input(f"{prompt} [{default}]: ").strip()
        return user_input if user_input else default
    else:
        return input(f"{prompt}: ").strip()


def print_divider():
    print("\n" + "-" * 60)


def print_case(case, show_notes=True):
    """
    Print a single case in a readable format.
    """
    print(f"\n  Case ID:       {case.get('Case ID', '')}")
    print(f"  Date Received: {case.get('Date Received', '')}")
    print(f"  Reporter Type: {case.get('Reporter Type', '')}")
    print(f"  Product:       {case.get('Product', '')}")
    print(f"  Query Topic:   {case.get('Query Topic', '')}")
    print(f"  Category:      {case.get('Category', '')}")
    print(f"  AE Flag:       {case.get('AE Flag', '')}")
    print(f"  Status:        {case.get('Status', '')}")
    print(f"  Assigned To:   {case.get('Assigned To', '')}")
    if show_notes:
        print(f"  Notes:         {case.get('Notes', '')}")
    if case.get("Date Closed"):
        print(f"  Date Closed:   {case.get('Date Closed', '')}")


# --- MAIN MENU ACTIONS ---

def log_new_case(cases):
    """
    Action 1: Log a new MI inquiry case.
    Prompts the user to fill in all fields, then saves the case.
    """
    print_divider()
    print("LOG NEW CASE")
    print_divider()

    today = str(date.today())   # Format: YYYY-MM-DD

    new_case = {
        "Case ID":       generate_case_id(cases),
        "Date Received": ask_text("Date received (YYYY-MM-DD)", default=today),
        "Reporter Type": ask_choice("Reporter type", REPORTER_TYPES),
        "Product":       ask_text("Product name"),
        "Query Topic":   ask_text("Query topic (brief description)"),
        "Category":      ask_choice("Category", CATEGORIES),
        "AE Flag":       ask_choice("AE flag — does this inquiry contain an adverse event?", AE_FLAGS),
        "Status":        ask_choice("Status", STATUSES),
        "Assigned To":   ask_text("Assigned to (initials or name)"),
        "Notes":         ask_text("Notes (optional)", default=""),
        "Date Closed":   "",   # Empty until the case is closed
    }

    # If AE flag is Yes or Possible, remind the user to notify PV
    if new_case["AE Flag"] in ["Yes", "Possible"]:
        print("\n  ⚠️  AE FLAG SET — ensure this case is forwarded to Pharmacovigilance.")

    cases.append(new_case)
    save_cases(cases)

    print(f"\n  ✅ Case {new_case['Case ID']} logged successfully.")
    return cases


def view_open_cases(cases):
    """
    Action 2: Display all cases with status Open or In progress.
    """
    print_divider()
    print("OPEN CASES")
    print_divider()

    open_cases = [c for c in cases if c.get("Status") in ["Open", "In progress"]]

    if not open_cases:
        print("\n  No open cases found.")
        return

    print(f"\n  {len(open_cases)} open case(s):\n")
    for case in open_cases:
        print_case(case, show_notes=False)
        print()


def view_all_cases(cases):
    """
    Action 3: Display all cases including closed ones.
    """
    print_divider()
    print("ALL CASES")
    print_divider()

    if not cases:
        print("\n  No cases logged yet.")
        return

    print(f"\n  {len(cases)} total case(s):\n")
    for case in cases:
        print_case(case, show_notes=False)
        print()


def update_case(cases):
    """
    Action 4: Update the status or notes on an existing case.
    """
    print_divider()
    print("UPDATE CASE")
    print_divider()

    case_id = ask_text("Enter Case ID to update (e.g. MI-0001)").upper()

    # Find the case with this ID
    matching = [c for c in cases if c.get("Case ID") == case_id]

    if not matching:
        print(f"\n  Case {case_id} not found.")
        return cases

    case = matching[0]
    print("\n  Current case details:")
    print_case(case)

    print("\n  What would you like to update?")
    update_field = ask_choice("Select field to update", ["Status", "Notes", "Assigned To", "AE Flag"])

    if update_field == "Status":
        new_value = ask_choice("New status", STATUSES)
        case["Status"] = new_value
        # If closing the case, record today's date
        if new_value == "Closed":
            case["Date Closed"] = str(date.today())
            print(f"\n  Case closed. Date closed set to {case['Date Closed']}.")

    elif update_field == "Notes":
        existing_notes = case.get("Notes", "")
        print(f"\n  Current notes: {existing_notes}")
        addition = ask_text("Add note (will be appended to existing notes)")
        if addition:
            if existing_notes:
                case["Notes"] = f"{existing_notes} | {str(date.today())}: {addition}"
            else:
                case["Notes"] = f"{str(date.today())}: {addition}"

    elif update_field == "Assigned To":
        case["Assigned To"] = ask_text("New assignee")

    elif update_field == "AE Flag":
        case["AE Flag"] = ask_choice("New AE flag", AE_FLAGS)
        if case["AE Flag"] in ["Yes", "Possible"]:
            print("\n  ⚠️  AE FLAG SET — ensure this case is forwarded to Pharmacovigilance.")

    save_cases(cases)
    print(f"\n  ✅ Case {case_id} updated.")
    return cases


def export_summary(cases):
    """
    Action 5: Print a summary report of case statistics.
    """
    print_divider()
    print("SUMMARY REPORT")
    print_divider()

    if not cases:
        print("\n  No cases to report on.")
        return

    total         = len(cases)
    open_count    = sum(1 for c in cases if c.get("Status") == "Open")
    inprog_count  = sum(1 for c in cases if c.get("Status") == "In progress")
    closed_count  = sum(1 for c in cases if c.get("Status") == "Closed")
    ae_count      = sum(1 for c in cases if c.get("AE Flag") in ["Yes", "Possible"])

    # Count cases by category
    category_counts = {}
    for case in cases:
        cat = case.get("Category", "Unknown")
        category_counts[cat] = category_counts.get(cat, 0) + 1

    # Count cases by product
    product_counts = {}
    for case in cases:
        prod = case.get("Product", "Unknown")
        product_counts[prod] = product_counts.get(prod, 0) + 1

    print(f"\n  Total cases logged:   {total}")
    print(f"  Open:                 {open_count}")
    print(f"  In progress:          {inprog_count}")
    print(f"  Closed:               {closed_count}")
    print(f"  AE flagged (Y/Poss):  {ae_count}")

    print("\n  Cases by category:")
    for cat, count in sorted(category_counts.items()):
        print(f"    {cat:<25} {count}")

    print("\n  Cases by product:")
    for prod, count in sorted(product_counts.items(), key=lambda x: -x[1]):
        print(f"    {prod:<25} {count}")

    print(f"\n  Case log file: {os.path.abspath(CASE_FILE)}")


# --- MAIN PROGRAM ---

def main():
    """
    Main loop: show the menu and handle user choices until they exit.
    """
    print("\n" + "="*60)
    print("MI Case Tracker")
    print("Medical Information Inquiry Log")
    print("="*60)

    # Load existing cases from file
    cases = load_cases()
    print(f"\n  {len(cases)} existing case(s) loaded from {CASE_FILE}")

    # Menu loop — keeps running until the user chooses to exit
    while True:
        print("\n" + "="*60)
        print("MENU")
        print("="*60)
        print("  1. Log a new case")
        print("  2. View open cases")
        print("  3. View all cases")
        print("  4. Update a case")
        print("  5. Summary report")
        print("  6. Exit")

        choice = input("\nEnter choice (1–6): ").strip()

        if choice == "1":
            cases = log_new_case(cases)
        elif choice == "2":
            view_open_cases(cases)
        elif choice == "3":
            view_all_cases(cases)
        elif choice == "4":
            cases = update_case(cases)
        elif choice == "5":
            export_summary(cases)
        elif choice == "6":
            print("\n  Exiting. Case log saved to", CASE_FILE)
            break
        else:
            print("\n  Invalid choice. Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
