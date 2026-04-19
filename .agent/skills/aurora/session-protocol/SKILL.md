# SKILL.md — Session & Token Protocol

## Description
Operating rules to minimize token consumption per session. Apply these before and during every work session to maximize throughput per credit.

## When to use
At session start, and whenever context feels heavy or a task changes domain.

---

## How Token Cost Works

Each message re-reads the ENTIRE conversation history. Cost is **compound**, not linear:
- Message 1 reads itself → cheap
- Message 30 reads all 29 previous messages + itself → ~30× cost of message 1

**CLAUDE.md** is read once per conversation and stays in context — every line costs tokens on every message. Skills are loaded on-demand only.

---

## Pre-Session Checklist

Before starting any non-trivial work:

1. **Disconnect unused MCPs** — Run `/mcp` and disconnect any server not needed for this task. Each connected MCP adds ~10k-30k tokens of invisible overhead per message.
2. **Check context** — Run `/context` to see current token consumption and what's eating budget.
3. **Use Plan Mode first** — Press `Shift+Tab` to activate Plan Mode before any complex task. Claude maps the approach, you approve, then it executes. This prevents 2–5× token waste from wrong-direction rework.
4. **One conversation per domain** — Never carry context from Task A into Task B. Different topics = `/clear` and start fresh.
5. **New project memory bootstrap** — On greenfield repos or repo-onboarding work, load `.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md` unless the user explicitly does not want a LightRAG + MCP + Obsidian setup.

---

## During Execution

### The 60% Rule
When context reaches ~60% capacity, run:
```
/compact Keep: tests that passed, architecture decisions, edited files. Discard: failed attempt history, exploratory dead ends.
```
Do NOT wait for autocompact at 95% — by then context quality has already degraded ("Lost in the Middle" effect).

### Stay Watching
Do not send a prompt and switch tabs on complex tasks. If Claude enters a loop (reading the same files repeatedly, regenerating the same code), **interrupt immediately** — loops produce zero value and burn context fast.

### Surgical File References
Never say "here's the repo, find the bug." Point directly:
- Good: `@src/api/auth.ts line 87`
- Bad: paste the entire file

Paste only the relevant function/section. An entire 1000-line file = ~5k tokens. The relevant 30-line function = ~200 tokens.

### Group Prompts — Never Chain
3 separate messages cost ~3× more than 1 combined message. If Claude made a mistake, **edit the original message and regenerate** — don't send a correction as a follow-up. Follow-ups permanently accumulate in history; edits replace the exchange.

---

## Model Selection per Task

| Task Type | Model | Rationale |
|-----------|-------|-----------|
| Architecture decisions, complex trade-offs | Opus | Critical thinking justifies 5–10× cost |
| Feature implementation, debugging, tests | Sonnet | Best default — quality + efficiency |
| Simple search, classification, formatting | Haiku | Same-quality on simple tasks at lower cost |
| Sub-agents for research/lookup | Haiku | Never spawn Sonnet/Opus sub-agents for simple lookups |

**Rule**: Opus for < 20% of tasks. Default to Sonnet. Delegate simple sub-agent work to Haiku.

---

## CLAUDE.md Maintenance Rules

The CLAUDE.md is paid on **every message** in **every conversation**. Keep it lean:

- **Hard limit**: 60 lines maximum. Under 40 is ideal.
- **What belongs in CLAUDE.md**: stack identity, squad map, key pointers to skills.
- **What does NOT belong**: detailed guides, checklists, examples, workflow steps — move these to skills.
- **Rule of thumb**: If an instruction repeats in > 3 sessions → add to CLAUDE.md. If it's workflow-specific → make it a skill.

---

## Multi-Agent Cost Awareness

Each sub-agent spawned initializes from scratch with the full context (CLAUDE.md + MCPs + system prompt). Spawning 3 sub-agents for a single task = 4× context overhead before any real work begins.

**Rules**:
- Use parallel sub-agents only when tasks are truly independent and each justifies the overhead
- Prefer sequential single-agent execution for most tasks
- When sub-agents are necessary, assign Haiku to simple lookups and Sonnet to complex work
- Never spawn Opus sub-agents for auxiliary tasks

---

## Quick Reference

| Situation | Action |
|-----------|--------|
| Starting unrelated task | `/clear` then start fresh |
| Context at ~60% | `/compact` with explicit keep/discard instructions |
| Loop detected | Interrupt immediately with Escape |
| MCP not needed for this task | Disconnect via `/mcp` |
| About to paste large file | Paste only the relevant section |
| About to send follow-up correction | Edit original message and regenerate instead |
| Complex task with unclear requirements | `Shift+Tab` Plan Mode first |
| Simple sub-agent lookup | Explicitly request Haiku model |
