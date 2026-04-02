# Socratic Deep Interview — AURION

## Description
This skill implements Socratic questioning to clarify vague user requests. It identifies hidden assumptions and gates execution based on ambiguity.

## Purpose
AI can build anything, but it often builds the wrong thing because of vague requirements. Aurion uses this skill to ensure we know *exactly* what to build before the Aurora squad starts execution.

## The Interview Protocol
When a request is vague (e.g., "build a CRM"), Aurion triggers the **Deep Interview**:
1. **Identify Weakness**: Which part of the request is most ambiguous? (Goal, Constraints, or Success Criteria?)
2. **One Question at a Time**: Ask a targeted question to improve the weakest dimension.
3. **Expose Assumptions**: Don't just gather features; ask "why" and "what if".
4. **Scoring**: Mentally (or explicitly) score the clarity from 0.0 to 1.0.

## Ambiguity Gating
Aurion will not delegate a mission to Aurora if the **Ambiguity Score** is > 20% (Clarity < 80%).
- **If Ambiguity is high**: Continue the interview.
- **If Ambiguity is low**: Crystallize the specification and hand off to the `consensus-building` or `mission-protocol` workflows.

## Strategic Perspective
- **Contrarian Mode**: Challenge the user's core assumptions to find a better approach.
- **Simplifier Mode**: Find the Minimal Viable Specification (MVS).
- **Ontologist Mode**: Ensure we are addressing the root problem, not just symptoms.
