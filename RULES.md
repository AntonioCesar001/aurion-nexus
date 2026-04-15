# ⚖️ RULES — OpenClaw Aurion

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

### ⚡ Token Efficiency (apply always)
1. **CLAUDE.md stays lean**: Hard limit 60 lines. Detail lives in skills (on-demand), not CLAUDE.md (every message).
2. **Model matching**: Opus only for critical architecture decisions (<20% of tasks). Sonnet for implementation. Haiku for sub-agents doing search/classification.
3. **Surgical references**: Point to specific files and line numbers. Never share entire repositories or paste full files.
4. **Group prompts**: Combine related asks into a single message. Avoid follow-up chains — they compound context cost.
5. **/compact at 60%**: Do not wait for autocompact at 95%. Run `/compact` with explicit keep/discard instructions at ~60% context.
6. **One conversation per domain**: Use `/clear` when switching unrelated tasks. Carrying foreign context costs tokens and degrades focus.
7. **MCP hygiene**: Disconnect unused MCP servers before each session. Each connected server adds 10k–30k invisible tokens per message.
8. **Plan before execute**: Use Plan Mode (Shift+Tab) on complex tasks to avoid wrong-direction rework, which wastes 2–5× tokens.
9. **Monitor execution**: Do not send and switch tabs. Stop loops immediately — they produce zero value and burn context.
