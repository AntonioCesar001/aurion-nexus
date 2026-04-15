# SKILL.md — SEIP v2 Execution Reference (Aurora Squad)

## Description
Operational reference that maps each execution phase to the correct SEIP repositories, tools, and patterns. Aurora agents MUST consult this guide when choosing implementation approaches.

## When to use
- Before starting any new module, feature, or service implementation.
- When choosing tools, libraries, or patterns for a specific technical domain.
- During code reviews to verify alignment with SEIP reference patterns.
- When the Architect, Security Reviewer, or QA agents need authoritative references.

---

## Phase 1 — Structure & Foundations

**Goal**: Stop mixing everything. Learn modularization, separation of concerns, boundaries.

### Backend Architecture
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `Sairyss/domain-driven-hexagon` | DDD + Hexagonal + Clean/Onion with ports/adapters | avançado |
| `kgrzybek/modular-monolith-with-ddd` | Modular monolith without premature microservices | avançado |

### Frontend Architecture
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `alan2207/bulletproof-react` | Scalable React by features, layers, and conventions | intermediário |

### Aurora Enforcement
- **Architect Agent**: Verify hexagonal boundaries before approving any PR.
- **Code Reviewer**: Reject code that violates separation of concerns.
- File size limit: 200-400 lines (800 hard max per RULES.md).

---

## Phase 2 — Domain & Business Rules

**Goal**: Software starts from entities, states, events, and invariants — not from CRUD.

### Core Domain
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `ddd-by-examples/library` | Strategic analysis, ubiquitous language, event storming, tactical DDD | avançado |
| `ContextMapper/context-mapper-dsl` | Bounded contexts, context mapping, service decomposition | avançado |
| `ContextMapper/context-mapper-examples` | Concrete examples of strategic modeling | intermediário |

### Product & Analytics
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `PostHog/posthog` | Product analytics, feature flags, experimentation | intermediário |
| `metabase/metabase` | Accessible BI and business data exploration | intermediário |

### Business Domains
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `twentyhq/twenty` | Modern CRM, sales pipeline | intermediário |
| `frappe/erpnext` | Full enterprise domain (sales, inventory, finance) | avançado |
| `saleor/saleor` | API-first commerce (catalog, orders, payments) | avançado |
| `mastodon/mastodon` | Social domain, timelines, federation | avançado |
| `chatwoot/chatwoot` | Omnichannel support, customer success | intermediário |

### Aurora Enforcement
- **TDD Guide**: Entity invariants MUST have tests before any logic implementation.
- **Database Reviewer**: Tables reflect domain entities, not UI forms.

---

## Phase 3 — Product & Interface

**Goal**: Scalable frontend, design systems, componentization, documentation.

### Frontend & Components
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `shadcn-ui/ui` | Modern componentization with accessibility and customization | intermediário |
| `radix-ui/primitives` | Accessible low-level primitives for design systems | avançado |
| `style-dictionary/style-dictionary` | Cross-platform design tokens | avançado |
| `primer/react` | Mature enterprise design system in React | avançado |

### Aurora Enforcement
- **Design Standards**: All components must pass the "AI Slop" test.
- **Code Reviewer**: Components without accessibility = not shippable.
- Integrate with existing [design-standards](../design-standards/SKILL.md) references.

---

## Phase 4 — Backend Contracts & Consistency

**Goal**: Contract before improvisation. Consistency before convenience. Idempotency before blind retry.

### API & Contracts
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `OAI/OpenAPI-Specification` | API as formal contract | intermediário |
| `OpenAPITools/openapi-generator` | SDK/stub generation from contract | intermediário |
| `stoplightio/spectral` | OpenAPI/AsyncAPI lint and governance | intermediário |
| `bufbuild/buf` | Professional Protobuf/gRPC work | avançado |
| `asyncapi/spec` | Async API and event contracts | avançado |
| `pact-foundation/pact-js` | Consumer-driven contract testing | avançado |

### Integrations
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `n8n-io/n8n` | Practical automation between systems | intermediário |

### Aurora Enforcement
- **Backend Standards**: All new APIs start with OpenAPI spec, THEN implementation.
- **Execution Contract**: Validate contracts with Spectral before code review.
- **QA Tester**: Contract tests (Pact) required for multi-service boundaries.

---

## Phase 5 — Persistence & Data Modeling

**Goal**: Not "pick an ORM" — learn modeling, integrity, migration, query cost.

### Databases
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `postgres/postgres` | Mature relational DB for real systems | avançado |
| `flyway/flyway` | Schema versioning and reliable migrations | intermediário |
| `prisma/prisma` | Typed data access with modern DX | intermediário |

### Vector Databases (RAG/Semantic Search)
| Reference | What It Teaches | When NOT to Use | Level |
|-----------|----------------|-----------------|-------|
| `pgvector/pgvector` | Native PostgreSQL vector search | > 10M vectors or ms-latency critical → use Qdrant/Weaviate | intermediário |
| `chroma-core/chroma` | Simple vector DB for RAG prototypes | Production at scale → use pgvector or Qdrant | iniciante |

### Aurora Enforcement
- **Database Reviewer**: Every schema change has a versioned migration (up + down).
- **Backend Standards**: Normalize to 3NF minimum. UUIDs for PKs. Always `created_at`/`updated_at`.
- **Security Reviewer**: RLS enabled on all Supabase tables. No temporary disabling.

---

## Phase 6 — Security, Tests & Governance

**Goal**: Prevent the AI from testing only happy paths, treating security as post-processing, trusting clients, or leaking sensitive data.

### Security
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `OWASP/CheatSheetSeries` | Concrete secure coding practices | intermediário |
| `owasp/www-project-code-review-guide` | Code review with vulnerability focus | avançado |

### Identity & Authorization
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `keycloak/keycloak` | Complete IAM, SSO/OIDC | avançado |
| `ory/kratos` | Headless cloud-native identity | avançado |
| `cerbos/cerbos` | Decoupled contextual authorization policies | avançado |
| `openfga/openfga` | Fine-grained Zanzibar-style permissions | avançado |

### Governance & Compliance
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `open-policy-agent/opa` | Policy as code | avançado |
| `codenotary/immudb` | Immutable tamper-proof audit trails | avançado |
| `cloud-custodian/cloud-custodian` | Cloud governance via YAML policies | avançado |
| `usnistgov/oscal` | Structured compliance controls | avançado |

### Aurora Enforcement
- **Security Reviewer**: OWASP CheatSheet is the baseline for every PR touching auth, sessions, or inputs.
- **Code Reviewer**: Permissions logic must be decoupled (Cerbos/OPA pattern), not embedded in routes.
- **QA Tester**: Security edge cases are mandatory test scenarios, not optional.

---

## Phase 7 — Quality, Delivery & Operations

### Testing
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `goldbergyoni/javascript-testing-best-practices` | Testing strategy and real-world practices | intermediário |
| `microsoft/playwright` | Cross-browser E2E testing | intermediário |
| `testcontainers/testcontainers-node` | Integration tests with real dependencies in containers | avançado |

### Performance
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `GoogleChrome/lighthouse` | Automated web performance audit | intermediário |
| `grafana/k6` | Modern load testing | intermediário |
| `mcollina/autocannon` | Fast HTTP API benchmarking | intermediário |

### Observability
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `open-telemetry/opentelemetry-collector` | Telemetry pipeline (metrics, logs, traces) | avançado |
| `prometheus/prometheus` | Metrics monitoring and alerting | avançado |
| `grafana/grafana` | Operational visualization and correlation | intermediário |

### Messaging & Events
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `apache/kafka` | Distributed event streaming | avançado |
| `rabbitmq/rabbitmq-server` | Traditional message broker | intermediário |
| `taskforcesh/bullmq` | Node/Redis queues and background jobs | intermediário |

### Workflows
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `temporalio/temporal` | Durable execution and resilient processes | avançado |
| `camunda/camunda` | BPMN/DMN business process orchestration | avançado |
| `apache/airflow` | Programmatic workflow scheduling | intermediário |

### Deploy & Infrastructure
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `docker/awesome-compose` | Realistic Docker Compose service composition | iniciante |
| `hashicorp/terraform` | Declarative infrastructure as code | avançado |
| `coollabsio/coolify` | Self-hosted PaaS and simplified deploy | intermediário |
| `ansible/ansible` | Server automation and configuration | avançado |

### Aurora Enforcement
- **Testing Standards**: 80%+ coverage. Unit + Integration + E2E layers. No happy-path-only tests.
- **Performance Optimizer**: Lighthouse + k6 before any launch.
- **Infra Deploy**: Docker Compose for dev, Terraform for staging/prod.
- **Mission Protocol**: The Ralph Loop (Plan → Exec → Verify → Fix) applies to all delivery phases.

---

## Phase 8 — AI Intelligence & Automation

### Agent Orchestration
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `langchain-ai/langgraph` | Stateful agent orchestration with resilient flows | avançado |
| `crewAIInc/crewai` | Multi-agent collaboration with defined roles | intermediário |
| `microsoft/semantic-kernel` | Enterprise LLM integration | avançado |

### RAG & Semantic Retrieval
| Reference | What It Teaches | When NOT to Use | Level |
|-----------|----------------|-----------------|-------|
| `run-llama/llama_index` | Production RAG pipelines, indexing, chunking | Complex stateful agentic workflows → use LangGraph | avançado |
| `langchain-ai/langchain` | LLM chain composition, RAG, tools, memory | High-performance custom pipelines → overhead not worth it | intermediário |

### AI Evaluation
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `promptfoo/promptfoo` | Systematic prompt/LLM/RAG evaluation (CI/CD for AI) | intermediário |
| `BerriAI/litellm` | Unified multi-provider LLM abstraction | intermediário |

### MCP (Model Context Protocol)
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `modelcontextprotocol/servers` | MCP server implementation (tools, resources, prompts) | avançado |
| `modelcontextprotocol/typescript-sdk` | Official TypeScript SDK for MCP | avançado |

### Aurora Enforcement
- **MCP Health**: All MCP integrations must be monitored and auto-recoverable.
- **Security Reviewer**: LLM pipelines without guardrails are a hard block.
- **QA Tester**: promptfoo evaluations required before deploying any prompt change.

---

## Phase 9 — AI Safety, Guardrails & Red Teaming

**Goal**: Building with AI without guardrails = deploying without security tests.

### Guardrails & LLM Protection
| Reference | What It Teaches | When NOT to Use | Level |
|-----------|----------------|-----------------|-------|
| `NVIDIA/NeMo-Guardrails` | Programmable safety rails for LLMs | Infra/data protection → use OWASP + Keycloak | avançado |
| `guardrails-ai/guardrails` | Structured LLM output validation with schemas | Not a substitute for input sanitization | intermediário |

### Red Teaming & AI Security Evaluation
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `Azure/PyRIT` | Automated AI red teaming (attacks, evaluation, scoring) | avançado |
| `OWASP LLM Top 10` | 10 most critical LLM security risks | avançado |

### AI Observability
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `arize-ai/phoenix` | LLM/RAG pipeline tracing, evaluation, debugging | avançado |

### Aurora Enforcement
- **Security Reviewer**: OWASP LLM Top 10 review mandatory for any system integrating LLMs.
- **Architect Agent**: NeMo Guardrails or equivalent required in production AI pipelines.
- **QA Tester**: Red teaming (PyRIT) required before deploying user-facing AI features.

---

## Phase 10 — Design Excellence (Anti-AI Slop)

**Goal**: Interfaces that look like they were built by senior product designers, not generated by default AI.

### Component Catalog & Documentation
| Reference | What It Teaches | When NOT to Use | Level |
|-----------|----------------|-----------------|-------|
| `storybookjs/storybook` | Component development, documentation, testing in isolation | Small projects — setup overhead | intermediário |

### Accessibility
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `dequelabs/axe-core` | Automated WCAG accessibility auditing | intermediário |
| `w3c/wcag` | Official web accessibility guidelines | avançado |

### Motion & Animation
| Reference | What It Teaches | When NOT to Use | Level |
|-----------|----------------|-----------------|-------|
| `framer/motion` | Declarative physics animation in React | Pure CSS animations without interactivity | intermediário |

### Visual Testing
| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `applitools/eyes-storybook` | Visual regression testing with Storybook | avançado |
| `chromaui/chromatic` | Visual CI with automatic component diff | intermediário |

### Aurora Enforcement
- **Design Standards**: Every UI component must pass Impeccable Design Standards + axe-core.
- **Code Reviewer**: No generic colors (pure red/blue), no default spacing, no typography without hierarchy.
- **QA Tester**: Visual regression tests required for all design system changes.
- Integrate with existing [design-standards](../design-standards/SKILL.md) and [reference guides](../design-standards/reference/).

---

## Platform & Documentation (Transversal)

| Reference | What It Teaches | Level |
|-----------|----------------|-------|
| `backstage/backstage` | Software catalog and engineering portal | avançado |
| `facebook/docusaurus` | Modern versioned technical documentation | intermediário |
| `mkdocs/mkdocs` | Simple clear Markdown documentation | iniciante |
| `npryce/adr-tools` | ADR generation and management in CLI | intermediário |

---

## Quick Decision Matrix

When an Aurora agent needs to choose a tool, use this matrix:

| I Need To... | Use This | NOT This |
|--------------|----------|----------|
| Define an API contract | OpenAPI Specification | Code-first endpoints |
| Test between services | Pact.js (contract) | Only E2E tests |
| Test user flows | Playwright (E2E) | Manual testing |
| Test with real deps | Testcontainers | Mocked dependencies |
| Store relational data | PostgreSQL | SQLite in prod |
| Add semantic search | pgvector (moderate scale) | Full vector DB for small data |
| Prototype RAG | Chroma | pgvector for quick prototype |
| Build agent workflows | LangGraph (stateful) | Raw LLM calls |
| Validate LLM output | Guardrails-AI | Trust raw output |
| Evaluate prompt quality | promptfoo | Manual spot-checking |
| Protect LLM pipeline | NeMo Guardrails | No protection |
| Monitor AI pipeline | Phoenix (Arize) | printf debugging |
| Deploy locally | Docker Compose | Manual setup |
| Deploy to cloud | Terraform | ClickOps |
| Manage permissions | Cerbos/OpenFGA | Hardcoded if-else in routes |
| Audit trail | immudb | Regular database logs |
