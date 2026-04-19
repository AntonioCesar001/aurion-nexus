# Mission Protocol — AURORA Squad

## Description
This protocol defines the standard operating procedure for any mission assigned to the Aurora squad. It ensures high quality, security, and performance.

## Autonomic Mission Standard
This protocol is the **standard operating procedure** for all Aurora tasks. Do not wait for a "mission" command; any complex delivery must follow this loop:

1. **Plan**: Assembly of specialists (Architect, Reviewer, etc.).
2. **Exec**: High-precision code generation following `RULES.md`.
3. **Verify**: Mandatory run of QA and Security reviewers.
4. **Fix**: Automatic iterative resolution of any found issues.
Aurora does not consider a mission complete until it is verified.
`Plan → Execute → Verify → Fix (Loop if verification fails)`

### Phase 1: Planning
1. **Context Refresh**: Read [[.agent/docs/CHRONICLE.md|CHRONICLE.md]] and [[CLAUDE.md]] to align with the project's history.
2. **Knowledge Anchor**: Consult the relevant [[.agent/knowledge/|Knowledge Catalogs]] to justify structural decisions. **Prohibited**: Implementing architectural patterns not supported by a Gold Standard reference without justification.
3. **Architect Review**: Spawn an `architect` agent to analyze the current codebase.
4. **Implementation Strategy**: Create a step-by-step TODO list with clear acceptance criteria.


### Phase 2: Execution
1. **Specialized Implementation**: Use the appropriate expertise for the task (Frontend, Backend, etc.).
2. **Incremental Changes**: Make atomic, testable commits.

### Phase 3: Verification
1. **QA Protocol**: Spawn a `qa-tester` to run automated tests or E2E scripts.
2. **Review**: Spawn a `code-reviewer` to check for security vulnerabilities (Security Reviewer) or architectural alignment (Architect).

### Phase 4: Fix / Polish
1. If any test fails or reviewer requests changes, return to Phase 1/2.
2. If all checks pass, proceed to Final Validation.

## Specialized Agents
Aurora can delegate specific sub-tasks to specialized agents:
- `architect`: For root cause analysis and complex design decisions.
- `code-reviewer`: For security and excellence audits.
- `qa-tester`: For creating and running verification scripts.
- `debugger`: When 3+ fix attempts have failed.

## Quality Gates
- **Zero AI Slop**: Use the Impeccable Design Standards.
- **Evidence Based**: Every architectural claim must cite a file and line number.
- **Traceability**: Every bug fix must have a corresponding test case.
