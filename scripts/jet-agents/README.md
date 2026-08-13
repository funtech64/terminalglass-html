# Jet Agent catalog refresh scripts

Repeatable workflow for updating terminal.glass Jet Agent pages from the official Ollama cloud catalog.

## Commands

```bash
# Full refresh (recommended order)
python3 scripts/jet-agents/scrape-ollama-cloud.py
python3 scripts/jet-agents/refresh-catalog.py
python3 scripts/jet-agents/generate-jet-agent-pages.py
python3 scripts/jet-agents/generate-jet-agent-index.py
python3 scripts/jet-agents/update-sitemap.py
python3 scripts/validate-site.py
```

## What each script does

| Script | Output |
|--------|--------|
| `scrape-ollama-cloud.py` | `data/jet-agents/raw/scrape-*.json`, `data/jet-agents/normalized/catalog.json` |
| `refresh-catalog.py` | `data/jet-agents/normalized/catalog-status.json`, `AGENTS/reports/jet-agent-catalog-refresh.md` |
| `generate-jet-agent-pages.py` | `/jet-agents/<slug>/index.html` per cloud tag |
| `generate-jet-agent-index.py` | `/jet-agents/catalog/index.html` |
| `update-sitemap.py` | Adds Jet Agent URLs to `sitemap.xml` |

## Normalized record fields

| Field | Source |
|-------|--------|
| `ollama_tag` | Exact runnable Ollama cloud tag |
| `display_name` | Ollama library page title |
| `description` | Ollama meta description |
| `publisher` | Inferred from family/description when stated; else `unknown` |
| `context_length` | Stated on Ollama page; else `unknown` |
| `parameter_size` | Stated on Ollama page; else `not stated` |
| `license` | Stated on Ollama page; else `not stated` |
| `vision_support` / `tool_support` / `thinking_support` | Ollama capability badges |
| `classifications` | terminal.glass capability-based categories |
| `eight_ball_featured` | `data/jet-agents/normalized/featured-8ball.json` |
| `catalog_status` | `current`, `new`, `changed`, or `possibly_removed` |

## Human review rules

- **possibly_removed** models are reported but pages are not auto-deleted.
- Do not change 8-BALL featured tags without 8-BALL source material.
- Do not infer licenses, context sizes, or parameter counts.
