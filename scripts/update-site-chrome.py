#!/usr/bin/env python3
"""Batch-update terminal.glass pages with unified nav, footer, and head assets."""

import os
import re

ROOT = "/workspace"

FAVICON = '<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">\n'

SKIP_LINK = '<a class="skip-link" href="#main">Skip to content</a>\n\n'

CORE_NAV = """      <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/pricing/">Pricing</a></li>
        <li><a href="/hosting/">Hosting</a></li>
        <li><a href="/models/">Models</a></li>
        <li><a href="/jet-agents/">Agents</a></li>
        <li><a href="/contact/">Contact</a></li>
      </ul>"""

MODEL_NAV = """        <div class="flex gap-6 text-slate-400">
          <a href="/models/" class="hover:text-white">Model Briefs</a>
          <a href="/jet-agents/" class="hover:text-white">Agents</a>
          <a href="/pricing/" class="hover:text-white">Pricing</a>
          <a href="/contact/" class="hover:text-white">Contact</a>
        </div>"""

FOOTER = """<footer class="site-footer">
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
        <li><a href="/jet-agents/#glass-agents">Glass Agents</a></li>
        <li><a href="/jet-agents/#jet-agents">Jet Agents</a></li>
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
</footer>"""

MODEL_FOOTER = """  <footer class="border-t border-slate-800 bg-slate-950 px-6 py-8 text-center text-sm text-slate-500">
    <p>Terminal.Glass is an independent deployment platform. For local self-hosting guides, see <a href="https://nocloudgpt.com/models/" class="text-cyan-300 hover:text-cyan-200">NoCloudGPT</a>.</p>
    <p class="mt-3"><a href="/pricing/" class="text-cyan-300 hover:text-cyan-200">Pricing</a> · <a href="/jet-agents/" class="text-cyan-300 hover:text-cyan-200">Agents</a> · <a href="/contact/" class="text-cyan-300 hover:text-cyan-200">Contact</a></p>
  </footer>"""


def add_favicon(content):
    if 'rel="icon"' not in content:
        content = content.replace('<link rel="stylesheet"', FAVICON + '<link rel="stylesheet"', 1)
        if 'rel="icon"' not in content and '<script src="https://cdn.tailwindcss.com">' in content:
            content = content.replace('<script src="https://cdn.tailwindcss.com">', FAVICON + '<script src="https://cdn.tailwindcss.com">', 1)
        if 'rel="icon"' not in content and '<style>' in content:
            content = content.replace('<style>', FAVICON + '<style>', 1)
    return content


def add_skip_link(content):
    if 'skip-link' not in content and 'site.css' in content:
        content = content.replace('<body>\n\n<header>', '<body>\n\n' + SKIP_LINK + '<header>', 1)
        content = content.replace('<body>\n\n<header ', '<body>\n\n' + SKIP_LINK + '<header ', 1)
    if '<main>' in content and 'id="main"' not in content:
        content = content.replace('<main>', '<main id="main">', 1)
    return content


def replace_core_nav(content, current_page=None):
    content = re.sub(
        r'<ul>\s*<li><a href="/">Home</a></li>.*?</ul>',
        CORE_NAV,
        content,
        count=1,
        flags=re.DOTALL,
    )
    if current_page == 'pricing':
        content = content.replace('<li><a href="/pricing/">Pricing</a></li>', '<li><a href="/pricing/" aria-current="page">Pricing</a></li>', 1)
    elif current_page == 'contact':
        content = content.replace('<li><a href="/contact/">Contact</a></li>', '<li><a href="/contact/" aria-current="page">Contact</a></li>', 1)
    elif current_page == 'hosting':
        content = content.replace('<li><a href="/hosting/">Hosting</a></li>', '<li><a href="/hosting/" aria-current="page">Hosting</a></li>', 1)
    elif current_page == 'models':
        content = content.replace('<li><a href="/models/">Models</a></li>', '<li><a href="/models/" aria-current="page">Models</a></li>', 1)
    elif current_page == 'jet-agents':
        content = content.replace('<li><a href="/jet-agents/">Agents</a></li>', '<li><a href="/jet-agents/" aria-current="page">Agents</a></li>', 1)
    # normalize CTA labels
    content = content.replace('Pricing &amp; Order Now', 'Pricing')
    content = content.replace('Start Your Order', 'Contact Sales')
    return content


def replace_core_footer(content):
    content = re.sub(r'<footer[^>]*>.*?</footer>', FOOTER, content, count=1, flags=re.DOTALL)
    return content


def replace_model_nav(content):
    content = re.sub(
        r'<div class="flex gap-6 text-slate-400">.*?</div>\s*</nav>',
        MODEL_NAV + '\n      </nav>',
        content,
        count=1,
        flags=re.DOTALL,
    )
    return content


def update_model_footer(content):
    # Replace varied footers with standard model footer
    if 'tailwindcss' in content or 'bg-slate-950' in content:
        content = re.sub(
            r'<footer class="border-t border-slate-800.*?</footer>',
            MODEL_FOOTER.strip(),
            content,
            count=1,
            flags=re.DOTALL,
        )
    return content


CORE_PAGES = {
    'index.html': None,
    'pricing/index.html': 'pricing',
    'contact/index.html': 'contact',
    'hosting/index.html': 'hosting',
    'models/index.html': 'models',
}

for rel, page in CORE_PAGES.items():
    path = os.path.join(ROOT, rel)
    if not os.path.exists(path):
        continue
    with open(path) as f:
        c = f.read()
    orig = c
    c = add_favicon(c)
    c = add_skip_link(c)
    c = replace_core_nav(c, page)
    c = replace_core_footer(c)
    if c != orig:
        with open(path, 'w') as f:
            f.write(c)
        print('updated core', rel)

# deepseek-v3.1 inline footer
path = os.path.join(ROOT, 'models/deepseek-v3.1-cloud/index.html')
if os.path.exists(path):
    with open(path) as f:
        c = f.read()
    c = add_favicon(c)
    c = replace_core_nav(c)
    c = re.sub(r'<footer>.*?</footer>', FOOTER, c, count=1, flags=re.DOTALL)
    c = c.replace('<main>', '<main id="main">', 1)
    with open(path, 'w') as f:
        f.write(c)
    print('updated deepseek-v3.1')

for root, dirs, files in os.walk(os.path.join(ROOT, 'models')):
    for f in files:
        if f != 'index.html':
            continue
        rel = os.path.relpath(os.path.join(root, f), ROOT)
        if rel == 'models/index.html' or rel == 'models/deepseek-v3.1-cloud/index.html':
            continue
        path = os.path.join(ROOT, rel)
        if os.path.getsize(path) == 0:
            continue
        with open(path) as fh:
            c = fh.read()
        orig = c
        c = add_favicon(c)
        if 'tailwindcss' in c:
            c = replace_model_nav(c)
            c = update_model_footer(c)
        if c != orig:
            with open(path, 'w') as fh:
                fh.write(c)
            print('updated model', rel)

print('done')
