#!/usr/bin/env python3
"""Compare current normalized catalog against previous scrape; write status + review report."""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "jet-agents"
NORM = DATA / "normalized"
REPORT_DIR = ROOT / "AGENTS" / "reports"


def load_catalog(path: Path) -> dict:
    if not path.exists():
        return {"agents": []}
    return json.loads(path.read_text())


def agent_key(agent: dict) -> str:
    return agent.get("ollama_tag") or agent.get("slug", "")


def main() -> int:
    catalog_path = NORM / "catalog.json"
    status_path = NORM / "catalog-status.json"
    prev_path = NORM / "catalog-previous.json"

    current = load_catalog(catalog_path)
    previous = load_catalog(prev_path)

    cur_map = {agent_key(a): a for a in current.get("agents", [])}
    prev_map = {agent_key(a): a for a in previous.get("agents", [])}

    new_models = sorted(set(cur_map) - set(prev_map))
    removed_models = sorted(set(prev_map) - set(cur_map))
    common = set(cur_map) & set(prev_map)

    changed = []
    for tag in sorted(common):
        cur = cur_map[tag]
        prev = prev_map[tag]
        diff_fields = []
        for field in (
            "description", "context_length", "parameter_size", "capabilities",
            "classifications", "publisher", "license", "primary_cloud_tag",
        ):
            if cur.get(field) != prev.get(field):
                diff_fields.append(field)
        if diff_fields:
            changed.append({"ollama_tag": tag, "changed_fields": diff_fields})

    statuses = []
    for tag, agent in cur_map.items():
        if tag in new_models:
            status = "new"
        elif tag in changed:
            status = "changed"
        else:
            status = "current"
        statuses.append({**agent, "catalog_status": status})

    for tag in removed_models:
        prev = prev_map[tag]
        statuses.append({
            **prev,
            "catalog_status": "possibly_removed",
            "scrape_date": current.get("scrape_date"),
        })

    status_payload = {
        "comparison_date": date.today().isoformat(),
        "current_scrape_date": current.get("scrape_date"),
        "previous_scrape_date": previous.get("scrape_date"),
        "new_models": new_models,
        "possibly_removed": removed_models,
        "changed": changed,
        "agents": statuses,
    }
    status_path.write_text(json.dumps(status_payload, indent=2) + "\n")

    report = build_report(current, previous, new_models, removed_models, changed, statuses)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    report_path = REPORT_DIR / "jet-agent-catalog-refresh.md"
    report_path.write_text(report)

    print(f"Wrote {status_path}")
    print(f"Wrote {report_path}")
    print(f"  new: {len(new_models)}, changed: {len(changed)}, possibly_removed: {len(removed_models)}")
    return 0


def build_report(current, previous, new_models, removed_models, changed, statuses) -> str:
    scrape_date = current.get("scrape_date", "unknown")
    source = current.get("source_url", "https://ollama.com/search?c=cloud")
    featured = json.loads((NORM / "featured-8ball.json").read_text()).get("featured_cloud_tags", [])

    lines = [
        "# Jet Agent Catalog Refresh Report",
        "",
        f"**Report date:** {date.today().isoformat()}",
        "",
        "## Scrape metadata",
        "",
        f"| Field | Value |",
        f"|-------|-------|",
        f"| SCRAPE DATE | {scrape_date} |",
        f"| OLLAMA SOURCE | {source} |",
        f"| RECORD COUNT | {len(current.get('agents', []))} |",
        "",
        "## Previous featured 8-BALL Jets",
        "",
    ]
    for tag in featured:
        lines.append(f"- `{tag}`")
    lines += [
        "",
        "## Current cloud models discovered",
        "",
    ]
    for a in sorted(current.get("agents", []), key=lambda x: x.get("ollama_tag", "")):
        feat = " (8-BALL Featured)" if a.get("eight_ball_featured") else ""
        lines.append(f"- `{a.get('ollama_tag')}` — {a.get('display_name')}{feat}")

    lines += ["", "## New models not previously represented", ""]
    if new_models:
        for tag in new_models:
            lines.append(f"- `{tag}`")
    else:
        lines.append("- None (first scrape or no new models)")

    lines += ["", "## Existing models updated", ""]
    if changed:
        for item in changed:
            lines.append(f"- `{item['ollama_tag']}` — fields: {', '.join(item['changed_fields'])}")
    else:
        lines.append("- None")

    lines += ["", "## Models requiring human review", ""]
    review = [s for s in statuses if s.get("catalog_status") == "possibly_removed"]
    if review:
        for s in review:
            lines.append(f"- `{s.get('ollama_tag')}` — **possibly_removed** (still listed in prior catalog)")
    else:
        lines.append("- None")

    lines += [
        "",
        "## Deliverables",
        "",
        "| Item | Status |",
        "|------|--------|",
        "| JET INDEX PAGE | `/jet-agents/catalog/` |",
        f"| INDIVIDUAL PAGES | `/jet-agents/<slug>/` ({len(current.get('agents', []))} pages) |",
        "| DATA FILES | `data/jet-agents/raw/`, `data/jet-agents/normalized/` |",
        "| REFRESH TOOLING | `scripts/jet-agents/` |",
        "",
        "## Navigation and SEO changes",
        "",
        "- Added `/jet-agents/catalog/` Jet Agent index with category sections",
        "- Linked catalog from `/jet-agents/`, `/models/` Jet Models panel, and footer Explore columns",
        f"- Added {len(current.get('agents', []))} individual Jet Agent pages under `/jet-agents/<slug>/`",
        "- Updated `sitemap.xml` with Jet Agent catalog URLs",
        "",
        "## Files modified",
        "",
        "- `data/jet-agents/` — raw scrape evidence and normalized catalog",
        "- `scripts/jet-agents/` — scrape, refresh, generate, and sitemap scripts",
        "- `jet-agents/catalog/index.html` — Jet Agent catalog index",
        "- `jet-agents/<slug>/index.html` — generated individual pages",
        "- `jet-agents/index.html` — catalog link and Jet Agent copy clarification",
        "- `models/index.html` — link to Jet Agent catalog",
        "- `assets/css/site.css` — Jet Agent page utility styles",
        "- `sitemap.xml` — Jet Agent URLs",
        "- `AGENTS/jet-agent-catalog-architecture.md` — working architecture note",
        "",
        "## Known gaps",
        "",
        "- 8-BALL repository (`funtech64/8-BALL`) was not accessible in this workspace; featured Jet tags sourced from terminalglass-html model pages.",
        "- License and parameter metadata is only recorded when explicitly stated on Ollama library pages.",
        "- Models absent from Ollama cloud search but present in legacy terminal.glass inventory are flagged when not re-discovered.",
        "",
        "## Recommended next scrape",
        "",
        "Re-run monthly or when Ollama announces new cloud models:",
        "",
        "```bash",
        "python3 scripts/jet-agents/scrape-ollama-cloud.py",
        "python3 scripts/jet-agents/refresh-catalog.py",
        "python3 scripts/jet-agents/generate-jet-agent-pages.py",
        "python3 scripts/jet-agents/generate-jet-agent-index.py",
        "python3 scripts/jet-agents/update-sitemap.py",
        "python3 scripts/validate-site.py",
        "```",
        "",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    sys.exit(main())
