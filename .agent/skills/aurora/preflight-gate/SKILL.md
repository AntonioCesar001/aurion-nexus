# SKILL.md — Aurora Preflight Gate

## Description
Validates that all required MCPs, credentials, workspace paths, and acceptance criteria are confirmed before any Aurora execution cycle starts.

## When to use
Before every execution cycle, the COO and CPTO must run this preflight checklist.

## Checklist
1. **MCPs operational** — Call a real tool on each required MCP (Stitch, Vercel, Supabase, TestSprite). Schema loading alone is NOT sufficient.
2. **Credentials valid** — Verify each credential in `docs/aurora/CREDENTIAL_MAP.md` is current and not expired.
3. **Acceptance criteria** — Confirm the Execution Contract has an explicit, testable acceptance criterion.
4. **Workspace paths** — Verify all referenced file paths and agent dirs exist and are accessible.
5. **No strategic ambiguity** — If the contract has unclear requirements or multiple interpretations, STOP and escalate to Aurion.

## Failure actions
- If any MCP fails → escalate to CPTO for repair.
- If credentials are expired → escalate to CPTO for rotation.
- If contract is ambiguous → escalate to Aurion (CEO).
- **Never start execution with a failed preflight.**

## Owners
- Primary: COO (`coordinator`)
- Support: CPTO (`platform_engineer`)
