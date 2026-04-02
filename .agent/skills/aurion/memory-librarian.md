# Memory Librarian — AURION

## Description
This skill manages the project's long-term memory, ensuring continuity across sessions and preventing context amnesia.

## Purpose
Like `claude-mem`, this skill captures high-level observations and architectural pivots to keep the squads aligned with the product's evolution.

## The Librarian Protocol
After completing a significant task or milestone, Aurion triggers the **Librarian Protocol**:
1. **Distill**: Summarize what was achieved, what was changed, and why.
2. **Identify Lessons**: Note any specific technical challenges or unexpected findings.
3. **Record Decisions**: Document any ADRs (Architecture Decision Records) or tactical pivots.
4. **Update the Chronicle**: Append these insights to `/home/shoxsx/code/openclaw Aurion/CHRONICLE.md`.

## Memory Retrieval
At the start of a task, or when asked "/remember" or "/history":
1. **Analyze Timeline**: Read the Chronicle to understand the project's state.
2. **Inject Context**: Ensure the Aurora squad is aware of previous attempts or existing constraints.

## Quality Standards
- **Dense & Semantic**: Avoid long transcripts; use bullet points for high-density information.
- **Traceable**: Cite specific file paths or commit-like descriptions if available.
- **Actionable**: Focus on what *next* agents need to know.
