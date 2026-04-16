# MI Response Drafting Tool

A single-file web application that guides a Medical Information specialist through the full 2nd-line response workflow — powered by Claude.

## What It Does

Four sequential steps, each calling the Claude API:

| Step | Name | What Claude does |
|---|---|---|
| 1 | **Intake** | Classifies the query, identifies AE content, suggests routing |
| 2 | **Gap Check** | Assesses whether an existing SRD covers the query |
| 3 | **Draft** | Writes a 2nd-line response from your source material |
| 4 | **QC Review** | Reviews the draft for compliance, accuracy, and promotional language |

Outputs from each step auto-populate the next — so the query entered in Step 1 flows through to Steps 2, 3, and 4 without re-typing.

## How to Use

### Option A — Open directly in a browser
1. Download `mi-drafting-tool.html`
2. Open it in Chrome, Firefox, or Edge
3. Enter your [Anthropic API key](https://console.anthropic.com/) in the field at the top
4. Work through Steps 1–4

> **Note:** Some browsers block API calls from local files due to CORS restrictions. If the tool doesn't connect, use Option B.

### Option B — Run via a local server (recommended)
If you have Python installed:
```bash
# Navigate to the folder containing the file
cd path/to/tool

# Start a local server
python -m http.server 8000

# Open in browser
# http://localhost:8000/mi-drafting-tool.html
```

## API Key

You need an Anthropic API key to use this tool:
1. Sign up at [console.anthropic.com](https://console.anthropic.com/)
2. Generate an API key under API Keys
3. Paste it into the key field at the top of the tool

Your API key is held in memory only for the current browser session — it is never stored or transmitted anywhere other than the Anthropic API.

## Important Disclaimers

- All Claude outputs are **drafts only** — human review by a qualified Medical Information professional is required before dispatch
- Do **not** enter patient-identifiable information
- Do **not** enter proprietary company data or unpublished clinical trial data
- This tool does not replace company SOPs, validated workflows, or medical sign-off processes
- The response drafting step (Step 3) instructs Claude to use only the source material you paste — do not rely on it for clinical data outside of what you provide

## Requirements

- Modern web browser (Chrome, Firefox, Edge)
- Anthropic API key
- Internet connection (for API calls)

No installation, no dependencies, no server required for basic use.
