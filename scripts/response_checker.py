"""
response_checker.py
--------------------
A quality check tool for Medical Information response drafts.

Paste a draft MI response into this tool and it will flag common
compliance and quality issues before the response goes for human review.

This is a pre-review screening tool — it does not replace medical judgement.
All flags are suggestions that require human assessment.

HOW TO USE:
    Option A — Interactive mode (paste your text when prompted):
        python response_checker.py

    Option B — Pass a text file directly:
        python response_checker.py my_response.txt

WHAT IT CHECKS:
    1. AE reporting reminder — is it present?
    2. Promotional language — flags words/phrases that may be problematic
    3. References — are sources cited?
    4. Off-label signals — flags phrases that may indicate off-label content
    5. Comparative claims — flags competitor comparisons
    6. Absolute language — flags overly certain claims
    7. Word count — flags responses that are very short or very long
    8. SmPC mention — is the prescribing information referenced?
    9. Medical Information sign-off — is the closing line present?
"""

# --- IMPORTS ---
import sys      # For reading command-line arguments (the filename if provided)
import re       # For pattern matching (finding phrases in the text)


# --- CHECK DEFINITIONS ---
# Each check is a dictionary describing what to look for and how to flag it.
# You can add your own checks by following the same pattern.

# --- 1. AE REPORTING REMINDER ---
# MI responses should always remind the HCP to report adverse events.
AE_REMINDER_PHRASES = [
    "adverse event",
    "adverse reaction",
    "yellow card",
    "report",
    "pharmacovigilance",
    "side effect",
    "undesirable effect",
]

# --- 2. PROMOTIONAL LANGUAGE ---
# These words and phrases can make a response sound like marketing material.
# Any of these appearing in a medical response should be reviewed carefully.
PROMOTIONAL_PHRASES = [
    "best in class",
    "superior",
    "unmatched",
    "leading",
    "innovative",
    "breakthrough",
    "revolutionary",
    "gold standard",
    "most effective",
    "highly effective",
    "proven to be",
    "outperforms",
    "significantly better than",
    "preferred treatment",
    "treatment of choice",
    "the only",
    "unlike any other",
    "world-class",
    "cutting-edge",
    "state-of-the-art",
]

# --- 3. REFERENCE SIGNALS ---
# A well-supported MI response should cite sources.
# These patterns suggest references are present.
REFERENCE_PATTERNS = [
    r"smpc",                        # Summary of Product Characteristics
    r"section \d",                  # e.g. "Section 4.2"
    r"\(\d{4}\)",                   # Year in brackets e.g. (2021)
    r"et al",                       # Academic citation shorthand
    r"study",                       # Reference to a study
    r"trial",                       # Reference to a clinical trial
    r"data on file",
    r"prescribing information",
    r"label",
    r"published",
]

# --- 4. OFF-LABEL SIGNALS ---
# These phrases may indicate the response contains off-label information.
# Not automatically a problem — but should be reviewed carefully.
OFF_LABEL_PHRASES = [
    "off-label",
    "unlicensed",
    "unapproved",
    "not approved",
    "not indicated",
    "outside the licence",
    "outside the label",
    "beyond the indication",
    "investigational",
    "compassionate use",
    "named patient",
    "expanded access",
]

# --- 5. COMPARATIVE CLAIMS ---
# Comparisons to other products should be scrutinised for accuracy and compliance.
COMPARATIVE_PHRASES = [
    "compared to",
    "versus",
    " vs ",
    "better than",
    "superior to",
    "more effective than",
    "lower risk than",
    "fewer side effects than",
    "outperforms",
]

# --- 6. ABSOLUTE LANGUAGE ---
# Overly certain language may not reflect the weight of evidence.
ABSOLUTE_PHRASES = [
    "always",
    "never",
    "guaranteed",
    "definitive",
    "conclusively",
    "proven",
    "without doubt",
    "certain",
    "100%",
    "eliminates",
    "completely safe",
    "no risk",
]

# --- 7. WORD COUNT THRESHOLDS ---
MIN_WORDS = 100     # Flag if response seems too short
MAX_WORDS = 1000    # Flag if response may be too long for dispatch

# --- 8. SMPC MENTION ---
SMPC_PHRASES = [
    "smpc",
    "summary of product characteristics",
    "prescribing information",
    "product information",
    "package insert",
]

# --- 9. MI CLOSING LINE SIGNALS ---
CLOSING_PHRASES = [
    "medical information",
    "if you have any further",
    "do not hesitate",
    "please contact",
    "further information",
    "happy to help",
    "kind regards",
    "yours sincerely",
]


# --- CHECKER FUNCTIONS ---

def check_ae_reminder(text):
    """
    Check whether the response includes an AE reporting reminder.
    Returns a flag if none of the AE reminder phrases are found.
    """
    text_lower = text.lower()
    found = any(phrase in text_lower for phrase in AE_REMINDER_PHRASES)

    if not found:
        return {
            "type":    "❌ MISSING",
            "check":   "AE Reporting Reminder",
            "detail":  "No adverse event reporting reminder detected. All MI responses should include an AE reporting prompt.",
            "action":  "Add standard AE reporting reminder before dispatch."
        }
    return None   # None means this check passed


def check_promotional_language(text):
    """
    Scan the response for promotional words or phrases.
    Returns a flag for each one found.
    """
    text_lower = text.lower()
    found_phrases = [p for p in PROMOTIONAL_PHRASES if p in text_lower]

    if found_phrases:
        return {
            "type":   "⚠️  WARNING",
            "check":  "Promotional Language",
            "detail": f"Potentially promotional phrase(s) found: {', '.join(found_phrases)}",
            "action": "Review for promotional tone. Ensure language is factual and balanced."
        }
    return None


def check_references(text):
    """
    Check whether the response contains any reference signals.
    Returns a flag if no reference patterns are found.
    """
    text_lower = text.lower()
    found = any(re.search(pattern, text_lower) for pattern in REFERENCE_PATTERNS)

    if not found:
        return {
            "type":   "⚠️  WARNING",
            "check":  "References / Source Citations",
            "detail": "No reference signals detected (SmPC, study citations, section numbers, etc.).",
            "action": "Verify all factual claims are referenced to approved source material."
        }
    return None


def check_off_label(text):
    """
    Flag if the response contains phrases suggesting off-label content.
    """
    text_lower = text.lower()
    found_phrases = [p for p in OFF_LABEL_PHRASES if p in text_lower]

    if found_phrases:
        return {
            "type":   "⚠️  WARNING",
            "check":  "Off-Label Content",
            "detail": f"Possible off-label content detected: {', '.join(found_phrases)}",
            "action": "Confirm this was a solicited request. Ensure Medical Affairs approval if off-label content is included."
        }
    return None


def check_comparative_claims(text):
    """
    Flag if the response makes comparisons to other products.
    """
    text_lower = text.lower()
    found_phrases = [p for p in COMPARATIVE_PHRASES if p in text_lower]

    if found_phrases:
        return {
            "type":   "⚠️  WARNING",
            "check":  "Comparative Claims",
            "detail": f"Comparative language detected: {', '.join(found_phrases)}",
            "action": "Review comparative claims carefully. Ensure they are evidence-based, balanced, and compliant with applicable code."
        }
    return None


def check_absolute_language(text):
    """
    Flag if the response uses absolute language that may overstate certainty.
    """
    text_lower = text.lower()
    found_phrases = [p for p in ABSOLUTE_PHRASES if p in text_lower]

    if found_phrases:
        return {
            "type":   "ℹ️  NOTE",
            "check":  "Absolute Language",
            "detail": f"Absolute or definitive language detected: {', '.join(found_phrases)}",
            "action": "Consider whether this language accurately reflects the evidence. May need qualifying language (e.g. 'data suggest', 'in clinical trials')."
        }
    return None


def check_word_count(text):
    """
    Check whether the response is within a reasonable word count range.
    """
    words = len(text.split())

    if words < MIN_WORDS:
        return {
            "type":   "ℹ️  NOTE",
            "check":  "Word Count",
            "detail": f"Response is short ({words} words). Minimum recommended: {MIN_WORDS} words.",
            "action": "Verify the response fully addresses the query."
        }
    elif words > MAX_WORDS:
        return {
            "type":   "ℹ️  NOTE",
            "check":  "Word Count",
            "detail": f"Response is long ({words} words). Maximum recommended: {MAX_WORDS} words.",
            "action": "Consider whether the response can be condensed without losing key information."
        }
    return None


def check_smpc_reference(text):
    """
    Check whether the SmPC or prescribing information is referenced.
    """
    text_lower = text.lower()
    found = any(phrase in text_lower for phrase in SMPC_PHRASES)

    if not found:
        return {
            "type":   "ℹ️  NOTE",
            "check":  "SmPC / Prescribing Information",
            "detail": "No reference to the SmPC or prescribing information detected.",
            "action": "Consider whether the SmPC should be referenced or enclosed with this response."
        }
    return None


def check_closing_line(text):
    """
    Check whether the response ends with a standard MI closing line.
    """
    text_lower = text.lower()
    found = any(phrase in text_lower for phrase in CLOSING_PHRASES)

    if not found:
        return {
            "type":   "ℹ️  NOTE",
            "check":  "MI Closing Line",
            "detail": "No standard closing line detected.",
            "action": "Ensure response ends with an offer to provide further information and Medical Information sign-off."
        }
    return None


# --- RUN ALL CHECKS ---

def run_all_checks(text):
    """
    Run every check and collect the results.
    Returns a list of flags (issues found) and a pass count.
    """
    # List of all check functions to run
    checks = [
        check_ae_reminder,
        check_promotional_language,
        check_references,
        check_off_label,
        check_comparative_claims,
        check_absolute_language,
        check_word_count,
        check_smpc_reference,
        check_closing_line,
    ]

    flags = []
    passed = 0

    for check_function in checks:
        result = check_function(text)
        if result:
            flags.append(result)
        else:
            passed += 1

    return flags, passed


# --- OUTPUT ---

def print_report(flags, passed, word_count):
    """
    Print the QC report in a readable format.
    """
    total_checks = passed + len(flags)

    print("\n" + "="*65)
    print("MI RESPONSE QUALITY CHECK — REPORT")
    print("="*65)
    print(f"\nWord count:    {word_count}")
    print(f"Checks run:    {total_checks}")
    print(f"Passed:        {passed}")
    print(f"Flags raised:  {len(flags)}")

    if not flags:
        print("\n✅ No issues detected. Proceed to human review before dispatch.")
        return

    # Separate flags by severity for clearer output
    errors   = [f for f in flags if "MISSING" in f["type"]]
    warnings = [f for f in flags if "WARNING" in f["type"]]
    notes    = [f for f in flags if "NOTE" in f["type"]]

    if errors:
        print("\n--- ISSUES REQUIRING ATTENTION ---")
        for flag in errors:
            print(f"\n{flag['type']}: {flag['check']}")
            print(f"  Detail: {flag['detail']}")
            print(f"  Action: {flag['action']}")

    if warnings:
        print("\n--- WARNINGS ---")
        for flag in warnings:
            print(f"\n{flag['type']}: {flag['check']}")
            print(f"  Detail: {flag['detail']}")
            print(f"  Action: {flag['action']}")

    if notes:
        print("\n--- NOTES ---")
        for flag in notes:
            print(f"\n{flag['type']}: {flag['check']}")
            print(f"  Detail: {flag['detail']}")
            print(f"  Action: {flag['action']}")

    print("\n" + "="*65)
    print("⚠️  This tool flags potential issues only.")
    print("All responses require human review by a qualified")
    print("Medical Information professional before dispatch.")
    print("="*65)


# --- MAIN PROGRAM ---

def main():
    """
    Main entry point.
    Accepts text from a file argument, or prompts the user to paste text.
    """
    print("\n" + "="*65)
    print("MI Response Quality Checker")
    print("Pre-review screening tool — not a substitute for human review")
    print("="*65)

    text = ""

    # Check if a filename was passed as a command-line argument
    # e.g. python response_checker.py my_response.txt
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        if not os.path.exists(filename):
            print(f"\nError: File '{filename}' not found.")
            sys.exit(1)
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
        print(f"\nLoaded response from file: {filename}")

    else:
        # Interactive mode — ask the user to paste the response
        print("\nPaste your MI response draft below.")
        print("When finished, press Enter twice (or Ctrl+D on Mac/Linux, Ctrl+Z on Windows).")
        print("-" * 65)

        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass

        text = "\n".join(lines).strip()

    if not text:
        print("\nNo text provided. Exiting.")
        sys.exit(0)

    # Count words
    word_count = len(text.split())

    # Run all checks
    flags, passed = run_all_checks(text)

    # Print the report
    print_report(flags, passed, word_count)


if __name__ == "__main__":
    main()
