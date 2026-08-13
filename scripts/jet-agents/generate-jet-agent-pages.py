#!/usr/bin/env python3
"""Generate individual Jet Agent pages from normalized catalog data."""

from __future__ import annotations

import html
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CATALOG = ROOT / "data" / "jet-agents" / "normalized" / "catalog.json"
OUT_BASE = ROOT / "jet-agents"

CLASS_LABELS = {
    "general-chat": "General / Chat",
    "reasoning": "Reasoning",
    "coding": "Coding",
    "vision-multimodal": "Vision / Multimodal",
    "tool-use": "Tool Use",
    "long-context": "Long Context",
    "agentic-work": "Agentic Work",
    "lightweight-fast": "Lightweight / Fast",
    "enterprise-large": "Enterprise / Large Workloads",
}


def esc(value) -> str:
    return html.escape(str(value) if value not in (None, "") else "not stated")


def yn(value) -> str:
    if value is True:
        return "Yes"
    if value is False:
        return "No"
    return "not stated"


def model_brief_link(agent: dict) -> str | None:
    family = agent.get("ollama_family", "")
    candidates = [
        f"{family}-cloud",
        family.replace(".", "-") + "-cloud",
    ]
    for slug in candidates:
        path = ROOT / "models" / slug / "index.html"
        if path.exists() and path.stat().st_size > 500:
            return f"/models/{slug}/"
    return None


def render_page(agent: dict, scrape_date: str) -> str:
    slug = agent["slug"]
    tag = agent["ollama_tag"]
    featured_badge = ""
    if agent.get("eight_ball_featured"):
        featured_badge = '<span class="tag tag-featured">8-BALL Featured Jet</span>'

    classifications = agent.get("classifications", [])
    class_items = "".join(
        f"<li>{esc(CLASS_LABELS.get(c, c))}</li>" for c in classifications
    )
    rec_work = "".join(f"<li>{esc(w)}</li>" for w in agent.get("recommended_work", []))
    caps = ", ".join(esc(c) for c in agent.get("capabilities", []))

    model_link = model_brief_link(agent)
    model_brief_block = ""
    if model_link:
        model_brief_block = f'<p class="section-link"><a href="{model_link}">Read the Terminal.Glass model brief →</a></p>'

    title = f"{agent['display_name']} — Jet Agent | Terminal.Glass"
    description = (
        f"{agent.get('description', '')[:155]} "
        f"Ollama cloud tag: {tag}. Catalog verified {scrape_date}."
    ).strip()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="https://terminal.glass/jet-agents/{slug}/">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:url" content="https://terminal.glass/jet-agents/{slug}/">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(description)}">
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
    <p class="section-link" style="margin-bottom:1rem;"><a href="/jet-agents/catalog/">← Jet Agent catalog</a></p>
    <span class="kicker">Jet Agent</span>
    {featured_badge}
    <h1>{esc(agent['display_name'])}</h1>
    <p class="lead">{esc(agent.get('description', 'not stated'))}</p>
    <p class="hero-tagline">Ollama cloud tag: <code>{esc(tag)}</code></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="grid-2">
      <div class="card">
        <span class="tag">CLOUD</span>
        <h2>How Jet Agents work</h2>
        <p>Jet Agents use cloud-hosted models through Ollama. The model runs on remote compute rather than requiring your server to hold the full model weights in RAM or VRAM. Your team keeps the familiar local Ollama workflow — sign in, pull or run the cloud tag, and interact through Terminal.Glass.</p>
        <p>This is not a Glass Agent. Glass Agents are OpenClaw-powered workers that operate through approved tools inside your environment. Jet Agents are model endpoints backed by Ollama Cloud.</p>
      </div>
      <div class="card">
        <span class="tag">METADATA</span>
        <h2>Catalog facts</h2>
        <dl class="meta-dl">
          <dt>Publisher</dt><dd>{esc(agent.get('publisher'))}</dd>
          <dt>Context</dt><dd>{esc(agent.get('context_length'))}</dd>
          <dt>Parameters</dt><dd>{esc(agent.get('parameter_size'))}</dd>
          <dt>License</dt><dd>{esc(agent.get('license'))}</dd>
          <dt>Cloud status</dt><dd>{'Listed on Ollama cloud catalog' if agent.get('cloud_designation') else 'not stated'}</dd>
          <dt>Vision</dt><dd>{yn(agent.get('vision_support'))}</dd>
          <dt>Tools</dt><dd>{yn(agent.get('tool_support'))}</dd>
          <dt>Thinking / reasoning</dt><dd>{yn(agent.get('thinking_support'))}</dd>
          <dt>Capabilities</dt><dd>{caps}</dd>
          <dt>Catalog verified</dt><dd>{esc(scrape_date)}</dd>
        </dl>
      </div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <span class="kicker">Classification</span>
    <h2>Terminal.Glass categories</h2>
    <p class="section-sub">Categories are based on capabilities stated on Ollama. They are not performance rankings.</p>
    <ul class="bullet-list">{class_items}</ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <span class="kicker">Recommended work</span>
    <h2>Kinds of work this Jet Agent supports</h2>
    <ul class="bullet-list">{rec_work if rec_work else '<li>General cloud inference through Ollama</li>'}</ul>
    {model_brief_block}
  </div>
</section>

<section class="section section-alt">
  <div class="wrap">
    <span class="kicker">Official source</span>
    <h2>Ollama reference</h2>
    <p class="section-sub">This page reflects information available from Ollama and upstream model sources as of <strong>{esc(scrape_date)}</strong>. Cloud availability and tags can change — confirm on Ollama before deployment.</p>
    <pre class="code-block"><code>ollama signin
ollama run {esc(tag)}</code></pre>
    <p class="section-link"><a href="{esc(agent.get('official_url'))}" rel="noopener noreferrer">View on ollama.com →</a></p>
    <p class="fine-print">Terminal.Glass does not publish local hardware requirements for cloud models. Inference runs on Ollama Cloud compute.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cta-row">
      <a class="btn btn-primary" href="/contact/?interest=Jet+Agents">Plan a Jet Agent deployment</a>
      <a class="btn btn-secondary" href="/jet-agents/catalog/">Browse all Jet Agents</a>
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


def main() -> int:
    if not CATALOG.exists():
        print("Run scrape-ollama-cloud.py first.", file=sys.stderr)
        return 1

    data = json.loads(CATALOG.read_text())
    scrape_date = data.get("scrape_date", "unknown")
    agents = data.get("agents", [])
    active_slugs = {a["slug"] for a in agents}
    generated = 0

    # Remove stale generated pages not in current catalog
    if OUT_BASE.exists():
        for child in OUT_BASE.iterdir():
            if child.is_dir() and child.name not in active_slugs and child.name not in ("catalog", "_template"):
                import shutil
                shutil.rmtree(child)

    for agent in agents:
        slug = agent["slug"]
        out_dir = OUT_BASE / slug
        out_dir.mkdir(parents=True, exist_ok=True)
        page = render_page(agent, scrape_date)
        (out_dir / "index.html").write_text(page)
        generated += 1

    print(f"Generated {generated} Jet Agent pages under {OUT_BASE}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
