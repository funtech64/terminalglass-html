# Terminal Glass Cloud Model Inventory

Date: 2026-06-18
Project: `funtech64/nocloudgpt-html`
Working directory focus: `/models/`

## Decision

Terminal Glass cloud-backed models should live as **their own family folders directly inside `/models/`**.

Do **not** make `/models/terminal-glass/<model>/` the primary site structure.
Do **not** hide cloud variants inside the local model family folders.

Use this pattern instead:

```text
/models/gpt-oss-cloud/index.html
/models/qwen3.5-cloud/index.html
/models/gemma4-cloud/index.html
/models/deepseek-v4-flash-cloud/index.html
/models/kimi-k2.6-cloud/index.html
```

This is cleaner for sales because a Terminal Glass cloud model is not just another local size option. It is a different deployment lane:

- The customer gets the Ollama/OpenWebUI-style workflow.
- The local machine has very small hardware requirements.
- The heavy inference work runs through Ollama Cloud.
- The product story becomes speed, simplicity, and deployment convenience.

## Product distinction

| Product lane | Where the model runs | Sales promise | Folder style |
|---|---|---|---|
| NoCloudGPT Private Instance | Customer-controlled local server, on-prem box, or private cloud server | Private AI that runs on infrastructure the customer controls | `/models/<family>/` |
| Terminal Glass Cloud Instance | Ollama Cloud-backed inference with a small local Linux host | Fast pre-built AI workflow without buying GPU hardware | `/models/<family-or-model>-cloud/` |

## Official Ollama Cloud behavior to reflect in copy

Ollama Cloud models run through the normal Ollama workflow, but the model computation is offloaded to Ollama Cloud. The local machine does not need the same GPU/RAM profile required for local inference. Ollama's docs show cloud model usage with names such as:

```bash
ollama run gpt-oss:120b-cloud
ollama pull gpt-oss:120b-cloud
```

Cloud models require the user to sign in with an Ollama account using:

```bash
ollama signin
```

Important copywriting rule: Terminal Glass is not an air-gapped product. It should be described as a **cloud-accelerated private AI workflow**, not as fully local or fully offline AI.

Sources checked:

- https://docs.ollama.com/cloud
- https://ollama.com/library

## Current `/models/` inventory observed

The current `/models/` directory already contains a broad catalog, including local model families, embeddings, coding models, safety models, deployment pages, pricing pages, and comparison pages.

Observed folders / files from the repository view include:

`airoboros`, `all-minilm`, `alpaca`, `aya`, `bakllava`, `bespoke-minicheck`, `bge`, `chatglm`, `chatgpt-alternatives`, `codegeex4`, `codegemma`, `codellama`, `codestral`, `cogito`, `command-r`, `compare`, `deepseek-coder`, `deepseek`, `deploy`, `duckdb-nsql`, `embedding-gemma`, `exaone`, `falcon`, `firefunction`, `gemma`, `glm`, `glm5`, `gpt-2`, `gpt-oss`, `granite-code`, `granite-embedding`, `granite-guardian`, `granite`, `granite4`, `internlm`, `jamba`, `kimi`, `laguna`, `lfm`, `llama-guard-3`, `llama`, `llava`, `magicoder`, `magistral`, `medgemma`, `meditron`, `minicpm-v`, `minimax`, `mistral-family`, `mistral`, `mixtral`, `moondream`, `mxbai`, `mythomax`, `nemotron`, `nemotron4`, `neural-chat`, `nomic-embed`, `nous-hermes`, `nuextract`, `obsidian`, `olmo`, `openchat`, `opencoder`, `openhermes`, `paligemma`, `paraphrase-multilingual`, `phi`, `phind-codellama`, `pixtral`, `qwen-embedding`, `qwen`, `qwen2.5-coder`, `reader-lm`, `recurrentgemma`, `reflection`, `samantha`, `shieldgemma`, `smollm`, `snowflake-arctic-embed`, `solar`, `sqlcoder`, `stablelm`, `starcoder`, `tinyllama`, `translategemma`, `tulu`, `whisper`, `wizardcoder`, `wizardlm`, `yi`, `zamba2`, `zephyr`, plus `index.html`, `note.md`, `note2.md`, `pricing.html`, and `quote.html`.

## Recommended cloud family folders

These folders are **verified Terminal Glass cloud family folders** (30 active). Each one deserves an `index.html` sales page. Hold/candidate families without confirmed Ollama `cloud` tags are listed separately in `models/data/terminal-glass-cloud-hold-models.json` — not in the active sales inventory.

| Priority | Folder | Ollama model / family | Sales positioning | Relationship to local model catalog |
|---:|---|---|---|---|
| 1 | `/models/gemma3-cloud/` | `gemma3` | Google Gemma 3 multimodal cloud variants (4B–27B). | Separate from `/models/gemma/`. |
| 2 | `/models/gemma4-cloud/` | `gemma4` | Google-backed multimodal and general-purpose cloud option. | Separate from `/models/gemma/`. |
| 3 | `/models/qwen3.5-cloud/` | `qwen3.5` | Strong all-rounder for thinking, tools, multimodal, and business workflows. | Separate from `/models/qwen/`. |
| 4 | `/models/gpt-oss-cloud/` | `gpt-oss` | Flagship cloud reasoning and agentic work. | Keep `/models/gpt-oss/` for local/open-weight SEO. |
| 5 | `/models/qwen3-coder-cloud/` | `qwen3-coder` | Coding agents, long-context development, repository work. | Separate from `/models/qwen2.5-coder/`. |
| 6 | `/models/nemotron-3-super-cloud/` | `nemotron-3-super` | Efficient complex multi-agent work. | Separate from `/models/nemotron/`. |
| 7 | `/models/glm-5-cloud/` | `glm-5` | Large reasoning and agentic model. | Separate from `/models/glm5/`. |
| 8 | `/models/minimax-m2.5-cloud/` | `minimax-m2.5` | Productivity and coding cloud option. | Separate from `/models/minimax/`. |
| 9 | `/models/glm-5.1-cloud/` | `glm-5.1` | Agentic engineering and coding. | Separate from `/models/glm5/`. |
| 10 | `/models/gemini-3-flash-preview-cloud/` | `gemini-3-flash-preview` | Speed-focused frontier cloud model. | New cloud-only folder; needs careful branding review. |
| 11 | `/models/minimax-m2.7-cloud/` | `minimax-m2.7` | Coding, productivity, and agentic workflows. | Separate from `/models/minimax/`. |
| 12 | `/models/glm-4.7-cloud/` | `glm-4.7` | Coding capability and technical work. | Separate from `/models/glm/`. |
| 13 | `/models/deepseek-v3.2-cloud/` | `deepseek-v3.2` | Efficient reasoning and agent performance. | Separate from `/models/deepseek/`. |
| 14 | `/models/minimax-m2.1-cloud/` | `minimax-m2.1` | Multilingual code engineering. | Separate from `/models/minimax/`. |
| 15 | `/models/qwen3-coder-next-cloud/` | `qwen3-coder-next` | Next-generation coding agent lane. | New cloud-only folder. |
| 16 | `/models/ministral-3-cloud/` | `ministral-3` | Edge-oriented Mistral cloud/vision/tool model. | Separate from `/models/mistral/`. |
| 17 | `/models/devstral-small-2-cloud/` | `devstral-small-2` | Codebase exploration and multi-file editing. | Separate from Mistral local/coding folders. |
| 18 | `/models/deepseek-v3.1-cloud/` | `deepseek-v3.1` | Hybrid thinking/non-thinking DeepSeek lane. | Separate from `/models/deepseek/`. |
| 19 | `/models/nemotron-3-nano-cloud/` | `nemotron-3-nano` | Efficient open agentic model with cloud option. | Separate from `/models/nemotron/`. |
| 20 | `/models/rnj-1-cloud/` | `rnj-1` | 8B code/STEM cloud-supporting model. | New cloud-only folder. |
| 21 | `/models/kimi-k2.5-cloud/` | `kimi-k2.5` | Native multimodal agentic model. | Separate from `/models/kimi/`. |
| 22 | `/models/kimi-k2.6-cloud/` | `kimi-k2.6` | Long-horizon coding, design, and autonomous execution. | Separate from `/models/kimi/`. |
| 23 | `/models/devstral-2-cloud/` | `devstral-2` | Large coding agent model. | Separate from Mistral local/coding folders. |
| 24 | `/models/deepseek-v4-pro-cloud/` | `deepseek-v4-pro` | Frontier MoE reasoning, long context, multi-mode reasoning. | New cloud-only folder. |
| 25 | `/models/deepseek-v4-flash-cloud/` | `deepseek-v4-flash` | Fast, efficient DeepSeek reasoning cloud option. | New cloud-only folder. |
| 26 | `/models/mistral-large-3-cloud/` | `mistral-large-3` | Production-grade multimodal MoE cloud model. | Separate from `/models/mistral/`. |
| 27 | `/models/minimax-m3-cloud/` | `minimax-m3` | Coding and agentic frontier with multimodality. | Separate from `/models/minimax/`. |
| 28 | `/models/glm-5.2-cloud/` | `glm-5.2` | Long-horizon tasks and agentic workflows. | Separate from `/models/glm5/`. |
| 29 | `/models/kimi-k2.7-code-cloud/` | `kimi-k2.7-code` | Moonshot coding-focused agentic cloud model. | Separate from `/models/kimi/`. |
| 30 | `/models/nemotron-3-ultra-cloud/` | `nemotron-3-ultra` | NVIDIA long-running agent workflows and high-throughput reasoning. | Separate from `/models/nemotron/`. |

## Hold — not in active cloud inventory

Do not sell or deploy these as Terminal Glass Cloud pages until Ollama confirms `cloud` tags. See `models/data/terminal-glass-cloud-hold-models.json`.

| Folder | Ollama model / family | Hold reason |
|---|---|---|
| `/models/qwen3.6-cloud/` | `qwen3.6` | Ollama page shows vision/tools/thinking variants, not `cloud`. |
| `/models/nemotron-cascade-2-cloud/` | `nemotron-cascade-2` | Ollama page shows tools/thinking 30b, not `cloud`. |

## Deprecated or risky cloud items

Do not prioritize these as new customer-facing sales pages unless they are retained only as redirect/comparison content:

| Model | Recommended alternative |
|---|---|
| `kimi-k2-thinking` | `kimi-k2.6` |
| `kimi-k2:1t` | `kimi-k2.6` |
| `minimax-m2` | `minimax-m3` |
| `glm-4.6` | `glm-5.1` |
| `qwen3-next:80b` | `qwen3.5` |
| `qwen3-vl:235b` | `qwen3.5` |
| `qwen3-vl:235b-instruct` | `qwen3.5` |
| `cogito-2.1:671b` | `deepseek-v4-flash` |

## Recommended cloud page build order

1. `/models/gpt-oss-cloud/index.html`
2. `/models/qwen3.5-cloud/index.html`
3. `/models/gemma4-cloud/index.html`
4. `/models/qwen3-coder-cloud/index.html`
5. `/models/deepseek-v4-flash-cloud/index.html`
6. `/models/kimi-k2.6-cloud/index.html`
7. `/models/kimi-k2.7-code-cloud/index.html`
8. `/models/minimax-m3-cloud/index.html`
9. `/models/glm-5.2-cloud/index.html`
10. `/models/nemotron-3-ultra-cloud/index.html`
11. `/models/mistral-large-3-cloud/index.html`
12. `/models/devstral-2-cloud/index.html`

## Recommended CTA language

Use this CTA box across Terminal Glass pages:

> **Fast, efficient pre-built private AI workflow**  
> Run a familiar Ollama/OpenWebUI experience without buying a workstation GPU. Terminal Glass connects your small private server to Ollama Cloud-backed models for speed, simplicity, and a clean upgrade path.
>
> Button: **Deploy a Terminal Glass Cloud Instance**

## Short sales distinction

Use this plain explanation somewhere near the top of every Terminal Glass cloud family page:

> NoCloudGPT is for customers who want AI running on their own server. Terminal Glass is for customers who want the same simple private AI workflow, but with heavy model computation handled by Ollama Cloud. It is the fast lane for small teams that want capability first and hardware complexity later.

## Data file

Maintain the **active** cloud family list in:

```text
/models/data/terminal-glass-cloud-models.json
```

Hold/candidate families (not sellable yet) live in:

```text
/models/data/terminal-glass-cloud-hold-models.json
```

See `models/data/README.md` for the active vs hold rule.

Each active entry should include:

```json
{
  "slug": "gpt-oss-cloud",
  "displayName": "GPT-OSS Cloud",
  "ollamaFamily": "gpt-oss",
  "exampleRun": "ollama run gpt-oss:120b-cloud",
  "category": "reasoning-agentic",
  "priority": 1,
  "folder": "/models/gpt-oss-cloud/",
  "localFamilyFolder": "/models/gpt-oss/",
  "deploymentMode": "terminal-glass-cloud",
  "status": "active"
}
```

This gives the site one maintainable list that can feed the cloud model index, quote page, and sidebar CTA boxes while keeping every cloud model as its own clean sales family folder.
