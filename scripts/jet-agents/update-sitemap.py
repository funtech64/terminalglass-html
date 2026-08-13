#!/usr/bin/env python3
"""Add Jet Agent catalog pages to sitemap.xml."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "data" / "jet-agents" / "normalized" / "catalog.json"
SITEMAP = ROOT / "sitemap.xml"
BASE = "https://terminal.glass"


def main() -> int:
    data = json.loads(CATALOG.read_text())
    scrape_date = data.get("scrape_date", date.today().isoformat())
    agents = data.get("agents", [])

    jet_urls = {f"{BASE}/jet-agents/catalog/"}
    for agent in agents:
        jet_urls.add(f"{BASE}/jet-agents/{agent['slug']}/")

    content = SITEMAP.read_text()
    # Remove existing jet-agents entries (except main /jet-agents/ overview)
    content = re.sub(
        r"\s*<url>\s*<loc>https://terminal\.glass/jet-agents/[^<]+</loc>.*?</url>",
        "",
        content,
        flags=re.S,
    )

    entries = []
    for url in sorted(jet_urls):
        entries.append(f"""  <url>
    <loc>{url}</loc>
    <lastmod>{scrape_date}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.65</priority>
  </url>""")

    block = "\n".join(entries)
    content = content.replace("</urlset>", block + "\n</urlset>")
    SITEMAP.write_text(content)
    print(f"Updated sitemap with {len(jet_urls)} Jet Agent URLs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
