# TDD Workflow — AURORA

## Description
This skill enforces Test-Driven Development (TDD) as the mandatory standard for all software changes.

## Purpose
To ensure code reliability, prevent regressions, and maintain at least 80% test coverage.

## The TDD Cycle
Every task must follow the **Red → Green → Improve** cycle:
1. **Red**: Write a failing unit or integration test that defines the expected behavior.
2. **Green**: Write the minimal code necessary to make the test pass.
3. **Improve**: Refactor the code for quality, performance, and readability while ensuring tests still pass.

## Success Criteria
- **Coverage**: Minimum 80% coverage for the affected module.
- **Verification**: All tests must pass before the `mission-protocol` is considered complete.
- **Consistency**: Use existing testing frameworks (Jest, Vitest, PyTest, etc.) and mock external dependencies.

## Specialized Support
- **tdd-guide**: Invoke this agent to help design the test plan.
- **performance-optimizer**: Use after the GREEN phase to ensure refactoring remains efficient.
