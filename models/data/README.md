# Terminal Glass Cloud model data

This directory holds machine-readable inventories for **Terminal Glass Cloud** model pages (`/models/<family>-cloud/`).

## Files

| File | Purpose |
|------|---------|
| `terminal-glass-cloud-models.json` | **Active / verified** cloud models — sellable and deployable Terminal Glass Cloud pages. Must match the verified list in `../cloud-page-flat-list.md` (30 entries). |
| `terminal-glass-cloud-hold-models.json` | **Hold** candidates — not for sales or deployment yet. These families do not have confirmed Ollama `cloud` tags at last review. |

## Rules

- **Active JSON** = only models in the verified section of `cloud-page-flat-list.md`. Each entry uses `"status": "active"`.
- **Hold JSON** = models listed under “Hold / do not build as cloud pages yet”. Each entry uses `"status": "hold"`.
- Do not mix hold or unverified candidates into the active JSON.
- Terminal Glass Cloud pages are a different product lane from local **NoCloudGPT Private Instance** pages under `/models/<family>/`.
- When Ollama adds a `cloud` tag for a hold family, move the entry from hold JSON into active JSON and add the page path to the verified section of `cloud-page-flat-list.md`.

## Source of truth order

1. `../cloud-page-flat-list.md` — which cloud pages are verified vs hold
2. `terminal-glass-cloud-models.json` — active sellable inventory (feeds catalog, quote, CTAs)
3. `terminal-glass-cloud-hold-models.json` — planning only; not customer-facing sales inventory
