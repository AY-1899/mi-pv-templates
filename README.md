# Medical Information & Pharmacovigilance Templates

A collection of professional markdown templates for Medical Information (MI) operations and pharmacovigilance workflows, based on 7+ years of experience across EU pharmaceutical environments.

These templates are designed to be:
- **Regulatory-aware** — aligned with ICH, EU GVP, and ABPI/EFPIA frameworks
- **System-agnostic** — adaptable to Salesforce, IRMS, Veeva, and other MI platforms
- **Market-adaptable** — structured for localisation across UK, Nordic, and Irish markets

---

## Templates & Workflow Guides

| File | Description |
|---|---|
| [`mi-workflow-guide.md`](./mi-workflow-guide.md) | End-to-end MI inquiry handling — triage, classification, response prep, QC, dispatch |
| [`srd-template.md`](./srd-template.md) | Standard Response Document structure with document control, key messages, evidence summary, and approval workflow |
| [`pv-icsr-checklist.md`](./pv-icsr-checklist.md) | ICSR processing checklist — validity, triage, data entry, seriousness, causality, narrative QC, reporting timelines |

## AI Prompt Libraries

Modular prompts for AI-assisted MI and PV workflows. All prompts use `[VARIABLE]` placeholders and are compatible with Claude, GPT-4, or any instruction-following LLM. AI outputs require human review before use in live operations.

| File | Prompts | Use Case |
|---|---|---|
| [`prompt-library-hcp-2nd-line.md`](./prompt-library-hcp-2nd-line.md) | 7 prompts | Query intake, 2nd-line response drafting, literature summary, SRD gap check, cover letter, QC review, escalation handoff |
| [`prompt-library-ae-triage.md`](./prompt-library-ae-triage.md) | 8 prompts | AE signal detection, minimum criteria check, data extraction, seriousness assessment, MedDRA coding, narrative drafting, follow-up letters, PV handoff |
| [`prompt-library-srd-drafting.md`](./prompt-library-srd-drafting.md) | 8 prompts | SRD scoping, evidence synthesis, key messages, summary response, FAQ generation, SRD review, gap analysis, market localisation |

---

## Background

These templates reflect real-world MI and PV workflows across Eli Lilly, Pfizer, AstraZeneca, and IQVIA, including:

- Multi-market operations (UK, Ireland, Denmark, Sweden, Norway)
- Salesforce Classic/Lightning and Omnichannel environments
- Oncology-focused 2nd-line response management
- ICSR processing at volume (100+ cases)
- SRD authorship and cross-market localisation

---

## How to Use

Clone or fork this repository and adapt the templates to your organisation's SOPs. All templates use standard markdown and render cleanly on GitHub, Notion, Confluence, and most documentation platforms.

```bash
git clone https://github.com/[your-username]/mi-pv-templates.git
```

---

## Disclaimer

These templates are for **reference and educational purposes only**. They do not replace validated company SOPs or regulatory guidance. Always follow your organisation's approved procedures for live case processing, SRD authorship, and regulatory submissions.

---

## Contact

[LinkedIn](https://www.linkedin.com/in/ammar-jawad-b2a373114/) · ammar.jawad195@gmail.com
