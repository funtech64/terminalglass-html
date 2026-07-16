# Terminal.Glass Artwork Audit and Transfer Plan

**Date:** 2026-07-10  
**Scope:** Audit only — no HTML changes, no image downloads, no NoCloudGPT file modifications.  
**Goal:** Identify which existing NoCloudGPT artwork is safe and appropriate to reuse for a calm, infrastructure-software Terminal.Glass look.

---

## Audit summary

### What was reviewed

| Source | Location in NoCloudGPT repo | Present in `terminalglass-html`? |
|--------|----------------------------|----------------------------------|
| Artwork manifest | `models/artwork-sources.md` | **No** — reviewed from `funtech64/nocloudgpt-html` |
| Processing log (licensed secondaries) | `models/art/processing-log.md` | **No** |
| Model folder images | `/models/<slug>/hero.webp`, `hero.jpg`, `secondary.webp` | **No image files** — HTML references only |

### Current state of `terminalglass-html`

- **0** binary image files in the repository (`webp`, `jpg`, `png`).
- **7** cloud model HTML pages reference `hero.webp` paths that do not exist on disk yet.
- **3** cloud model pages reference Wikimedia-sourced `secondary.webp` paths that do not exist on disk yet.
- **No** `card.webp`, `sidebar.webp`, `og.webp`, or `brand.webp` files exist anywhere in the NoCloudGPT repo either — only `hero.*` and `secondary.webp` were found (326 total images in NoCloudGPT).

### Selection criteria applied

**Included:** Linux/server/datacenter/GPU/terminal/cybersecurity/engineering-workstation/document-RAG/abstract technical diagrams with clear Wikimedia or processing-log attribution.

**Excluded:** Animal, food, fantasy, pun-based, or whimsical artwork (e.g. alpaca, bagel, bakllava, crab claws for OpenClaw, constellation Gemini, wizard hats, mythological figures). Ollama library hero images are listed separately as `REVIEW BEFORE USE` because they are model-brand assets, not infrastructure photography.

---

## Recommended candidates (16 total)

Listed in priority order. Copy source paths are relative to the **NoCloudGPT** repository (`funtech64/nocloudgpt-html`). Terminal.Glass target paths use the standard naming convention where practical.

---

### 1. Wikimedia server rack — primary infrastructure hero

| Field | Value |
|-------|-------|
| **Source model/folder** | `nemotron4` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Wikimedia_Servers-0001_42.jpg |
| **License** | CC BY-SA 3.0 |
| **Attribution** | "Wikimedia Servers-0001 42.jpg" by Helpameout — Own work |
| **Why it fits** | Literal rack-server photography. Quiet, factual, immediately reads as infrastructure. Best single asset for a mature software-company homepage. |
| **Where to use** | Homepage hero (`/assets/hero.webp` or `/assets/images/hero.webp`), hosting page hero, model catalog page header |
| **Target filenames** | `hero.webp`, `og.webp` (crop to 1200×630) |
| **Status** | **Recommended** |

---

### 2. University supercomputer map — HPC / private compute

| Field | Value |
|-------|-------|
| **Source model/folder** | `nemotron-3-super-cloud` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Top_supercomputers_at_universities_in_the_United_States.webp |
| **License** | CC0 |
| **Attribution** | "Top supercomputers at universities in the United States.webp" by Wikideas1 — Own work |
| **Why it fits** | Clean technical diagram of compute infrastructure. Supports “serious hardware / serious workloads” without AI clichés. |
| **Where to use** | Hosting page (managed / GPU sizing section), optional homepage alternate hero, Nemotron cloud model pages |
| **Target filenames** | `card.webp` on hosting page; `sidebar.webp` on `nemotron-3-super-cloud` |
| **Status** | **Recommended** |

---

### 3. NVIDIA GPU hardware photo — GPU sizing context

| Field | Value |
|-------|-------|
| **Source model/folder** | `nemotron-3-nano-cloud` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:NVIDIA_GPU_reflow.jpg |
| **License** | CC BY-SA 2.0 |
| **Attribution** | "NVIDIA GPU reflow.jpg" by Binary Koala — https://www.flickr.com/photos/binary_koala/16123411683/ |
| **Why it fits** | Real GPU hardware. Directly supports hosting/GPU guidance without cartoon mascots. |
| **Where to use** | Hosting page (GPU instances), `nemotron-3-nano-cloud` and `nemotron-3-super-cloud` cloud briefs, model catalog “cloud-accelerated” lane |
| **Target filenames** | `sidebar.webp`, `card.webp` |
| **Status** | **Recommended** |

---

### 4. NATO cyber defense conference — private / secure operations

| Field | Value |
|-------|-------|
| **Source model/folder** | `granite-guardian` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:NATO_Cyber_Defense_Pledge_Conference_at_The_Hague,_Netherlands_on_17_May_2024_-_NAVO_Cyber_Defence_Pledge_Conference_(53727534173).jpg |
| **License** | CC BY-SA 2.0 |
| **Attribution** | "NATO Cyber Defense Pledge Conference…" by Ministerie van Buitenlandse Zaken — NAVO Cyber Defence Pledge Conference |
| **Why it fits** | Professional cybersecurity setting. Supports private hosting and firewall narrative without stock “hacker in hoodie” imagery. |
| **Where to use** | Hosting page (self-hosted / security), contact page subtle sidebar, optional pricing page reassurance band |
| **Target filenames** | `sidebar.webp` (hosting), `card.webp` (contact) |
| **Status** | **Recommended** |

---

### 5. Cybersecurity shield icon — minimal security accent

| Field | Value |
|-------|-------|
| **Source model/folder** | `llama-guard-3` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Cybersecurity.png |
| **License** | CC0 |
| **Attribution** | "Cybersecurity.png" by jaydeep_ |
| **Why it fits** | Simple icon-style graphic. Works as a small accent where photography would be heavy. |
| **Where to use** | Contact page, pricing page sidebar, footer-adjacent trust strip |
| **Target filenames** | `sidebar.webp`, `brand.webp` (if cropped small) |
| **Status** | **Recommended** |

---

### 6. Document scanner hardware — RAG / document search

| Field | Value |
|-------|-------|
| **Source model/folder** | `nuextract` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:HP-Scanjet4C-ADF-C2525B_10.jpg |
| **License** | CC BY-SA 4.0 |
| **Attribution** | "HP-Scanjet4C-ADF-C2525B 10.jpg" by Thomas Schanz |
| **Why it fits** | Physical document-ingest hardware. Maps cleanly to RAG and internal document search — a concrete IT workflow, not “AI magic.” |
| **Where to use** | Model catalog page (embedding/RAG lane), `command-r` family context, stack section supporting RAG use cases |
| **Target filenames** | `card.webp` |
| **Status** | **Recommended** |

---

### 7. Document stacks at desk — long-context / knowledge work

| Field | Value |
|-------|-------|
| **Source model/folder** | `jamba` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Man_working_behind_a_desk._Desk_is_filled_with_stacks_of_manuscripts._LCCN2014684500.jpg |
| **License** | Public domain |
| **Attribution** | "Man working behind a desk…" — Unknown (Library of Congress) |
| **Why it fits** | Document-volume metaphor without futuristic visuals. Supports long-context and enterprise knowledge bases. |
| **Where to use** | Model catalog sidebar, optional pricing page “documentation included” band |
| **Target filenames** | `sidebar.webp` |
| **Status** | **Recommended** |

---

### 8. Engineering workstation — deployment / coding context

| Field | Value |
|-------|-------|
| **Source model/folder** | `devstral-2-cloud` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Workspace_@_Nottingham_Flat.jpg |
| **License** | CC BY 2.0 |
| **Attribution** | "Workspace @ Nottingham Flat.jpg" by David Wellbeloved — https://www.flickr.com/photos/davewellbeloved/5378333486/ |
| **Why it fits** | Real engineering desk with monitors. Fits coding-agent and deployment-support messaging. |
| **Where to use** | Contact page, pricing page, `devstral-2-cloud` / `qwen3-coder-cloud` cloud briefs |
| **Target filenames** | `card.webp` (contact), `sidebar.webp` (coder cloud pages) |
| **Status** | **Recommended** |

---

### 9. US Naval Research Lab — research computing facility

| Field | Value |
|-------|-------|
| **Source model/folder** | `glm5` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:US_Naval_Research_Lab.jpg |
| **License** | Public domain |
| **Attribution** | "US Naval Research Lab.jpg" by Reese Brown — https://www.dvidshub.net/image/3464709/national-capital-region-aerial-photography-flight |
| **Why it fits** | Serious institutional computing environment. Professional tone for enterprise buyers. |
| **Where to use** | Hosting page alternate card, GLM cloud family pages |
| **Target filenames** | `card.webp` |
| **Status** | **Recommended** — building exterior, not a server room; use as secondary option |

---

### 10. Vintage computer festival — terminal / legacy computing aesthetic

| Field | Value |
|-------|-------|
| **Source model/folder** | `gpt-2` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Vintage_Computer_Festival_Southeast_3.0_(17348434711).jpg |
| **License** | CC BY 2.0 |
| **Attribution** | "Vintage Computer Festival Southeast 3.0…" by Kevin Savetz — SAM_0614 |
| **Why it fits** | Hardware-forward, terminal-era computing. Useful if Terminal.Glass wants a subtle “terminal” brand echo without illustration. |
| **Where to use** | Optional homepage accent (low priority), about/contact sidebar |
| **Target filenames** | `sidebar.webp` |
| **Status** | **Recommended** — niche; use sparingly |

---

### 11. Deep neural network diagram — abstract technical

| Field | Value |
|-------|-------|
| **Source model/folder** | `rnj-1-cloud` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Deep_neural_networks_diagram.png |
| **License** | CC BY 4.0 |
| **Attribution** | "Deep neural networks diagram.png" by Cmglee |
| **Why it fits** | Clean architecture-style diagram. Acceptable for model-page secondary art if kept small. |
| **Where to use** | `rnj-1-cloud` brief only — not homepage |
| **Target filenames** | `sidebar.webp` on `rnj-1-cloud` |
| **Status** | **REVIEW BEFORE USE** — generic “AI diagram” tone; OK for a single model page, not core branding |

---

### 12. Conditional neural field diagram — abstract technical

| Field | Value |
|-------|-------|
| **Source model/folder** | `glm-5-cloud` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Conditional_neural_field_auto-decoder_01.jpg |
| **License** | CC0 |
| **Attribution** | "Conditional neural field auto-decoder 01.jpg" by FjordJarl9 — Own work |
| **Why it fits** | Minimal abstract diagram. Small file, unobtrusive. |
| **Where to use** | GLM cloud pages sidebar only |
| **Target filenames** | `sidebar.webp` on `glm-5-cloud` |
| **Status** | **REVIEW BEFORE USE** — abstract ML art; fine at small size on model pages |

---

### 13. Gates Computer Science Building — campus computing

| Field | Value |
|-------|-------|
| **Source model/folder** | `glm-5.1-cloud` |
| **Existing filename** | `secondary.webp` |
| **Original source URL** | https://commons.wikimedia.org/wiki/File:Gates_Computer_Science_Building_(2025)-L1007406.jpg |
| **License** | CC BY-SA 4.0 |
| **Attribution** | "Gates Computer Science Building (2025)-L1007406.jpg" by Frank Schulenburg — Own work |
| **Why it fits** | Recognizable CS research building. Professional but not a datacenter. |
| **Where to use** | `glm-5.1-cloud` page only |
| **Target filenames** | `sidebar.webp` |
| **Status** | **REVIEW BEFORE USE** — architecture photo, not infrastructure close-up |

---

### 14. Ollama library hero — Mistral family

| Field | Value |
|-------|-------|
| **Source model/folder** | `mistral` → reuse on `mistral-large-3-cloud`, `ministral-3-cloud` |
| **Existing filename** | `hero.webp` |
| **Original source URL** | https://ollama.com/library/mistral |
| **License** | Ollama library asset — **verify terms before production use** |
| **Attribution** | Sourced from Ollama model library listing (per NoCloudGPT HTML comments) |
| **Why it fits** | Intended reference in manifest: data-center photography theme. Appropriate for model-specific cards if the actual image is infrastructure-themed. |
| **Where to use** | Homepage model preview (`mistral-large-3-cloud`), cloud model hero (`card.webp` derived from hero) |
| **Target filenames** | Copy to `models/mistral-large-3-cloud/hero.webp`, `card.webp` |
| **Status** | **REVIEW BEFORE USE** — inspect image visually before import; do not use if whimsical |

---

### 15. Ollama library hero — DeepSeek family

| Field | Value |
|-------|-------|
| **Source model/folder** | `deepseek` → reuse on `deepseek-v3.1-cloud`, `deepseek-v3.2-cloud` |
| **Existing filename** | `hero.webp` (exists on `deepseek-v3.1-cloud`, `deepseek-v3.2-cloud` in NoCloudGPT) |
| **Original source URL** | https://ollama.com/library/deepseek-v3.1 |
| **License** | Ollama library asset — **verify terms before production use** |
| **Attribution** | Per NoCloudGPT cloud page: shared DeepSeek family artwork from Ollama listing |
| **Why it fits** | Manifest references programming/math workstation imagery. Suitable for homepage model preview if visually technical. |
| **Where to use** | Homepage model preview cards, DeepSeek cloud brief heroes |
| **Target filenames** | `hero.webp`, `og.webp`, `card.webp` per cloud slug |
| **Status** | **REVIEW BEFORE USE** |

---

### 16. Ollama library hero — Qwen 3.5 Cloud

| Field | Value |
|-------|-------|
| **Source model/folder** | `qwen3.5-cloud` |
| **Existing filename** | `hero.webp` |
| **Original source URL** | https://ollama.com/library/qwen3.5 |
| **License** | Ollama library asset — **verify terms before production use** |
| **Attribution** | Per NoCloudGPT: artwork shared with local Qwen family page, sourced from Ollama library |
| **Why it fits** | Flagship homepage catalog model. Use only if hero image is technical/professional on inspection. |
| **Where to use** | Homepage model preview, `qwen3.5-cloud` brief, model catalog |
| **Target filenames** | `hero.webp`, `card.webp`, `og.webp` |
| **Status** | **REVIEW BEFORE USE** |

---

## Page-by-page placement guide

### Homepage hero

| Priority | Candidate | Source |
|----------|-----------|--------|
| 1st | Rack servers (`nemotron4/secondary.webp`) | Wikimedia CC BY-SA 3.0 |
| 2nd | Supercomputer map (`nemotron-3-super-cloud/secondary.webp`) | Wikimedia CC0 |

Do **not** use Ollama model mascots or SVG placeholders for the homepage hero until reviewed.

### Homepage model preview (6 cards)

Use `card.webp` derived from reviewed Ollama heroes **only after visual inspection**:

| Model card | NoCloudGPT source | Fallback |
|------------|-------------------|----------|
| DeepSeek V3.1 Cloud | `deepseek-v3.1-cloud/hero.webp` | GPU photo (#3) |
| DeepSeek V3.2 Cloud | `deepseek-v3.2-cloud/hero.webp` | GPU photo (#3) |
| GPT-OSS Cloud | `gpt-oss-cloud/hero.webp` | Server rack (#1) |
| Qwen 3.5 Cloud | `qwen3.5-cloud/hero.webp` | Server rack (#1) |
| Gemma 4 Cloud | No hero file in NoCloudGPT | Server rack (#1) or skip art |
| Kimi K2.6 Cloud | `kimi-k2.6-cloud/hero.webp` | Server rack (#1) |

All Ollama-sourced card art: **REVIEW BEFORE USE**.

### Pricing page

| Asset | Source | Role |
|-------|--------|------|
| Engineering workstation | `devstral-2-cloud/secondary.webp` | Quiet sidebar — “we deploy on your stack” |
| Cybersecurity icon | `llama-guard-3/secondary.webp` | Small trust accent |
| Server rack (cropped) | `nemotron4/secondary.webp` | Optional narrow banner |

### Hosting page

| Asset | Source | Role |
|-------|--------|------|
| Server rack | `nemotron4/secondary.webp` | Self-hosted hero |
| Supercomputer map | `nemotron-3-super-cloud/secondary.webp` | Managed / HPC context |
| GPU photo | `nemotron-3-nano-cloud/secondary.webp` | GPU sizing section |
| Cyber defense photo | `granite-guardian/secondary.webp` | Security / private network |

### Contact page

| Asset | Source | Role |
|-------|--------|------|
| Engineering workstation | `devstral-2-cloud/secondary.webp` | Human, professional, not salesy |
| Cybersecurity icon | `llama-guard-3/secondary.webp` | Optional small graphic |

Keep contact art minimal — one sidebar image maximum.

### Model catalog page

| Asset | Source | Role |
|-------|--------|------|
| Server rack | `nemotron4/secondary.webp` | Page header |
| Document scanner | `nuextract/secondary.webp` | RAG / embedding lane |
| GPU photo | `nemotron-3-nano-cloud/secondary.webp` | Cloud-accelerated lane |

### Terminal.Glass cloud model pages

**Prefer Wikimedia secondaries** (already attributed in HTML) over Ollama heroes for body copy illustrations:

| Cloud slug | Primary art | Secondary art |
|------------|-------------|---------------|
| `nemotron-3-nano-cloud` | `hero.jpg` (Ollama) — REVIEW | `secondary.webp` GPU — **import** |
| `nemotron-3-super-cloud` | `hero.jpg` (Ollama) — REVIEW | `secondary.webp` supercomputer map — **import** |
| `devstral-2-cloud` | `hero.jpg` (Ollama) — REVIEW | `secondary.webp` workspace — **import** |
| `rnj-1-cloud` | — | `secondary.webp` network diagram — REVIEW |
| `glm-5-cloud` | — | `secondary.webp` neural diagram — REVIEW |
| `glm-5.1-cloud` | — | `secondary.webp` CS building — REVIEW |
| `glm-4.7-cloud` | — | `secondary.webp` AI scale diagram — **skip** (AI cliché) |
| `mistral-large-3-cloud` | `hero.webp` (Ollama) — REVIEW | — |
| `qwen3-coder-cloud` | `hero.webp` (Ollama) — REVIEW | workspace (#8) as sidebar |
| Other cloud slugs with `hero.webp` in NoCloudGPT | Copy hero after review | Use server/GPU stock from #1–#3 as fallback |

---

## Explicitly rejected for Terminal.Glass core pages

These exist in `models/art/processing-log.md` but should **not** be transferred:

| Folder | Reason |
|--------|--------|
| `alpaca`, `aquila`, `dolphin`, `orca-mini`, `tigerbot` | Animal-themed |
| `bagel`, `bakllava` | Food pun |
| `airoboros`, `mythomax`, `nous-hermes`, `wizardcoder`, `magicoder` | Fantasy / myth / wizard |
| `openclaw` | Crab claws — animal pun |
| `gemini-3-flash-preview-cloud` | Constellation — zodiac pun |
| `ministral` | Historical portrait — not infrastructure |
| `devstral-small-2-cloud` | Child with toy car — not enterprise tone |
| `glm-4.7-cloud` | “Artificial Intelligence Scale” icon — AI cliché |
| `moondream`, `laguna`, `grok`, `reka` | Space/nebula scenery — off-brand |
| `solar`, `zephyr`, `mistral-family` | Weather/wind/mill unrelated imagery |

NoCloudGPT files are **not** modified or deleted by this plan.

---

## Import procedure (when approved — not executed yet)

1. Copy selected files from `nocloudgpt-html` into `terminalglass-html` using the naming convention:
   - `hero.webp` — page hero
   - `card.webp` — grids and homepage model preview (resize from hero or secondary)
   - `sidebar.webp` — narrow column art
   - `og.webp` — 1200×630 social crop
   - `brand.webp` — small logos/icons only (e.g. cybersecurity shield)

2. Add attribution blocks to each page footer (Wikimedia entries already drafted in NoCloudGPT HTML).

3. Visually inspect every **REVIEW BEFORE USE** Ollama `hero.webp` before placing on homepage, pricing, or hosting.

4. Do not hotlink — serve from `/models/<slug>/` or `/assets/images/`.

5. Copy `models/artwork-sources.md` and `models/art/processing-log.md` into `terminalglass-html` for ongoing reference (documentation only).

---

## Gaps and follow-ups

| Gap | Recommendation |
|-----|----------------|
| No images in `terminalglass-html` today | First import batch: candidates #1–#8 (all Wikimedia, fully attributed) |
| No `card.webp` / `og.webp` / `sidebar.webp` / `brand.webp` in source repo | Generate from `hero.webp` or `secondary.webp` during import |
| `gemma4-cloud` has no hero in NoCloudGPT | Use server rack (#1) or leave text-only until Ollama asset confirmed |
| `artwork-sources.md` not in Terminal.Glass repo | Copy from NoCloudGPT when import begins |
| Ollama hero license unclear | Legal review before using on homepage or OG tags |
| Site-level pages (pricing, hosting, contact) have no art today | Use candidates #1, #4, #8 — no new downloads required |

---

## Recommended first import batch (10 files)

When transfer is approved, start with these — all exist in NoCloudGPT, all have processing-log attribution, none are pun/animal artwork:

1. `nemotron4/secondary.webp` → homepage + hosting hero  
2. `nemotron-3-super-cloud/secondary.webp` → hosting  
3. `nemotron-3-nano-cloud/secondary.webp` → hosting + nemotron cloud pages  
4. `granite-guardian/secondary.webp` → hosting security section  
5. `llama-guard-3/secondary.webp` → contact / pricing accent  
6. `nuextract/secondary.webp` → model catalog RAG lane  
7. `jamba/secondary.webp` → model catalog sidebar  
8. `devstral-2-cloud/secondary.webp` → contact + pricing  
9. `glm5/secondary.webp` → hosting alternate  
10. `gpt-2/secondary.webp` → optional terminal-brand sidebar  

Defer all Ollama `hero.webp` files until visual review is complete.
