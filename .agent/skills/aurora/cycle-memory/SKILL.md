# SKILL.md — Cycle Memory Recording

## Description
How to document decisions, deliveries, and incidents at the end of each Aurora execution cycle.

## When to use
- After every completed delivery cycle
- After every incident resolution
- After any significant technical decision

## Memory format
Always follow this structure:

```
## [Date] — [Cycle/Incident Title]

### Context
What was the objective? What was the Execution Contract about?

### Problem
What challenges or blockers were encountered?

### Solution
How were they resolved? What approach was taken?

### Prevention
What can be done to prevent this in the future?

### Impact
What was delivered? Test results? Deploy status?

### Agents involved
Which Aurora executives participated and what did each do?
```

## Memory types

### Permanent memory
Store when the learning applies across future cycles:
- Architectural decisions (e.g., "We chose RLS over middleware auth")
- MCP credential patterns (e.g., "Stitch needs bridge due to GCP permissions")
- Recurring failure patterns (e.g., "Vercel PAT expires every 90 days")

### Cycle log
Store for every cycle, even successful ones:
- What was done
- Who did it (which agent/executive)
- Outcome and test results
- Time to completion

## Where to store
- Permanent memory: `manage_memory` tool
- Cycle logs: `memory/` directory in the workspace

## Mandatory after incidents
After any production incident, the post-mortem is **not optional**:
1. Root cause identified
2. Resolution documented
3. Prevention measure defined
4. Impacted agents listed

## Owner
CLO (`knowledge_manager`)
