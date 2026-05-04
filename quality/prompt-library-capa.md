# Prompt Library: CAPA & Deviation Management

> **Version:** 1.0  
> **Use case:** AI-assisted Quality Management — CAPA investigation, deviation reporting, and quality event documentation in GxP-regulated pharmaceutical environments  
> **Compatible with:** Claude, GPT-4, or any instruction-following LLM  
> **Variables:** All placeholders are in `[SQUARE BRACKETS]` — replace before use

---

## How to Use This Library

Each prompt is self-contained. Copy the prompt block, fill in the `[VARIABLES]`, and paste into your AI tool of choice. Prompts are designed to produce **draft outputs only** — all content must be reviewed by a qualified Quality professional before use in any GxP-regulated system.

> ⚠️ These prompts do not replace validated Quality Management System (QMS) procedures, company SOPs, or regulatory requirements. AI-generated drafts must be reviewed, approved, and handled in accordance with applicable GxP regulations (GMP, GCP, GLP) and company procedures before entry into any regulated system. All records must maintain data integrity in accordance with ALCOA+ principles.

---

## Prompt Index

| # | Prompt Name | Use When |
|---|---|---|
| 1 | [Deviation Intake Summariser](#1-deviation-intake-summariser) | Structuring an initial deviation report for QMS entry |
| 2 | [Root Cause Analysis — 5-Why](#2-root-cause-analysis--5-why) | Conducting a structured 5-Why root cause investigation |
| 3 | [Root Cause Analysis — Ishikawa](#3-root-cause-analysis--ishikawa) | Building a cause-and-effect diagram for complex deviations |
| 4 | [CAPA Plan Drafter](#4-capa-plan-drafter) | Drafting corrective and preventive actions from a confirmed root cause |
| 5 | [CAPA Effectiveness Check](#5-capa-effectiveness-check) | Assessing whether a closed CAPA has been effective |
| 6 | [Deviation Risk Classifier](#6-deviation-risk-classifier) | Classifying deviation severity (critical / major / minor) |
| 7 | [CAPA Closure Report Generator](#7-capa-closure-report-generator) | Drafting the closure summary for a completed CAPA |
| 8 | [Regulatory Impact Assessor](#8-regulatory-impact-assessor) | Assessing whether a deviation has regulatory reporting implications |

---

## 1. Deviation Intake Summariser

**Use when:** A quality event has been identified and needs to be structured for initial entry into the QMS before investigation begins.

```
You are a pharmaceutical Quality Assurance specialist. A quality event has been reported and needs to be structured for QMS entry.

TASK: Produce a structured intake summary for the quality event described below.

---
EVENT DESCRIPTION (verbatim as reported):
[PASTE VERBATIM DESCRIPTION OF THE QUALITY EVENT HERE]

PRODUCT / MATERIAL: [PRODUCT NAME / BATCH NUMBER / MATERIAL CODE — or "Not applicable"]
PROCESS / AREA: [MANUFACTURING STEP / DEPARTMENT / SITE — e.g. "Filling line 3 / Sterile Manufacturing / Copenhagen"]
DATE OF OCCURRENCE: [DD-MMM-YYYY]
DATE DETECTED: [DD-MMM-YYYY]
REPORTED BY: [ROLE / DEPARTMENT — do not include personal names]
MARKET: [If product is released / intended for release — specify market(s)]
---

Produce a structured intake summary with the following sections:

1. EVENT SUMMARY
   Describe the quality event in 2–3 clear sentences. What happened, where, and when?

2. EVENT TYPE
   Classify as one of:
   - Manufacturing deviation
   - Laboratory deviation (OOS / OOT)
   - Documentation error
   - Equipment failure
   - Environmental excursion
   - Supply chain / material issue
   - Change control deviation
   - Other — specify

3. PRELIMINARY SEVERITY
   Classify as: Critical / Major / Minor
   Provide brief rationale. (Full risk assessment should follow in a separate step.)

4. PRODUCT / PATIENT IMPACT ASSESSMENT
   - Is released product potentially affected? Yes / No / Under investigation
   - Is there a potential patient safety impact? Yes / No / Cannot determine at this stage
   - Is a market action (recall, field alert) potentially indicated? Yes / No / Too early to determine

5. IMMEDIATE CONTAINMENT ACTIONS REQUIRED
   List any immediate actions that should be taken before investigation begins (e.g. quarantine batch, stop line, notify QP).

6. INVESTIGATION SCOPE
   What processes, systems, batches, or time periods should be included in the investigation?

7. MISSING INFORMATION
   What additional information is needed to complete the intake record?

Be factual. Do not speculate on root cause at this stage — that is for the investigation phase.
```

---

## 2. Root Cause Analysis — 5-Why

**Use when:** A deviation has been confirmed and you are conducting a structured root cause investigation using the 5-Why methodology.

```
You are a pharmaceutical Quality Assurance specialist conducting a root cause investigation.

TASK: Conduct a structured 5-Why root cause analysis for the quality event described below.

---
DEVIATION SUMMARY:
[PASTE THE CONFIRMED DEVIATION DESCRIPTION — what happened, where, when]

PRODUCT / PROCESS AFFECTED: [PRODUCT NAME / PROCESS STEP / EQUIPMENT]
DEVIATION TYPE: [e.g. OOS result / Documentation error / Equipment failure / Environmental excursion]
SEVERITY: [Critical / Major / Minor]

KNOWN FACTS (paste any investigation findings gathered so far):
[PASTE INVESTIGATION DATA, LAB RESULTS, OPERATOR STATEMENTS, EQUIPMENT LOGS — or write "None yet"]
---

Conduct a 5-Why analysis structured as follows:

PROBLEM STATEMENT
State the confirmed problem in one clear sentence (what happened, not why).

5-WHY CHAIN

Why 1: [Why did the problem occur?]
→ Answer: [Based on known facts — flag if assumption]

Why 2: [Why did that happen?]
→ Answer: [Based on known facts — flag if assumption]

Why 3: [Why did that happen?]
→ Answer: [Based on known facts — flag if assumption]

Why 4: [Why did that happen?]
→ Answer: [Based on known facts — flag if assumption]

Why 5: [Why did that happen?]
→ Answer: [Root cause — the systemic or process failure that, if fixed, prevents recurrence]

ROOT CAUSE STATEMENT
State the confirmed or suspected root cause in one clear sentence.

ROOT CAUSE CATEGORY
Classify the root cause as one of:
- Human error (training / procedure / workload)
- Procedural / SOP deficiency
- Equipment / instrument failure
- Environmental / facility
- Material / supplier
- Design / process deficiency
- Management / oversight system

CONTRIBUTING FACTORS
List any secondary factors that contributed to the event but are not the primary root cause.

DATA GAPS
List any points in the 5-Why chain where you had to make assumptions due to missing information. Flag these for follow-up investigation.

CAPA TRIGGER
Based on this root cause, what type of CAPA is indicated?
- Corrective action only (fix the specific failure)
- Preventive action only (prevent occurrence elsewhere)
- Both corrective and preventive actions required
```

---

## 3. Root Cause Analysis — Ishikawa

**Use when:** A deviation is complex or multifactorial and you need a broader cause-and-effect analysis across multiple categories before identifying the root cause.

```
You are a pharmaceutical Quality Assurance specialist conducting a root cause investigation using the Ishikawa (fishbone) methodology.

TASK: Build a structured Ishikawa cause-and-effect analysis for the quality event below.

---
PROBLEM STATEMENT:
[ONE SENTENCE: what is the confirmed quality problem — e.g. "OOS result for assay on Batch X of Product Y"]

PRODUCT / PROCESS: [PRODUCT / MANUFACTURING STEP / EQUIPMENT]
INVESTIGATION FINDINGS TO DATE:
[PASTE ANY KNOWN FACTS, LAB DATA, OBSERVATIONS, OPERATOR INPUT — or "None yet"]
---

Analyse potential causes across each of the six standard Ishikawa categories. For each category, list all plausible contributing causes based on the investigation findings and general knowledge of pharmaceutical manufacturing. Flag each cause as:
- CONFIRMED — supported by investigation data
- POSSIBLE — plausible but not yet confirmed; requires follow-up
- UNLIKELY — considered and ruled out; state reason

CATEGORY ANALYSIS:

1. MAN (People)
   Potential causes related to: operator error, training gaps, fatigue, communication failure, staffing.

2. MACHINE (Equipment)
   Potential causes related to: equipment malfunction, calibration, maintenance, instrument qualification.

3. METHOD (Process / Procedure)
   Potential causes related to: SOP deficiency, unclear instructions, process design, validation gaps.

4. MATERIAL
   Potential causes related to: raw material quality, supplier change, incorrect material, storage conditions.

5. MEASUREMENT
   Potential causes related to: analytical method, sample preparation, laboratory equipment, analyst technique.

6. ENVIRONMENT
   Potential causes related to: temperature, humidity, contamination, facility conditions, HVAC.

MOST LIKELY ROOT CAUSE(S)
Based on the analysis above, identify the 1–3 most likely root causes. Rank by likelihood and state the evidence basis for each.

RECOMMENDED NEXT INVESTIGATION STEPS
What specific actions, tests, or data reviews are needed to confirm the root cause?
```

---

## 4. CAPA Plan Drafter

**Use when:** The root cause has been confirmed and you need to draft a structured CAPA plan with specific, measurable actions.

```
You are a pharmaceutical Quality Assurance specialist drafting a CAPA plan.

TASK: Draft a structured CAPA plan based on the confirmed root cause below.

---
DEVIATION REFERENCE: [QMS REFERENCE NUMBER]
PRODUCT / PROCESS AFFECTED: [PRODUCT / PROCESS / SITE]
CONFIRMED ROOT CAUSE: [STATE THE CONFIRMED ROOT CAUSE IN ONE SENTENCE]
ROOT CAUSE CATEGORY: [Human error / Procedural / Equipment / Environmental / Material / Process / Management system]
DEVIATION SEVERITY: [Critical / Major / Minor]

CONTRIBUTING FACTORS (if any):
[LIST ANY SECONDARY CONTRIBUTING FACTORS IDENTIFIED IN THE INVESTIGATION]

RECURRENCE RISK: [High / Medium / Low — with brief rationale]
---

Draft a CAPA plan with the following structure:

CORRECTIVE ACTIONS
(Actions to address the specific failure that occurred — fix the immediate problem)

For each corrective action provide:
- Action description: [What will be done]
- Owner: [Role / department — not individual names]
- Target completion date: [Relative — e.g. "30 days from CAPA approval"]
- Success criterion: [How will completion be verified?]
- Evidence of completion: [What documented evidence will demonstrate the action is done?]

PREVENTIVE ACTIONS
(Actions to prevent recurrence of this failure — and to prevent similar failures elsewhere in the system)

For each preventive action provide:
- Action description: [What will be done]
- Scope: [Which products / processes / sites does this apply to?]
- Owner: [Role / department]
- Target completion date: [Relative]
- Success criterion: [How will completion be verified?]
- Evidence of completion: [Documented evidence required]

EFFECTIVENESS CRITERIA
Define how the effectiveness of this CAPA will be measured after implementation:
- What metric will be monitored?
- What is the target / threshold for success?
- Over what time period will effectiveness be assessed?
- Who is responsible for the effectiveness check?

CAPA RISK SUMMARY
- If CAPA actions are not completed on time, what is the risk?
- Are any interim control measures required while CAPA is in progress?

Flag any action where the proposed solution may require change control, revalidation, regulatory notification, or additional QA review.
```

---

## 5. CAPA Effectiveness Check

**Use when:** CAPA actions have been completed and you need to formally assess whether the CAPA has been effective before closure.

```
You are a pharmaceutical Quality Assurance specialist conducting a CAPA effectiveness review.

TASK: Assess whether the CAPA described below has been effective and whether it is ready for closure.

---
CAPA REFERENCE: [QMS REFERENCE NUMBER]
ORIGINAL DEVIATION: [BRIEF DESCRIPTION OF THE ORIGINAL QUALITY EVENT]
CONFIRMED ROOT CAUSE: [ROOT CAUSE AS DOCUMENTED IN THE CAPA]
CAPA ACTIONS IMPLEMENTED: [LIST EACH ACTION THAT WAS COMPLETED]
EFFECTIVENESS CRITERIA (as defined at CAPA approval): [PASTE THE AGREED EFFECTIVENESS CRITERIA]

POST-IMPLEMENTATION DATA:
[PASTE MONITORING DATA, AUDIT RESULTS, RECURRENCE CHECKS, LAB RESULTS, TRAINING RECORDS — whatever evidence has been gathered to assess effectiveness]

TIME PERIOD MONITORED: [e.g. "3 months post-implementation"]
---

Assess CAPA effectiveness against the following criteria:

1. ACTIONS COMPLETED
   Were all planned CAPA actions completed as described?
   - Yes — all actions completed and evidenced
   - Partial — list any outstanding or incomplete actions
   - No — state what was not completed and why

2. ROOT CAUSE ADDRESSED
   Does the evidence indicate that the confirmed root cause has been eliminated or adequately controlled?
   - Yes — state the evidence
   - Partially — explain what remains unresolved
   - No — explain why the root cause persists

3. RECURRENCE CHECK
   Has the same or similar deviation recurred since CAPA implementation?
   - No recurrence detected
   - Possible recurrence — describe
   - Recurrence confirmed — CAPA ineffective; escalate

4. EFFECTIVENESS CRITERIA MET
   For each effectiveness criterion defined at CAPA approval, state whether it has been met:
   | Criterion | Target | Actual | Met? |
   |---|---|---|---|
   | [criterion 1] | [target] | [actual result] | Yes / No |

5. SYSTEMIC REVIEW
   Is there any evidence that the root cause exists in other products, processes, or sites not covered by this CAPA?

6. OVERALL EFFECTIVENESS RECOMMENDATION:
   - ✅ EFFECTIVE — CAPA ready for closure. State rationale.
   - ⚠️ PARTIALLY EFFECTIVE — additional actions required before closure. List actions.
   - ❌ INEFFECTIVE — CAPA must be reopened or replaced. State reason and recommended next steps.
```

---

## 6. Deviation Risk Classifier

**Use when:** A deviation has been identified and you need a structured risk assessment to determine severity classification before investigation prioritisation.

```
You are a pharmaceutical Quality Assurance risk assessor.

TASK: Classify the severity of the quality deviation described below and assess its potential impact on product quality, patient safety, and regulatory compliance.

---
DEVIATION DESCRIPTION:
[DESCRIBE THE QUALITY EVENT — what happened, where, when, what product/process was affected]

PRODUCT: [PRODUCT NAME / INN / BATCH NUMBER]
DOSAGE FORM: [e.g. oral solid / sterile injectable / biological]
STAGE: [In-process / Finished product / Released product / Distributed product]
MARKET(S) AFFECTED: [If released — which markets]
GxP CONTEXT: [GMP / GCP / GLP / GDP — specify]
---

Assess the deviation across the following risk dimensions:

1. PATIENT SAFETY IMPACT
   Could this deviation result in harm to a patient?
   - Direct safety risk (e.g. wrong dose, contamination, mislabelling): High / Medium / Low / None
   - Indirect safety risk (e.g. efficacy impact, stability): High / Medium / Low / None
   - Rationale:

2. PRODUCT QUALITY IMPACT
   Does this deviation affect product quality attributes?
   - Identity, strength, purity, or quality affected: Yes / Possibly / No
   - Batch disposition implication: Reject / Quarantine / Conditional release / No impact
   - Rationale:

3. REGULATORY / COMPLIANCE IMPACT
   Does this deviation represent a GxP compliance failure?
   - Regulatory reporting potentially required: Yes / Possibly / No
   - Inspection finding risk (could this be cited in an audit): High / Medium / Low
   - Breach of marketing authorisation: Yes / Possibly / No
   - Rationale:

4. SCOPE
   - Single batch / single event: Yes / No
   - Systemic / recurring issue: Yes / Possibly / No
   - Other sites or products potentially affected: Yes / Possibly / No

OVERALL SEVERITY CLASSIFICATION:

| Classification | Criteria |
|---|---|
| **CRITICAL** | Direct patient safety risk OR potential regulatory action OR product recall indication |
| **MAJOR** | Indirect patient safety risk OR significant GxP compliance failure OR batch rejection likely |
| **MINOR** | No patient safety impact, no regulatory implication, contained quality impact |

ASSIGNED CLASSIFICATION: [Critical / Major / Minor]
RATIONALE: [2–3 sentences justifying the classification]

ESCALATION REQUIRED:
- Qualified Person (QP) notification: Yes / No
- Regulatory authority notification: Yes / No / Under assessment
- Senior management notification: Yes / No
- Market action assessment required: Yes / No
```

---

## 7. CAPA Closure Report Generator

**Use when:** A CAPA has been assessed as effective and you need to draft the formal closure summary for QMS entry and audit trail.

```
You are a pharmaceutical Quality Assurance specialist drafting a CAPA closure report.

TASK: Draft a formal CAPA closure summary for QMS entry.

---
CAPA REFERENCE: [QMS REFERENCE NUMBER]
ORIGINAL DEVIATION REFERENCE: [LINKED DEVIATION REFERENCE]
PRODUCT / PROCESS: [PRODUCT NAME / PROCESS / SITE]
CAPA OPENED: [DD-MMM-YYYY]
CAPA CLOSED: [DD-MMM-YYYY]
ROOT CAUSE (confirmed): [STATE ROOT CAUSE]
EFFECTIVENESS ASSESSMENT OUTCOME: [Effective / Partially effective — with date of assessment]

ACTIONS COMPLETED:
[LIST EACH CORRECTIVE AND PREVENTIVE ACTION WITH COMPLETION DATE AND EVIDENCE REFERENCE]

EFFECTIVENESS EVIDENCE:
[SUMMARISE THE DATA OR OBSERVATIONS USED TO CONFIRM EFFECTIVENESS]
---

Draft a CAPA closure report with the following sections:

1. EXECUTIVE SUMMARY
   3–5 sentences summarising: what the original deviation was, what root cause was identified, what actions were taken, and how effectiveness was confirmed.

2. ORIGINAL DEVIATION SUMMARY
   Brief factual description of the quality event that triggered this CAPA.

3. ROOT CAUSE
   Confirmed root cause as documented. Include root cause category.

4. CORRECTIVE ACTIONS — SUMMARY OF COMPLETION
   For each corrective action: description, completion date, evidence reference, outcome.

5. PREVENTIVE ACTIONS — SUMMARY OF COMPLETION
   For each preventive action: description, scope, completion date, evidence reference, outcome.

6. EFFECTIVENESS ASSESSMENT SUMMARY
   How was effectiveness assessed? What data was reviewed? What criteria were met?

7. LESSONS LEARNED
   What broader lessons does this CAPA offer for the quality system? Are there implications for other processes, products, or sites?

8. CLOSURE STATEMENT
   Formal statement confirming: CAPA actions are complete, effectiveness has been confirmed, the CAPA is approved for closure, and the quality record is complete for audit purposes.

Tone: formal, factual, audit-ready. Written for a QA reviewer or regulatory inspector who may read this record during an inspection.
```

---

## 8. Regulatory Impact Assessor

**Use when:** A deviation has occurred and you need to assess whether it triggers regulatory reporting obligations — e.g. Field Safety Corrective Action, Urgent Safety Restriction, or national competent authority notification.

```
You are a pharmaceutical Regulatory Affairs and Quality specialist assessing the regulatory reporting implications of a quality deviation.

TASK: Assess whether the deviation described below triggers any regulatory reporting or market action obligations.

---
DEVIATION DESCRIPTION:
[DESCRIBE THE QUALITY EVENT IN DETAIL]

PRODUCT: [PRODUCT NAME / INN]
DOSAGE FORM: [e.g. sterile injectable / oral tablet / biological]
AUTHORISATION STATUS: [Marketed / Investigational / Named patient]
MARKETS WHERE PRODUCT IS DISTRIBUTED: [List all relevant markets]
BATCH(ES) AFFECTED: [Batch numbers / quantities / distribution status]
SEVERITY CLASSIFICATION: [Critical / Major / Minor]
PATIENT SAFETY ASSESSMENT: [Summary of any patient safety impact]
---

Assess the following regulatory dimensions:

1. PRODUCT RECALL / WITHDRAWAL
   Does this deviation indicate that a product recall or market withdrawal may be required?
   - Recall potentially indicated: Yes / No / Under assessment
   - If yes: likely classification (Class I / II / III under EMA/MHRA framework)
   - Regulatory basis:

2. FIELD SAFETY CORRECTIVE ACTION (FSCA)
   For combination products or devices: is an FSCA required?
   - Applicable: Yes / No / Not applicable (non-device product)

3. COMPETENT AUTHORITY NOTIFICATION
   Which regulatory authorities may need to be notified, and under what obligation?

   | Market | Authority | Obligation | Indicative Timeline |
   |---|---|---|---|
   | EU | EMA / National CA | [e.g. Quality defect report] | [e.g. 15 days] |
   | UK | MHRA | [e.g. Yellow card / Quality defect] | [e.g. As soon as practicable] |
   | [Other] | [Authority] | [Obligation] | [Timeline] |

4. MARKETING AUTHORISATION IMPACT
   Does this deviation represent a breach of the approved Marketing Authorisation (MA)?
   - MA breach: Yes / Possibly / No
   - Variation required: Yes / No / Under assessment
   - Rationale:

5. GCP / CLINICAL TRIAL IMPLICATIONS
   If the affected product is used in clinical trials:
   - Suspected Unexpected Serious Adverse Reaction (SUSAR) assessment required: Yes / No / Not applicable
   - Protocol deviation notification to sponsor / ethics committee: Yes / No / Not applicable

6. OVERALL REGULATORY ACTION RECOMMENDATION:
   - No regulatory reporting required at this time — state rationale and monitoring plan
   - Regulatory notification required — list authorities, obligations, and timelines
   - Urgent action required — escalate immediately to Regulatory Affairs and QP

⚠️ This assessment is a preliminary screening tool only. All regulatory reporting decisions must be confirmed by a qualified Regulatory Affairs professional and/or Qualified Person with knowledge of current applicable regulations and the specific product's authorisation status.
```

---

## Usage Notes

### Variable Reference

| Variable | Description |
|---|---|
| `[QMS REFERENCE NUMBER]` | Internal deviation or CAPA reference from your Quality Management System |
| `[PRODUCT NAME / BATCH NUMBER]` | Product and batch details — use internal codes, not patient data |
| `[PROCESS / AREA]` | Manufacturing step, department, or site where the event occurred |
| `[ROOT CAUSE]` | Confirmed root cause from investigation — one clear sentence |
| `[SEVERITY]` | Critical / Major / Minor — based on risk assessment |

### Recommended Workflow Sequence

```
Quality event identified
        ↓
Prompt 6 — Risk Classifier (severity and escalation)
        ↓
Prompt 1 — Deviation Intake Summariser (QMS entry)
        ↓
Prompt 8 — Regulatory Impact Assessor (reporting obligations)
        ↓
Prompt 2 or 3 — Root Cause Analysis (5-Why or Ishikawa)
        ↓
Prompt 4 — CAPA Plan Drafter
        ↓
[Implementation period]
        ↓
Prompt 5 — CAPA Effectiveness Check
        ↓
Prompt 7 — CAPA Closure Report
```

### GxP Compliance Reminders

- **Data integrity** — all QMS entries must comply with ALCOA+ principles (Attributable, Legible, Contemporaneous, Original, Accurate — plus Complete, Consistent, Enduring, Available). AI-generated drafts must be reviewed and approved by a qualified individual before entry into any validated system.
- **Audit trail** — document that AI assistance was used in drafting, and that the output was reviewed and approved by a named qualified individual.
- **Prompt 8 (Regulatory Impact)** — always requires confirmation by a qualified Regulatory Affairs professional or QP. Never act on AI output alone for regulatory reporting decisions.
- **Change control** — CAPA actions that modify a validated process, equipment, or document may require a formal change control record. Flag these during CAPA planning.

---

*Prompt library maintained for reference and AI-assisted workflow development. All AI outputs require review and approval by a qualified Quality professional through the applicable QMS process before use in any GxP-regulated operation.*
