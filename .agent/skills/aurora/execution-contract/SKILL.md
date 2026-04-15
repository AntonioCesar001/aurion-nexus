# SKILL.md — Execution Contract Handling

## Description
How to receive, validate, decompose, and track an Execution Contract from the Aurion squad. All contracts are assessed against the SEIP v2 value chains before work begins.

## When to use
When an Execution Contract arrives from Aurion (CEO) to Aurora (COO).

---

## Contract Structure

Every valid Execution Contract must contain:
1. **Objective** — What needs to be delivered. Specific, not vague.
2. **Context** — Background, constraints, existing code/systems involved.
3. **Acceptance Criteria** — Measurable. "User can do X and sees Y" — not "it works".
4. **SEIP Phase Tags** — Which SEIP phases apply (auto-detected in Preflight Gate Block 3).
5. **Value Chain** — Which interdependency chain governs this work.

---

## SEIP Value Chain Assessment

Before decomposing any contract into tasks, the COO MUST identify the governing value chain and enforce its sequence. **Never skip steps in a chain.**

### Chain 1 — Contract → Implementation → Validation
**Applies to**: New APIs, modified endpoints, service integrations, multi-service boundaries.
```
1. OpenAPI spec defined and Spectral-linted FIRST
2. SDK/stubs generated from spec (openapi-generator)
3. Contract tests written (Pact.js) — consumer defines expectations
4. Implementation to fulfill contract
5. Provider verification against Pact broker
6. E2E validation (Playwright) of full flow
```
**Rule**: Code review of implementation is blocked if step 1 (OpenAPI spec) is absent.

### Chain 2 — Domain → Backend → Data
**Applies to**: New business modules, entities, state machines, domain events.
```
1. Domain model reviewed by Aurion (Deep Interview + ADR if significant)
2. Entities, value objects, invariants defined as tests first (TDD)
3. Hexagonal structure applied (domain core isolated from adapters)
4. Backend implementation
5. Persistence layer (schema, migrations via Flyway/Prisma)
6. Database Reviewer sign-off
```
**Rule**: No database table is created before the domain entity is modeled and reviewed.

### Chain 3 — Identity → Authorization → Audit
**Applies to**: Auth changes, permission system, RBAC/ABAC, user data access, compliance.
```
1. Identity layer verified (Keycloak/Kratos/Supabase Auth pattern)
2. Authorization policies defined and decoupled (Cerbos/OpenFGA — NOT inline if-else)
3. Audit trail confirmed (immudb or equivalent for regulated actions)
4. Security Reviewer sign-off
```
**Rule**: Inline permission checks in route handlers require Security Reviewer mandatory review.

### Chain 4 — Event → Workflow → Observability
**Applies to**: Async processing, background jobs, event-driven integrations, long-running workflows.
```
1. AsyncAPI spec defined for event contracts
2. Message schema validated
3. Workflow orchestration layer (Temporal/BullMQ) with retry and error handling
4. OpenTelemetry instrumentation on all async paths
5. Grafana/dashboard alert defined for failure rate
```
**Rule**: Async work without observability instrumentation cannot be deployed.

### Chain 5 — AI → RAG → Safety → Eval
**Applies to**: LLM integration, RAG pipelines, agent tools, prompt engineering, AI-generated output.
```
1. Agent orchestration architecture approved (LangGraph pattern if stateful)
2. Vector storage strategy defined (pgvector vs Qdrant, based on scale)
3. Guardrails implemented (NeMo Guardrails or guardrails-ai)
4. AI Safety Reviewer sign-off (OWASP LLM Top 10 review)
5. promptfoo evaluations: core behavior + safety probes + format compliance
6. Observability: Phoenix/Arize tracing on LLM pipeline
```
**Rule**: Steps 3, 4, and 5 are **hard gates**. No LLM feature ships without all three.

### Chain 6 — Design → Component → Accessibility → Visual Test
**Applies to**: New UI components, pages, design system changes, frontend features.
```
1. Design tokens applied (no magic numbers, no pure defaults)
2. Component built on accessible primitives (Radix UI or equivalent)
3. Composed into design system (shadcn pattern or project DS)
4. Storybook story created for component documentation
5. axe-core accessibility audit (zero critical/serious violations)
6. Visual regression baseline captured (Chromatic or Playwright snapshots)
```
**Rule**: Steps 5 and 6 are mandatory for any shared/system component change.

---

## Workflow

1. **COO receives** the contract and runs Preflight Gate (all 4 blocks).
2. **COO identifies** the governing SEIP value chain(s) for this contract.
3. **CINO validates** technical assumptions (research phase — never skip on new domain).
4. **CPO decomposes** into tasks per specialist, respecting the chain sequence.
5. **Specialists execute** (CDO/CTO/CIO) in parallel where chains allow, sequentially where they don't.
6. **CQO reviews** all layers: code quality + SEIP compliance + testing standards.
7. **QA Director tests** critical flows (E2E, contract, performance as applicable).
8. **AI Safety Reviewer** clears any Phase 8/9 items (mandatory, not optional).
9. **Design QA** clears any Phase 10 items (mandatory for UI work).
10. **CXO consolidates** delivery evidence and prepares handoff.
11. **CLO records** the cycle memory with chain compliance status.

---

## Handoff Back to Aurion

Deliver to Aurion:
- Completed artifact(s)
- SEIP chain compliance status (which chains ran, any deviations documented)
- Test results: unit coverage % + E2E pass/fail + contract status + accessibility violations
- Deploy link (if applicable)
- ADR references if architectural decisions were made
- Cycle memory summary from CLO

---

## Escalation Rules

| Trigger | Action | SLA |
|---------|--------|-----|
| Ambiguous requirements | Escalate to Aurion, run Deep Interview | Immediate |
| Scope change mid-cycle | Pause affected tasks, notify Aurion | Within 15 minutes |
| Strategic blocker | Escalate to Aurion | Within 30 minutes |
| SEIP chain violation detected | Stop affected work, restore chain sequence | Before proceeding |
| Phase 9 gate fails (AI safety) | Hard block — do not deploy | Immediate |
| Phase 6 gate fails (security CRITICAL) | Hard block — notify immediately | Immediate |

---

## Contract Anti-Patterns (Reject These)

| Anti-Pattern | Why It Fails | Correct Form |
|-------------|-------------|--------------|
| "Make the API work" | No acceptance criteria | "POST /orders returns 201 with order ID when valid payload is sent" |
| "Add auth to the app" | No chain identified | "Add JWT auth to /api/* routes using Chain 3 (Identity → Auth → Audit)" |
| "Build the chat feature" with no Phase tag | AI feature without safety gate | Tag with Phase 8+9, require AI Safety Reviewer before decomposition |
| "Fix the bug ASAP" | Skips preflight and chain assessment | Still run preflight — fast does not mean unsafe |
| Contract with no testable criterion | QA cannot verify "done" | Rewrite criterion before accepting |
