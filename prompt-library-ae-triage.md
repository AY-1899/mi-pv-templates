# Prompt Library: Adverse Event Triage

> **Version:** 1.0  
> **Use case:** AI-assisted identification, triage, and initial processing of adverse events within Medical Information and pharmacovigilance workflows  
> **Compatible with:** Claude, GPT-4, or any instruction-following LLM  
> **Variables:** All placeholders are in `[SQUARE BRACKETS]` — replace before use

---

## How to Use This Library

These prompts support AE identification and triage at the point of MI inquiry receipt, and initial case structuring before handoff to a pharmacovigilance team. They are not a substitute for validated PV database entry or regulatory submission workflows.

> ⚠️ All AI outputs must be reviewed by a qualified pharmacovigilance or Medical Information professional. These prompts do not replace company SOPs, ICH E2A/E2B requirements, or GVP Module VI obligations. Never submit AI-generated narratives or assessments to a regulatory authority without full human review and validation.

---

## Prompt Index

| # | Prompt Name | Use When |
|---|---|---|
| 1 | [AE Signal Detector](#1-ae-signal-detector) | Screening any inbound text (email, call notes, inquiry) for AE content |
| 2 | [Minimum Criteria Checker](#2-minimum-criteria-checker) | Determining whether a report meets the four minimum validity criteria |
| 3 | [AE Data Extractor](#3-ae-data-extractor) | Pulling structured AE data fields from unstructured source text |
| 4 | [Seriousness Assessor](#4-seriousness-assessor) | Assessing whether an event meets ICH E2A seriousness criteria |
| 5 | [MedDRA Coding Suggester](#5-meddra-coding-suggester) | Suggesting MedDRA PT/LLT coding from verbatim event description |
| 6 | [Safety Narrative Drafter](#6-safety-narrative-drafter) | Drafting an ICSR narrative from structured case data |
| 7 | [Follow-up Letter Drafter](#7-follow-up-letter-drafter) | Writing a follow-up request to obtain missing case information |
| 8 | [PV Handoff Summary](#8-pv-handoff-summary) | Preparing a structured handoff note from MI to PV team |

---

## 1. AE Signal Detector

**Use when:** Screening inbound communications — emails, call notes, inquiry transcripts, social media reports — for potential adverse event content before routing.

```
You are a pharmacovigilance specialist screening inbound communications for potential adverse events.

TASK: Review the following text and determine whether it contains any potential adverse event, product quality complaint, or safety signal.

---
SOURCE TEXT:
[PASTE FULL TEXT OF EMAIL / CALL NOTE / INQUIRY / MESSAGE HERE]

PRODUCT(S) OF INTEREST: [PRODUCT NAME(S) — or write "any medicinal product"]
SOURCE TYPE: [HCP email / Patient call / Web form / Social media / Literature / Other]
MARKET: [UK / IE / DK / other]
---

Assess the text and provide:

1. AE PRESENT: Yes / No / Possible
   - If Yes or Possible: quote the exact phrase(s) that indicate an adverse event

2. PRODUCT QUALITY COMPLAINT (PQC) PRESENT: Yes / No / Possible
   - If Yes or Possible: quote the relevant phrase(s)

3. MINIMUM CRITERIA CHECK (preliminary):
   - Identifiable reporter? Yes / No / Unclear
   - Identifiable patient? Yes / No / Unclear
   - Suspect product named? Yes / No / Unclear
   - Adverse event described? Yes / No / Unclear

4. RECOMMENDED ACTION:
   - No AE content — process as standard MI inquiry
   - Possible AE — flag for pharmacovigilance review; do not close without PV assessment
   - Confirmed AE — route to PV immediately; document receipt date as Day 0

5. URGENCY: Routine / Priority / Urgent
   - Mark Urgent if: death, life-threatening event, hospitalisation, congenital anomaly, or pregnancy exposure is mentioned

Do not speculate beyond what the text states. If uncertain, err on the side of flagging.
```

---

## 2. Minimum Criteria Checker

**Use when:** A potential AE has been identified and you need to formally assess whether it meets the four ICH minimum validity criteria before opening a case.

```
You are a pharmacovigilance case intake specialist.

TASK: Assess whether the following report meets the four ICH minimum criteria required to constitute a valid Individual Case Safety Report (ICSR).

---
REPORT TEXT:
[PASTE SOURCE TEXT OR CASE NOTES HERE]

PRODUCT: [PRODUCT NAME]
DATE RECEIVED: [DD-MMM-YYYY]
SOURCE: [Spontaneous / Literature / Clinical trial / Regulatory authority / Other]
---

Assess each criterion and provide evidence from the text:

1. IDENTIFIABLE REPORTER
   - Met? Yes / No / Partially
   - Evidence: [quote or note what identifier is present/absent]
   - If absent: what information would satisfy this criterion?

2. IDENTIFIABLE PATIENT
   - Met? Yes / No / Partially
   - Evidence: [quote or note what identifier is present/absent]
   - If absent: what information would satisfy this criterion?

3. SUSPECT MEDICINAL PRODUCT
   - Met? Yes / No / Partially
   - Evidence: [product name or description found in text]
   - If absent: what information would satisfy this criterion?

4. ADVERSE EVENT OR OUTCOME
   - Met? Yes / No / Partially
   - Evidence: [quote the adverse event description]
   - If absent: what information would satisfy this criterion?

OVERALL VALIDITY:
- All four criteria met → Valid ICSR — open case, start reporting clock (Day 0 = [DATE RECEIVED])
- One or more criteria missing → Invalid at this time — initiate follow-up for missing information; document attempt
- Cannot determine → Flag for pharmacovigilance medical review

FOLLOW-UP REQUIRED: Yes / No
If yes, list the specific missing information to request.
```

---

## 3. AE Data Extractor

**Use when:** You have a valid AE report in unstructured text form (email, call transcript, letter) and need to extract all relevant data fields for database entry.

```
You are a pharmacovigilance data entry specialist.

TASK: Extract all relevant adverse event data fields from the source text below. Present findings in a structured format ready for safety database entry.

---
SOURCE TEXT:
[PASTE FULL SOURCE DOCUMENT — email, call notes, letter, etc.]

PRODUCT: [PRODUCT NAME]
DATE OF RECEIPT: [DD-MMM-YYYY]
CASE REFERENCE: [IF ALREADY ASSIGNED]
---

Extract and present the following fields. Write "Not reported" if information is absent — do not infer or assume.

REPORTER INFORMATION
- Reporter type:
- Reporter name / identifier:
- Reporter profession:
- Country:
- Contact details (for follow-up):
- Reporter's causality assessment (if stated):

PATIENT INFORMATION
- Patient identifier (initials / reference):
- Age or date of birth:
- Sex:
- Weight / height (if provided):
- Relevant medical history:
- Concomitant medications (name, dose, indication):

SUSPECT PRODUCT
- Product name:
- Indication for use:
- Dose:
- Route of administration:
- Frequency:
- Start date:
- Stop date:
- Batch / lot number:
- Action taken (none / withdrawn / dose reduced / dose increased / unknown):
- Dechallenge result (if applicable):
- Rechallenge result (if applicable):

ADVERSE EVENT(S)
- Event description (verbatim — as reported):
- Onset date:
- Duration / end date:
- Severity (mild / moderate / severe — if stated):
- Outcome at time of report:
  (recovered / recovering / not recovered / recovered with sequelae / fatal / unknown)
- If fatal: date of death / cause of death / autopsy:

RELEVANT TESTS & INVESTIGATIONS
- Lab values (with dates and units):
- Diagnostic procedures:
- Other relevant clinical information:

PREGNANCY (if applicable)
- Pregnancy status:
- Gestational age at exposure:
- Pregnancy outcome (if known):

MISSING INFORMATION — FLAG FOR FOLLOW-UP:
List any fields above marked "Not reported" that are clinically significant and should be pursued via follow-up.
```

---

## 4. Seriousness Assessor

**Use when:** You have an extracted AE and need a structured assessment of whether it meets ICH E2A seriousness criteria.

```
You are a pharmacovigilance medical assessor.

TASK: Assess whether the adverse event described below meets ICH E2A seriousness criteria.

---
ADVERSE EVENT DESCRIPTION:
[PASTE VERBATIM EVENT DESCRIPTION AND ANY RELEVANT CLINICAL CONTEXT]

PRODUCT: [PRODUCT NAME]
PATIENT: [AGE / SEX / RELEVANT COMORBIDITIES IF KNOWN]
OUTCOME: [AS REPORTED — e.g. recovered / ongoing / fatal / unknown]
---

Assess each ICH E2A seriousness criterion:

1. RESULTS IN DEATH
   - Met? Yes / No / Unknown
   - Evidence or rationale:

2. LIFE-THREATENING
   (Patient was at immediate risk of death at the time of the event — not hypothetically if more severe)
   - Met? Yes / No / Unknown / Requires medical review
   - Evidence or rationale:

3. REQUIRES OR PROLONGS INPATIENT HOSPITALISATION
   - Met? Yes / No / Unknown
   - Evidence or rationale:

4. RESULTS IN PERSISTENT OR SIGNIFICANT DISABILITY / INCAPACITY
   - Met? Yes / No / Unknown
   - Evidence or rationale:

5. CONGENITAL ANOMALY / BIRTH DEFECT
   - Met? Yes / No / Unknown
   - Evidence or rationale:

6. IMPORTANT MEDICAL EVENT
   (May jeopardise the patient or require medical/surgical intervention to prevent one of the above)
   - Met? Yes / No / Possible / Requires medical review
   - Evidence or rationale:

OVERALL SERIOUSNESS ASSESSMENT:
- SERIOUS — criterion/criteria met: [list which]
- NON-SERIOUS — no criteria met
- REQUIRES MEDICAL REVIEW — insufficient information or clinical ambiguity

REPORTING IMPLICATION (indicative — verify against local SOP):
- Serious unexpected: 15-day expedited report (7-day if fatal/life-threatening)
- Serious expected: 15-day expedited report
- Non-serious: periodic reporting (PSUR/PBRER)

Note: "Important medical event" always requires pharmacovigilance physician sign-off. Flag for medical review if this is the only criterion being considered.
```

---

## 5. MedDRA Coding Suggester

**Use when:** You need suggested MedDRA Preferred Term (PT) coding for a verbatim adverse event description. Always verify suggestions in the current MedDRA browser before entering into a safety database.

```
You are a pharmacovigilance coding specialist with knowledge of MedDRA terminology.

TASK: Suggest appropriate MedDRA coding for the following verbatim adverse event description.

---
VERBATIM TERM (as reported):
[PASTE EXACT WORDS USED BY THE REPORTER]

CLINICAL CONTEXT (if available):
[PASTE ANY ADDITIONAL CLINICAL DETAIL THAT HELPS CLARIFY THE EVENT — e.g. diagnosis, test results, clinical notes]

PRODUCT: [PRODUCT NAME]
THERAPEUTIC AREA: [e.g. oncology / cardiovascular / immunology]
---

Provide the following:

1. INTERPRETATION
   What clinical event does this verbatim term most likely represent?
   Note any ambiguity in the reported term.

2. SUGGESTED MedDRA CODING
   Present in hierarchy order:

   | Level | Term | Notes |
   |---|---|---|
   | LLT (Lowest Level Term) | [suggested LLT] | Closest to verbatim |
   | PT (Preferred Term) | [suggested PT] | Recommended for coding |
   | HLT (High Level Term) | [suggested HLT] | |
   | HLGT (High Level Group Term) | [suggested HLGT] | |
   | SOC (System Organ Class) | [suggested SOC] | Primary SOC |

3. ALTERNATIVE PTs TO CONSIDER
   If the verbatim term is ambiguous, list 2–3 alternative PTs and explain when each would apply.

4. CODING GUIDANCE
   - Is additional clinical information needed to code this accurately? (Yes / No — specify)
   - Should this be coded as a single PT or multiple PTs? (explain if multiple)

⚠️ IMPORTANT: These are suggestions only. All MedDRA coding must be verified in the current MedDRA version using the official MedDRA browser (meddra.org) before entry into a safety database. MedDRA is a licensed terminology — do not rely on AI outputs as a substitute for the official browser.
```

---

## 6. Safety Narrative Drafter

**Use when:** You have completed data extraction (Prompt 3) and seriousness assessment (Prompt 4) and are ready to draft the ICSR narrative.

```
You are a pharmacovigilance narrative writer. Your task is to draft a factual, chronological ICSR narrative from the structured case data provided.

TASK: Write a case narrative suitable for inclusion in an Individual Case Safety Report (ICSR).

---
CASE DATA:
[PASTE THE STRUCTURED OUTPUT FROM THE AE DATA EXTRACTOR (PROMPT 3) HERE]

CASE REFERENCE: [REFERENCE NUMBER]
DATE OF RECEIPT: [DD-MMM-YYYY]
SERIOUSNESS: [Serious / Non-serious]
SERIOUSNESS CRITERIA MET: [e.g. Hospitalisation / Life-threatening / None]
EXPECTEDNESS: [Expected (labelled) / Unexpected (unlabelled)]
REPORTER CAUSALITY: [Related / Not related / Unknown / Not assessed]
COMPANY CAUSALITY: [To be completed by medical assessor]
---

Write a narrative that:

STRUCTURE (follow this order):
1. Case identifier, source, and report date
2. Patient demographics and relevant medical history
3. Concomitant medications and relevant conditions
4. Suspect product — indication, dose, route, start date
5. Adverse event onset — date, description, clinical course
6. Management and treatment of the event
7. Relevant investigations and results (with values, units, dates)
8. Outcome
9. Dechallenge / rechallenge information (if applicable)
10. Reporter's causality assessment
11. Missing information (explicitly stated)

STYLE REQUIREMENTS:
- Past tense, third person throughout
- Factual only — do not speculate or interpret beyond what is reported
- Dates in DD-MMM-YYYY format
- Abbreviations defined on first use
- Missing data explicitly flagged as "not reported" or "unknown at time of report"
- No promotional language
- No copy-paste of verbatim reporter language as the narrative body (verbatim belongs in the verbatim field)
- Self-contained — readable without reference to individual data fields

TARGET LENGTH: [SHORT (150–250 words) / STANDARD (250–400 words) / DETAILED (400–600 words for complex cases)]

After the narrative, add a section:
MISSING INFORMATION — LIST any data gaps that should be pursued via follow-up, with specific questions to ask the reporter.
```

---

## 7. Follow-up Letter Drafter

**Use when:** A case is missing key information and you need to contact the reporter to obtain it.

```
You are a Medical Information / pharmacovigilance specialist drafting a follow-up request to a healthcare professional or patient reporter.

TASK: Write a follow-up letter / email requesting missing adverse event information.

---
CASE REFERENCE: [INTERNAL CASE NUMBER]
ORIGINAL REPORT DATE: [DD-MMM-YYYY]
REPORTER TYPE: [HCP — specify profession / Patient / Caregiver]
REPORTER NAME: [DR / MR / MS SURNAME — or "Healthcare Professional" if unknown]
PRODUCT: [PRODUCT NAME]
ADVERSE EVENT: [BRIEF DESCRIPTION — e.g. "elevated liver enzymes"]

MISSING INFORMATION TO REQUEST:
[LIST EACH MISSING DATA POINT — e.g.:
- Patient date of birth or age
- Onset date of the adverse event
- Batch number of the product
- Outcome / current status
- Relevant lab values]

MARKET: [UK / IE / DK / other]
---

Write a follow-up communication that:
- Thanks the reporter for their original report
- References the case by product and event (not by internal case number in external communications)
- Clearly and specifically lists each piece of missing information requested
- Explains briefly why this information helps with the safety assessment (without being technical or burdensome)
- Provides contact details for the reporter to respond: [PHONE / EMAIL / BOTH]
- Includes a standard AE reporting reminder
- Is professional, concise, and non-promotional

Format: [Email / Formal letter]
Tone: Professional and appreciative — reporters are not obligated to provide follow-up
Length: 200–250 words maximum
```

---

## 8. PV Handoff Summary

**Use when:** An AE has been identified during an MI inquiry and needs to be formally handed off to the pharmacovigilance team with all relevant information.

```
You are a Medical Information specialist preparing a pharmacovigilance handoff summary.

TASK: Write a structured handoff note transferring an adverse event case from the MI team to the PV team.

---
MI CASE REFERENCE: [MI CRM REFERENCE]
DATE AE IDENTIFIED: [DD-MMM-YYYY] — this is Day 0 for the PV reporting clock
IDENTIFIED BY: [Name / Role]
SOURCE OF REPORT: [Phone call / Email / Web form / Other]

ORIGINAL MI INQUIRY TOPIC: [Brief description of what the HCP/patient originally called about]

AE IDENTIFIED:
- Product: [PRODUCT NAME]
- Event description (verbatim): [EXACT WORDS USED BY REPORTER]
- Reporter type: [HCP / Patient / Caregiver]
- Reporter name / identifier: [If available]
- Patient identifier: [Initials / age / sex if provided]
- Any other AE data collected: [PASTE ANY DETAILS CAPTURED DURING THE MI INTERACTION]

PRELIMINARY SERIOUSNESS: [Serious / Non-serious / Unknown — based on information available]
PRELIMINARY CAUSALITY (reporter): [Related / Not related / Not assessed / Not stated]

MI ACTIONS TAKEN:
[e.g. AE acknowledged to reporter / follow-up contact details obtained / reporter directed to report via Yellow Card / standard AE reminder provided]

OUTSTANDING INFORMATION: [List anything not captured that PV may wish to follow up on]
---

Write a handoff summary that:
- Clearly states Day 0 and the reporting clock start
- Summarises the AE in 3–5 sentences
- Lists all data captured vs data outstanding
- States the preliminary seriousness flag
- Confirms what the reporter was told during the MI interaction
- Notes any specific PV actions recommended (e.g. follow-up call, batch number retrieval)

Keep to 300 words or fewer. Written for a PV colleague who has no prior context on this case.
```

---

## Usage Notes

### Variable Reference

| Variable | Description |
|---|---|
| `[PASTE SOURCE TEXT]` | Raw unstructured text — email, call notes, transcript |
| `[PRODUCT NAME]` | Brand name or INN |
| `[DATE RECEIVED]` | Date the report was first received — this is Day 0 |
| `[CASE REFERENCE]` | Internal safety database or CRM reference number |
| `[MARKET]` | Country — affects regulatory reporting obligations |

### Recommended Workflow Sequence

For a new AE identified during an MI inquiry, run prompts in this order:

```
Prompt 1 — Screen for AE content
    └── AE identified
            ↓
Prompt 2 — Check minimum validity criteria
    └── Valid case
            ↓
Prompt 3 — Extract structured data fields
            ↓
Prompt 4 — Assess seriousness
            ↓
Prompt 5 — Suggest MedDRA coding (verify in MedDRA browser)
            ↓
Prompt 6 — Draft ICSR narrative
            ↓
Prompt 7 — Draft follow-up letter (if data gaps)
Prompt 8 — PV handoff summary (if AE identified in MI context)
```

### Key Reminders

- **Day 0** is always the date the report was first received — not the date of data entry or narrative completion
- **Prompt 5 (MedDRA)** outputs are suggestions only — always verify in the licensed MedDRA browser
- **Prompt 6 (Narrative)** should be run after Prompt 3 — the narrative quality depends entirely on the completeness of the data extraction
- **Never close an MI case** where a potential AE has been identified without confirming PV handoff is complete

---

*Prompt library maintained for reference and AI-assisted workflow development. All AI outputs require human review by a qualified pharmacovigilance professional before use in live operations.*
