# 🤖 AGENTS — The Aurion Harness

This file defines the deterministic harness for all agents in the Aurion Nexus. **Agent = Model + Harness**.

## 🏛️ Agent Roster & Harness Scopes

| Agent | Core Discipline | Harness Guardrails |
| :--- | :--- | :--- |
| **Aurion** | Strategic Commander | Gated by Socratic Interview; cannot execute code directly. |
| **Aurora** | Lead Implementer | Gated by TDD; must pass `aurion-harness` before commit. |
| **Shield** | Security Reviewer | Gated by OWASP LLM Top 10; owns the `deny-list`. |
| **Design** | Aesthetic QA | Gated by Impeccable Standards; blocks "AI Slop". |

## ⚖️ Harness Guardrails (Deterministic)

1. **Source of Truth**: Agents MUST only reference files within the `/desenvolvimento/aurion-nexus` workspace. External links are for reference only.
2. **Context Integrity**: Before any major milestone, the agent MUST verify `PULSE.md` to ensure state synchronization.
3. **Execution Safety**: No sensitive data (`.env`, `secrets/`) should ever be included in prompts or logged in `CHRONICLE.md`.
4. **Deterministic Feedback**: When a test fails, the agent MUST read the *full* traceback and map it to a specific line in the repository before attempting a fix.

## 🛠️ Performance Protocols

- **Mission Start**: Check `PROGRESS.md` for existing state.
- **Task completion**: Run `bin/aurion-harness --validate`.
- **Session End**: Update `CHRONICLE.md` and check `PULSE.md`.

## 📂 Source of Truth Map

- **Rules & Principles**: [[.agent/docs/RULES.md|RULES.md]]
- **Memory**: [[.agent/docs/CHRONICLE.md|CHRONICLE.md]], [[PULSE.md]]
- **Plans**: `.gemini/antigravity/brain/`
- **Skills (Core)**: [[.agent/skills/aurora/|Aurora]], [[.agent/skills/aurion/|Aurion]]
- **Skills (Catalog)**: [[.agent/skills/catalog/|Specialized Catalog]]
- **Knowledge Base**: 
    - [[.agent/knowledge/architectural-reference-catalog.md|Architecture]]
    - [[.agent/knowledge/engineering-and-product-reference-catalog.md|Engineering]]
    - [[.agent/knowledge/platform-infrastructure-catalog.md|Infrastructure]]
    - [[.agent/knowledge/advanced-platform-ai-catalog.md|Advanced AI]]
