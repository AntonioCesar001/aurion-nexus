# SKILL.md — Code Review Standards

## Description
Standards and criteria for reviewing code before merge, deploy, or delivery to production.

## When to use
- Before any merge to main/production branch
- Before any deploy to production environment
- Before delivering artifacts back to Aurion

## Review checklist

### Security
- [ ] No hardcoded secrets or API keys
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention (parameterized queries)
- [ ] XSS prevention (output encoding)
- [ ] OWASP Top 10 compliance check

### Performance
- [ ] No N+1 query patterns
- [ ] No unnecessary loops or redundant operations
- [ ] Proper indexing on frequently queried columns
- [ ] Lazy loading where appropriate

### Code quality
- [ ] Consistent naming conventions
- [ ] Functions are small and single-purpose
- [ ] Error handling is explicit and informative
- [ ] No dead code or unused imports
- [ ] Comments explain *why*, not *what*

### Architecture
- [ ] Follows established patterns in the codebase
- [ ] Separates concerns properly (logic/data/presentation)
- [ ] New dependencies are justified
- [ ] Breaking changes are documented

## Approval gates
1. All checklist items pass → **APPROVE**
2. Security issue found → **BLOCK** (mandatory fix before merge)
3. Performance concern → **REQUEST CHANGES** (fix recommended)
4. Style-only issues → **APPROVE WITH COMMENTS** (non-blocking)

## Owner
CQO (`reviewer`)
