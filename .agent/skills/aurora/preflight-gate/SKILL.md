# SKILL.md — Aurora Preflight Gate

## Description
Validates that all required MCPs, credentials, workspace paths, acceptance criteria, and SEIP alignment are confirmed before any Aurora execution cycle starts. No execution begins without a clean preflight.

## When to use
Before every execution cycle. The COO and CPTO must run this preflight checklist.

---

## Checklist

### Block 1 — Infrastructure
1. **MCPs operational** — Call a real tool on each required MCP (Stitch, Vercel, Supabase, TestSprite). Schema loading alone is NOT sufficient.
2. **Credentials valid** — Verify each credential in `docs/aurora/CREDENTIAL_MAP.md` is current and not expired.
3. **Workspace paths** — Verify all referenced file paths and agent directories exist and are accessible.

### Block 2 — Contract Quality
4. **Acceptance criteria** — Confirm the Execution Contract has an explicit, testable acceptance criterion. Vague criteria (e.g., "make it work") = STOP.
5. **No strategic ambiguity** — If the contract has unclear requirements or multiple interpretations, STOP and escalate to Aurion. Never start execution guessing intent.

### Block 3 — SEIP Phase Applicability
Determine which SEIP phases apply to this execution contract. Check each:

| SEIP Phase | Trigger Condition | Required Action |
|-----------|------------------|-----------------|
| **Phase 1** (Structure) | New module, service, or major refactor | Verify hexagonal boundaries and modular organization before implementation |
| **Phase 2** (Domain) | New business entity, event, or state machine | Deep Interview must model domain before any DB schema or endpoint is created |
| **Phase 3** (Product/UI) | Any new UI component, page, or design system change | Trigger Design QA agent + Design Standards review |
| **Phase 4** (Contracts) | New API endpoint, changed payload, new service integration | OpenAPI spec must exist BEFORE code. Pact contract must exist for multi-service boundaries |
| **Phase 5** (Persistence) | New table, schema change, migration, vector search | Database Reviewer must approve schema. Migration must be reversible |
| **Phase 6** (Security) | Auth, permissions, user input, external API, payment | Security Reviewer mandatory. OWASP checklist required |
| **Phase 7** (Quality/Ops) | Any deployable feature | E2E tests required. Performance baseline checked |
| **Phase 8** (AI/LLM) | LLM integration, RAG pipeline, agent tool, prompt change | AI Safety Reviewer mandatory. promptfoo evaluations required |
| **Phase 9** (AI Safety) | Any user-facing AI feature | Full OWASP LLM Top 10 review. Guardrails required. Hard block without them |
| **Phase 10** (Design Excellence) | Any UI work | Design QA agent required. axe-core audit required. Visual regression baseline updated |

If Phase 8 applies on a new or unprepared repository, run `.agent/skills/aurora/lightrag-project-bootstrap/SKILL.md` before implementation whenever the team needs repo memory, a project-scoped MCP, or a terminal RAG workflow.

### Block 4 — Value Chain Alignment
For complex tasks, identify which SEIP value chain applies and confirm dependencies are in place:

| Chain | Applies When | Pre-condition |
|-------|-------------|---------------|
| Contract → Impl → Validation | New API or service integration | OpenAPI spec exists and linted by Spectral |
| Domain → Backend → Data | New business module | Domain model reviewed by Aurion before code starts |
| Identity → Auth → Audit | Auth or permission changes | Keycloak/Cerbos pattern in use. immudb or equivalent for audit trail |
| Event → Workflow → Observability | Async processing or background jobs | OpenTelemetry instrumentation in place |
| AI → RAG → Safety → Eval | LLM pipeline work | Guardrails defined. promptfoo config exists |
| Design → Component → A11y → Visual Test | UI work | Design tokens in use. axe-core integrated in CI |

---

## Failure Actions

| Failure | Action |
|---------|--------|
| Any MCP fails | Escalate to CPTO for repair. Do not proceed |
| Credentials expired | Escalate to CPTO for rotation. Do not proceed |
| Contract is ambiguous | Escalate to Aurion (CEO). Run Deep Interview |
| SEIP Phase 8/9 applies but no AI Safety Reviewer | Hard block — cannot start LLM work |
| SEIP Phase 10 applies but Design QA not available | Block UI work — queue for next cycle |
| Value chain dependency missing | Resolve dependency first, then restart preflight |

**Never start execution with a failed preflight.**

---

## Preflight Sign-off Format

```markdown
## Preflight Gate — [Contract Name]
**Date**: YYYY-MM-DD
**COO**: [name/id]

### Block 1 — Infrastructure
- [ ] MCPs operational
- [ ] Credentials valid
- [ ] Workspace paths verified

### Block 2 — Contract Quality
- [ ] Acceptance criteria: explicit and testable
- [ ] No strategic ambiguity

### Block 3 — SEIP Phases Active
- [ ] Phase 1 (Structure): [YES / NO / N/A]
- [ ] Phase 2 (Domain): [YES / NO / N/A]
- [ ] Phase 3 (Product/UI): [YES / NO / N/A]
- [ ] Phase 4 (Contracts): [YES / NO / N/A]
- [ ] Phase 5 (Persistence): [YES / NO / N/A]
- [ ] Phase 6 (Security): [YES / NO / N/A]
- [ ] Phase 7 (Quality/Ops): [YES / NO / N/A]
- [ ] Phase 8 (AI/LLM): [YES / NO / N/A]
- [ ] Phase 9 (AI Safety): [YES / NO / N/A]
- [ ] Phase 10 (Design Excellence): [YES / NO / N/A]

### Block 4 — Value Chains
- Active chains: [list]
- Dependencies confirmed: [YES / NO]

### Verdict
**[CLEAR TO EXECUTE / BLOCKED — reason]**
```

---

## Owners
- Primary: COO (`coordinator`)
- Support: CPTO (`platform_engineer`)
- AI Safety gate: `ai-safety-reviewer`
- Design gate: `design-qa`
