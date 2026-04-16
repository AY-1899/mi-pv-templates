# Prompt Library: Standard Response Document (SRD) Drafting

> **Version:** 1.0  
> **Use case:** AI-assisted authorship, review, and maintenance of Standard Response Documents  
> **Compatible with:** Claude, GPT-4, or any instruction-following LLM  
> **Variables:** All placeholders are in `[SQUARE BRACKETS]` — replace before use

---

## How to Use This Library

These prompts support the SRD authorship lifecycle — from initial drafting through evidence synthesis, internal review, gap analysis, and localisation. They are designed to accelerate the content development process while keeping a qualified Medical Affairs or Medical Information professional in control of all outputs.

> ⚠️ AI-generated SRD content must be reviewed against current SmPC, CCSI, and published evidence by a qualified medical reviewer before any approval or use in live operations. These prompts do not replace medical sign-off, regulatory review, or document control requirements.

---

## Prompt Index

| # | Prompt Name | Use When |
|---|---|---|
| 1 | [SRD Topic Scoper](#1-srd-topic-scoper) | Defining the scope and key messages of a new SRD before drafting |
| 2 | [Evidence Synthesiser](#2-evidence-synthesiser) | Synthesising SmPC and clinical data into structured SRD body content |
| 3 | [Key Messages Drafter](#3-key-messages-drafter) | Writing the core key messages section |
| 4 | [Summary Response Drafter](#4-summary-response-drafter) | Drafting the short-form cover letter response |
| 5 | [FAQ Generator](#5-faq-generator) | Generating anticipated follow-up questions and answers |
| 6 | [SRD Reviewer](#6-srd-reviewer) | Reviewing a completed SRD draft for quality and compliance |
| 7 | [SRD Gap Analyser](#7-srd-gap-analyser) | Identifying gaps in an existing SRD against current evidence |
| 8 | [Market Localisation Adaptor](#8-market-localisation-adaptor) | Adapting an approved SRD for a different market |

---

## 1. SRD Topic Scoper

**Use when:** Starting a new SRD and needing to define its scope, intended audience, and key messages before writing begins.

```
You are a Medical Affairs content strategist helping to scope a new Standard Response Document (SRD).

TASK: Produce a scoping brief for a new SRD based on the information below.

---
PRODUCT: [PRODUCT NAME]
INDICATION: [APPROVED INDICATION]
THERAPEUTIC AREA: [e.g. oncology / cardiovascular / immunology]
QUERY TOPIC: [e.g. "Use of [product] in patients with severe renal impairment"]
TARGET AUDIENCE: [HCP only / Patient only / Both]
MARKETS: [UK / IE / DK / SE / NO — list all applicable]
TRIGGER FOR THIS SRD: [e.g. Recurring inquiry type / New label update / Launch / Regulatory request]

AVAILABLE SOURCE MATERIAL (list what exists):
[e.g. SmPC Section 4.2 and 4.4 / Phase III trial data / Post-marketing data / None — needs literature search]
---

Produce a scoping brief that includes:

1. SRD TITLE (suggested): Clear, specific, query-aligned title

2. SCOPE STATEMENT: What this SRD will and will not cover (2–3 sentences)

3. PROPOSED KEY MESSAGES: Draft 4–6 key messages this SRD should communicate, based on the topic and what is typically known about this query area. Flag any that will require clinical data to support.

4. CONTENT SECTIONS RECOMMENDED: List the sections this SRD should include (e.g. Background / Approved dosing / Clinical trial data / Special populations / Safety / FAQs)

5. SOURCE MATERIAL REQUIREMENTS: What data sources will be needed to complete this SRD?
   - SmPC sections required:
   - Clinical trial data required:
   - Literature search recommended: Yes / No — if yes, suggested search terms
   - Other:

6. REVIEW PATHWAY RECOMMENDED:
   - Medical reviewer required: Yes / No
   - Regulatory review required: Yes / No (e.g. if off-label content is involved)
   - Local affiliate review required: Yes / No (for market-specific content)

7. RELATED DOCUMENTS: List any existing SRDs or FAQs this new document should cross-reference or align with.
```

---

## 2. Evidence Synthesiser

**Use when:** You have gathered source material (SmPC content, trial data, published literature) and need to synthesise it into structured SRD body content.

```
You are a Medical Information content author synthesising clinical evidence for a Standard Response Document.

TASK: Synthesise the source material provided into structured SRD body content for the section specified.

---
PRODUCT: [PRODUCT NAME]
INDICATION: [APPROVED INDICATION]
SRD TOPIC: [e.g. "Dosing in hepatic impairment"]
SECTION TO DRAFT: [e.g. Section 4.2 — Evidence Summary / Background / Special Populations]
TARGET AUDIENCE: [HCP / Both HCP and patient]

SOURCE MATERIAL (use only this content — do not draw on general training knowledge):
[PASTE ALL RELEVANT SOURCE MATERIAL HERE — SmPC sections, trial summaries, abstract text, internal data]

CITATION FORMAT: [Vancouver / APA / SmPC section reference — specify]
---

Draft the specified SRD section using only the source material provided. The output should:

- Be written in clear, scientific prose appropriate for [TARGET AUDIENCE]
- Present information in a logical, structured order
- Include data tables where multiple data points are compared or listed (e.g. dosing by severity grade, AE incidence by arm)
- Cite every factual claim to the source material (e.g. "SmPC Section 4.2", "[Trial name], N=X")
- Be balanced — include clinically relevant limitations, safety caveats, and contra-indications where applicable
- Not contain promotional language, superlatives, or unsolicited comparisons to competitors
- Explicitly flag any gaps where source material is insufficient to fully address the topic

After the drafted section, add:
FLAGGED GAPS: List any aspects of the topic not covered by the source material provided.
SUGGESTED FOLLOW-UP: What additional evidence would strengthen this section?
```

---

## 3. Key Messages Drafter

**Use when:** You have reviewed the evidence and need to draft the Key Messages section — the concise, reviewable core of the SRD.

```
You are a Medical Information content author drafting the Key Messages section of a Standard Response Document.

TASK: Draft 4–6 key messages for the SRD described below.

---
PRODUCT: [PRODUCT NAME]
INDICATION: [APPROVED INDICATION]
SRD TOPIC: [e.g. "Cardiac monitoring requirements during treatment"]
TARGET AUDIENCE: [HCP / Both]

EVIDENCE SUMMARY (paste the synthesised evidence or key data points this SRD will be based on):
[PASTE EVIDENCE SUMMARY OR KEY DATA POINTS HERE]

SMPC REFERENCE: [Relevant SmPC sections — e.g. 4.2, 4.4, 4.8]
---

Draft Key Messages that:

- Are numbered and self-contained — each message should stand alone
- Are factual and directly supported by the evidence provided
- Use active, clear language — one idea per message
- Reflect the hierarchy of information (most critical / most commonly asked first)
- Do not contain promotional language
- Include the primary safety message relevant to this topic (if applicable)
- Are appropriate in depth for an HCP audience

FORMAT per message:
**[Message number]. [Key message — 1–2 sentences]**
*Supporting evidence: [Brief citation — e.g. SmPC 4.4 / Trial X primary endpoint]*

After the key messages, note:
GAPS: Are there aspects of the topic that the evidence does not support a clear key message for? List them.
REVIEW NOTE: Flag any message that will require specific medical or regulatory sign-off (e.g. messages relating to off-label use, comparative claims, or emerging data).
```

---

## 4. Summary Response Drafter

**Use when:** You have approved key messages and evidence, and need to draft the short-form cover letter response — the version sent directly to HCPs or patients.

```
You are a Medical Information specialist drafting the summary response section of an SRD — the short-form text used as the cover letter response to an HCP or patient inquiry.

TASK: Draft two versions of the summary response — one for HCP and one for patient/consumer (or HCP only if specified).

---
PRODUCT: [PRODUCT NAME]
INDICATION: [APPROVED INDICATION]
SRD TOPIC: [e.g. "Use during pregnancy"]
KEY MESSAGES (approved):
[PASTE APPROVED KEY MESSAGES FROM PROMPT 3 OR EXISTING CONTENT]

SAFETY INFORMATION TO INCLUDE: [e.g. "Contraindicated in pregnancy — SmPC Section 4.6" — or write "none specific"]
AE REPORTING REMINDER: [Include standard text — or paste local version: e.g. "Adverse events should be reported via the Yellow Card scheme at www.mhra.gov.uk/yellowcard"]
MARKET: [UK / IE / DK / other]
---

Draft the following:

VERSION A — HCP SUMMARY RESPONSE
- Scientific terminology appropriate for a prescriber
- Key messages presented with supporting data references
- Relevant safety information included
- SmPC referenced for full prescribing information
- AE reporting reminder included
- Standard MI closing line
- Target length: 200–300 words

VERSION B — PATIENT / CONSUMER SUMMARY RESPONSE (omit if HCP only)
- Plain language — avoid jargon; define any medical terms used
- Reassuring but factual tone
- Directs patient to speak with their HCP for clinical decisions
- Does not include raw clinical data or statistical values
- AE reporting reminder included (patient-appropriate version)
- Standard MI closing line
- Target length: 150–200 words

For both versions:
- Do not use the patient's name (this is a template)
- Do not include promotional language
- Flag if any content is market-specific and requires localisation review
```

---

## 5. FAQ Generator

**Use when:** You have a drafted SRD and want to anticipate the most likely follow-up questions an HCP might ask, and draft concise answers.

```
You are a Medical Information specialist generating the FAQ section for a Standard Response Document.

TASK: Generate 5–8 anticipated follow-up questions and concise answers based on the SRD content below.

---
PRODUCT: [PRODUCT NAME]
SRD TOPIC: [e.g. "Drug interactions with CYP3A4 inhibitors"]
SRD BODY CONTENT (paste the evidence summary and key messages):
[PASTE SRD CONTENT HERE]

SMPC REFERENCE SECTIONS: [e.g. 4.5, 4.2]
TARGET AUDIENCE: [HCP / Both]
---

Generate FAQs that:
- Reflect genuine clinical questions an HCP is likely to ask after reading the standard response
- Are ordered by clinical priority (most critical / most commonly asked first)
- Have concise answers (3–6 sentences per FAQ)
- Cite each answer to the SRD content or SmPC section
- Cover edge cases and common sub-populations where relevant (e.g. elderly patients, renal impairment, paediatric use)
- Flag any FAQ where the answer requires escalation to 2nd line or Medical Affairs

FORMAT per FAQ:
**Q[number]: [Question text]**
A: [Answer — factual, concise, referenced]
*Source: [SmPC section / trial reference / SRD section]*
*Escalate: Yes / No* — (Yes if this cannot be answered from approved content alone)

After the FAQs, add:
GAPS IDENTIFIED: Questions generated that cannot be answered from current SRD content — flag as potential SRD update requirements or topics requiring a new SRD.
```

---

## 6. SRD Reviewer

**Use when:** A full SRD draft is complete and needs a structured quality and compliance review before formal medical sign-off.

```
You are a Medical Information quality reviewer conducting a pre-approval review of a Standard Response Document draft.

TASK: Review the SRD draft below and produce a structured review report. Your role is to identify issues — not to rewrite the document.

---
SRD DRAFT:
[PASTE FULL SRD DRAFT HERE]

PRODUCT: [PRODUCT NAME]
MARKETS: [UK / IE / DK / other]
TARGET AUDIENCE: [HCP / Patient / Both]
SMPC VERSION USED: [Version number and date]
OTHER SOURCE DOCUMENTS: [List]
PREVIOUS VERSION (if update): [Reference or "New document"]
---

Review against the following criteria and produce a structured report:

1. SCOPE & COMPLETENESS
   - Does the SRD address the stated query topic fully?
   - Are there clinical sub-questions left unanswered?
   - Is the scope statement consistent with the content?

2. ACCURACY & EVIDENCE
   - Are all factual claims supported by cited source material?
   - Are there any statements that appear to conflict with the current SmPC?
   - Are data values, doses, and statistics presented correctly?
   - Are references complete and traceable?

3. BALANCE & TONE
   - Is the content balanced — does it include relevant safety information alongside efficacy data?
   - Is there any language that could be considered promotional?
   - Are limitations and uncertainties acknowledged where appropriate?

4. OFF-LABEL CONTENT
   - Does the SRD contain any off-label information? (Yes / No — flag specific statements)
   - If yes: is there documented Medical Affairs approval for inclusion?

5. SAFETY INFORMATION
   - Is relevant safety content from SmPC Sections 4.3, 4.4, and 4.8 included where appropriate?
   - Is the AE reporting reminder present?

6. LANGUAGE & AUDIENCE APPROPRIATENESS
   - Is terminology appropriate for the target audience?
   - Is the patient version (if present) in plain language?
   - Are abbreviations defined?

7. DOCUMENT CONTROL
   - Are all document control fields complete (version, date, markets, owner, expiry)?
   - Is the approval/sign-off section complete?

8. LOCALISATION (for multi-market SRDs)
   - Are market-specific regulatory requirements reflected? (e.g. UK vs EU labelling differences)
   - Are market-specific disclaimers present?

OVERALL REVIEW OUTCOME:
- ✅ Approved for medical sign-off — no issues identified
- ⚠️ Minor revisions required — list each item with section reference
- ❌ Major revision required before medical review — list reasons

PRIORITY ISSUES (if any): [List any issues that block approval]
```

---

## 7. SRD Gap Analyser

**Use when:** An existing SRD needs to be assessed against updated evidence (new SmPC, new trial data, new label update) to determine whether a revision is required.

```
You are a Medical Information content manager reviewing an existing SRD for currency and completeness.

TASK: Compare the existing SRD content against the updated source material and identify gaps, outdated content, and recommended changes.

---
EXISTING SRD CONTENT:
[PASTE EXISTING SRD BODY CONTENT OR KEY MESSAGES]

SRD REFERENCE: [Document number and current version]
SRD APPROVAL DATE: [DD-MMM-YYYY]
SRD EXPIRY DATE: [DD-MMM-YYYY]

UPDATED SOURCE MATERIAL (new SmPC version / new trial data / new label update):
[PASTE UPDATED SOURCE MATERIAL HERE]

REASON FOR REVIEW: [SmPC update / New trial publication / Regulatory request / Periodic review / Triggered by MI inquiry]
---

Produce a gap analysis with the following sections:

1. OUTDATED CONTENT
   For each section of the SRD, identify any statements that are no longer consistent with the updated source material.
   Format: Section → Current statement → Issue → Recommended update

2. MISSING CONTENT
   What clinically relevant information in the updated source material is not reflected in the current SRD?

3. KEY MESSAGE REVIEW
   Are the current key messages still accurate, complete, and appropriately prioritised?
   Flag any that require revision and suggest updated wording.

4. SAFETY UPDATES
   Are there any new or updated safety signals, warnings, contraindications, or risk minimisation measures in the updated source material that must be reflected?

5. REVISION RECOMMENDATION:
   - Minor update (wording / reference corrections): estimated effort — low
   - Moderate update (new section / revised key messages): estimated effort — medium
   - Full redraft required: estimated effort — high
   - No update required at this time

6. URGENCY:
   - Routine (update at next scheduled review)
   - Priority (update within [30 / 60] days)
   - Urgent (withdraw from use until updated — safety-related change)
```

---

## 8. Market Localisation Adaptor

**Use when:** An SRD approved for one market needs to be adapted for a different country with different regulatory requirements, label versions, or language needs.

```
You are a Medical Information localisation specialist adapting a Standard Response Document for a new market.

TASK: Identify all localisation requirements and produce an adapted version of the SRD for the target market.

---
ORIGINAL SRD CONTENT:
[PASTE APPROVED SRD CONTENT]

ORIGINAL MARKET: [e.g. UK]
TARGET MARKET: [e.g. Denmark / Norway / Ireland]
TARGET LANGUAGE: [English / Danish / Norwegian — specify if translation required]
TARGET AUDIENCE: [HCP / Patient / Both]

KNOWN DIFFERENCES (if any):
[e.g. SmPC differs between markets / Different approved indication / Different dosing recommendation / Additional local warning / Different AE reporting body]

LOCAL SMPC / LABEL VERSION FOR TARGET MARKET (if available):
[PASTE RELEVANT SECTIONS OR NOTE "NOT PROVIDED"]
---

Produce a localisation report and adapted content:

1. LOCALISATION REQUIREMENTS IDENTIFIED
   List every element that requires change for the target market:
   - Regulatory / label differences (indication, dose, warnings, contraindications)
   - AE reporting body and contact details
   - Local code compliance (e.g. LIF for Sweden, Medicin Industrien for Denmark)
   - Local affiliate disclaimer requirements
   - Language / terminology differences
   - Any content present in the original that is not approved in the target market

2. ADAPTED SRD CONTENT
   Produce the adapted version with all target-market changes applied.
   Mark each change with: [LOCALISED — reason]

3. CONTENT REQUIRING LOCAL AFFILIATE REVIEW
   List any sections where local medical or regulatory input is required before the adapted SRD can be approved.

4. TRANSLATION NOTES (if applicable)
   Flag any English terms, product names, or clinical concepts that require specific attention during translation to ensure regulatory accuracy.

5. DOCUMENT CONTROL UPDATE REQUIRED:
   - Markets field: update to include [TARGET MARKET]
   - Version: increment to [NEXT VERSION]
   - Local affiliate approval: required before use in [TARGET MARKET]
```

---

## Usage Notes

### Variable Reference

| Variable | Description |
|---|---|
| `[PRODUCT NAME]` | Brand name or INN |
| `[INDICATION]` | Approved indication as per current SmPC |
| `[SRD TOPIC]` | Specific query topic the SRD addresses |
| `[SOURCE MATERIAL]` | Paste only what you want the AI to use — SmPC sections, trial data, abstracts |
| `[TARGET AUDIENCE]` | HCP / Patient / Both — affects language and depth |
| `[MARKET]` | Country — affects regulatory framework and disclaimers |

### Recommended Authorship Workflow

```
Prompt 1 — Scope the SRD
        ↓
Prompt 2 — Synthesise evidence (run once per major content section)
        ↓
Prompt 3 — Draft key messages
        ↓
Prompt 4 — Draft summary response (HCP + patient versions)
        ↓
Prompt 5 — Generate FAQs
        ↓
Prompt 6 — Full SRD review
        ↓
Medical sign-off → Approved SRD
        ↓
Prompt 7 — Gap analysis at review cycle
Prompt 8 — Localisation for additional markets
```

### Content Governance Reminders

- **Prompt 2 (Evidence Synthesiser)** — always paste the source material explicitly; never rely on the AI's training knowledge for clinical data in an SRD
- **Prompt 6 (SRD Reviewer)** — use before submitting to a medical reviewer, not as a substitute for it
- **Prompt 8 (Localisation)** — always requires local affiliate medical sign-off before use; never deploy a localised SRD based on AI output alone
- All SRDs must go through your organisation's validated document control and approval process regardless of how they were drafted

---

*Prompt library maintained for reference and AI-assisted content development. All AI outputs require review and approval by a qualified Medical Affairs professional through the applicable document control process before use in live operations.*
