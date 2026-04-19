# LightRAG Project Bootstrap Playbook

Use this reference after `lightrag-project-bootstrap/SKILL.md` triggers. It is the execution contract for installing a repo-scoped LightRAG stack that includes:

- project MCP via `.mcp.json`
- `rag` CLI for terminal use
- Obsidian export with Graph View support

When the runtime is Codex rather than Claude Code, map:

- `AskUserQuestion` => one concise direct user question that bundles the missing decisions
- `TodoWrite` => `update_plan` or a visible checklist in progress updates
- background jobs => long-running terminal session plus polling

## Phase 0 — Discovery and prereqs

### Silent discovery checklist
Explore these in parallel before changing anything:

- `git rev-parse --show-toplevel`
- stack files: `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `requirements.txt`
- top-level structure: `app/`, `src/`, `components/`, `convex/`, `prisma/`, `docs/`
- `.env.local`, `.env`, `.env.example` — list keys only, never values
- `.gitignore` — confirm `.env*`
- `.mcp.json` — detect existing servers for merge-safe updates
- `.claude/settings.local.json` — context only; never register MCP there
- `uname -s`
- `command -v uv`, `command -v brew`, `command -v curl`, `command -v python3`
- Obsidian presence:
  - macOS: `ls /Applications/ | grep -i Obsidian`
  - Linux: `ls ~/.config/obsidian ~/.var/app/md.obsidian.Obsidian 2>/dev/null`

### Auto-install `uv`
If `uv` is missing, narrate first:

> "Nao achei o `uv` (gerenciador de pacotes Python moderno). Vou instalar agora — leva ~10 segundos, sem prompts interativos."

Then install:

macOS:

```bash
command -v brew >/dev/null && brew install uv
command -v brew >/dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh
```

Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If `command -v uv` still fails, add:

```bash
export PATH="$HOME/.local/bin:$PATH"
```

### Auto-install Python 3.11+
If `python3` is missing or below 3.11, narrate first:

> "Python 3.11+ nao encontrado. Vou instalar uma versao gerenciada pelo `uv` (nao mexe no Python do sistema)."

Then run:

```bash
uv python install 3.11
```

Do not install LightRAG or Python libraries yet. That happens only via `uv sync --project tools/lightrag`.

### Obsidian handling
Obsidian is optional and never blocks setup.

- If missing, do not auto-install during Phase 0.
- Mention its status in the report.
- Offer installation only after the Phase 1 decision bundle, not before.

### Validation gate
After prereqs, confirm with:

```bash
uv --version
uv run --python 3.11 python --version
```

If this still fails, stop and show the exact error. Do not invent workarounds.

### Phase 0 report
Before Phase 1, send a short summary with:

- detected stack
- `uv` version and Python 3.11+ status
- Obsidian installed or not
- one line mentioning any auto-installed prereqs

## Phase 1 — Single bundled decision round

Ask these four decisions together.

### P1 — LLM provider

- `Gemini Flash + embedding (Recommended)` => `gemini-2.5-flash` + `gemini-embedding-001` => env `GOOGLE_API_KEY`
- `OpenAI` => `gpt-4o-mini` + `text-embedding-3-small` => env `OPENAI_API_KEY`
- `Anthropic + Voyage` => `claude-haiku-4-5` + `voyage-3` => env `ANTHROPIC_API_KEY` + `VOYAGE_API_KEY`
- `Ollama local` => `qwen2.5-coder:7b` + `nomic-embed-text`

### P2 — Scope

- `Codigo + docs + config (Recommended)`
- `Apenas docs + schemas`
- `Tudo + historico git`

### P3 — Vault path

- `docs/knowledge-graph/ no repo (Recommended)`
- `Pasta externa ~/Obsidian/<repo>-kg/`
- `Adicionar a vault Obsidian existente`

### P4 — Git strategy

- `Versionar markdown, gitignore storage (Recommended)`
- `Gitignorar tudo`

Persist them as `PROVIDER`, `SCOPE`, `VAULT_MODE`, and `GIT_MODE`.

## Phase 2 — Conditional follow-ups only

Ask only what is still missing:

- API key availability if the chosen provider is not Ollama and the expected env var is not present in `.env.local` or `.env`
  - options: `Vou colar agora`
  - options: `Ja esta em .env.local`
- absolute vault path if `VAULT_MODE` is not repo-local
- autonomy mode:
  - `Me pergunte antes de indexar (Recommended)`
  - `Rode tudo sem confirmar`

## Phase 3 — Scaffold `tools/lightrag/`

### Required structure

```text
tools/lightrag/
├── pyproject.toml
├── .gitignore
├── README.md
├── lightrag_kg/
│   ├── __init__.py
│   ├── config.py
│   ├── llm.py
│   ├── rag.py
│   ├── index.py
│   ├── server.py
│   ├── to_obsidian.py
│   └── cli.py
└── tests/test_smoke.py
```

### Required implementation rules

1. Use batch insert:

```python
await rag.ainsert([t1, t2, ...], ids=[...], file_paths=[...])
```

2. Create `LightRAG(...)` with explicit performance settings:

```python
LightRAG(
    llm_model_max_async=8,
    max_parallel_insert=6,
    embedding_batch_num=32,
    chunk_token_size=1200,
    chunk_overlap_token_size=100,
)
```

3. Use robust slugify:

```python
def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[/\\\\]", "-", text)
    text = re.sub(r"[^a-z0-9\\s_-]", "", text)
    text = re.sub(r"\\s+", "-", text)
    text = re.sub(r"-+", "-", text).strip("-_")
    return (text[:180] if text else "unknown")
```

4. Wrap document content before insert:

```python
f"FILE: {rel}\\nLANG: {lang}\\n---\\n{content}"
```

5. Use deterministic doc ids:

```python
f"doc-{sha1(rel_path.encode()).hexdigest()[:12]}"
```

6. Maintain incremental manifest `.index_manifest.json` with `{path: sha1(bytes)[:16]}`.
7. Implement provider fallback caches for model resolution.
8. Retry `429/500/503/504/UNAVAILABLE` with `tenacity`.
9. Obsidian export must use `file_path` for "Appears in", split `<SEP>`, and use `louvain_communities(seed=42)`.
10. MCP server must expose only `kg_query`, `kg_insert_text`, and `kg_stats`.

### `pyproject.toml`

Use these base dependencies plus the chosen provider SDKs:

```toml
[project]
name = "lightrag-kg"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = [
    "lightrag-hku>=1.4.0",
    "python-dotenv>=1.0.0",
    "mcp>=1.2.0",
    "rich>=13.0.0",
    "networkx>=3.0",
    "numpy>=1.26",
    "tenacity>=8.0",
    "nano-vectordb>=0.0.4",
    "aiofiles>=23.0",
    "tiktoken>=0.7",
    "pipmaster>=0.0.20",
]

[project.scripts]
kg-server = "lightrag_kg.server:main"
kg-index = "lightrag_kg.index:main"
kg-to-obsidian = "lightrag_kg.to_obsidian:main"
rag = "lightrag_kg.cli:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["lightrag_kg"]
```

Add exactly one provider set:

- Gemini => `google-genai>=1.0.0`
- OpenAI => `openai>=1.50.0`
- Anthropic + Voyage => `anthropic>=0.40.0`, `voyageai>=0.3`
- Ollama => `ollama>=0.4`

### Unified `rag` CLI contract

Required subcommands:

- `rag search "<term>"`
- `rag ask "<question>"`
- `rag chunks "<term>"`
- `rag local "<term>"`
- `rag global "<term>"`
- `rag stats`
- `rag top [N=20]`
- `rag find "<entity>"`
- `rag show "<entity>"`
- `rag index [--full|--dry-run|--incremental]`
- `rag export [--clean]`
- `rag insert "<text>" [--source LABEL]`
- `rag shell`
- `rag mcp-check`

CLI requirements:

- `rag search` is the default ergonomic path and renders Markdown via `rich.markdown.Markdown`
- support global `--json`
- `rag shell` supports `/local`, `/global`, `/chunks`, `/stats`, `/top`, `/find`, `/show`, `/exit`
- `rag mcp-check` validates `.mcp.json`, the absolute `tools/lightrag` path, and that `kg-server` imports or `--help` works

### `.mcp.json` rules

- Read `.mcp.json` if it exists; otherwise create `{"mcpServers": {}}`
- merge safely and preserve existing entries
- add:

```json
"lightrag": {
  "command": "uv",
  "args": [
    "run",
    "--project",
    "<ABSOLUTE_PATH>/tools/lightrag",
    "kg-server"
  ]
}
```

- use the git top-level absolute path, never a relative path
- if `.claude/settings.local.json` contains `mcpServers`, remove only that key and keep the rest
- remind the user that the next Claude Code start will ask: `Trust this .mcp.json?`

### Include/exclude rules

Include according to stack:

- Node/Next/React => `app/**/*.{ts,tsx}`, `components/**`, `pages/**`, `lib/**`, `src/**/*.{ts,tsx}`
- Python => `src/**/*.py`, `<pkg>/**/*.py`
- Rust => `src/**/*.rs`, `Cargo.toml`
- Go => `**/*.go`, `go.mod`
- Convex => `convex/**/*.ts` excluding `convex/_generated/**`
- Prisma => `prisma/schema.prisma`
- Always => root `*.md`, `docs/**/*.md`, main config files

Always exclude:

- `node_modules`
- `.next`
- `dist`
- `build`
- `.git`
- `target`
- `__pycache__`
- `.venv`
- `tests`
- `__tests__`
- `*-generated`
- `_generated`
- binaries
- `*.lock`
- `*.tsbuildinfo`
- `tools/lightrag/**`
- `<vault_path>/**`

## Phase 4 — Install and validate

1. Narrate before dependency install:

> "Instalando LightRAG e dependencias num venv isolado (~30s, sem prompts)."

2. Run:

```bash
uv sync --project tools/lightrag
```

3. Probe the chosen provider:
   - chat probe should answer `OK`
   - embed probe should accept `["probe"]`
   - report resolved models and apply fallback automatically on `404`

4. Run dry plan:

```bash
uv run --project tools/lightrag kg-index --dry-run
```

5. If autonomy is confirm-first, pause before the paid index.
6. Run the full index in the background and poll status every ~45s:
   - report `total`, `processed`, `processing`, `pending`, `failed`
   - treat `Content already exists` as duplicate, not fatal

7. Export:

```bash
uv run --project tools/lightrag kg-to-obsidian --clean
```

8. Validate:

```bash
uv run --project tools/lightrag rag stats
uv run --project tools/lightrag rag search "explique o projeto em 2 frases"
uv run --project tools/lightrag rag mcp-check
```

Also confirm:

- `.mcp.json` exists and contains `lightrag`
- the absolute `--project` path points to `tools/lightrag`
- `uv run --project <path> kg-server --help` does not crash
- exported vault contains entities, sources, and communities

## Phase 5 — Final delivery

Deliver four sections:

### 1. Summary

Keep it under ten bullets and include:

- created files and folders
- provider + resolved models
- entities / relations / communities
- actual cost
- indexing duration

### 2. CLI usage

Default guidance must prefer venv activation first:

```bash
source tools/lightrag/.venv/bin/activate
rag search "como funciona X"
rag stats
rag shell
rag index --incremental
rag export --clean
deactivate
```

Also mention:

- `rag ask`, `rag local`, `rag global`, `rag chunks`
- `rag top`, `rag find`, `rag show`
- `rag insert ... --source ...`
- `rag mcp-check`
- `--json`
- verbose fallback without venv:

```bash
uv run --project tools/lightrag rag search "termo"
```

### 3. Obsidian checklist

Use markdown checkboxes:

- open the vault path
- trust author
- open Graph View
- filter `path:entities/`
- verify group colors by `entity_type`
- click top entities from `INDEX.md`

### 4. MCP activation checklist

Use markdown checkboxes:

- close current Claude Code session
- reopen Claude Code in this repo
- accept `Trust this .mcp.json?`
- confirm `lightrag` is connected in Project MCPs
- test `kg_stats` or `kg_query`

### Maintenance commands

```bash
rag index
rag index --full
rag export --clean
```

## Golden rules

- MCP config always lives in `.mcp.json`, never `.claude/settings.local.json`
- always use absolute paths in the `uv run --project ...` MCP entry
- never commit `.env.local`, `rag_storage/`, or `.index_manifest.json`
- never expose reindex/export tools through MCP
- always merge `.mcp.json` safely
- default user guidance is `source tools/lightrag/.venv/bin/activate`
- auto-install prereqs when possible instead of blocking on manual setup
- if anything outside the expected happy path breaks, stop and ask
