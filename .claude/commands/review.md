# /review — Code Review

Perform a thorough code review of the specified file or recent changes.

## Usage
```
/review [file or directory]
/review src/components/UserProfile.tsx
/review (reviews staged git changes)
```

## What this does
1. Reads the target file(s) or `git diff --staged` output
2. Checks against project conventions in CLAUDE.md
3. Reports issues in these categories:
   - Security vulnerabilities (OWASP top 10)
   - Type safety and TypeScript strict mode compliance
   - Test coverage gaps
   - Performance concerns
   - Accessibility issues
   - Code style and naming conventions

## Checklist Applied
- [ ] No hardcoded secrets or credentials
- [ ] All inputs validated and sanitized
- [ ] Proper error handling in place
- [ ] Tests written for new logic
- [ ] No console.log in production paths
- [ ] Conventional commit message used
- [ ] Lint and typecheck would pass

## Output Format
Produces a structured report with **Critical**, **Warning**, and **Suggestion** items.
