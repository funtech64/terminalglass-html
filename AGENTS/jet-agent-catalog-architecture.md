# Jet Agent catalog — architecture working note

Date: 2026-08-13  
Repository: `funtech64/terminalglass-html`

## Existing page structure

| Route | Purpose |
|-------|---------|
| `/` | Homepage |
| `/pricing/`, `/hosting/`, `/contact/` | Product pages |
| `/models/` | Jet Model + Private Model catalog index (tabbed) |
| `/models/<family>-cloud/` | Jet Model **sales briefs** (Tailwind, long-form) |
| `/jet-agents/` | Glass Agents + Jet Agents **overview** (site.css) |
| `/jet-agents/catalog/` | **Jet Agent catalog index** (new) |
| `/jet-agents/<slug>/` | **Individual Jet Agent pages** (new, generated) |
| `/agents/` | Redirect to `/jet-agents/` |

## Navigation

- Global nav: Home, Pricing, Hosting, Models, Agents, Contact
- Jet Agent catalog linked from `/jet-agents/` and footer Explore column
- Model brief pages (Tailwind) link to `/jet-agents/` in header

## Reusable HTML patterns

- **Site chrome pages** (`site.css`): `.page-hero`, `.section`, `.card`, `.grid-2`, `.catalog-grid`, `.catalog-card`, `.kicker`, `.site-footer`
- **Model brief pages** (Tailwind CDN): separate lane for sales content under `/models/*-cloud/`

## Best locations (implemented)

| Asset | Location |
|-------|----------|
| Raw scrape evidence | `data/jet-agents/raw/scrape-YYYY-MM-DD.json` |
| Normalized catalog | `data/jet-agents/normalized/catalog.json` |
| 8-BALL featured tags | `data/jet-agents/normalized/featured-8ball.json` |
| Jet Agent index | `jet-agents/catalog/index.html` |
| Individual Jet Agent pages | `jet-agents/<slug>/index.html` |
| Generation scripts | `scripts/jet-agents/` |
| Change reports | `AGENTS/reports/jet-agent-catalog-refresh.md` |

## 8-BALL source findings

The `funtech64/8-BALL` repository was **not available** in this workspace (not cloned; GitHub returned not found).

Featured Jet defaults are documented in existing terminalglass-html model pages:

| Featured tag | Source page |
|--------------|-------------|
| `qwen3.5:cloud` | `models/qwen3.5-cloud/index.html` |
| `mistral-large-3:675b-cloud` | `models/mistral-large-3-cloud/index.html` |
| `qwen3-coder:480b-cloud` | `models/qwen3-coder-cloud/index.html` |

These match the task's stated 8-BALL trial installer featured set. Preserved in `featured-8ball.json` without modifying installer scripts.

## Product lane distinction

- **Glass Agents** — OpenClaw/action-capable workers (`/jet-agents/#glass-agents`)
- **Jet Agents** — Ollama Cloud model endpoints (`/jet-agents/catalog/`)
- **Jet Models** — Terminal.Glass sales briefs (`/models/*-cloud/`)
