# terminal.glass Launch Readiness Audit

**Repository:** funtech64/terminalglass-html  
**Domain:** https://terminal.glass  
**Audit date:** 2026-07-16  
**Public pages reviewed:** 33  
**Excluded:** `assets/components/order-panel.html` (fragment), `models/minimax-m2.1-cloud/index.html` (empty stub), internal docs under `models/data/`

---

## Launch Readiness Scores (Post-Fix)

| Area | Score | Notes |
|------|-------|-------|
| Branding | 8/10 | Core site consistent; 8 legacy model briefs retain educational tone and “Terminal Glass” spelling |
| Navigation | 8.5/10 | Unified nav on all pages; no dedicated Agents page exists yet |
| SEO | 8.5/10 | Canonical, OG, and Twitter tags on all pages; model briefs lack JSON-LD |
| Metadata | 9/10 | Unique titles/descriptions; all pages have H1 |
| Commercial messaging | 9/10 | Pricing page authoritative; homepage/hosting updated to Sunrise packages |
| Conversion | 8.5/10 | Strong CTAs on core pages; model catalog now has bottom CTA block |
| Accessibility | 7/10 | Good heading order; model pages use Tailwind CDN without skip links |
| Performance | 7/10 | 27 model pages load Tailwind from CDN; no image lazy-loading |
| **Overall production readiness** | **8/10** | Ready for sitemap submission after deploy; follow-up items below |

---

## 1. Public Pages Reviewed

### Core commercial pages (5)

| URL | Title | H1 | Nav | Footer |
|-----|-------|-----|-----|--------|
| `/` | Terminal.Glass — Private AI on One Computer, Over 100 Models | Private AI. One Computer. Over 100 Models. | ✓ | ✓ |
| `/pricing/` | terminal.glass Pricing \| Private AI Servers, Cloud Deployments, and Glass Licenses | Private AI pricing that grows with your business | ✓ | ✓ |
| `/hosting/` | Hosting — Terminal.Glass \| Private AI Deployment Options | Where should your private AI server run? | ✓ | ✓ |
| `/models/` | Models — Terminal.Glass \| Jet Models and Private AI Catalog | Choose the AI models your team needs. | ✓ | ✓ |
| `/contact/` | Contact terminal.glass \| Private AI Sales and Deployment Help | Let's build your private AI platform. | ✓ | ✓ |

### Jet Model brief pages (28)

All at `https://terminal.glass/models/{slug}-cloud/` — linked from `/models/` catalog. Each has unique title, description, H1, canonical URL, Open Graph tags, compact nav (Terminal.Glass · Model Briefs · Pricing · Contact), and footer.

**Template variants:**
- **site.css** — 5 core pages
- **Tailwind CDN (compact brief)** — 19 pages (e.g. gemma3-cloud, deepseek-v3.2-cloud)
- **Tailwind CDN (educational legacy)** — 8 pages (qwen3.5-cloud, glm-5.2-cloud, rnj-1-cloud, etc.)
- **Inline CSS** — 1 page (deepseek-v3.1-cloud)

---

## 2. Cosmetic Inconsistencies

| Issue | Pages affected | Status |
|-------|----------------|--------|
| Two visual systems (site.css vs Tailwind slate) | Core vs model briefs | **Accepted** — preserves existing design; not a redesign |
| Legacy educational layout (wider hero, plain-English H1s) | 8 model briefs | **Partially addressed** — nav/footer/canonical fixed; copy tone intentionally educational |
| `deepseek-v3.1-cloud` uses inline CSS matching site tokens | 1 page | **Accepted** — distinct but on-brand |
| Homepage previously used “Starter, Business, or Professional” | `/`, `/hosting/` | **Fixed** → Sunrise Starter / Sunrise Business |
| `minimax-m3-cloud` had corrupted duplicate HTML | 1 page | **Fixed** |
| Footer on core pages lacks Products/Privacy/Terms/GitHub sections | All core pages | **Open** — see recommendations |
| No shared header/footer component (duplicated markup) | All pages | **Open** — maintenance risk, not launch-blocking |

---

## 3. Navigation Issues

### Current primary navigation (consistent across core pages)

Home · Pricing & Order Now · Hosting · Models · Contact · **Start Your Order** (CTA)

### Model brief compact navigation

Terminal.Glass · Model Briefs · Pricing · Contact

### Issues found and resolved

| Issue | Resolution |
|-------|------------|
| 8 legacy pages used NoCloudGPT brand in header | **Fixed** → Terminal.Glass |
| Legacy nav linked to `/deploy/lightsail-guide.html`, `/quote.html` | **Fixed** → `/hosting/`, `/contact/` |
| `ministral-3-cloud` linked to `/pricing.html`, `/contact.html`, `/deploy.html` | **Fixed** → proper paths |
| 26 model pages linked to non-existent `/deploy/{slug}/` routes | **Fixed** → `/contact/?intent=order` |

### Open items

- **No `/agents/` page** — Glass Agents and Jet Agents are described on Pricing and Contact but have no dedicated landing page. Do not add to primary nav until the page exists.
- **Nav label inconsistency:** Core nav says “Pricing & Order Now”; model briefs say “Pricing”. Low priority.
- **Hosting vs Deploy:** User guide suggested “Hosting or Deploy”; site correctly uses **Hosting** (page exists).

---

## 4. Metadata Issues

### Before audit

- Missing canonical: `/`, `/hosting/`, `/models/`
- Missing Open Graph: all core pages + most model briefs
- Wrong canonical (nocloudgpt.com): 8 legacy model pages
- Duplicate titles/descriptions: none found
- Missing H1: none found

### After fixes

- **All 33 pages** have unique `<title>`, meta description, canonical URL, and Open Graph title/description.
- **Twitter Card** (`summary_large_image`) added to all pages.
- Legacy pages retain longer educational titles (e.g. “A Do-It-All AI…”) — unique and indexable; optional future normalization.

---

## 5. SEO Issues

| Check | Status |
|-------|--------|
| Unique titles | ✓ All pages |
| Unique meta descriptions | ✓ All pages |
| Canonical URLs | ✓ All point to terminal.glass |
| Open Graph tags | ✓ All pages |
| Twitter Card tags | ✓ All pages |
| robots.txt compatibility | ✓ `Allow: /` |
| Heading hierarchy | ✓ H1 present on every page; model briefs use H2 sections |
| Alt text | ✓ Hero images on legacy pages have alt text; core pages use aria-label on diagrams |
| Structured data | ✓ Pricing page has JSON-LD via `pricing-page.js`; other pages lack schema |
| Internal linking | ✓ All public pages reachable from `/models/` or core nav |
| Semantic HTML | ✓ `<main>`, `<nav>`, `<footer>`, `<article>` where appropriate |

### Remaining SEO opportunities

- Add `WebSite` + `Organization` JSON-LD on homepage
- Add `Product` or `SoftwareApplication` schema on model briefs
- Add `og:image` to core pages (currently only some model briefs have hero images)
- Normalize legacy page titles to “{Model} Cloud — Model Brief | Terminal.Glass” format

---

## 6. Broken Links

### Before audit: 111 broken internal links

Primary causes:
- `/deploy/*` routes (copied from NoCloudGPT, never existed on terminal.glass)
- `/quote.html`, `/pricing.html`, `/contact.html`, `/deploy.html`
- Internal NoCloudGPT model paths (`/models/qwen3.5/`, `/models/glm5/`) on terminal.glass

### After fixes: 0 broken internal page links

External NoCloudGPT links (`https://nocloudgpt.com/models/...`) are **intentional** for local/self-hosting education.

---

## 7. Internal Linking Improvements

**Implemented:**
- Model brief CTAs now route to `/contact/?intent=order`, `/pricing/`, `/contact/`
- Legacy private-instance links point to `https://nocloudgpt.com/models/...`
- Models catalog links to all 28 Jet Model briefs
- Homepage highlights 6 model briefs + catalog link
- Models page bottom CTA: Start with Sunrise · View Pricing · Contact Sales

**Recommended:**
- Add “Glass Agents” and “Jet Agents” anchor sections on `/pricing/` linked from model briefs
- Cross-link `/hosting/` from every model brief “Learn More” section
- Add footer link to NoCloudGPT on core pages (currently only on some model footers)

---

## 8. Cross-Site Branding Recommendations

| Site | Role | Link strategy |
|------|------|---------------|
| **terminal.glass** | Commercial — Glass Licenses, Sunrise packages, deployment, Jet Agents | Primary domain for indexing and conversion |
| **NoCloudGPT** | Educational — local AI, self-hosting, model catalog | Linked from model briefs “Learn More” and Private Models tab |

**Implemented:**
- Legacy pages no longer canonicalize to nocloudgpt.com
- Private-instance references link out to nocloudgpt.com
- Footers on updated legacy pages mention Terminal.Glass first with NoCloudGPT cross-link

**Recommended for NoCloudGPT (external repo):**
- Ensure nocloudgpt.com pages link back to terminal.glass `/pricing/`, `/contact/`, `/hosting/`
- Align “Get a Quote” CTAs on NoCloudGPT to terminal.glass `/contact/?intent=order`
- Use `rel=canonical` on NoCloudGPT only for nocloudgpt.com URLs

---

## 9. Commercial Messaging Verification

### Authoritative pricing (from `assets/js/pricing-config.js`)

| Package | Price | Glass Licenses |
|---------|-------|----------------|
| Sunrise Starter | $199 | 2 |
| Sunrise Business | $399 | 6 |
| Additional Glass License | $99 | 1 (expansion) |

**One Glass License = one active deployment** supporting NoCloudGPT, YourCloudGPT, Glass Agents, or Jet Agents.

### Issues found and fixed

| Location | Issue | Fix |
|----------|-------|-----|
| Homepage `#packages` | “Starter, Business, or Professional” (obsolete) | Updated to Sunrise Starter / Sunrise Business with prices |
| `/hosting/` step 1 | Referenced old plan names | Updated to Sunrise packages |

### Verified correct

- `/pricing/` — full plan cards, comparison table, FAQs, structured data
- `/contact/` — Glass License and Sunrise package intent parameters
- Pricing config — no conflicting package structures

---

## 10. Conversion Review

| Page | Primary CTAs | Status |
|------|--------------|--------|
| Home | Start Your Order, Browse Models, Pricing & Order Now | ✓ Strong |
| Pricing | Get Sunrise Starter, Choose Sunrise Business, Add a Glass License | ✓ Strong |
| Contact | Form with package/intent prefill | ✓ Strong |
| Hosting | Start Your Order, Contact Us, Compare pricing | ✓ Good |
| Models | **Added** Start with Sunrise, View Pricing, Contact Sales | ✓ Fixed |
| Model briefs | Deploy with Terminal.Glass, View Pricing, Contact | ✓ Good |
| Legacy model briefs | Get quote → now `/contact/?intent=order` | ✓ Fixed |

**No dead-end pages** — every public page has at least one path to contact or pricing.

---

## 11. Footer Review

### Current footer (core pages)

Terminal.Glass blurb + links: Home · Pricing · Hosting · Models · Contact

### Gaps vs recommended structure

| Section | Present | Notes |
|---------|---------|-------|
| Products | Partial | Models + Hosting implied, not labeled “Products” |
| Pricing | ✓ | |
| Contact | ✓ | |
| Privacy | ✗ | No privacy page in repo |
| Terms | ✗ | No terms page in repo |
| GitHub | ✗ | Not linked |
| Copyright | ✗ | No © line |
| NoCloudGPT cross-link | Partial | On some model footers only |

---

## 12. robots.txt

**No changes required.**

```
User-agent: *
Allow: /

Sitemap: https://terminal.glass/sitemap.xml
```

Verified: allows all crawlers, correct sitemap location.

---

## 13. sitemap.xml Changes

### Before
- 5 URLs (core pages only)
- lastmod: 2026-07-10

### After
- **33 URLs** — all legitimate public routes
- lastmod: file modification dates (2026-07-16 for updated pages)
- Excluded: empty stub `minimax-m2.1-cloud`, component fragments, internal docs

**Priority scheme:**
- `/` — 1.0
- `/pricing/`, `/hosting/` — 0.9
- `/contact/`, `/models/` — 0.8
- Model briefs — 0.6

---

## 14. Performance & Accessibility

### Performance
- Static HTML — fast baseline
- Tailwind CDN on 27 model pages adds ~100KB+ JS parse on first visit
- Hero `.webp` images present on 21 model folders; no explicit `loading="lazy"` on below-fold images
- No build pipeline — no bundle optimization

### Accessibility
- Core pages: mobile nav toggle with `aria-label`, `aria-current` on active nav item
- Model lane tabs on `/models/`: proper `role="tablist"`, `aria-selected`, keyboard arrow support
- Diagram regions use `role="img"` + `aria-label`
- Model brief pages: no skip-to-content link
- Color contrast on slate/cyan Tailwind pages appears adequate but not formally tested

### Practical improvements
1. Add `loading="lazy"` to hero/secondary images on model briefs
2. Preconnect to `cdn.tailwindcss.com` or migrate model briefs to compiled CSS subset
3. Add skip link on all pages: `<a href="#main" class="skip-link">Skip to content</a>`

---

## 15. Orphan & Duplicate Analysis

| Category | Finding |
|----------|---------|
| Orphan pages | **None** — all 33 pages linked from nav or `/models/` catalog |
| Duplicate pages | **None** — unique URLs and content per page |
| Duplicate titles | **None** |
| Duplicate descriptions | **None** |
| Stub excluded | `models/minimax-m2.1-cloud/` (0 bytes, not in catalog or sitemap) |

---

## Files Modified

| File | Change summary |
|------|----------------|
| `index.html` | SEO meta tags; Sunrise package messaging |
| `hosting/index.html` | SEO meta tags; Sunrise plan reference |
| `models/index.html` | SEO meta tags; conversion CTA section |
| `pricing/index.html` | Twitter Card tags |
| `contact/index.html` | Twitter Card tags |
| `sitemap.xml` | Regenerated with 33 URLs |
| `models/deepseek-v3.1-cloud/index.html` | Open Graph + Twitter tags |
| `models/minimax-m3-cloud/index.html` | Repaired corrupted HTML; SEO tags |
| `models/ministral-3-cloud/index.html` | Fixed canonical, nav, and broken links |
| 8 legacy model briefs | Nav, canonical, OG, footer, quote/deploy links |
| 18 Tailwind model briefs | Fixed `/deploy/` CTAs; added OG/Twitter tags |

**Total: 34 files changed**

`robots.txt` — **unchanged**

---

## Top 20 Recommendations Before Google Search Console Submission

1. **Deploy this branch** and verify live URLs match sitemap entries.
2. **Submit sitemap** at `https://terminal.glass/sitemap.xml` in Google Search Console.
3. **Request indexing** for `/`, `/pricing/`, `/hosting/`, `/models/`, `/contact/` manually after deploy.
4. **Add `og:image`** to core pages (1200×630 branded share image).
5. **Add Organization JSON-LD** to homepage with terminal.glass logo and contact URL.
6. **Create `/agents/` landing page** before adding Agents to primary nav.
7. **Normalize legacy model brief titles** to consistent “Model Brief | Terminal.Glass” format (optional, post-launch).
8. **Add Privacy Policy page** — required for commercial site and ad/analytics compliance.
9. **Add Terms of Service page** — supports enterprise sales conversations.
10. **Add GitHub link** to footer if public repos should be discoverable.
11. **Add copyright line** to footer: `© 2026 terminal.glass`.
12. **Add NoCloudGPT cross-link** to core site footer under “Learn” or “Resources”.
13. **Replace Tailwind CDN** on model briefs with compiled CSS from `site.css` tokens (performance).
14. **Add `loading="lazy"`** to below-fold model hero/secondary images.
15. **Add skip-to-content link** for keyboard users on all templates.
16. **Verify Formspree contact form** submits successfully in production.
17. **Audit NoCloudGPT canonical tags** — ensure no duplicate indexing with terminal.glass model briefs.
18. **Add WebPage schema** to pricing page (already has offer schema via JS).
19. **Monitor Search Console** for “Alternate page with proper canonical” on legacy educational URLs.
20. **Build minimax-m2.1-cloud page** or remove empty directory to prevent accidental deployment.

---

## Summary

This audit reviewed all 33 public pages on terminal.glass, fixed critical launch blockers (broken links, wrong canonicals, missing SEO metadata, obsolete pricing copy), regenerated the sitemap from the live page inventory, and preserved the existing design language throughout.

The site is **ready for production indexing** at an overall readiness score of **8/10**. Remaining work is polish (footer completeness, Agents page, structured data, performance) rather than correctness.
