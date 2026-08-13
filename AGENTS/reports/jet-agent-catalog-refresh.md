# Jet Agent Catalog Refresh Report

**Report date:** 2026-08-13

## Scrape metadata

| Field | Value |
|-------|-------|
| SCRAPE DATE | 2026-08-13 |
| OLLAMA SOURCE | https://ollama.com/search?c=cloud |
| RECORD COUNT | 26 |

## Previous featured 8-BALL Jets

- `qwen3.5:cloud`
- `mistral-large-3:675b-cloud`
- `qwen3-coder:480b-cloud`

## Current cloud models discovered

- `deepseek-v4-flash:0731-cloud` — Deepseek V4 Flash
- `deepseek-v4-flash:cloud` — Deepseek V4 Flash
- `deepseek-v4-flash:preview-cloud` — Deepseek V4 Flash
- `deepseek-v4-pro:cloud` — Deepseek V4 Pro
- `devstral-2:123b-cloud` — Devstral 2
- `devstral-small-2:24b-cloud` — Devstral Small 2
- `gemini-3-flash-preview:cloud` — Gemini 3 Flash Preview
- `gemma4:31b-cloud` — Gemma4
- `gemma4:cloud` — Gemma4
- `glm-5.1:cloud` — Glm 5.1
- `glm-5.2:cloud` — Glm 5.2
- `gpt-oss:120b-cloud` — Gpt Oss
- `gpt-oss:20b-cloud` — Gpt Oss
- `kimi-k2.6:cloud` — Kimi K2.6
- `kimi-k2.7-code:cloud` — Kimi K2.7 Code
- `kimi-k3:cloud` — Kimi K3
- `minimax-m2.1:cloud` — Minimax M2.1
- `minimax-m2.7:cloud` — Minimax M2.7
- `minimax-m3:cloud` — Minimax M3
- `mistral-large-3:675b-cloud` — Mistral Large 3 (8-BALL Featured)
- `nemotron-3-nano:30b-cloud` — Nemotron 3 Nano
- `nemotron-3-super:cloud` — Nemotron 3 Super
- `nemotron-3-ultra:cloud` — Nemotron 3 Ultra
- `qwen3-coder:480b-cloud` — Qwen3 Coder (8-BALL Featured)
- `qwen3.5:397b-cloud` — Qwen3.5
- `qwen3.5:cloud` — Qwen3.5 (8-BALL Featured)

## New models not previously represented

- None (first scrape or no new models)

## Existing models updated

- None

## Models requiring human review

- `delivering-1-5-m-tps-inference-on-nvidia-gb200-nvl72-nvidia-accelerates-openai-gpt-oss-models-from-cloud` — **possibly_removed** (still listed in prior catalog)

## Deliverables

| Item | Status |
|------|--------|
| JET INDEX PAGE | `/jet-agents/catalog/` |
| INDIVIDUAL PAGES | `/jet-agents/<slug>/` (26 pages) |
| DATA FILES | `data/jet-agents/raw/`, `data/jet-agents/normalized/` |
| REFRESH TOOLING | `scripts/jet-agents/` |

## Known gaps

- 8-BALL repository (`funtech64/8-BALL`) was not accessible in this workspace; featured Jet tags sourced from terminalglass-html model pages.
- License and parameter metadata is only recorded when explicitly stated on Ollama library pages.
- Models absent from Ollama cloud search but present in legacy terminal.glass inventory are flagged when not re-discovered.

## Recommended next scrape

Re-run monthly or when Ollama announces new cloud models:

```bash
python3 scripts/jet-agents/scrape-ollama-cloud.py
python3 scripts/jet-agents/refresh-catalog.py
python3 scripts/jet-agents/generate-jet-agent-pages.py
python3 scripts/jet-agents/generate-jet-agent-index.py
python3 scripts/jet-agents/update-sitemap.py
python3 scripts/validate-site.py
```
