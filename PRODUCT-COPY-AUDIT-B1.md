# PRODUCT-COPY-AUDIT-B1.md

Pre-edit inventory and resolution status for B1 product-truth repair.

| File | Issue | Correction | Owner? | Status |
|------|-------|------------|--------|--------|
| `index.html` | Hero used “Over 100 Models” as headline | Primary headline → “Private AI with no more guesswork.” | No | Fixed |
| `index.html` | Weak catalog claim “100+ models” | 240 families / 44,000 sizes / 100+ Meta | No | Fixed |
| `index.html` | YourCloudGPT promoted in meta and packages | AWS / DigitalOcean customer-owned cloud | No | Fixed |
| `index.html` | Generic Glass/Jet agent definitions | OpenClaw + Ollama CPU/GPU definitions | No | Fixed |
| `index.html` | Missing Happy Nerds Menu / DokuWiki | Added inclusion section | Partial | Fixed (detail pending owner) |
| `index.html` | Links to `/agents/` | `/jet-agents/` | No | Fixed |
| `hosting/index.html` | Generic “four paths” without AWS/DO/GCP/Azure | Three current paths + coming soon | No | Fixed |
| `hosting/index.html` | No guided sizing emphasis | “Remove the guesswork” + 😎 | No | Fixed |
| `jet-agents/index.html` (new) | N/A — replaced `agents/index.html` content | Full agent truth page | No | Created |
| `agents/index.html` | Public page collided with instruction folder | Permanent redirect to `/jet-agents/` | No | Fixed |
| `pricing/index.html` | Alchemist section and CTA | Removed | No | Fixed |
| `pricing/index.html` | YourCloudGPT in hero viz | AWS node | No | Fixed |
| `assets/js/pricing-config.js` | Alchemist in plans, promos, comparison | Removed; agent/deployment truth updated | No | Fixed |
| `assets/js/contact-config.js` | Alchemist interest option | Removed | No | Fixed |
| `assets/js/contact-page.js` | `alchemist-founders` intent map | Removed | No | Fixed |
| `assets/css/pricing.css` | `.alchemist-*` rules | Removed unused styles | No | Fixed |
| `sitemap.xml` | Listed `/agents/` | `/jet-agents/` only | No | Fixed |
| `scripts/update-site-chrome.py` | Chrome templates used `/agents/`, Alchemist footer | Updated to `/jet-agents/`, no Alchemist | No | Fixed |
| `models/index.html` | “100+ Private Models” lead | 240 / 44,000 catalog claims | No | Fixed |
| All core footers | YourCloudGPT deployment link | AWS or DigitalOcean contact interest | No | Fixed |
| `LAUNCH-READINESS.md` | Historical `/agents/` references | Preserved (historical doc) | No | Intentionally unchanged |

## Public Alchemist references removed

- `agents/index.html` (section removed via redirect)
- `pricing/index.html` (section + CTA)
- `assets/js/pricing-config.js` (plan feature, promo, comparison row, `alchemistConductor` object removed)
- `assets/js/pricing-page.js` (`renderAlchemistSection` removed)
- `assets/js/contact-config.js` (interest option + URL map)
- `assets/js/contact-page.js` (intent handler)
- `assets/css/pricing.css` (alchemist styles)
- All footer `Alchemist Conductor` links across public HTML pages

## YourCloudGPT operational identifiers retained (internal)

- `pricing-config.js` — no public YourCloudGPT product cards remain; internal `yourcloudgpt` id removed from deployment type cards
- `models/data/*.json` — unchanged operational metadata
- `models/terminal-glass_cloudModels.md` — internal documentation unchanged

## Route migration summary

| Old | New |
|-----|-----|
| `https://terminal.glass/agents/` | `https://terminal.glass/jet-agents/` (301-style HTML redirect at old path) |
| `agents/index.html` (public page) | `jet-agents/index.html` |
| `agents/cursorFileB1.md` | Unchanged (instruction folder) |
