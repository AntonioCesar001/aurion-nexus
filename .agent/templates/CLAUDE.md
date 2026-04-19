# OpenClaw Aurion — System Identity

Intent-based agentic collective for autonomous software delivery. Describe the goal; the system assembles the right squad.

## Governance
- Soul & principles: [SOUL.md](SOUL.md)
- Non-negotiable rules: [RULES.md](RULES.md)
- Project memory: [CHRONICLE.md](CHRONICLE.md) — read before major tasks
- Current pulse: [PULSE.md](PULSE.md) when present

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

## Token Efficiency
- Skills load on-demand. Keep `CLAUDE.md` lean.
- Use `/compact` at 60% context and `/clear` between unrelated domains.
- Point to specific files and lines instead of pasting large blobs.
