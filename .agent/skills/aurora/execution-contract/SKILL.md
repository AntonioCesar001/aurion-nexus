# SKILL.md — Execution Contract Handling

## Description
How to receive, validate, decompose, and track an Execution Contract from the Aurion squad.

## When to use
When an Execution Contract arrives from Aurion (CEO) to Aurora (COO).

## Contract structure
Every valid Execution Contract must contain:
1. **Objective** — What needs to be delivered.
2. **Context** — Background, constraints, existing code/systems involved.
3. **Acceptance criteria** — How to verify the work is done.

## Workflow
1. **COO receives** the contract and runs preflight.
2. **CINO validates** technical assumptions (research phase).
3. **CPO decomposes** into tasks per specialist with sequencing.
4. **Specialists execute** (CDO/CTO/CIO) in parallel where possible.
5. **CQO reviews** before merge/deploy.
6. **QA Director tests** critical flows.
7. **CXO consolidates** delivery evidence and prepares handoff.
8. **CLO records** the cycle memory.

## Handoff back to Aurion
Deliver to Aurion:
- Completed artifact(s)
- Test results (pass/fail/coverage)
- Deploy link (if applicable)
- Cycle memory summary from CLO

## Escalation rules
- Ambiguous requirements → escalate to Aurion immediately
- Scope change mid-cycle → pause affected tasks, notify Aurion
- Strategic blocker → SLA: escalate within 30 minutes
