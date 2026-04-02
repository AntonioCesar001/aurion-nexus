# Development Manual — AURION NEXUS

## 🏛️ Strategic Engineering Principles
This manual defines the technical excellence required for the sovereign core. It supplements `SOUL.md` and `RULES.md`.

### 1. Hexagonal & Sovereign Architecture
- **Isolation**: Business logic must be decoupled from external tools (MCP, APIs, Databases).
- **Core First**: Implement the domain model before integrating with the "real world".
- **Interchangeability**: Assume every MCP tool or database could be replaced.

### 2. The Intention-Based Loop
- Always prioritize the **Deep Interview** for high-ambiguity tasks.
- Every major technical shift must have an **ADR** (Architecture Decision Record).

### 3. Quality Control (The Gated Flow)
- **TDD (Mandatory)**: No logic code without tests.
- **Security Audit**: Required for any code touching `secrets/`, network, or file system writes.
- **Performance Threshold**: Latency and resource budget must be considered in the design phase.

### 4. Continuous Harmonization
- The system should maintain its own health.
- If a skill becomes redundant, it must be deprecated or merged immediately.
- The `CHRONICLE.md` should be a living narrative, not just a log.

## 👥 Squad Coordination (Paperclip Cycle)
- Aurion manages the **Blueprints** and **Consensus**.
- Aurora manages the **Contract Execution** and **Reliability**.
- Verification is the final barrier: No mission is complete until the **QA** and **Security** agents sign off.
