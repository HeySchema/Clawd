# Skill: Security Audit

## Purpose
Systematically audit the codebase or a specific area for security vulnerabilities, misconfigurations, and compliance gaps.

## Trigger
Use this skill when asked to audit security, check for vulnerabilities, or prepare for a security review.

## Audit Checklist

### Authentication & Authorization
- [ ] Supabase Auth helpers used correctly (no manual JWT parsing)
- [ ] Row-level security (RLS) policies defined in Supabase
- [ ] Protected routes validated server-side, not only client-side
- [ ] No authorization logic duplicated across client and server

### Input Validation
- [ ] All user inputs validated with a schema library (e.g., Zod)
- [ ] File uploads restricted by type and size
- [ ] Query parameters sanitized before use

### Data Exposure
- [ ] No sensitive fields returned in API responses unnecessarily
- [ ] `console.log` statements removed from production paths
- [ ] Error messages do not leak stack traces to clients

### Secrets & Config
- [ ] No secrets committed to the repository
- [ ] All secrets sourced from environment variables
- [ ] `.env.example` contains only placeholder values

### Dependencies
- [ ] `npm audit` passes with no critical findings
- [ ] Dependency versions pinned in `package.json`

### Database
- [ ] Parameterized queries used exclusively (via Prisma)
- [ ] No raw SQL with user-supplied interpolation

## Output
A risk-rated report: **High / Medium / Low / Info** per finding, with remediation guidance.
