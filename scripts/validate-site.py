#!/usr/bin/env python3
"""Validate terminal.glass static site — base checks plus B1 product-truth gates."""

import os
import re
import sys
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urljoin

ROOT = "/workspace"
BASE = "https://terminal.glass"
ERRORS = []
WARNINGS = []

INTERNAL_DOC_GLOBS = (
    "agents/cursorFileB1.md",
    "LAUNCH-READINESS.md",
    "PRODUCT-COPY-AUDIT-B1.md",
    "PRODUCT-TRUTH.md",
    "OWNER-DECISIONS-B1.md",
    "README.md",
    "terminal-glass-artwork-plan.md",
    "models/terminal-glass_cloudModels.md",
    "models/AGENTS.txt",
)


class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.in_title = False
        self.h1 = []
        self.in_h1 = False
        self.canonical = None
        self.has_og = False
        self.has_twitter = False
        self.links = []
        self.body_text = []

    def handle_starttag(self, tag, attrs):
        d = dict(attrs)
        if tag == "title":
            self.in_title = True
        elif tag == "h1":
            self.in_h1 = True
        elif tag == "link" and d.get("rel") == "canonical":
            self.canonical = d.get("href")
        elif tag == "meta":
            prop = d.get("property", "")
            name = d.get("name", "")
            if prop.startswith("og:"):
                self.has_og = True
            if name.startswith("twitter:"):
                self.has_twitter = True
        elif tag == "a":
            self.links.append(d.get("href", ""))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        elif tag == "h1":
            self.in_h1 = False

    def handle_data(self, data):
        if self.in_title:
            self.title += data
        elif self.in_h1:
            self.h1.append(data.strip())
        self.body_text.append(data)


def collect_pages():
    pages = {}
    for root, dirs, files in os.walk(ROOT):
        if ".git" in root or "scripts" in root:
            continue
        for f in files:
            if f != "index.html":
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, ROOT)
            if rel.startswith("assets/") or os.path.getsize(path) == 0:
                continue
            if rel == "index.html":
                url_path = "/"
            else:
                url_path = "/" + rel.replace("/index.html", "/").replace("index.html", "")
            pages[url_path] = {"file": path, "rel": rel}
    return pages


def resolve(base, href):
    if not href or href.startswith("#") or href.startswith("mailto:") or href.startswith("tel:"):
        return None
    if href.startswith("http"):
        return href
    if href.startswith("/"):
        p = href.split("?")[0].split("#")[0]
        if not p.endswith("/") and "." not in os.path.basename(p):
            p = p.rstrip("/") + "/"
        return p
    base_dir = base if base.endswith("/") else base.rsplit("/", 1)[0] + "/"
    p = urljoin(base_dir, href).split("?")[0].split("#")[0]
    if not p.endswith("/") and "." not in os.path.basename(p):
        p = p.rstrip("/") + "/"
    return p


def is_internal_doc(rel):
    return rel in INTERNAL_DOC_GLOBS or rel.startswith("models/data/")


def scan_public_text(pattern, label, exclude_redirect=True):
    rx = re.compile(pattern, re.I)
    for root, _, files in os.walk(ROOT):
        if ".git" in root:
            continue
        for f in files:
            if not f.endswith((".html", ".js", ".css")):
                continue
            rel = os.path.relpath(os.path.join(root, f), ROOT)
            if is_internal_doc(rel):
                continue
            if exclude_redirect and rel == "agents/index.html":
                continue
            content = open(os.path.join(root, f)).read()
            if rx.search(content):
                ERRORS.append(f"Public {label} remains in {rel}")


def main():
    pages = collect_pages()
    print(f"Public pages: {len(pages)}")

    for path, info in pages.items():
        content = open(info["file"]).read()
        if re.search(r"\$200|\$400|Group Plan|Professional plan", content, re.I):
            ERRORS.append(f"Obsolete pricing/branding in {info['rel']}")
        if "localhost" in content or "staging." in content:
            ERRORS.append(f"Staging/localhost reference in {info['rel']}")
        if "nocloudgpt.com/pric" in content.lower():
            ERRORS.append(f"NoCloudGPT pricing link in {info['rel']}")
        if "formspree.io/f/xnjepnjq" not in content and info["rel"] == "contact/index.html":
            ERRORS.append("Contact page missing Formspree endpoint")
        if info["rel"] == "contact/index.html" and "jonathan@nocloudgpt.com" not in content:
            ERRORS.append("Contact page missing fallback email")

        p = MetaParser()
        p.feed(content)
        if info["rel"] != "agents/index.html" and not p.h1:
            ERRORS.append(f"Missing H1: {path}")
        if info["rel"] != "agents/index.html" and not p.canonical:
            WARNINGS.append(f"Missing canonical: {path}")
        elif p.canonical and not p.canonical.startswith(BASE):
            ERRORS.append(f"Wrong canonical domain on {path}: {p.canonical}")
        if info["rel"] != "agents/index.html" and not p.has_og:
            WARNINGS.append(f"Missing OG tags: {path}")

        for href in p.links:
            resolved = resolve(path, href)
            if not resolved or resolved.startswith("http"):
                continue
            if any(resolved.endswith(ext) for ext in (".css", ".js", ".webp", ".png", ".jpg", ".svg")):
                continue
            if resolved not in pages and resolved != "/agents/":
                ERRORS.append(f"Broken link {href} -> {resolved} from {path}")

        if info["rel"] == "jet-agents/index.html":
            text = " ".join(p.body_text)
            if "openclaw" not in text.lower():
                ERRORS.append("jet-agents page missing OpenClaw reference")
            if "ollama" not in text.lower():
                ERRORS.append("jet-agents page missing Ollama reference")

        if info["rel"] == "index.html":
            text = " ".join(p.body_text)
            if "no more guesswork" not in text.lower():
                ERRORS.append("Homepage missing primary headline")
            if "240" not in text:
                ERRORS.append("Homepage missing 240 model families claim")

    # Redirect page checks
    redirect_path = os.path.join(ROOT, "agents/index.html")
    if os.path.exists(redirect_path):
        redirect = open(redirect_path).read()
        if "/jet-agents/" not in redirect:
            ERRORS.append("agents/index.html redirect missing /jet-agents/ target")
        if "location.replace" not in redirect and 'http-equiv="refresh"' not in redirect:
            ERRORS.append("agents/index.html missing redirect mechanism")
        if "canonical" not in redirect or "jet-agents" not in redirect:
            ERRORS.append("agents/index.html missing canonical to jet-agents")
    else:
        ERRORS.append("Missing agents/index.html redirect")

    # B1 forbidden public terms
    scan_public_text(r"alchemist", "Alchemist reference")
    scan_public_text(r"yourcloudgpt", "YourCloudGPT public product reference")
    scan_public_text(r'href="/agents/"', "legacy /agents/ internal link", exclude_redirect=True)

    # config checks
    cfg = open(os.path.join(ROOT, "assets/js/contact-config.js")).read()
    if "xnjepnjq" not in cfg:
        ERRORS.append("contact-config.js missing Formspree endpoint")
    if "jonathan@nocloudgpt.com" not in cfg:
        ERRORS.append("contact-config.js missing fallback email")
    if "alchemist" in cfg.lower():
        ERRORS.append("contact-config.js still references Alchemist")

    pricing = open(os.path.join(ROOT, "assets/js/pricing-config.js")).read()
    for price in ("price: 199", "price: 399", "price: 99"):
        if price not in pricing:
            ERRORS.append(f"pricing-config.js missing {price}")
    if "alchemist" in pricing.lower():
        ERRORS.append("pricing-config.js still references Alchemist")

    # sitemap
    sitemap_path = os.path.join(ROOT, "sitemap.xml")
    tree = ET.parse(sitemap_path)
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    locs = [el.text.rstrip("/") + "/" if not el.text.endswith("/") else el.text for el in tree.findall(".//sm:loc", ns)]
    if not locs:
        locs = [el.text for el in tree.findall(".//{http://www.sitemaps.org/schemas/sitemap/0.9}loc")]
    sitemap_urls = set()
    for loc in locs:
        path = loc.replace(BASE, "")
        if not path:
            path = "/"
        if not path.endswith("/"):
            path += "/"
        sitemap_urls.add(path)

    page_urls = set(pages.keys()) - {"/agents/"}
    missing_from_sitemap = page_urls - sitemap_urls
    extra_in_sitemap = sitemap_urls - page_urls
    if missing_from_sitemap:
        ERRORS.append(f"Pages missing from sitemap: {sorted(missing_from_sitemap)}")
    if extra_in_sitemap:
        ERRORS.append(f"Sitemap URLs without pages: {sorted(extra_in_sitemap)}")
    if "https://terminal.glass/agents/" in locs or "/agents/" in sitemap_urls:
        ERRORS.append("Sitemap still lists legacy /agents/ URL")

    robots = open(os.path.join(ROOT, "robots.txt")).read()
    if "Allow: /" not in robots or "terminal.glass/sitemap.xml" not in robots:
        ERRORS.append("robots.txt incorrect")

    print(f"Sitemap URLs: {len(sitemap_urls)}")
    print(f"Errors: {len(ERRORS)}")
    for e in ERRORS:
        print("  ERROR:", e)
    print(f"Warnings: {len(WARNINGS)}")
    for w in WARNINGS[:10]:
        print("  WARN:", w)

    return 1 if ERRORS else 0


if __name__ == "__main__":
    sys.exit(main())
