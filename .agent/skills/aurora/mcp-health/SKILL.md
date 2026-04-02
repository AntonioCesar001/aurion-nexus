# SKILL.md — MCP Health Monitoring

## Description
How to validate, monitor, and repair MCP integrations that the Aurora squad depends on.

## When to use
- Before every execution cycle (preflight)
- When any MCP returns errors, timeouts, or auth failures
- After credential rotation

## Required MCPs

### Stitch (UI Design)
- **Transport**: Bridge local (`stitch-bridge-final.mjs`)
- **Health check**: Call `list_projects` — must return real project data
- **Common failure**: GCP permission error → restart bridge
- **Repair**: `node stitch-bridge-final.mjs` and verify output

### Vercel (Deploy)
- **Transport**: Remote MCP via `https://mcp.vercel.com`
- **Auth**: `Authorization: Bearer <Vercel PAT>`
- **Health check**: Call `list_projects` — must return deployments
- **Common failure**: 401 Unauthorized → PAT expired
- **Repair**: Generate new PAT at vercel.com/account/tokens, update `mcporter.json`

### Supabase (Backend)
- **Transport**: Remote SSE via `mcp.supabase.com`
- **Auth**: `Authorization: Bearer <Supabase PAT>`
- **Health check**: Call `list_tables` — must return schema
- **Common failure**: 401 → PAT expired or wrong project_ref
- **Repair**: Generate new PAT at supabase.com/dashboard/account/tokens

### TestSprite (QA)
- **Transport**: stdio via npx
- **Auth**: `API_KEY` env var (`TESTSPRITE_API_KEY` pode ser mantida por compatibilidade)
- **Health check**: Call any test listing endpoint
- **Common failure**: Invalid API key
- **Repair**: Regenerate at testsprite.com, update `mcporter.json`

## Operational rule
> A MCP is only **operational** when a **real tool returns real data** — not just when the schema loads.

## After repair
1. Update `docs/aurora/CREDENTIAL_MAP.md` with new credentials
2. Update `mcporter.json` as source of truth
3. Notify COO that preflight can proceed

## Owner
CPTO (`platform_engineer`)
