# Prompt Library: 2nd-Line HCP Query Handling

> **Version:** 1.0  
> **Use case:** AI-assisted Medical Information — 2nd-line HCP response drafting  
> **Compatible with:** Claude, GPT-4, or any instruction-following LLM  
> **Variables:** All placeholders are in `[SQUARE BRACKETS]` — replace before use

---

## How to Use This Library

Each prompt is self-contained. Copy the prompt block, fill in the `[VARIABLES]`, and paste into your AI tool of choice. Prompts are designed to produce **draft outputs only** — all responses must be reviewed by a qualified Medical Information professional before dispatch.

> ⚠️ These prompts do not replace medical judgement, company SOPs, or approved Standard Response Documents. AI-generated drafts must be reviewed against current SmPC and approved content before use.

---

## Prompt Index

| # | Prompt Name | Use When |
|---|---|---|
| 1 | [Query Intake Summariser](#1-query-intake-summariser) | Structuring an inbound HCP query for routing |
| 2 | [2nd-Line Response Drafter](#2-2nd-line-response-drafter) | Drafting a response to a complex clinical question |
| 3 | [Literature Summary for MI Response](#3-literature-summary-for-mi-response) | Summarising a clinical paper for inclusion in a response |
| 4 | [Gap Identifier — SRD vs Query](#4-gap-identifier--srd-vs-query) | Checking whether an existing SRD fully covers a query |
| 5 | [Cover Letter Generator](#5-cover-letter-generator) | Writing the cover letter to accompany an SRD or response pack |
| 6 | [Response QC Reviewer](#6-response-qc-reviewer) | Reviewing a drafted response for compliance and accuracy risks |
| 7 | [Escalation Summary](#7-escalation-summary) | Preparing a concise handoff note when escalating to Medical Affairs |

---

## 1. Query Intake Summariser

**Use when:** An HCP query has arrived via phone, email, or web form and needs to be structured before routing or response.

```
You are a Medical Information specialist. A healthcare professional has submitted the following inquiry:

---
INQUIRY TEXT:
[PASTE VERBATIM INQUIRY HERE]
---

PRODUCT: [PRODUCT NAME]
REPORTER TYPE: [HCP — specify: physician / pharmacist / nurse / other]
MARKET: [UK / IE / DK / other]
CHANNEL: [Phone / Email / Web form]

Please analyse this inquiry and produce a structured intake summary with the following sections:

1. CORE QUESTION: What is the HCP specifically asking? (1–2 sentences, plain language)
2. CLINICAL CONTEXT: What patient/clinical context has the HCP provided?
3. INQUIRY TYPE: Classify as one of — Standard (SRD likely available) / Complex 2nd-line / Off-label / Compassionate use / Safety/AE related
4. AE FLAG: Does the inquiry contain any mention of an adverse event, unexpected symptom, or patient harm? (Yes / No / Possible — explain)
5. SUGGESTED ROUTING: 1st line (SRD response) / 2nd line SME / Medical Affairs / Compassionate use team
6. MISSING INFORMATION: What additional detail, if any, would improve the response?

Be concise. Do not speculate beyond what the inquiry states.
```

---

## 2. 2nd-Line Response Drafter

**Use when:** A query has been escalated to 2nd line and you are drafting a clinical response, drawing on provided source material.

```
You are a 2nd-line Medical Information specialist with expertise in [THERAPEUTIC AREA — e.g. oncology / cardiovascular / immunology].

TASK: Draft a 2nd-line Medical Information response to the HCP query below, using only the source material provided.

---
HCP QUERY:
[PASTE QUERY TEXT]

PRODUCT: [PRODUCT NAME]
INDICATION: [APPROVED INDICATION]
MARKET: [UK / IE / DK / other]
HCP TYPE: [Physician / Oncologist / Pharmacist / Nurse — specify]

SOURCE MATERIAL (use only this — do not draw on general training knowledge):
[PASTE RELEVANT SMPC SECTIONS / STUDY SUMMARIES / INTERNAL DATA POINTS HERE]
---

Draft a response that:
- Directly addresses the specific question asked
- Uses scientific language appropriate for [HCP TYPE]
- Cites each factual claim to the source material provided (e.g. "SmPC Section 4.2", "Study X, N=...")
- Is factual and balanced — includes relevant safety information where applicable
- Does not contain promotional language or unsolicited off-label information
- Flags any aspect of the query that cannot be answered from the source material provided

FORMAT:
- Opening: acknowledge the query topic (1 sentence)
- Body: structured response with subheadings if covering multiple aspects
- Closing: standard MI closing line + AE reporting reminder
- References: list all sources cited

Target length: [SHORT (200–300 words) / STANDARD (400–600 words) / DETAILED (600–900 words)]
```

---

## 3. Literature Summary for MI Response

**Use when:** You have retrieved a clinical paper relevant to a query and need a structured summary suitable for inclusion in a 2nd-line response.

```
You are a Medical Information specialist preparing a literature summary for inclusion in an HCP response.

TASK: Summarise the following clinical paper in a format suitable for a Medical Information response.

---
PAPER TEXT / ABSTRACT:
[PASTE FULL ABSTRACT OR PAPER EXCERPT HERE]

QUERY CONTEXT: The HCP has asked about [BRIEF DESCRIPTION OF QUERY — e.g. "dosing of [product] in patients with hepatic impairment"]
PRODUCT OF INTEREST: [PRODUCT NAME]
---

Produce a structured summary with the following sections:

1. STUDY OVERVIEW
   - Study type (RCT / observational / retrospective / case series / other)
   - Population (N, key inclusion/exclusion criteria)
   - Intervention and comparator (if applicable)
   - Primary endpoint

2. KEY FINDINGS RELEVANT TO THE QUERY
   - State findings directly relevant to the HCP's question
   - Include specific data points (%, hazard ratios, p-values, CIs) where available
   - Note statistical significance and clinical relevance

3. SAFETY / TOLERABILITY DATA
   - Relevant AEs from this study (if applicable to the query)

4. LIMITATIONS
   - Study design limitations relevant to interpreting the findings

5. RELEVANCE TO QUERY
   - One paragraph: how does this paper address (or partially address) the HCP's question?
   - Note any gaps — e.g. the study population differs from the HCP's patient

Do not interpret beyond what the paper states. Flag any findings that appear to conflict with the current SmPC.
```

---

## 4. Gap Identifier — SRD vs Query

**Use when:** You have an SRD and want to quickly assess whether it fully covers an inbound HCP query, or whether a 2nd-line response is needed.

```
You are a Medical Information quality reviewer.

TASK: Compare the HCP query below against the available Standard Response Document (SRD) content and identify any gaps.

---
HCP QUERY:
[PASTE QUERY TEXT]

SRD CONTENT (paste the relevant sections or key messages):
[PASTE SRD CONTENT HERE]
---

Produce a gap analysis with the following sections:

1. QUERY COMPONENTS: Break the HCP query into its distinct sub-questions (bullet list)

2. COVERAGE ASSESSMENT: For each sub-question, state:
   - COVERED — the SRD directly addresses this
   - PARTIALLY COVERED — the SRD touches on this but lacks specificity
   - NOT COVERED — the SRD does not address this

3. GAPS REQUIRING 2ND-LINE INPUT: List any sub-questions that cannot be answered using the SRD alone

4. RECOMMENDED ACTION:
   - Can this be answered at 1st line using the SRD? (Yes / No / Partially)
   - If No or Partially: what additional source material or SME input is needed?

5. SRD UPDATE FLAG: Does this query suggest the SRD should be updated to cover a common clinical question? (Yes / No — brief rationale)
```

---

## 5. Cover Letter Generator

**Use when:** Drafting the cover letter to accompany an SRD or response pack being sent to an HCP.

```
You are a Medical Information specialist writing a cover letter to accompany a response to an HCP inquiry.

DETAILS:
- HCP name: [DR / PROF / MR / MS — SURNAME] (use "Dear Healthcare Professional" if name unknown)
- HCP type: [Physician / Oncologist / Pharmacist / Nurse / Other]
- Query topic: [BRIEF DESCRIPTION — e.g. "use of [product] in patients with renal impairment"]
- Product: [PRODUCT NAME]
- Market: [UK / IE / DK / other]
- Response type being enclosed: [SRD only / SRD + SmPC / SRD + literature / Full 2nd-line response]
- Any specific context to acknowledge: [e.g. "query related to a specific patient case" / "follow-up to a previous inquiry" / none]

Write a professional cover letter that:
- Opens by thanking the HCP for their inquiry and referencing the query topic
- Briefly introduces what is enclosed and why it addresses their question
- Includes a standard AE reporting reminder
- Closes with an offer to provide further information if needed
- Signs off as "Medical Information" (do not use individual names)

Tone: professional, concise, non-promotional
Length: 150–200 words maximum
Market-specific disclaimer to include: [PASTE LOCAL DISCLAIMER IF APPLICABLE — e.g. ABPI code statement / or write "standard UK MI disclaimer"]
```

---

## 6. Response QC Reviewer

**Use when:** You have a drafted MI response (AI-generated or human-written) and want a structured compliance and quality check before dispatch.

```
You are a Medical Information quality reviewer. Your role is to critically review a drafted HCP response for compliance, accuracy risks, and completeness — not to rewrite it.

---
DRAFTED RESPONSE:
[PASTE FULL DRAFTED RESPONSE HERE]

PRODUCT: [PRODUCT NAME]
MARKET: [UK / IE / DK / other]
HCP TYPE: [Physician / Pharmacist / Nurse / Other]
SOURCE MATERIAL USED: [LIST SOURCES — e.g. SmPC v[X], Study X, SRD reference]
---

Review the draft against the following criteria and produce a structured QC report:

1. QUERY ADDRESSED: Does the response directly answer the question that was asked? (Yes / Partially / No — explain)

2. FACTUAL ACCURACY RISKS: Are there any claims that appear unsupported by the source material listed, or that conflict with standard SmPC content? List each with the specific statement flagged.

3. PROMOTIONAL LANGUAGE CHECK: Does the response contain superlatives, comparative claims, or language that could be considered promotional? (Yes — flag specific phrases / No)

4. OFF-LABEL CONTENT: Does the response contain any off-label information? (Yes — flag / No). If yes, was this solicited?

5. SAFETY INFORMATION: Is relevant safety information included where appropriate? Is the AE reporting reminder present?

6. TONE & AUDIENCE: Is the language appropriate for the HCP type specified?

7. REFERENCES: Are all factual claims referenced? Are references complete and traceable?

8. OVERALL RECOMMENDATION:
   - ✅ Approved to send as written
   - ⚠️ Minor revisions required (list)
   - ❌ Significant revision required before dispatch (list reasons)
```

---

## 7. Escalation Summary

**Use when:** A query needs to be handed off to a Medical Affairs colleague, 2nd-line SME, or another team, and you need to write a concise escalation note.

```
You are a 1st-line Medical Information specialist preparing a handoff note to escalate a complex query.

TASK: Write a concise escalation summary for the following case.

---
ORIGINAL QUERY:
[PASTE QUERY TEXT]

PRODUCT: [PRODUCT NAME]
REPORTER: [HCP TYPE AND MARKET]
DATE RECEIVED: [DATE]
CASE REFERENCE: [CRM CASE NUMBER]

REASON FOR ESCALATION: [e.g. Off-label question / requires clinical interpretation / SRD does not cover / compassionate use element / safety concern]

ACTIONS ALREADY TAKEN:
[e.g. SRD searched — not available / SmPC reviewed — does not address / 1st-line response attempted but insufficient]

ESCALATING TO: [2nd-line SME / Medical Affairs / Compassionate Use team / other]
---

Write an escalation summary that includes:

1. CASE SUMMARY: What did the HCP ask? (2–3 sentences)
2. CLINICAL CONTEXT: What patient/clinical context was provided?
3. WHY ESCALATING: Clear statement of why this cannot be handled at 1st line
4. ACTIONS TAKEN TO DATE: What has already been done?
5. SPECIFIC QUESTION FOR ESCALATION RECIPIENT: What exactly does the 2nd-line reviewer need to address?
6. URGENCY: Routine / Priority / Urgent (with brief rationale if Priority or Urgent)

Keep the summary under 250 words. Write for a colleague who has no prior context on this case.
```

---

## Usage Notes

### Variable Reference

| Variable | Description |
|---|---|
| `[PRODUCT NAME]` | Brand name or INN of the medicinal product |
| `[THERAPEUTIC AREA]` | Disease area — e.g. oncology, cardiovascular |
| `[HCP TYPE]` | Profession of the healthcare professional |
| `[MARKET]` | Country/region — affects regulatory context |
| `[PASTE QUERY TEXT]` | Verbatim or summarised inquiry from the HCP |
| `[SOURCE MATERIAL]` | SmPC sections, study abstracts, SRD content — only paste what you want the AI to use |

### Best Practice Tips

- **Always specify source material** in Prompts 2 and 3 — do not rely on the AI's training knowledge for clinical data
- **Use Prompt 6 (QC Reviewer)** on any AI-generated draft before it goes anywhere near a dispatch queue
- **Prompt 4 (Gap Identifier)** works well as a first step before deciding whether to escalate — can save unnecessary 2nd-line routing
- **Combine prompts** for complex cases: run Prompt 1 first to structure the intake, then Prompt 4 to check SRD coverage, then Prompt 2 if escalation is needed

---

*Prompt library maintained for reference and AI-assisted workflow development. All AI outputs require human review by a qualified Medical Information professional before use in live operations.*
