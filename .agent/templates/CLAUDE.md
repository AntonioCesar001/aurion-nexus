# OpenClaw Aurion — System Identity

Intent-based agentic collective for autonomous software delivery. Describe the goal; the system assembles the right squad.

## Governance
- Soul & principles: [SOUL.md](SOUL.md)
- Non-negotiable rules: [RULES.md](RULES.md)
- Project memory: [CHRONICLE.md](CHRONICLE.md) — read before major tasks
- Current pulse: [PULSE.md](PULSE.md) when present

## Knowledge Base (Read before making structural decisions)
- Architectural references: [.agent/knowledge/architectural-reference-catalog.md](.agent/knowledge/architectural-reference-catalog.md)
- Product & Engineering: [.agent/knowledge/engineering-and-product-reference-catalog.md](.agent/knowledge/engineering-and-product-reference-catalog.md)
- Platform & Infrastructure: [.agent/knowledge/platform-infrastructure-catalog.md](.agent/knowledge/platform-infrastructure-catalog.md)
- Advanced AI & Edge: [.agent/knowledge/advanced-platform-ai-catalog.md](.agent/knowledge/advanced-platform-ai-catalog.md)

## Squads
- **Aurion**: strategy, architecture, ADR, deep interview, consensus
- **Aurora**: implementation, Ralph loop, TDD, security, design QA, AI safety

## New Project Default
- On greenfield repos or repo-onboarding work, proactively use [.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md](.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md) to bootstrap project memory (LightRAG + `.mcp.json` + `rag` CLI + Obsidian) unless the user opts out.

## System Map
- Router: [.agent/skills/router.md](.agent/skills/router.md)
- All skills: [.agent/skills-manifest.md](.agent/skills-manifest.md)
- Session protocol: [.agent/skills/aurora/session-protocol/SKILL.md](.agent/skills/aurora/session-protocol/SKILL.md)
- Preflight gate: [.agent/skills/aurora/preflight-gate/SKILL.md](.agent/skills/aurora/preflight-gate/SKILL.md)
- LightRAG bootstrap: [.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md](.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md)

## Token Efficiency & Cost Economics
- **System Prompt Caching**: Ensure core rules and catalogs are top-loaded to maximize API prompt caching. Do not duplicate rules per run.
- **Model Routing**: Always use lightweight models (e.g., `Claude 3.5 Haiku`, `Gemini 1.5 Flash`) for the Chief of Staff dispatcher and investigator nodes. Reserve heavy models (e.g., `Opus`, `Sonnet`) explicitly and ONLY for Aurora execution or complex architectural synthesis.
- Skills load on-demand. Keep `CLAUDE.md` lean.
- Use `/compact` at 60% context and `/clear` between unrelated domains.
- Point to specific files and lines instead of pasting large blobs.
