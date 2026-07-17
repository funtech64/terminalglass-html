# cursorFileB1.md
## Terminal.Glass Product Truth and Sales Conversion Repair

**Series:** Cursor Files B  
**Task number:** B1  
**Repository:** `funtech64/terminalglass-html`  
**Priority:** Critical / launch-blocking  
**Approval level:** Yellow — implementation requires human review before merge or deployment  
**Supersedes:** Any earlier `cursorFileB1.md` that treated deployment synchronization or SEO submission as the first task

---

# 1. Role

Act as the lead product-copy engineer, technical SEO engineer, and conversion-focused website editor for Terminal.Glass.

This is not a cosmetic SEO pass.

The current website contains product language that is incomplete, inaccurate, or commercially confusing. Ranking incorrect product information would damage customer trust and reduce sales. The first responsibility is to make the website accurately explain what Terminal.Glass sells, how it deploys, what is included, and why the customer should care.

Work carefully. Preserve working code and existing visual identity. Do not invent business policies. Do not publish automatically.

---

# 2. Primary objective

Repair the public Terminal.Glass website so that a business owner can quickly understand the offer:

> **One server. One script. Your private AI.**

The corrected site must explain that Terminal.Glass:

1. helps the customer choose private AI models;
2. fully guides and customizes the server sizing;
3. removes CPU, RAM, storage, GPU, operating-system, and cloud-instance guesswork;
4. provides one deployable installation script;
5. deploys one complete Terminal.Glass instance on one customer-controlled computer or cloud server;
6. supports NoCloudGPT, AWS, and DigitalOcean deployment paths;
7. includes built-in team and agent capabilities without misrepresenting their technology;
8. presents accurate licensing and expansion pricing;
9. removes all public Alchemist references;
10. updates SEO metadata only after the sales story is correct.

Do not move to search-console submission, SERPs.io baselining, or automated publishing in this task.

---

# 3. Authority and conflict rule

For public website copy, this B1 file is the controlling instruction for this repair pass.

When this file conflicts with:

- existing website copy;
- old Cursor files;
- old launch-readiness reports;
- old pricing descriptions;
- previous Alchemist language;
- public YourCloudGPT product cards;
- older Glass Agent or Jet Agent definitions;

follow this file and document the conflict.

Do not silently rewrite historical planning documents. Preserve history, but prevent obsolete language from appearing on the public site.

---

# 4. Non-negotiable product truth

## 4.1 Public brand

The primary public brand is:

> **Terminal.Glass**

Terminal.Glass is the customer-facing product, sales destination, licensing experience, deployment guidance system, and private AI platform.

Use consistent brand capitalization within each page. Prefer `Terminal.Glass` in headings and prose unless the existing style system intentionally uses `terminal.glass` for domain-style branding.

---

## 4.2 Core promise

Lock the following message into the site architecture:

> **One server. One script. Your private AI.**

Supporting meaning:

- one customer-controlled computer or cloud server;
- one Terminal.Glass instance;
- one installation script;
- private AI models selected for the customer’s needs;
- a complete guided deployment path;
- no server-sizing guesswork.

Do not imply clusters, multiple servers under one server license, or a complicated multi-stage assembly process.

---

## 4.3 One server license relationship

Use this relationship consistently:

```text
1 server license
    -> 1 computer or cloud server
    -> 1 Terminal.Glass instance
    -> 1 installation script
```

Public wording may say:

> One server license activates one Terminal.Glass instance on one computer or cloud server.

Do not state that Glass Agents or Jet Agents automatically consume separate server licenses unless an approved business rule explicitly says so.

---

## 4.4 NoCloudGPT

NoCloudGPT is the Terminal.Glass deployment path for:

- Ubuntu Linux 24/26 virtual machines;
- standalone Ubuntu Linux servers;
- supported bare-metal server hardware.

Preferred public label:

> **NoCloudGPT — Ubuntu Linux VMs and standalone servers**

Preferred description:

> Run Terminal.Glass on an Ubuntu Linux 24/26 virtual machine or standalone server you control.

Use `bare metal` in technical detail where useful, but do not rely on that term alone in customer-facing headlines.

---

## 4.5 Supported deployment paths

The public site must clearly present three current deployment paths:

1. **NoCloudGPT** — Ubuntu Linux 24/26 VM or standalone server;
2. **AWS** — a customer-owned AWS server that Terminal.Glass helps size and specify;
3. **DigitalOcean** — a customer-owned DigitalOcean server that Terminal.Glass helps size and specify.

Also state clearly:

- **Google Cloud Platform support is coming soon.**
- **Microsoft Azure support is coming soon.**

Do not imply that Terminal.Glass itself is the hosting provider unless that is explicitly true.

The customer owns or controls the server or cloud account.

---

## 4.6 YourCloudGPT

YourCloudGPT remains a valid internal cloud-deployment framework and identifier.

It may remain in:

- internal deployment metadata;
- structured technical records;
- configuration values;
- analytics labels;
- code comments;
- internal documentation;
- operational routing.

It must not be promoted as a separate public product that customers must understand or choose instead of Terminal.Glass.

Do not remove operational YourCloudGPT identifiers without first confirming they are unused.

Public rule:

> Customers choose a supported deployment location. Terminal.Glass remains the product they buy and use.

---

## 4.7 Server sizing and guidance

Do not reduce the offer to “standardized server specifications” or unsupported “do-it-yourself guides.”

The site must communicate that Terminal.Glass fully guides and customizes sizing to remove all guesswork.

Approved meaning:

- help select the right private AI models;
- match model families and deployment sizes to the customer’s use case;
- specify CPU;
- specify RAM;
- specify storage;
- specify GPU requirements where applicable;
- specify the supported operating system;
- select or recommend the correct AWS or DigitalOcean instance;
- provide the exact guided deployment path;
- provide one installation script.

Preferred public language:

> Tell us which models, users, agents, and workloads you need. We translate those requirements into a complete server specification and deployment path.

And:

> We remove the CPU, memory, storage, GPU, operating-system, and cloud-instance guesswork.

And:

> You create the recommended server, run one installation script, and receive one complete Terminal.Glass instance.

Use “complete guided deployment instructions” or “step-by-step guided deployment,” not language that suggests the customer is abandoned with a generic DIY document.

---

## 4.8 AI catalog claims

The owner has approved the following sourced catalog claims for website use:

- **240 documented AI model families**;
- **more than 44,000 documented deployment sizes**;
- **more than 100 Meta AI model options**;
- customers choose the private AI models appropriate for their deployment;
- completely private deployments are available.

Preferred phrasing:

> Choose from 240 documented AI model families and more than 44,000 documented deployment sizes, including more than 100 Meta AI model options.

Use `AI models`, `model families`, or `AIs`. Do not write the plural as `AI’s`.

Do not replace these specific numbers with the weaker generic phrase “over 100 models” as the primary catalog claim.

Use “completely private” only for deployment paths in which the customer controls the server and model inference remains within the approved environment. Do not attach that claim to an external inference service unless verified.

---

## 4.9 Happy Nerds Menu

Every Terminal.Glass instance includes the:

> **Happy Nerds Menu**

This feature is currently missing from the public sales story and must be restored.

Required public statement:

> Every Terminal.Glass instance includes the Happy Nerds Menu.

Do not invent a detailed item list if no authoritative source exists in the repository. Add a clear high-level mention and record missing detail as an owner follow-up.

Search the repository and existing project documentation for authoritative Happy Nerds Menu content before writing more specific copy.

---

## 4.10 Built-in DokuWiki

Every server instance includes built-in DokuWiki for team documentation.

The site should explain this as a practical team feature, for example:

> Every Terminal.Glass server includes a built-in DokuWiki so teams can maintain private documentation alongside their AI instance.

Do not describe DokuWiki as an optional external integration if it is included per instance.

---

## 4.11 Glass Agents

Correct definition:

> **Glass Agents powered by OpenClaw**

Glass Agents are OpenClaw-powered agents operating through approved tools, environments, and workflows.

Use wording such as:

> Glass Agents powered by OpenClaw can work through customer-approved tools and workflows inside the Terminal.Glass environment.

Do not present Glass Agents as a generic cloud-model category.

Do not claim a separate license is required for every Glass Agent unless the owner has approved that policy.

---

## 4.12 Jet Agents

Correct definition:

> **Jet Agents are Ollama-powered CPU/GPU compute agents.**

They use selected AI models through CPU or GPU compute.

Use wording such as:

> Jet Agents use Ollama-powered CPU or GPU compute to run the private AI models selected for the workload.

Do not describe Jet Agents as generic external cloud reasoning agents.

Do not imply that all Jet Agent data leaves the customer’s environment.

Do not claim a separate license is required for every Jet Agent unless an approved rule explicitly says so.

---

## 4.13 Alchemist removal

Alchemist and Alchemist Conductor must not appear anywhere on the public website.

Remove public references from:

- visible HTML;
- navigation;
- footer;
- pricing copy;
- agent pages;
- contact options;
- CTA parameters;
- metadata;
- Open Graph fields;
- Twitter fields;
- JSON-LD;
- sitemap entries;
- public JavaScript configuration;
- public images or alt text;
- page titles and descriptions.

Do not create an Alchemist page, preview, founder list, or coming-soon card.

Historical internal documents may record that it was removed, but no public page should promote or expose it.

---

# 5. Licensing and pricing truth

## 5.1 Sunrise account

A Sunrise account includes two server licenses, creating group-capable value from the start.

Approved meaning:

- two server licenses are included;
- each server license activates one server instance;
- additional server licenses for a Sunrise account are **$99 each**.

Preferred public wording:

> Every Sunrise account includes two server licenses, so you can begin with two private AI server instances without purchasing a second starter account.

And:

> Add server licenses to a Sunrise account for $99 each.

Do not describe the included second server as “free” in structured pricing data unless the owner specifically approves that sales language. Emphasize included value.

---

## 5.2 Group plan expansion

Approved rule:

- additional server licenses for the Group plan are **$49 each**;
- larger purchases may receive a private in-account volume offer;
- the deeper discount schedule is not public and must not be invented.

Preferred public wording:

> Group accounts can add server licenses for $49 each. Larger deployments may qualify for private volume pricing.

Do not invent the base Group plan price, included license count, eligibility threshold, or discount ladder if those values are not present in an approved source.

If the existing site does not contain an approved Group plan definition, add the missing details to the owner-decision report rather than fabricating them.

---

## 5.3 Provisional migration and deployment-key policy

The following policy is under consideration and is not approved for public sales copy during B1:

- up to two migrations per license;
- up to five total deployment-key issuances per license.

Create a draft policy note for owner review. Do not publish these numbers as contractual promises until the owner explicitly approves them.

The draft must distinguish:

- a completed migration;
- a failed installation caused by a Terminal.Glass defect;
- a customer-initiated rebuild;
- an emergency key reset;
- a server replacement;
- a provider migration.

---

# 6. Unresolved policies — do not invent

The website currently lacks approved public terms for:

- software-update duration;
- warranty or deployment assurance;
- included technical support;
- paid support options;
- support response times;
- maintenance renewals.

Do not create public promises for these items in B1.

Do not add “lifetime updates,” “lifetime support,” unlimited migrations, guaranteed response times, or warranty language.

Create `OWNER-DECISIONS-B1.md` containing:

1. the missing policy;
2. where the site needs the answer;
3. two or three clearly labeled options;
4. commercial risks of each option;
5. a recommended option;
6. the exact decision required from the owner.

The public site may say only what is already approved. Where necessary, use neutral wording such as:

> Deployment documentation and available support options are provided with your account.

Only use that sentence if it does not conflict with existing operations.

---

# 7. Required workflow

## Step 1 — Create a repair branch

Create a dedicated branch from current `main`, for example:

```text
cursor/product-truth-sales-repair-b1
```

Do not work directly on `main`.

Do not deploy automatically.

---

## Step 2 — Inventory the full public site before editing

Search the entire repository, including visible copy, metadata, structured data, JavaScript-generated copy, contact options, and sitemap files.

At minimum, search case-insensitively for:

```text
Alchemist
Alchemist Conductor
YourCloudGPT
NoCloudGPT
Glass Agent
Jet Agent
OpenClaw
Ollama
Happy Nerds
DokuWiki
100 models
over 100
240
44,000
bare metal
virtual machine
AWS
DigitalOcean
Google Cloud
GCP
Azure
server license
Glass License
migration
deployment key
warranty
support
updates
```

Create `PRODUCT-COPY-AUDIT-B1.md` before making the final edits.

For each issue, record:

- file;
- page or component;
- current wording;
- why it is inaccurate or weak;
- proposed correction;
- whether owner approval is required;
- final status.

Do not rely only on core pages. Inspect every public model page and every JavaScript configuration file that generates visible copy or JSON-LD.

---

## Step 3 — Create a durable source-of-truth file

Create:

```text
PRODUCT-TRUTH.md
```

This file must summarize the approved public product truth from Sections 4 and 5 of this prompt.

It must clearly separate:

- public customer-facing language;
- internal operational terminology;
- approved pricing facts;
- prohibited public claims;
- unresolved owner decisions.

Do not treat `PRODUCT-TRUTH.md` as immutable corporate truth outside this website repository. It is the source of truth for site copy until the owner replaces it.

---

## Step 4 — Repair the homepage sales story

The homepage must quickly answer:

1. What is Terminal.Glass?
2. Where can it run?
3. What does the customer have to do?
4. What does Terminal.Glass do for them?
5. What is included?
6. What should they do next?

Required homepage themes:

- One server. One script. Your private AI.
- customer-controlled computer or cloud server;
- NoCloudGPT, AWS, and DigitalOcean;
- GCP and Azure coming soon;
- fully guided and customized server sizing;
- 240 AI model families;
- more than 44,000 deployment sizes;
- more than 100 Meta AI model options;
- completely private deployment availability;
- Happy Nerds Menu included;
- built-in DokuWiki;
- Glass Agents powered by OpenClaw;
- Jet Agents powered by Ollama CPU/GPU compute;
- clear route to pricing or deployment planning.

Do not overload the hero with every detail. Use the hero for the promise, then supporting sections for proof and explanation.

Preferred hero direction:

```text
One server. One script. Your private AI.

We help you choose the models, fully size the server, and provide one guided installation path for Ubuntu Linux, AWS, or DigitalOcean.
```

This is a direction, not a requirement to copy mechanically. Improve readability while preserving the meaning.

---

## Step 5 — Repair the hosting/deployment page

The deployment page must present three current paths:

### NoCloudGPT

- Ubuntu Linux 24/26 VM or standalone server;
- customer-owned and customer-controlled;
- private AI on local, virtualized, or bare-metal infrastructure.

### AWS

- customer-owned AWS account;
- Terminal.Glass recommends the appropriate standardized instance;
- sizing is matched to selected models and workloads;
- one-script deployment.

### DigitalOcean

- customer-owned DigitalOcean account;
- Terminal.Glass recommends the appropriate standardized server;
- sizing is matched to selected models and workloads;
- one-script deployment.

### Coming soon

- Google Cloud Platform;
- Microsoft Azure.

The page must emphasize:

> We handle the server specification and remove the guesswork.

Replace generic hosting language that fails to explain the guided sizing service.

Do not create a public YourCloudGPT product card.

---

## Step 6 — Repair the Agents page

Rewrite the page around the approved definitions:

### Glass Agents

- “Glass Agents powered by OpenClaw”;
- approved tools and workflows;
- operate inside the Terminal.Glass environment;
- do not call them generic cloud workers.

### Jet Agents

- Ollama-powered CPU/GPU compute agents;
- execute selected AI models;
- can use customer-approved compute;
- do not call them generic external cloud-reasoning helpers.

Remove:

- Alchemist sections;
- Alchemist CTAs;
- founder-list links;
- one-license-per-agent claims unless independently approved;
- language implying Jet Agents necessarily send data outside the customer environment.

Add a clear relationship between server sizing and agent workloads:

> Agent workloads are included when Terminal.Glass helps size the server.

Use that concept only if it accurately reflects the operating model.

---

## Step 7 — Repair pricing and licensing language

Update visible pricing, pricing configuration, fallback `<noscript>` content, FAQs, comparison tables, contact options, and JSON-LD so they agree.

Required rules:

- Sunrise account includes two server licenses;
- one server license equals one active Terminal.Glass instance on one computer or cloud server;
- additional Sunrise server licenses are $99 each;
- Group plan additional server licenses are $49 each;
- larger deployments may qualify for private volume pricing;
- do not invent a Group plan base price or license count;
- do not describe agent licenses separately unless approved;
- do not expose Alchemist;
- do not present YourCloudGPT as a separate customer product.

If the current package names or base prices conflict with this prompt, list the conflict in `OWNER-DECISIONS-B1.md` before changing unapproved values.

Do not silently choose between conflicting base-plan definitions.

---

## Step 8 — Restore Happy Nerds Menu and DokuWiki inclusion

Add these as real included features wherever the sales journey needs them:

- homepage feature section;
- pricing inclusion list;
- deployment or product overview;
- FAQ where appropriate.

Required minimum truth:

- every Terminal.Glass instance includes the Happy Nerds Menu;
- every server instance includes built-in DokuWiki for teams.

Do not create unsupported feature details.

---

## Step 9 — Repair the model catalog story

The models section must explain the catalog using the approved scale:

- 240 documented AI model families;
- more than 44,000 documented deployment sizes;
- more than 100 Meta AI model options.

Explain that Terminal.Glass helps the customer choose model families and sizes that fit the server and workload.

The key differentiator is not merely a large model count. It is the combination of:

- model choice;
- documented deployment sizes;
- guided server sizing;
- one-script deployment;
- customer-controlled privacy.

Do not imply that every listed model or deployment size is suitable for every server.

Review individual model briefs for obsolete product language, incorrect agent definitions, incorrect deployment links, Alchemist references, and public YourCloudGPT positioning.

---

## Step 10 — Update metadata and structured data after copy is correct

Once visible copy is corrected, update:

- page titles;
- meta descriptions;
- canonical-related context if page structure changes;
- Open Graph titles and descriptions;
- Twitter titles and descriptions;
- JSON-LD descriptions;
- Product and Offer descriptions;
- FAQ schema;
- navigation labels;
- footer copy;
- contact-interest options;
- sitemap only if routes change.

Metadata must accurately match the public page.

YourCloudGPT may remain in internal or technical metadata, but must not be used to create a competing public product identity.

Remove Alchemist from all public metadata and structured data.

Do not keyword-stuff `240`, `44,000`, Meta, OpenClaw, Ollama, AWS, and DigitalOcean into every title. Use them naturally on the pages where they help users understand the offer.

---

## Step 11 — Preserve conversion paths

Every major page must have a clear next action:

- view pricing;
- plan a deployment;
- contact sales;
- choose a server path;
- review the model catalog.

Do not send the customer into dead or placeholder flows.

Verify that query parameters passed from pricing and deployment cards match the contact form options.

Do not alter the working Formspree endpoint or fallback email unless required and approved.

---

## Step 12 — Validate the repair

Run the existing site validator and improve it only as needed to verify B1.

Also perform targeted checks for this task.

### Required automated checks

- zero public Alchemist references;
- zero public claims that YourCloudGPT is a separate customer product;
- Glass Agent public copy includes OpenClaw;
- Jet Agent public copy includes Ollama and CPU/GPU compute;
- homepage includes the one-server/one-script promise;
- NoCloudGPT includes Ubuntu Linux VM/standalone-server language;
- AWS and DigitalOcean are visible current deployment paths;
- GCP and Azure are marked coming soon;
- Happy Nerds Menu is visible as included in every instance;
- DokuWiki is visible as included per server instance;
- 240 model families appears accurately;
- more than 44,000 deployment sizes appears accurately;
- more than 100 Meta AI options appears accurately;
- pricing copy agrees across HTML, JavaScript config, FAQ, contact options, and JSON-LD;
- no broken internal page links;
- all edited pages have one H1, title, description, and canonical;
- JSON-LD parses successfully;
- no accidental `noindex` is introduced.

### Required manual checks

Review desktop and mobile rendering for:

- homepage;
- pricing;
- hosting/deployment;
- models;
- agents;
- contact.

Capture before-and-after screenshots or preview links for the pull request.

Read every edited page as a customer. Confirm that it explains the offer without requiring knowledge of internal architecture.

---

# 8. Editorial rules

- Write for a business owner first.
- Use plain English before infrastructure terminology.
- Explain technical words when they are necessary.
- Preserve credibility; do not use exaggerated claims.
- Do not invent capabilities, support promises, or timelines.
- Do not describe the customer as doing unsupported DIY work.
- Do not use `AI’s` as a plural.
- Do not confuse a model family with a deployment size.
- Do not confuse a server license with an agent.
- Do not imply Terminal.Glass owns the customer’s AWS or DigitalOcean account.
- Do not hide important commercial facts only in FAQs.
- Keep one consistent promise across visible copy and metadata.

---

# 9. Prohibited actions

Do not:

- deploy to production;
- merge without review;
- submit the sitemap to search engines;
- start SERPs.io tracking against the repaired copy before deployment approval;
- add Alchemist anywhere public;
- remove operational YourCloudGPT identifiers without checking dependencies;
- invent Group plan base pricing;
- invent warranty, update, or support promises;
- publish provisional migration/deployment-key limits;
- change the Formspree destination without approval;
- redesign the entire site unnecessarily;
- delete historical reports to conceal old decisions;
- overwrite the agent constitution or development-plan files.

---

# 10. Required deliverables

The pull request must include:

1. corrected public website files;
2. `PRODUCT-TRUTH.md`;
3. `PRODUCT-COPY-AUDIT-B1.md`;
4. `OWNER-DECISIONS-B1.md`;
5. updated validation tooling or a B1 validation script if needed;
6. a validation report showing commands and results;
7. before-and-after screenshots or preview evidence;
8. a list of all public Alchemist references removed;
9. a list of operational YourCloudGPT identifiers intentionally retained;
10. a list of unresolved questions that blocked any copy from being finalized.

---

# 11. Completion criteria

B1 is complete only when all of the following are true:

- [ ] The homepage sells the one-server, one-script private AI offer clearly.
- [ ] The site explains that Terminal.Glass fully guides and customizes sizing.
- [ ] NoCloudGPT is correctly described as Ubuntu Linux 24/26 VMs and standalone servers.
- [ ] AWS and DigitalOcean are current supported deployment paths.
- [ ] GCP and Azure are shown as coming soon.
- [ ] YourCloudGPT is not promoted as a separate public product.
- [ ] Happy Nerds Menu is shown as included in every instance.
- [ ] DokuWiki is shown as included per server instance.
- [ ] Glass Agents are described as powered by OpenClaw.
- [ ] Jet Agents are described as Ollama-powered CPU/GPU compute agents.
- [ ] No public Alchemist reference remains.
- [ ] The model catalog uses the approved 240-family, 44,000-size, and 100+ Meta claims accurately.
- [ ] The one-server-license relationship is explained consistently.
- [ ] Sunrise includes two server licenses and $99 expansion pricing is represented accurately.
- [ ] Group-plan $49 expansion pricing is represented without inventing missing base-plan details.
- [ ] No unapproved migration, update, warranty, or support promise is published.
- [ ] Visible copy, metadata, JavaScript-generated content, contact options, and JSON-LD agree.
- [ ] Internal links and structured data validate.
- [ ] A human can review the changes in a pull request before any deployment.

---

# 12. Required final response from Cursor

When the task is complete, respond with this structure:

## B1 Status

- Completed / Blocked / Needs owner decision

## Pages changed

- list every public page and major component changed

## Product corrections made

- summarize each corrected concept

## Alchemist removal

- report public files searched and references removed

## YourCloudGPT handling

- report public references removed and operational identifiers retained

## Pricing findings

- report what was corrected and what still requires owner approval

## Policy decisions needed

- software updates
- warranty/deployment assurance
- technical support
- migration and deployment-key policy
- any missing Group plan base definition

## Validation

- commands run
- errors
- warnings
- unresolved issues

## Pull request

- branch
- commit(s)
- pull-request URL

Do not state that the site is ready for SEO launch merely because the files compile. B1 is a product-truth and sales-conversion repair gate. Production deployment and external SEO activation occur in later numbered tasks.

---

# 13. Handoff to cursorFileB2

Do not begin B2 automatically.

B2 should begin only after the owner reviews and approves:

- the corrected product story;
- all pricing language;
- the owner-decision report;
- the visual preview;
- the B1 pull request.

The expected B2 topic is production synchronization and live-site verification after the corrected sales copy is approved.


---

# B1 Addendum — Final Headline, Deployment Symbol, and Jet Agents Route

This addendum overrides any conflicting wording or route instructions earlier in this prompt. Do not rewrite the full prompt. Apply these changes as part of B1.

## 1. Primary Sales Headline

Replace the proposed primary statement:

> One server. One script. Your private AI.

with:

> **Private AI with no more guesswork.**

This is the authoritative primary sales headline.

The phrase “one server” and the one-script installation remain supporting proof points, not the primary headline.

Approved supporting copy:

> We help you choose the right private AI models, fully size the server, and provide the exact deployment path.

The supporting message may also explain:

- one Terminal.Glass instance per computer or cloud server
- one installation script
- customized CPU, RAM, storage, GPU, and provider-instance guidance
- deployment support for NoCloudGPT, AWS, and DigitalOcean
- complete guided deployment instructions

Do not turn the supporting proof points back into the main headline.

## 2. Smiling Deployment Symbol

Associate the smiling face emoji **🙂** with the promise:

> **Private AI with no more guesswork.**

Use the smiling face as a friendly deployment-completion and guided-deployment symbol.

Approved uses include:

- deployment cards
- the deployment process section
- successful sizing or installation states
- “no more guesswork” callouts
- installation-guide completion messaging

Example:

> **🙂 Private AI with no more guesswork.**

The symbol should communicate that deployment is understandable, guided, and approachable.

Do not overuse the emoji across every heading, navigation item, or paragraph. It should remain a recognizable deployment symbol rather than visual clutter.

Do not replace the Terminal.Glass logo with the emoji.

## 3. Rename the Public Agents Route

The repository-level `AGENTS/` directory is reserved for Cursor instructions, agent plans, and operational documents.

To prevent naming confusion, rename the public website folder and route:

```text
agents/ into jet-agents/
```

The public URL becomes:

```text
https://terminal.glass/jet-agents/
```

## 4. Update every reference

Update all internal links, canonical URLs, Open Graph URLs, Twitter card URLs, sitemap entries, navigation items, footer links, model brief cross-links, generated chrome in `scripts/update-site-chrome.py`, and validation scripts so they point to `/jet-agents/` instead of `/agents/`.

Do not rename the repository instruction folder (`agents/` or `AGENTS/`). Only the public website route changes.

## 5. Permanent redirect

Keep `agents/index.html` as a permanent redirect to `/jet-agents/`.

Preserve query parameters and URL fragments where practical using client-side `location.replace` plus a `<link rel="canonical">` and meta refresh fallback.

Do not list `/agents/` in `sitemap.xml`. The canonical agents page is `/jet-agents/`.

## 6. Navigation label

The navigation item may continue to read **Agents** while linking to `/jet-agents/`.

## 7. Emoji note (conversation override)

The owner conversation specifies **😎** (cool sunglasses) as the guided-deployment symbol associated with “no more guesswork,” overriding the earlier 🙂 example in draft copy.
