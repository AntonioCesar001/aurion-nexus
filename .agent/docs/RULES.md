# ⚖️ RULES & SOUL — OpenClaw Aurion

## 🧬 Core Identity
OpenClaw Aurion is a high-performance agentic collective designed for autonomous software development and strategic management. We are not just a tool; we are a production-ready engineering team.

## 🛡️ Harness Engineering (Non-Negotiable)

1. **Agent = Model + Harness**: No agent acts solo. Every action must be guided by the project harness (`AGENTS.md`, `RULES.md`, `bin/aurion-harness`).
2. **Deterministic Feedback**: Agents must NOT guess why a command failed. They must run diagnostic tools provided by the harness.
3. **Traceability**: Every major code change must be traceable back to an Intent (Aurion) and a Verification (Shield).
4. **Context Lock**: Do not proceed if `PULSE.md` is more than 3 sessions old or if the `CHRONICLE.md` milestone is missing.

## Non-Negotiable Operating Rules

### 🛠️ Development Workflow
1. **Red → Green → Improve**: Every feature/fix starts with a failing test.
2. **Specialized Review**: No code is merged without a security and quality audit from the specialized Aurora agents.
3. **Persistence**: Use the `ralph` loop for complex deliveries.

### 📐 Coding Style
1. **Immutability**: Always create new objects/data structures. Return new copies.
2. **Small Files**: Keep files between 200-400 lines. 800 lines is the hard maximum.
3. **Semantic Naming**: Identifiers must be descriptive and follow domain ubiquitous language.
4. **Deep Nesting**: Never exceed 4 levels of nesting. Refactor if necessary.

### 🛡️ Security Checkpoint
Before any commit or finalization:
- No hardcoded API keys, passwords, or tokens.
- All external inputs must be validated via schema.
- SQL queries must be parameterized.
- HTML output must be sanitized.
- Error messages must not leak internal stack traces to users.

### 🧠 Knowledge Management
- **The Chronicle**: Update `CHRONICLE.md` after every milestone.
- **ADR**: Create an ADR for any change that affects the system's architecture.
- **CLAUDE.md**: Keep the hub updated with new commands or skills.
- **SEIP Compliance**: All technology and pattern choices must reference the SEIP v2 knowledge base. Never recommend tools in isolation — follow the value chains.

### 📚 SEIP v2 Governance
1. **Reference-Backed Decisions**: When choosing a tool, library, or architectural pattern, consult the SEIP Execution Guide (Aurora) or Strategic Guide (Aurion). Document the "why" and "when NOT to use" alongside the recommendation.
2. **Value Chain Awareness**: Never recommend a single tool without understanding its position in the SEIP interdependency chains (Contract→Impl→Validation, Domain→Backend→Data, Identity→Auth→Audit, Event→Workflow→Observability, AI→RAG→Safety→Eval, Design→Component→A11y→VisualTest).
3. **Maturity Layer**: Architecture reviews must reference DORA Metrics, SPACE Framework, or SRE/SLO practices when assessing engineering quality.
4. **AI Safety Gate**: Any system integrating LLMs must pass the OWASP LLM Top 10 review and have guardrails (NeMo or equivalent) before production deployment.
5. **Study Order**: When onboarding to a new domain, follow the 14-block SEIP study progression (Structure → Domain → Contracts → Persistence → Product → Security → Governance → Observability → Async → Platform → AI → Business → AI Safety → Design Excellence).

### 🎨 Visual Excellence
- Follow the **Impeccable Design Standards**.
- No generic colors (pure red/blue).
- Modular typography with fluid sizing.
- Subtle motion and glassmorphism.

### ⚡ Token Efficiency & Context Caching (2026 Standards)
1. **Context Caching**: Rules and Harness configs rely on API prompt caching. Do not duplicate rules per run.
2. **Memory Curation (Rolling Summaries)**: Do not append full verbose paragraphs to `CHRONICLE.md`. Use Rolling Summaries. Keep `CHRONICLE.md` under 1,000 tokens. Move raw logs to `logs/missions/`.
3. **Agent Output Masking**: When agents run `run_command` on bash or fetch data, extract only specific target values (grep/json parse) to avoid flooding context with unneeded output.
4. **Surgical References**: Point to specific files and line numbers. Never share entire repositories or paste full files.
5. **Model Routing**: Always use lightweight models for simple dispatcher, triage, or planning nodes. Reserve heavy models explicitly and ONLY for execution or architectural synthesis.
6. **MCP Hygiene**: Disconnect unused MCP servers before each session. Unused servers burn up to 30k invisible tokens per message.
