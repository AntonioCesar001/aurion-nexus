# ADR Protocol — AURION

## Description
This skill formalizes the capture and documentation of Architecture Decision Records (ADRs).

## Purpose
To maintain a historical record of why specific architectural choices were made and what their consequences are.

## When to use
An ADR is mandatory for any decision that:
- Changes the system's core architecture.
- Introduces new major dependencies.
- Changes database schema significantly.
- Affects security or performance characteristics.

## Record Format
Every ADR must include:
1. **Title**: Short and descriptive (e.g., "ADR-001: Move to Hexagonal Architecture").
2. **Status**: Proposed, Accepted, Superceded, or Rejected.
3. **Context**: What is the problem? What are the constraints?
4. **Decision**: What did we choose?
5. **Consequences**: What are the trade-offs? (Positive and Negative).

## Storage
ADRs are stored in `/home/shoxsx/code/openclaw Aurion/ADR/` and linked in `CHRONICLE.md`.
