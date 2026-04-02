# 🛠️ Installation Guide: Aurion Nexus

This guide will walk you through setting up your own autonomous agentic collective.

## 📋 Prerequisites

- **Node.js**: v18.0.0 or higher.
- **Python**: v3.9 or higher.
- **Git**: For repository management.
- **MCP Servers**: Ensure you have `StitchMCP` and `GitHub MCP Server` configured.

## ⚙️ Step-by-Step Setup

### 1. Clone the Sovereign Core
```bash
git clone https://github.com/shoxsx/aurion-nexus.git
cd aurion-nexus
```

### 2. Configure Your Arsenal
Create a `secrets/` directory and add your environment-specific credentials:
- `supabase.env`: For your database.
- `stitch.env`: For your MCP access tokens.
- `vercel.env`: For automated deployments.

### 3. Initialize the Agents
```bash
npm run setup
# This will register the skills manifest and initialize the Aurora squad.
```

### 4. Smoke Test
Ask the system:
*"Aurion, quem é você e qual sua missão?"*
Verify that it references the `SOUL.md` and identifies your project context from the `Chronicle`.

---

## 💪 Why use Aurion Nexus?

### 1. Zero "Session Amnesia"
Unlike standard LLM chats, Aurion Nexus remembers your architectural decisions, bug history, and style preferences across weeks of work via the **Chronicle**.

### 2. Executive Quality Gates
Code isn't just written; it's audited. Every PR is checked by **Security**, **Performance**, and **QA** agents automatically.

### 3. Design Excellence
Integrated **Impeccable Design** standards ensure your project looks like a premium SaaS from Day 1, avoiding generic "AI-look" components.

### 4. True Autonomy
With the **Ralph Loop**, the agent can get stuck, try a different approach, fix its own errors, and verify the solution without you having to guide it step-by-step.

---

## 🛡️ Security Note
The `secrets/` and `projects/` directories are automatically ignored by Git. Never commit your `.env` files or project-specific data to the public repository.
