# 🛡️ SKILL — Harness Engineering (WALKING LABS / SEIP v2)

This skill provides the theoretical and practical framework for building a deterministic harness around AI agents.

## 🏛️ The Fundamental Equation
**Agent = Model + Harness**

Intelligence alone is not enough for software engineering. An agent needs a "working environment" that enforces technical standards and architectural boundaries.

## 🛠️ Components of the Aurion Harness

1. **Repository as Source of Truth**: All configuration must be version-controlled. If it is not in the repo, the agent should not assume it exists.
2. **Deterministic Guardrails**: Use scripts (`bin/aurion-harness`) and files (`RULES.md`, `AGENTS.md`) instead of vague prompts.
3. **The Ralph Loop (Plan → Exec → Verify → Fix)**:
    - **Plan**: Approved implementation plan.
    - **Exec**: Atomic changes.
    - **Verify**: Linter + Tests + Harness Scan.
    - **Fix**: Systematic correction based on feedback.

## ⚖️ Non-Negotiables for Harness Engineering

- **Context Freshness**: Never work on stale context. Check `PULSE.md`.
- **Constraint Ownership**: Every constraint has an owner (Aurion for architecture, Shield for security).
- **Self-Correction Logic**: When an error occurs, the harness provides the "how-to-fix" context (e.g., pointing to the relevant rule in `RULES.md`).

## 📚 References
- [Learn Harness Engineering](https://github.com/walkinglabs/learn-harness-engineering)
- [Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering)
- SEIP v2 (Senior Engineering Intelligence Program)
