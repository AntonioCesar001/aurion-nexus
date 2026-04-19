# SKILL.md — LightRAG Project Bootstrap

## Description
Interactive setup wizard for bootstrapping a repo-scoped LightRAG knowledge pipeline with project-level MCP wiring in `.mcp.json`, a local `rag` CLI, and an Obsidian export.

## When to use
- At new-project kickoff when the user wants persistent project memory, repo RAG, or a knowledge graph
- When asked for LightRAG, Obsidian graph export, `.mcp.json` MCP setup, or a terminal `rag` CLI
- Before AI/RAG implementation work when the repository still lacks a project memory layer

## Default stance
- On greenfield projects, proactively offer this bootstrap unless the user clearly opts out.
- Treat this as an Aurora operational bootstrap. Escalate to Aurion only if provider, scope, or autonomy choices are strategically ambiguous.
- MCP registration belongs in `.mcp.json` at the repo root. Never place MCP servers in `.claude/settings.local.json`.

## Interaction rules
- Bundle decisions into one question round whenever possible.
- Translate environment-specific instructions to the active agent runtime:
  - `AskUserQuestion` => one concise direct user message with only the missing decisions
  - `TodoWrite` => a visible checklist via plan updates or short progress summaries
  - background indexing => long-running terminal session plus periodic status polling
- Auto-install `uv` and Python 3.11+ when missing. Narrate each installation in one short human sentence before executing it.
- Never reveal secret values; inspect only variable names and presence.

## Non-negotiables
- Preserve existing `.mcp.json` entries and merge safely.
- Expose only `kg_query`, `kg_insert_text`, and `kg_stats` in the MCP server.
- Keep storage artifacts out of git: `.env.local`, `.env`, `rag_storage/`, `.index_manifest.json`, `.venv/`.
- Prefer `source tools/lightrag/.venv/bin/activate` as the default CLI usage guidance after installation.
- Stop and escalate if prereq installation still fails after the explicit validation gate.

## Workflow
1. Run silent discovery and prereq detection.
2. Auto-install `uv` and Python 3.11+ if required.
3. Ask the bundled decision set: provider, scope, vault mode, and git strategy.
4. Ask only the truly missing follow-ups: API key availability, absolute vault path, and autonomy mode.
5. Scaffold `tools/lightrag/` with provider-specific wiring, the MCP server, and the unified `rag` CLI.
6. Run `uv sync`, probe the provider, dry-run the index, then execute the real index with periodic status reporting.
7. Export to Obsidian, validate `rag`, validate MCP wiring, and deliver the usage checklist.
8. Fire `bin/nexus-push` to bridge local knowledge to the WikiMind Central Core.

## File layout and validation details
Read [references/setup-playbook.md](references/setup-playbook.md) before scaffolding or validating. It contains:
- prereq detection commands and narration rules
- provider/env matrix and follow-up decision logic
- mandatory project structure, CLI surface, and `.mcp.json` merge rules
- include/exclude rules for indexing
- final delivery checklist for CLI, Obsidian, and MCP activation

## Owner
Aurora COO (`coordinator`) with CPTO support for prereqs and MCP wiring
