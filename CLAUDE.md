# Project: My App

## Tech Stack
- Next.js 14, TypeScript, Tailwind
- Supabase for auth & database
- Prisma ORM, TRPC API layer

## Conventions
- Always write tests before code
- Use conventional commits
- Never commit directly to main
- Run lint + typecheck before PR

## Architecture
- src/components — React components
- src/services   — Business logic
- src/utils      — Shared helpers

## Security
- No secrets in code or logs
- Validate all user inputs
- Use parameterized queries only

## Project Conventions & Style Guide
- Use TypeScript strict mode
- Prefer functional components with hooks
- Co-locate tests with source files
- Use named exports over default exports

## Tech Stack & Architecture Overview
- API routes via TRPC procedures in src/server
- Database access only through Prisma client in src/services
- Authentication handled by Supabase Auth helpers

## Testing Requirements & Patterns
- Unit tests for all utility functions
- Integration tests for API endpoints
- E2E tests for critical user flows (auth, checkout)
- Minimum 80% code coverage

## Git Workflow & Branch Strategy
- main: production-ready code
- develop: integration branch
- feature/*: new features
- fix/*: bug fixes
- Always squash merge feature branches

## Security & Compliance Rules
- Never log sensitive user data
- Sanitize all user inputs before processing
- Use environment variables for all secrets
- Run `npm audit` before each release

## File Naming & Folder Conventions
- Components: PascalCase (e.g., UserProfile.tsx)
- Utilities: camelCase (e.g., formatDate.ts)
- Types: PascalCase interfaces, suffix with Type/Props
- Test files: *.test.ts or *.spec.ts

## Review Checklist Before Commits
- [ ] No hardcoded secrets or credentials
- [ ] Tests written and passing
- [ ] Lint and typecheck passing
- [ ] Meaningful commit message (conventional commits)
- [ ] No console.log statements in production code
- [ ] Accessibility considerations addressed
