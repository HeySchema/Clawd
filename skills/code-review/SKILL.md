# Skill: Code Review

## Purpose
Perform a thorough, structured code review against project conventions, security rules, and quality standards.

## Trigger
Use this skill when asked to review code, audit a PR, or check a file for issues.

## Steps

1. **Read the target** — load the file(s) or diff being reviewed
2. **Security scan** — check for OWASP top 10 issues, hardcoded secrets, unvalidated inputs
3. **Type safety** — verify TypeScript strict mode compliance, no `any` escape hatches
4. **Conventions** — validate naming (PascalCase components, camelCase utils), file structure, named exports
5. **Test coverage** — confirm tests exist for all new logic; flag untested branches
6. **Performance** — identify unnecessary re-renders, N+1 queries, missing memoization
7. **Accessibility** — check ARIA labels, keyboard navigation, color contrast where applicable
8. **Report** — output findings grouped by severity: Critical / Warning / Suggestion

## Output Format
```
## Code Review Report

### Critical
- [file:line] description

### Warning
- [file:line] description

### Suggestions
- [file:line] description
```

## References
- See `references/` for checklists and style guides
- See `assets/` for example reports
