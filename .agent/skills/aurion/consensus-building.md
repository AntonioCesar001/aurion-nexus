# Consensus Building (Ralplan) — AURION

## Description
This skill coordinates a multi-agent consensus loop to ensure that complex plans are architecturally sound and optimized.

## The Ralplan Loop
Aurion can spin up a temporary council of agents to review a plan:
1. **Planner**: Creates the initial implementation plan.
2. **Architect**: Reviews for root cause correctness, file:line evidence, and long-term impact.
3. **Critic**: Challenges the plan for quality, security, and testability.

## Consensus Criteria
- **Strongest Antithesis**: Every plan must survive a "steelman" counterargument.
- **Trade-offs**: At least one meaningful trade-off must be acknowledged.
- **Synthesis**: Competing ideas must be synthesized into a single, high-confidence plan.

## When to use
- High-risk architectural changes.
- Complex feature additions.
- Security-critical updates.

## Output
A **Consensus Plan** saved to the mission backlog, featuring an ADR (Architecture Decision Record) explaining the drivers, alternatives, and consequences of the choice.
