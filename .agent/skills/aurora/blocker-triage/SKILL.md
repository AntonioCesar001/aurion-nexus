# SKILL.md — Blocker Triage & Escalation

## Description
How to classify, triage, and escalate blockers during an Aurora execution cycle.

## When to use
When any agent encounters something that prevents forward progress.

## Blocker types

### Technical blocker
- **Definition**: A coding, integration, or tooling issue that a specialist can solve.
- **Owner**: Aurora (COO assigns the right specialist)
- **SLA**: Resolve within current cycle
- **Examples**: API returning unexpected format, dependency version conflict, test failing due to environment issue

### Strategic blocker
- **Definition**: An issue requiring business or product decision beyond Aurora's domain.
- **Owner**: Aurion (CEO)
- **SLA**: Escalate within 30 minutes of detection
- **Examples**: Ambiguous requirements, scope change request, conflicting priorities, feature direction unclear
- **Action**: Pause affected tasks. Continue unaffected work.

### Platform blocker
- **Definition**: MCP, credential, or infrastructure failure preventing tool usage.
- **Owner**: CPTO (`platform_engineer`)
- **SLA**: Begin repair immediately
- **Examples**: Stitch bridge down, Vercel PAT expired, Supabase connection timeout
- **Action**: COO reassigns unblocked work while CPTO repairs.

## Triage flow
1. Agent detects a blocker
2. **CXO classifies** the blocker type (technical / strategic / platform)
3. CXO routes to the correct owner
4. Owner resolves or escalates further
5. CXO confirms resolution and unblocks the pipeline

## Never do
- Never let a blocker sit unclassified
- Never escalate a technical blocker to Aurion (solve internally)
- Never ignore a strategic blocker hoping it resolves itself

## Owner
CXO (`operator`) — classification  
COO (`coordinator`) — resolution routing
