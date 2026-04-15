# SEIP v2 — Strategic Reference Guide (Aurion Squad)

## Description
This skill provides the **Aurion strategic squad** with the SEIP v2 Enhanced knowledge base to make informed architectural decisions, choose the right reference patterns, and govern the engineering maturity of any project.

## When to use
- During **architecture reviews** and ADR creation.
- When **choosing technologies, patterns, or reference repositories** for a new module or project.
- During **Deep Interview** sessions to challenge technical assumptions.
- When assessing **engineering maturity** of an existing codebase.
- When planning **study paths** for the team or new domains.

---

## The SEIP Philosophy

> Software sênior não é sobre "fazer mais código". É sobre:
> - estruturar antes de codar
> - modelar antes de implementar
> - justificar antes de decidir
> - proteger antes de expor
> - operar antes de escalar
> - evoluir sem caos
> - construir com IA de forma segura e auditável

---

## Reference Classification System

Every reference in the SEIP is classified by type and level. Use this taxonomy when recommending tools or patterns.

### Types
| Type | Teaches |
|------|---------|
| **referência arquitetural** | Decisions, boundaries, structure, trade-offs |
| **referência de organização** | Structure, modularization, workflow, patterns |
| **referência de código** | Concrete implementation and code patterns |
| **referência prática** | Real execution, real flow, real usage |
| **referência de documentação** | Specs, communication, ADRs, governance |
| **referência de IA/agentes** | Orchestration, prompting, RAG, eval, guardrails |
| **referência de dados** | Analytical modeling, pipelines, visualization |

### Levels
- **iniciante** — Foundational, low-barrier entry.
- **intermediário** — Production-relevant, requires context.
- **avançado** — Enterprise-grade, requires deep domain knowledge.

---

## Value Chains (Interdependencies)

These chains define **how SEIP blocks connect end-to-end**. The Aurion squad MUST understand these chains when making architecture decisions — never recommend a tool in isolation.

### Chain 1 — Contract → Implementation → Validation
```
OAI/OpenAPI-Specification
  → OpenAPITools/openapi-generator  (generates SDK and stubs)
    → pact-foundation/pact-js       (validates contract between services)
      → microsoft/playwright         (validates E2E flow)
```
**Aurion Guidance**: Always start with the contract. Never generate code before defining the API spec.

### Chain 2 — Domain → Backend → Data
```
ddd-by-examples/library
  → Sairyss/domain-driven-hexagon   (structures domain in backend)
    → postgres/postgres + prisma     (persists with consistency)
      → flyway/flyway                (evolves schema safely)
```
**Aurion Guidance**: Model the domain before touching the database. Tables reflect entities, not the other way around.

### Chain 3 — Identity → Authorization → Audit
```
keycloak/keycloak          (authentication and identity)
  → cerbos/cerbos          (decoupled authorization policies)
    → openfga/openfga      (granular relational permissions)
      → immudb             (immutable audit trail)
```
**Aurion Guidance**: Auth is not a feature — it's infrastructure. Separate identity, authorization, and audit from day one.

### Chain 4 — Event → Workflow → Observability
```
apache/kafka               (event streaming)
  → temporalio/temporal    (durable resilient execution)
    → opentelemetry        (flow instrumentation)
      → grafana            (operational visualization)
```
**Aurion Guidance**: Events without observability are invisible failures. Instrument before scaling.

### Chain 5 — AI → RAG → Safety → Eval
```
langchain-ai/langgraph         (agent orchestration)
  → pgvector / chromadb        (embedding storage)
    → NeMo Guardrails          (input/output protection)
      → promptfoo              (continuous quality evaluation)
```
**Aurion Guidance**: An AI system without evaluation is a system without tests. Never deploy LLM pipelines without guardrails and eval.

### Chain 6 — Design → Component → Accessibility → Visual Test
```
style-dictionary/style-dictionary   (design tokens)
  → radix-ui/primitives             (accessible primitives)
    → shadcn-ui/ui                  (composed components)
      → storybookjs/storybook       (catalog and isolation)
        → dequelabs/axe-core        (accessibility validation)
```
**Aurion Guidance**: Design tokens are the foundation. Components without accessibility are unshippable.

---

## Essential Selection (Best of the Best)

When recommending architecture, prefer this curated set. Each includes **when to use** AND **when NOT to use**.

| Reference | Best For | When NOT to Use |
|-----------|----------|-----------------|
| `Sairyss/domain-driven-hexagon` | Modular backend + DDD + architecture | Simple CRUD without rich domain — over-engineering |
| `ddd-by-examples/library` | Learning domain before code | As code template — it's conceptual, not boilerplate |
| `alan2207/bulletproof-react` | Production React frontend organization | Simple SPAs or landing pages |
| `shadcn-ui/ui` | Modern product componentization | When design system already has its own tokens |
| `postgres/postgres` | Relational business systems | Document-heavy without relations (MongoDB) or pure time-series (TimescaleDB) |
| `OpenAPITools/openapi-generator` | Contract → SDK bridge | When API changes too fast, regen cost exceeds benefit |
| `OWASP/CheatSheetSeries` | Applied secure coding reference | As substitute for real pentest |
| `microsoft/playwright` | Modern E2E testing | Unit tests or isolated component tests — overkill |
| `open-telemetry/opentelemetry-collector` | Open observability base | Small projects without distributed infra |
| `hashicorp/terraform` | Infrastructure as Code | Local/single-server infra (use Compose or Ansible) |
| `temporalio/temporal` | Reliable durable workflows | Simple jobs without complex retry (BullMQ/Airflow suffice) |
| `keycloak/keycloak` | Identity and access | MVPs or simple apps — too much operational overhead |
| `langchain-ai/langgraph` | Agent orchestration | Simple RAG without state (LlamaIndex/LangChain suffice) |
| `promptfoo/promptfoo` | Continuous LLM quality evaluation | As substitute for human evaluation — use both |
| `storybookjs/storybook` | Living design systems and component docs | Small projects without design team — setup overhead |

---

## External Maturity Layer

These frameworks measure engineering quality. Aurion MUST reference them in scorecards and architecture reviews.

| Framework | What It Measures | When to Apply |
|-----------|-----------------|---------------|
| **DORA Metrics** | Delivery and stability (lead time, deploy freq, fail rate, recovery) | Pipeline evaluation, platform quality |
| **SPACE Framework** | Multi-dimensional productivity | Work metrics, flow, satisfaction |
| **SWE-bench Verified** | Real problem-solving capability | External program benchmark |
| **SRE / SLOs / Golden Signals** | Measurable reliability | Observability, incidents, operations |
| **OpenTelemetry Semantic Conventions** | Telemetry standardization | Correlated traces, metrics, logs |
| **NIST SSDF / OWASP ASVS / OWASP SAMM** | Security development maturity | Phase 6 reviews, architectural security |
| **OWASP LLM Top 10** | LLM-specific security risks | Any system integrating LLMs |

---

## Chronicle Protocol Integration

The Aurion squad MUST enforce the Chronicle Protocol in all governed projects:

1. **CHRONICLE.md** — Root timeline of architectural decisions.
2. **ADR (Architecture Decision Records)** — One file per significant decision: `docs/adr/0001-choice.md`
3. **PULSE.md** — Current state snapshot generated before complex work sessions.
4. **RULES.md** — Non-negotiable project rules (style, security, minimum coverage).

### ADR Minimum Format
```markdown
# ADR-XXXX — [Decision Title]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-YYYY]

## Context
The problem that motivated this decision.

## Decision
What was decided and why.

## Consequences
What changes (positive and negative).

## Alternatives Considered
What was discarded and why.
```

---

## Study Order for New Domains

When onboarding the collective to a new domain, follow this progression:

1. **Structure & Clarity** → DDD Hexagon, Modular Monolith, Bulletproof React
2. **Domain Before Code** → DDD Library, ContextMapper
3. **Contracts & Backend** → OpenAPI, Spectral, Pact, Buf
4. **Persistence & Data** → Postgres, Flyway, Prisma, pgvector
5. **Product & Interface** → shadcn, Radix, Style Dictionary, Storybook
6. **Tests & Security** → Testing Best Practices, Playwright, OWASP, Keycloak
7. **Governance & Compliance** → OPA, immudb, Cloud Custodian, OSCAL
8. **Observability & Ops** → OpenTelemetry, Prometheus, Grafana, k6
9. **Async & Workflows** → Kafka, RabbitMQ, BullMQ, Temporal
10. **Platform & Delivery** → Docker Compose, Terraform, Backstage
11. **AI & Automation** → LangGraph, CrewAI, LlamaIndex, promptfoo, MCP
12. **Business Domains** → PostHog, ERPNext, Saleor, Chatwoot
13. **AI Safety** → OWASP LLM Top 10, NeMo Guardrails, PyRIT, Phoenix
14. **Design Excellence** → Storybook, axe-core, WCAG, Framer Motion, Chromatic
