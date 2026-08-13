#!/usr/bin/env python3
"""Generate the Jet Agent catalog index page at /jet-agents/catalog/."""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "data" / "jet-agents" / "normalized" / "catalog.json"
OUT = ROOT / "jet-agents" / "catalog" / "index.html"

SECTION_ORDER = [
    ("featured", "Featured 8-BALL Jets", lambda a: a.get("eight_ball_featured")),
    ("general", "General / Reasoning", lambda a: "general-chat" in a.get("classifications", []) or "reasoning" in a.get("classifications", [])),
    ("coding", "Coding", lambda a: "coding" in a.get("classifications", [])),
    ("vision", "Vision / Multimodal", lambda a: "vision-multimodal" in a.get("classifications", [])),
    ("agentic", "Agentic / Tools", lambda a: "agentic-work" in a.get("classifications", []) or "tool-use" in a.get("classifications", [])),
]

CLASS_LABELS = {
    "general-chat": "General",
    "reasoning": "Reasoning",
    "coding": "Coding",
    "vision-multimodal": "Vision",
    "tool-use": "Tools",
    "long-context": "Long context",
    "agentic-work": "Agentic",
    "lightweight-fast": "Lightweight",
    "enterprise-large": "Enterprise",
}


def esc(v) -> str:
    return html.escape(str(v))


def card(agent: dict) -> str:
    slug = agent["slug"]
    tag = agent["ollama_tag"]
    cats = ", ".join(CLASS_LABELS.get(c, c) for c in agent.get("classifications", [])[:3])
    featured = ""
    if agent.get("eight_ball_featured"):
        featured = '<span class="catalog-label">8-BALL Featured</span>'
    else:
        featured = '<span class="catalog-label">Jet Agent</span>'
    desc = esc(agent.get("description", "")[:140])
    return f"""        <a class="catalog-card" href="/jet-agents/{slug}/">
          {featured}
          <h4>{esc(agent['display_name'])}</h4>
          <p>{desc}</p>
          <span class="catalog-meta">{esc(tag)} · {esc(cats)}</span>
        </a>"""


def section_html(title: str, agents: list[dict]) -> str:
    if not agents:
        return ""
    cards = "\n".join(card(a) for a in agents)
    return f"""      <h3 class="catalog-category">{esc(title)}</h3>
      <div class="catalog-grid">
{cards}
      </div>"""


def main() -> int:
    data = json.loads(CATALOG.read_text())
    scrape_date = data.get("scrape_date", "unknown")
    agents = data.get("agents", [])
    placed = set()

    sections = []
    for _id, title, pred in SECTION_ORDER:
        group = [a for a in agents if pred(a) and a["slug"] not in placed]
        for a in group:
            placed.add(a["slug"])
        if group:
            sections.append(section_html(title, group))

    remaining = [a for a in agents if a["slug"] not in placed]
    if remaining:
        sections.append(section_html("Full Current Catalog", remaining))

    body_sections = "\n".join(sections)
    count = len(agents)

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Jet Agents — Ollama Cloud Model Catalog | Terminal.Glass</title>
<meta name="description" content="Browse {count} Ollama cloud Jet Agents for Terminal.Glass. Cloud-hosted models run on remote compute with a familiar local Ollama workflow — including 8-BALL featured Jets.">
<link rel="canonical" href="https://terminal.glass/jet-agents/catalog/">
<meta property="og:title" content="Jet Agents — Ollama Cloud Model Catalog | Terminal.Glass">
<meta property="og:description" content="Ollama cloud models as Jet Agents — remote compute, familiar workflow. Catalog verified {scrape_date}.">
<meta property="og:url" content="https://terminal.glass/jet-agents/catalog/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Jet Agents — Ollama Cloud Model Catalog">
<meta name="twitter:description" content="Ollama cloud models as Jet Agents for Terminal.Glass deployments.">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/site.css">
</head>
<body>

<a class="skip-link" href="#main">Skip to content</a>

<header>
  <div class="wrap nav">
    <a class="brand" href="/">
      <span class="logo-mark" aria-hidden="true">T&gt;||G</span>
      <span class="brand-name">Terminal.Glass</span>
    </a>
    <nav aria-label="Main navigation">
      <input type="checkbox" id="nav-toggle" class="nav-toggle">
      <label for="nav-toggle" class="nav-toggle-label" aria-label="Toggle menu">☰</label>
      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/pricing/">Pricing</a></li>
        <li><a href="/hosting/">Hosting</a></li>
        <li><a href="/models/">Models</a></li>
        <li><a href="/jet-agents/" aria-current="page">Agents</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>
      <div class="nav-actions">
        <a class="btn btn-primary btn-sm" href="/contact/?intent=order">Contact Sales</a>
      </div>
      <div class="nav-actions-mobile">
        <a class="btn btn-primary" href="/contact/?intent=order">Contact Sales</a>
      </div>
    </nav>
  </div>
</header>

<main id="main">

<section class="page-hero page-hero-compact">
  <div class="wrap">
    <p class="section-link" style="margin-bottom:1rem;"><a href="/jet-agents/">← Agents overview</a></p>
    <span class="kicker">Jet Agents</span>
    <h1>Ollama cloud Jet Agent catalog</h1>
    <p class="lead">Jet Agents use cloud-hosted models through Ollama. The model runs on remote compute rather than requiring your server to contain enough RAM or VRAM for the full model. Your team keeps the familiar local Ollama experience — sign in, run the cloud tag, and work through Terminal.Glass.</p>
    <p class="section-sub">This catalog is separate from <a href="/jet-agents/#glass-agents">Glass Agents</a> (OpenClaw workers) and from <a href="/models/">local private models</a> sized for customer-controlled hardware. Catalog last verified <strong>{esc(scrape_date)}</strong> against <a href="https://ollama.com/search?c=cloud" rel="noopener noreferrer">Ollama's official cloud catalog</a>.</p>
  </div>
</section>

<section class="section" style="padding-top:0;">
  <div class="wrap">
    <div class="catalog-sections">
{body_sections}
    </div>
    <p class="fine-print" style="margin-top:2rem;">{count} Jet Agents listed. Metadata comes from Ollama library pages; fields marked unknown or not stated were not established by the official source. 8-BALL featured Jets remain the default installer highlights unless 8-BALL source material changes them.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <span class="kicker">Get started</span>
    <h2>Plan a Jet Agent deployment</h2>
    <p class="section-sub">Tell us which Ollama cloud models, users, and workloads you need. Terminal.Glass helps size the server and guided deployment path.</p>
    <div class="cta-row">
      <a class="btn btn-primary" href="/contact/?interest=Jet+Agents">Contact Sales</a>
      <a class="btn btn-secondary" href="/models/">Jet Model briefs</a>
    </div>
  </div>
</section>

</main>

<footer class="site-footer">
  <div class="wrap footer-grid">
    <div class="footer-brand">
      <strong>Terminal.Glass</strong>
      <p>Your business AI, on your server or in your cloud.</p>
      <p class="footer-contact"><a href="mailto:jonathan@nocloudgpt.com">jonathan@nocloudgpt.com</a></p>
    </div>
    <div class="footer-col">
      <h4>Products</h4>
      <ul>
        <li><a href="/pricing/#plans">Sunrise Starter</a></li>
        <li><a href="/pricing/#plans">Sunrise Business</a></li>
        <li><a href="/pricing/#glass-license">Glass Licenses</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Deployments</h4>
      <ul>
        <li><a href="/hosting/">Hosting</a></li>
        <li><a href="/contact/?interest=NoCloudGPT+Deployment">NoCloudGPT</a></li>
        <li><a href="/contact/?interest=AWS+or+DigitalOcean+Deployment">AWS or DigitalOcean</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Explore</h4>
      <ul>
        <li><a href="/models/">Models</a></li>
        <li><a href="/jet-agents/catalog/">Jet Agents</a></li>
        <li><a href="/jet-agents/#glass-agents">Glass Agents</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Company</h4>
      <ul>
        <li><a href="/contact/">Contact</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Technical education</h4>
      <ul>
        <li><a href="https://nocloudgpt.com/models/" rel="noopener noreferrer">NoCloudGPT</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap footer-bottom">
    <p>© 2026 terminal.glass. Portable Glass Licenses for private AI deployments.</p>
  </div>
</footer>

</body>
</html>
"""

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(page)
    print(f"Wrote {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
