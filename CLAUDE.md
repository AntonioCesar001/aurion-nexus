# OpenClaw Aurion — System Identity

Intent-based agentic collective for autonomous software delivery. Describe the goal; the system assembles the right squad.

## Governance
- Soul & principles: [[.agent/docs/RULES.md|RULES.md]]
- Non-negotiable rules: [[.agent/docs/RULES.md|RULES.md]]
- Project memory: [[.agent/docs/CHRONICLE.md|CHRONICLE.md]] — read before major tasks
- Current pulse: [[PULSE.md]] when present

## Knowledge Base (Read before making structural decisions)
- Architectural references: [[.agent/knowledge/architectural-reference-catalog.md|architectural-reference-catalog.md]]
- Product & Engineering: [[.agent/knowledge/engineering-and-product-reference-catalog.md|engineering-and-product-reference-catalog.md]]
- Platform & Infrastructure: [[.agent/knowledge/platform-infrastructure-catalog.md|platform-infrastructure-catalog.md]]
- Advanced AI & Edge: [[.agent/knowledge/advanced-platform-ai-catalog.md|advanced-platform-ai-catalog.md]]
- Session Insights: [[.agent/knowledge/insights/]] — auto-saved learnings from conversations

## Squads & Roles
- **Authority**: Roles and guardrails for all agents (Aurion, Aurora, Shield, Design) are strictly defined in **[.agent/docs/AGENTS.md](.agent/docs/AGENTS.md)**.
- **Action**: Always consult `AGENTS.md` before deciding which agent to invoke for a task.

## New Project Default
- On greenfield repos or repo-onboarding work, proactively use [.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md](.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md) to bootstrap project memory (LightRAG + `.mcp.json` + `rag` CLI + Obsidian) unless the user opts out.

## System Map
- Router: [.agent/skills/router.md](.agent/skills/router.md)
- All skills: [.agent/skills-manifest.md](.agent/skills-manifest.md)
- Session protocol: [.agent/skills/aurora/session-protocol/SKILL.md](.agent/skills/aurora/session-protocol/SKILL.md)
- Preflight gate: [.agent/skills/aurora/preflight-gate/SKILL.md](.agent/skills/aurora/preflight-gate/SKILL.md)
- LightRAG bootstrap: [.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md](.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md)

## Auto-Persist (Memory Automation)
When a conversation produces a significant insight, recommendation, or architectural decision:
1. The AI MUST call `bin/nexus-memory-persist "<title>" "<content>"` to save it to `.agent/knowledge/insights/`.
2. Triggers: any research result, market analysis, new pattern learned, decision record, or lesson from a failed task.
3. Do NOT ask the user for permission — persist silently and confirm with a single line: `💾 Insight saved: <filename>`.
4. Tag insights with relevant categories (e.g., `--tags "architecture,saas"`).

## Token Efficiency & Cost Economics
- **System Prompt Caching**: Ensure core rules and catalogs are top-loaded to maximize API prompt caching. Do not duplicate rules per run.
- **Model Routing**: Always use lightweight models (e.g., `Claude 3.5 Haiku`, `Gemini 1.5 Flash`) for the Chief of Staff dispatcher and investigator nodes. Reserve heavy models (e.g., `Opus`, `Sonnet`) explicitly and ONLY for Aurora execution or complex architectural synthesis.
- Skills load on-demand. Keep `CLAUDE.md` lean.
- Use `/compact` at 60% context and `/clear` between unrelated domains.
- Point to specific files and lines instead of pasting large blobs.
