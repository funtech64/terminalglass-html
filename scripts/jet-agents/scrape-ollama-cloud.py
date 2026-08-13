#!/usr/bin/env python3
"""Scrape the official Ollama cloud catalog and write raw + normalized Jet Agent data."""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data" / "jet-agents"
RAW_DIR = DATA / "raw"
NORM_DIR = DATA / "normalized"
SOURCE_URL = "https://ollama.com/search?c=cloud"
TAGS_API = "https://ollama.com/api/tags?c=cloud"
FEATURED_PATH = NORM_DIR / "featured-8ball.json"

# Families known from prior terminal.glass inventory — checked even if absent from search.
LEGACY_FAMILIES = [
    "gemma3",
    "gemma4",
    "qwen3.5",
    "gpt-oss",
    "qwen3-coder",
    "nemotron-3-super",
    "glm-5",
    "minimax-m2.5",
    "glm-5.1",
    "gemini-3-flash-preview",
    "minimax-m2.7",
    "glm-4.7",
    "deepseek-v3.2",
    "minimax-m2.1",
    "qwen3-coder-next",
    "ministral-3",
    "devstral-small-2",
    "deepseek-v3.1",
    "nemotron-3-nano",
    "rnj-1",
    "kimi-k2.5",
    "kimi-k2.6",
    "devstral-2",
    "deepseek-v4-pro",
    "deepseek-v4-flash",
    "mistral-large-3",
    "minimax-m3",
    "glm-5.2",
    "kimi-k2.7-code",
    "kimi-k3",
    "nemotron-3-ultra",
]

CLASSIFICATION_RULES = [
    ("vision-multimodal", lambda c: c.get("vision_support") is True),
    ("coding", lambda c: _family_suggests_coding(c)),
    ("reasoning", lambda c: c.get("thinking_support") is True),
    ("tool-use", lambda c: c.get("tool_support") is True),
    ("agentic-work", lambda c: c.get("tool_support") is True and (
        c.get("thinking_support") is True or _family_suggests_agentic(c)
    )),
    ("long-context", lambda c: _context_tokens(c) >= 256_000),
    ("lightweight-fast", lambda c: _family_suggests_lightweight(c)),
    ("enterprise-large", lambda c: _family_suggests_enterprise(c)),
    ("general-chat", lambda c: True),
]

CODING_HINTS = (
    "coder", "code", "devstral", "codestral", "swe", "engineering", "repository",
)
AGENTIC_HINTS = ("agent", "agentic", "nemotron", "kimi-k", "glm-5")
LIGHTWEIGHT_HINTS = ("nano", "ministral", "flash", "small")
ENTERPRISE_HINTS = ("large", "675b", "397b", "480b", "ultra", "pro", "120b", "super")


def _family_suggests_coding(c: dict) -> bool:
    name = (c.get("ollama_family") or "").lower()
    desc = (c.get("description") or "").lower()
    return any(h in name or h in desc for h in CODING_HINTS)


def _family_suggests_agentic(c: dict) -> bool:
    name = (c.get("ollama_family") or "").lower()
    desc = (c.get("description") or "").lower()
    return any(h in name or h in desc for h in AGENTIC_HINTS)


def _family_suggests_lightweight(c: dict) -> bool:
    name = (c.get("ollama_family") or "").lower()
    tag = (c.get("primary_cloud_tag") or "").lower()
    return any(h in name or h in tag for h in LIGHTWEIGHT_HINTS)


def _family_suggests_enterprise(c: dict) -> bool:
    name = (c.get("ollama_family") or "").lower()
    tag = (c.get("primary_cloud_tag") or "").lower()
    params = (c.get("parameter_size") or "").lower()
    return any(h in name or h in tag or h in params for h in ENTERPRISE_HINTS)


def _context_tokens(c: dict) -> int:
    raw = c.get("context_length")
    if not raw or raw in ("unknown", "not stated"):
        return 0
    m = re.match(r"(\d+(?:\.\d+)?)\s*([KkMm])", str(raw))
    if not m:
        return 0
    val = float(m.group(1))
    unit = m.group(2).upper()
    if unit == "K":
        return int(val * 1000)
    if unit == "M":
        return int(val * 1_000_000)
    return 0


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "terminalglass-jet-catalog/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def fetch_json(url: str) -> dict:
    return json.loads(fetch(url))


def parse_search_families(search_html: str) -> list[str]:
    families = re.findall(r'href="/library/([^"?#]+)"', search_html)
    # Filter to model families on cloud search results (exclude static assets)
    return sorted({f for f in families if re.match(r"^[a-z0-9][a-z0-9._-]*$", f)})


def valid_cloud_tag(tag: str, family: str) -> bool:
    tag = tag.lower()
    if len(tag) > 80:
        return False
    if not (tag.endswith("-cloud") or tag.endswith(":cloud")):
        return False
    # Must belong to this model family
    base = tag.split(":")[0]
    if base != family and not base.startswith(family + "-"):
        return False
  # Reject URL-slug false positives (blog links, etc.)
    if base.count("-") > 8:
        return False
    return True


def parse_library_page(family: str, page_html: str) -> dict:
    title_m = re.search(r"<title>([^<]+)</title>", page_html, re.I)
    desc_m = re.search(r'<meta name="description" content="([^"]*)"', page_html, re.I)
    description = html.unescape(desc_m.group(1)).strip() if desc_m else "not stated"

    badge_text = page_html.lower()
    vision = "vision" in badge_text and f'/library/{family}' in page_html
    tools = bool(re.search(r">\s*tools\s*<", page_html, re.I))
    thinking = bool(re.search(r">\s*thinking\s*<", page_html, re.I))
    cloud = bool(re.search(r">\s*cloud\s*<", page_html, re.I)) or ":cloud" in page_html

    cloud_tags = sorted(set(
        re.findall(r"([a-z0-9][a-z0-9._-]*(?::[a-z0-9._-]+)?-cloud)", page_html, re.I)
        + re.findall(rf"({re.escape(family)}:cloud)", page_html, re.I)
        + re.findall(rf"ollama run\s+({re.escape(family)}:[^\s<'\"]+)", page_html, re.I)
    ))
    cloud_tags = [t.lower().rstrip("`'\"</") for t in cloud_tags]
    cloud_tags = [t for t in cloud_tags if valid_cloud_tag(t, family)]

    contexts = re.findall(r"(\d+[KkMm]?)\s*context", page_html, re.I)
    context_length = contexts[0] if contexts else "unknown"

    param_m = re.search(r"(\d+(?:\.\d+)?[BbMmKk]?)\s*parameters?", page_html, re.I)
    parameter_size = param_m.group(1) if param_m else "not stated"

    license_info = "not stated"
    for pattern in (
        r"license[:\s]+([A-Za-z0-9 .\-]+)",
        r"(Apache 2\.0|MIT License|Llama \d+ Community License|Gemma Terms of Use)",
    ):
        lm = re.search(pattern, page_html, re.I)
        if lm:
            license_info = html.unescape(lm.group(1)).strip()[:200]
            break

    publisher = infer_publisher(family, description)

    primary_tag = cloud_tags[0] if cloud_tags else "unknown"

    return {
        "ollama_family": family,
        "display_name": display_name_for(family, title_m.group(1) if title_m else family),
        "description": description if description else "not stated",
        "cloud_tags": cloud_tags,
        "primary_cloud_tag": primary_tag,
        "cloud_designation": cloud,
        "vision_support": vision if cloud else False if not cloud_tags else vision,
        "tool_support": tools,
        "thinking_support": thinking,
        "context_length": context_length,
        "parameter_size": parameter_size,
        "license": license_info,
        "publisher": publisher,
        "official_url": f"https://ollama.com/library/{family}",
        "capabilities": build_capabilities(vision, tools, thinking, cloud),
    }


def infer_publisher(family: str, description: str) -> str:
    desc = description.lower()
    mapping = {
        "qwen": "Alibaba Cloud (Qwen team)",
        "mistral": "Mistral AI",
        "gemma": "Google",
        "gemini": "Google",
        "deepseek": "DeepSeek",
        "glm": "Z.ai",
        "minimax": "MiniMax",
        "kimi": "Moonshot AI",
        "nemotron": "NVIDIA",
        "gpt-oss": "OpenAI (open-weight)",
        "devstral": "Mistral AI",
        "ministral": "Mistral AI",
        "rnj": "Essential AI",
    }
    for key, pub in mapping.items():
        if family.startswith(key) or key in desc:
            return pub
    return "unknown"


def display_name_for(family: str, raw_title: str) -> str:
    if raw_title and raw_title.lower() != family.lower():
        return raw_title.strip()
    return family.replace("-", " ").title()


def build_capabilities(vision: bool, tools: bool, thinking: bool, cloud: bool) -> list[str]:
    caps = []
    if cloud:
        caps.append("cloud")
    if vision:
        caps.append("vision")
    if tools:
        caps.append("tools")
    if thinking:
        caps.append("thinking")
    return caps or ["unknown"]


def slug_for(family: str, primary_tag: str) -> str:
    """Stable URL slug under /jet-agents/<slug>/."""
    if primary_tag and primary_tag != "unknown":
        return primary_tag.replace(":", "-").replace(".", "-")
    return family.replace(".", "-") + "-cloud"


def classify(record: dict) -> list[str]:
    cats = []
    for name, fn in CLASSIFICATION_RULES:
        if fn(record):
            cats.append(name)
    # Deduplicate while preserving order; drop general-chat if others exist
    seen = []
    for c in cats:
        if c not in seen:
            seen.append(c)
    if len(seen) > 1 and "general-chat" in seen:
        seen.remove("general-chat")
    return seen


def load_featured() -> list[str]:
    if FEATURED_PATH.exists():
        data = json.loads(FEATURED_PATH.read_text())
        return data.get("featured_cloud_tags", [])
    return [
        "qwen3.5:cloud",
        "mistral-large-3:675b-cloud",
        "qwen3-coder:480b-cloud",
    ]


def recommended_work(classifications: list[str]) -> list[str]:
    mapping = {
        "general-chat": "Everyday business chat and drafting",
        "reasoning": "Multi-step analysis and problem-solving",
        "coding": "Software engineering and repository work",
        "vision-multimodal": "Documents, images, and multimodal inputs",
        "tool-use": "Workflows that call external tools",
        "long-context": "Very long documents and conversation history",
        "agentic-work": "Autonomous and multi-step agent tasks",
        "lightweight-fast": "Responsive chat with lower cloud usage",
        "enterprise-large": "Demanding production workloads",
    }
    return [mapping[c] for c in classifications if c in mapping]


def main() -> int:
    scrape_date = date.today().isoformat()
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    NORM_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Fetching {SOURCE_URL} ...")
    search_html = fetch(SOURCE_URL)
    search_families = parse_search_families(search_html)

    print(f"Fetching {TAGS_API} ...")
    try:
        tags_api = fetch_json(TAGS_API)
    except (urllib.error.URLError, json.JSONDecodeError) as exc:
        print(f"Warning: tags API failed: {exc}", file=sys.stderr)
        tags_api = {"models": []}

    all_families = sorted(set(search_families) | set(LEGACY_FAMILIES))
    featured_tags = load_featured()

    raw_families = {}
    normalized = []

    for family in all_families:
        url = f"https://ollama.com/library/{family}"
        print(f"  {family} ...", end=" ", flush=True)
        try:
            page_html = fetch(url)
        except urllib.error.HTTPError as exc:
            print(f"HTTP {exc.code}")
            raw_families[family] = {"error": f"HTTP {exc.code}", "url": url}
            continue

        parsed = parse_library_page(family, page_html)
        in_search = family in search_families
        has_cloud = bool(parsed["cloud_tags"])

        raw_families[family] = {
            "url": url,
            "in_cloud_search": in_search,
            "has_cloud_tags": has_cloud,
            "cloud_tags": parsed["cloud_tags"],
            "description_excerpt": parsed["description"][:500],
            "capabilities": parsed["capabilities"],
        }
        print("ok" if has_cloud else "no cloud tags")

        if not has_cloud:
            continue

        for tag in parsed["cloud_tags"]:
            slug = slug_for(family, tag)
            record = {
                **parsed,
                "slug": slug,
                "ollama_tag": tag,
                "primary_cloud_tag": tag,
                "eight_ball_featured": tag in featured_tags,
                "classifications": [],
                "recommended_work": [],
                "catalog_status": "current",
                "scrape_date": scrape_date,
                "source_url": SOURCE_URL,
            }
            record["classifications"] = classify(record)
            record["recommended_work"] = recommended_work(record["classifications"])
            normalized.append(record)

    # Deduplicate by ollama_tag (keep first / most complete)
    by_tag: dict[str, dict] = {}
    for rec in normalized:
        tag = rec["ollama_tag"]
        if tag not in by_tag:
            by_tag[tag] = rec

    catalog = sorted(by_tag.values(), key=lambda r: (not r["eight_ball_featured"], r["display_name"].lower()))

    raw_payload = {
        "scrape_date": scrape_date,
        "source_url": SOURCE_URL,
        "tags_api_url": TAGS_API,
        "search_families": search_families,
        "legacy_families_checked": LEGACY_FAMILIES,
        "tags_api_models": tags_api.get("models", []),
        "families": raw_families,
    }

    raw_path = RAW_DIR / f"scrape-{scrape_date}.json"
    raw_path.write_text(json.dumps(raw_payload, indent=2) + "\n")
    (RAW_DIR / "scrape-latest.json").write_text(json.dumps(raw_payload, indent=2) + "\n")

    catalog_path = NORM_DIR / "catalog.json"
    prev_path = NORM_DIR / "catalog-previous.json"
    if catalog_path.exists():
        prev_path.write_text(catalog_path.read_text())
    catalog_path.write_text(json.dumps({
        "scrape_date": scrape_date,
        "source_url": SOURCE_URL,
        "record_count": len(catalog),
        "agents": catalog,
    }, indent=2) + "\n")

    # CSV export for review
    csv_path = NORM_DIR / "catalog.csv"
    import csv
    if catalog:
        fields = [
            "ollama_tag", "slug", "display_name", "publisher", "context_length",
            "parameter_size", "eight_ball_featured", "classifications", "official_url",
        ]
        with csv_path.open("w", newline="") as fh:
            writer = csv.DictWriter(fh, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            for row in catalog:
                out = dict(row)
                out["classifications"] = ";".join(row.get("classifications", []))
                writer.writerow(out)

    if not FEATURED_PATH.exists():
        FEATURED_PATH.write_text(json.dumps({
            "source": "8-BALL installer defaults (documented in terminalglass-html model pages; 8-BALL repo not available in this workspace)",
            "featured_cloud_tags": featured_tags,
            "notes": "Do not change without explicit 8-BALL source material.",
        }, indent=2) + "\n")

    print(f"\nWrote {raw_path}")
    print(f"Wrote {catalog_path} ({len(catalog)} Jet Agents)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
