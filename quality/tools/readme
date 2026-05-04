# Deviation & CAPA Drafting Tool

A single-file web application that guides a Quality professional through the full deviation and CAPA workflow — powered by Claude. Built for pharmaceutical GxP environments.

## What It Does

Four sequential steps, each calling the Claude API:

| Step | Name | What Claude does |
|---|---|---|
| 1 | **Intake** | Structures the event, classifies severity, assesses patient/product impact, recommends immediate containment |
| 2 | **Root Cause** | Conducts 5-Why or Ishikawa analysis using only the facts provided — assumptions clearly flagged |
| 3 | **CAPA Plan** | Drafts corrective and preventive actions with owners, timelines, success criteria, and effectiveness measures |
| 4 | **Closure Report** | Generates a formal audit-ready closure summary for QMS entry |

Outputs from each step auto-populate the next — context flows through the full workflow without re-entry.

## How to Use

### Option A — Open directly in a browser
1. Download `deviation-capa-tool.html`
2. Open in Chrome, Firefox, or Edge
3. Enter your [Anthropic API key](https://console.anthropic.com/) at the top
4. Work through Steps 1–4

> Some browsers block API calls from local HTML files. If the tool doesn't connect, use Option B.

### Option B — Run via local server (recommended)
```bash
cd path/to/quality/
python -m http.server 8000
# Open: http://localhost:8000/deviation-capa-tool.html
```

## Root Cause Methods

**5-Why Analysis** — best for focused, single-cause deviations. Drills through sequential cause chains to the systemic root.

**Ishikawa (Fishbone)** — best for complex or multifactorial events. Covers all six categories: Man, Machine, Method, Material, Measurement, Environment.

Select your preferred method in Step 2 before running the analysis.

## GxP Compliance Notes

- All outputs are **draft only** — must be reviewed and approved by a qualified Quality professional before entry into any validated QMS
- The tool instructs Claude to flag assumptions clearly — points where facts are missing will be explicitly marked in the output
- CAPA actions that modify validated processes, equipment, or documents may require formal change control — the tool will flag these
- Do not enter batch-specific data, commercially confidential information, or patient-identifiable data

## Requirements

- Modern web browser (Chrome, Firefox, Edge)
- Anthropic API key ([console.anthropic.com](https://console.anthropic.com/))
- Internet connection

No installation or dependencies required.

---

*Part of the [MI & Quality AI Toolkit](../README.md)*
