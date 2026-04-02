# SKILL.md — Testing & QA Standards

## Description
Standards for testing, quality assurance, and validation of deliverables.

## When to use
After any feature is complete, after significant refactoring, or before production deploy.

## Test types

### End-to-end (E2E)
- Test complete user flows from start to finish
- Use TestSprite for automated E2E testing
- Cover the critical path: signup → login → main action → result
- Run against staging before production deploy

### API contract testing
- Validate request/response schemas for all endpoints
- Test error cases (400, 401, 403, 404, 500)
- Verify pagination works correctly
- Test with edge cases (empty strings, very long inputs, special characters)

### Regression testing
- After any fix, verify the original bug is resolved
- Verify nearby functionality hasn't broken
- Document regression patterns for future cycles

## Test report format
```
## Test Report — [Feature/Fix Name]

**Date**: YYYY-MM-DD
**Environment**: staging / production
**Runner**: QA Director

### Results
- Total: X tests
- ✅ Passed: X
- ❌ Failed: X
- ⏭️ Skipped: X

### Critical flows
- [ ] Flow 1 — description — PASS/FAIL
- [ ] Flow 2 — description — PASS/FAIL

### Notes
Any observations, flaky tests, or edge cases discovered.
```

## When to block a release
- Any critical flow fails
- Security test fails
- Data integrity test fails
- Performance regression detected (>30% slower)

## When NOT to block
- Non-critical UI pixel differences
- Tests for features not part of current scope
- Known flaky tests (document and fix separately)

## Owner
QA Director (`api_tester`)
