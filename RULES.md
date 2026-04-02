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

### 🎨 Visual Excellence
- Follow the **Impeccable Design Standards**.
- No generic colors (pure red/blue).
- Modular typography with fluid sizing.
- Subtle motion and glassmorphism.
