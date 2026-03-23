# Skill: Text Writer

## Purpose
Generate well-structured, audience-appropriate written content — documentation, changelogs, commit messages, PR descriptions, and more.

## Trigger
Use this skill when asked to write, draft, or improve any text artifact related to the project.

## Supported Content Types

| Type | Description |
|------|-------------|
| Commit message | Conventional commit format (`feat:`, `fix:`, `chore:`) |
| PR description | Summary, motivation, test plan, screenshots |
| Changelog entry | User-facing summary of changes for a release |
| API docs | Endpoint descriptions, request/response examples |
| Onboarding guide | Step-by-step setup for new developers |
| Architecture doc | System overview, data flow, component responsibilities |

## Steps

1. **Identify the audience** — developer, end-user, or stakeholder
2. **Gather context** — read relevant code, diffs, or issue descriptions
3. **Draft content** — use clear, concise language; avoid jargon for non-developer audiences
4. **Apply formatting** — use Markdown headings, lists, and code blocks where appropriate
5. **Review** — ensure accuracy, completeness, and adherence to project style

## Style Rules
- Use active voice
- Prefer short sentences
- Lead with the most important information
- Never include internal implementation details in user-facing docs
