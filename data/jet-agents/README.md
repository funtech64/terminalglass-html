# Jet Agent catalog data

Machine-readable source for **terminal.glass Jet Agent** pages (`/jet-agents/<slug>/`).

Jet Agents are Ollama Cloud–hosted models. This is a separate product lane from:

- **Glass Agents** — OpenClaw/action-capable agent workers (`/jet-agents/#glass-agents`)
- **Jet Models** — Terminal.Glass sales briefs under `/models/<family>-cloud/`
- **Private Models** — customer-controlled local models (NoCloudGPT)

## Directory layout

| Path | Purpose |
|------|---------|
| `raw/scrape-YYYY-MM-DD.json` | Immutable scrape evidence (search families, per-family HTML excerpts, API tags) |
| `normalized/catalog.json` | Current normalized Jet Agent records for page generation |
| `normalized/featured-8ball.json` | 8-BALL featured Jet tags (installer defaults; do not change without 8-BALL source) |
| `normalized/catalog-status.json` | Per-model status: `current`, `new`, `changed`, `possibly_removed` |

## Source-of-truth order

1. **Ollama** — official cloud catalog (`https://ollama.com/search?c=cloud`, per-family library pages)
2. **8-BALL** — featured Jet defaults (`featured-8ball.json`; sourced from 8-BALL installer when available)
3. **terminalglass-html** — public Jet Agent web content generated from `normalized/catalog.json`

## Refresh workflow

```bash
# 1. Scrape Ollama and write raw + normalized catalog
python3 scripts/jet-agents/scrape-ollama-cloud.py

# 2. Compare against previous normalized catalog; write review report
python3 scripts/jet-agents/refresh-catalog.py

# 3. Regenerate Jet Agent index and individual pages
python3 scripts/jet-agents/generate-jet-agent-pages.py
python3 scripts/jet-agents/generate-jet-agent-index.py

# 4. Update sitemap entries for new/changed pages
python3 scripts/jet-agents/update-sitemap.py
```

Removed models are **not** auto-deleted from the site. `refresh-catalog.py` flags them as `possibly_removed` for human review.

See `scripts/jet-agents/README.md` for field definitions and `AGENTS/reports/jet-agent-catalog-refresh.md` for the latest change report.
