# SKILL.md — Infrastructure & Deploy Standards

## Description
Standards for managing deployments, CI/CD pipelines, and cloud infrastructure.

## When to use
Any task involving deploy, environment configuration, database migration, or cloud integration.

## Deployment rules

### Pre-deploy
- [ ] CQO has approved the code review
- [ ] QA Director has validated critical flows
- [ ] No unresolved blockers in the pipeline
- [ ] Environment variables are configured for the target environment

### Deploy process
1. Deploy to **staging** first — never skip
2. Validate on staging (smoke tests, basic flow check)
3. Deploy to **production** only after staging passes
4. Verify production health immediately after deploy

### Rollback
- Always have a rollback plan before deploying
- If production breaks within 15 minutes → rollback first, investigate later
- Document the rollback procedure for each deploy type

## Vercel specifics
- Use preview deployments for PR branches
- Configure environment variables per environment (dev/staging/production)
- Use Edge Functions for latency-sensitive endpoints

## Database migrations (Supabase)
- Every migration is versioned and reversible
- Apply migrations to staging before production
- Test data integrity after migration
- Never run `ALTER TABLE` directly — always through migration files

## Environment variable governance
- All env vars documented in project `.env.example`
- Secrets stored in `secrets/*.env` — never committed to git
- Rotate credentials on a regular schedule
- After any rotation → update `CREDENTIAL_MAP.md`

## Owner
CIO (`infrastructure_devops`)
