#!/usr/bin/env python3
"""Generate the full project guide as a PDF using ReportLab."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable, Preformatted
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT
import os

W, H = A4
OUT = "/home/user/Clawd/docs/project-guide.pdf"

# ── Styles ────────────────────────────────────────────────────────────────────
base = getSampleStyleSheet()

TITLE   = ParagraphStyle("TITLE",   parent=base["Title"],    fontSize=28, leading=34, textColor=colors.HexColor("#1a1a7e"), spaceAfter=8)
SUBTITLE= ParagraphStyle("SUBTITLE",parent=base["Normal"],   fontSize=13, leading=18, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=4)
DATE    = ParagraphStyle("DATE",    parent=base["Normal"],   fontSize=10, textColor=colors.HexColor("#888888"), alignment=TA_CENTER, spaceAfter=20)
H1      = ParagraphStyle("H1",      parent=base["Heading1"], fontSize=15, leading=20, textColor=colors.HexColor("#14147a"), backColor=colors.HexColor("#ededff"), spaceBefore=14, spaceAfter=6, borderPad=4)
H2      = ParagraphStyle("H2",      parent=base["Heading2"], fontSize=11, leading=15, textColor=colors.HexColor("#282828"), spaceBefore=10, spaceAfter=4)
H3      = ParagraphStyle("H3",      parent=base["Heading3"], fontSize=10, leading=13, textColor=colors.HexColor("#333333"), spaceBefore=7, spaceAfter=3)
BODY    = ParagraphStyle("BODY",    parent=base["Normal"],   fontSize=9,  leading=13, spaceAfter=4)
BULLET  = ParagraphStyle("BULLET",  parent=base["Normal"],   fontSize=9,  leading=13, leftIndent=14, bulletIndent=4, spaceAfter=2)
CODE    = ParagraphStyle("CODE",    parent=base["Code"],     fontSize=7.5,leading=10, backColor=colors.HexColor("#f5f5f5"), borderColor=colors.HexColor("#d0d0d0"), borderPad=6, fontName="Courier", spaceAfter=6)

def h1(text):      return Paragraph(text, H1)
def h2(text):      return Paragraph(text, H2)
def h3(text):      return Paragraph(text, H3)
def body(text):    return Paragraph(text, BODY)
def bullet(text):  return Paragraph(f"\u2022\u00a0 {text}", BULLET)
def sp(n=6):       return Spacer(1, n)
def hr():          return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor("#b0b0d0"), spaceAfter=4)
def code(text):    return Preformatted(text.strip(), CODE)

def tbl(headers, rows, col_widths=None):
    data = [headers] + rows
    if col_widths is None:
        col_widths = [(W - 3*cm) / len(headers)] * len(headers)
    t = Table(data, colWidths=col_widths)
    t.setStyle(TableStyle([
        ("BACKGROUND",  (0, 0), (-1, 0),  colors.HexColor("#dcdcf0")),
        ("TEXTCOLOR",   (0, 0), (-1, 0),  colors.HexColor("#111111")),
        ("FONTNAME",    (0, 0), (-1, 0),  "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, -1), 8),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.HexColor("#fafafe"), colors.white]),
        ("GRID",        (0, 0), (-1, -1), 0.4, colors.HexColor("#c0c0d8")),
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",  (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING",(0, 0),(-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
    ]))
    return t


def build():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    doc = SimpleDocTemplate(
        OUT, pagesize=A4,
        leftMargin=1.5*cm, rightMargin=1.5*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title="My App — Complete Developer Guide",
        author="Claude Code",
    )

    story = []

    # ── Cover ─────────────────────────────────────────────────────────────────
    story += [
        sp(60),
        Paragraph("My App", TITLE),
        Paragraph("Complete Developer Guide", SUBTITLE),
        HRFlowable(width="60%", thickness=1.5, color=colors.HexColor("#6464c8"), hAlign="CENTER", spaceAfter=8),
        Paragraph("Next.js 14  ·  TypeScript  ·  Tailwind  ·  Supabase  ·  Prisma  ·  TRPC", SUBTITLE),
        Paragraph("Generated: 2026-03-23", DATE),
        PageBreak(),
    ]

    # ── TOC ───────────────────────────────────────────────────────────────────
    story += [h1("Table of Contents"), sp(4)]
    toc_items = [
        ("1", "Project Overview"),
        ("2", "Initial Setup"),
        ("3", "CLAUDE.md — The AI Instruction File"),
        ("4", ".claude/settings.json — Hooks & Permissions"),
        ("5", ".claude/commands/ — Slash Commands"),
        ("6", "skills/ — Reusable Skill Definitions"),
        ("7", "agentx/ — Autonomous Agent Definitions"),
        ("8", "plugins/ — Claude Code Plugin System"),
        ("9", ".mcp.json — MCP Server Integration"),
        ("10", "src/ — Application Source Code"),
        ("11", "tests/ — Test Suite"),
        ("12", "docs/ — Documentation"),
        ("13", "scripts/ — Shell Scripts"),
        ("14", "Root Config Files"),
        ("15", "Day-to-Day Developer Workflow"),
    ]
    for num, title in toc_items:
        story.append(Paragraph(f"<font color='#6464c8'>{num}.</font>  {title}", BODY))
    story.append(PageBreak())

    # ── 1. Project Overview ───────────────────────────────────────────────────
    story += [h1("1. Project Overview"), body(
        "This project is a Next.js 14 full-stack application with a structured set of AI-assisted development "
        "tooling layered on top. There are two distinct layers:"
    ), sp(4)]
    story.append(tbl(
        ["Layer", "Purpose"],
        [
            ["AI tooling layer", ".claude/, skills/, agentx/, plugins/, .mcp.json — tells Claude Code how to behave in this repo"],
            ["Application layer", "src/, tests/, docs/, scripts/, config files — the actual app code"],
        ], [5*cm, 12*cm]
    ))
    story += [sp(4), body(
        "Understanding this separation is key. The AI tooling layer makes Claude Code project-aware, consistent, "
        "and automated. The application layer is what gets shipped."
    ), PageBreak()]

    # ── 2. Initial Setup ──────────────────────────────────────────────────────
    story += [h1("2. Initial Setup"), h3("First-time setup (new developer)")]
    story.append(code(
        "# 1. Clone and enter the repo\n"
        "git clone https://github.com/HeySchema/Clawd.git\n"
        "cd Clawd\n\n"
        "# 2. Automated bootstrap\n"
        "bash scripts/setup.sh\n\n"
        "# OR manually:\n"
        "npm install\n"
        "cp .env.example .env.local   # edit with real values\n"
        "npx prisma generate\n"
        "npx prisma migrate dev\n"
        "npm run db:seed\n"
        "npm run dev"
    ))
    story += [h3("What .env.local needs")]
    story.append(code(
        "NEXT_PUBLIC_APP_URL=http://localhost:3000\n"
        "NEXT_PUBLIC_SUPABASE_URL=https://xxxx.supabase.co\n"
        "NEXT_PUBLIC_SUPABASE_ANON_KEY=eyJ...\n"
        "SUPABASE_SERVICE_ROLE_KEY=eyJ...\n"
        "DATABASE_URL=postgresql://postgres:password@db.xxxx.supabase.co:5432/postgres\n"
        "GITHUB_TOKEN=ghp_...   # optional, for MCP GitHub"
    ))
    story += [body("Never commit .env.local — it is already in .gitignore."), PageBreak()]

    # ── 3. CLAUDE.md ──────────────────────────────────────────────────────────
    story += [h1("3. CLAUDE.md — The AI Instruction File"), h3("What it is"), body(
        "CLAUDE.md is the single most important file for AI-assisted development. Every time Claude Code "
        "starts a session in this repo, it reads this file automatically. It acts as a standing briefing — "
        "telling Claude the rules, conventions, and constraints of the project without you having to repeat them."
    ), sp(4)]
    story.append(tbl(
        ["Section", "Effect on Claude"],
        [
            ["Tech Stack", "Picks the right libraries automatically"],
            ["Conventions", "Writes tests before code, uses conventional commits, never pushes to main"],
            ["Architecture", "Puts new files in the right directories without being told"],
            ["Security", "Refuses console.log(sensitive data), always uses Prisma, validates inputs with Zod"],
            ["Testing", "Knows 80% coverage is required, writes tests for every new function"],
            ["Git Workflow", "Branches off develop, squash-merges feature branches"],
            ["Review Checklist", "Self-checks against this list before presenting code"],
        ], [4*cm, 13*cm]
    ))
    story += [sp(4), h3("How to modify it"), body(
        "Edit CLAUDE.md any time your conventions change. Changes take effect in the next session. "
        "Keep entries short and imperative."
    )]
    story.append(code(
        "## New Convention (example)\n"
        "- Always use `dayjs` for dates, never native Date methods\n"
        "- All new components must have a Storybook story in src/stories/"
    ))
    story.append(PageBreak())

    # ── 4. settings.json ─────────────────────────────────────────────────────
    story += [h1("4. .claude/settings.json — Hooks & Permissions"), h3("Permissions")]
    story.append(code(
        '"permissions": {\n'
        '  "allow": ["Bash(npm run *)", "Bash(git *)"],\n'
        '  "deny":  ["Bash(rm -rf *)", "Bash(curl * | bash)"]\n'
        "}"
    ))
    story += [body("allow: Claude can run without prompting.  deny: Blocked outright, regardless of context."), h3("Hooks"), sp(4)]
    story.append(tbl(
        ["Hook", "When it fires", "Default use"],
        [
            ["PreToolUse",   "Before any tool call",   "Safety check script"],
            ["PostToolUse",  "After tool completes",   "Auto-lint after file writes"],
            ["SessionStart", "When session opens",     "Echo CLAUDE.md, git fetch"],
            ["SessionEnd",   "When session closes",    "Notifications, cleanup"],
            ["PreCommit",    "Before git commit",      "lint + typecheck gate"],
        ], [4*cm, 5*cm, 8*cm]
    ))
    story += [sp(4), h3("Environment variables")]
    story.append(code(
        '"env": {\n'
        '  "MAX_THINKING_TOKENS": "10000",\n'
        '  "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE": "50"\n'
        "}"
    ))
    story += [body(
        "MAX_THINKING_TOKENS: Limits reasoning depth. "
        "CLAUDE_AUTOCOMPACT_PCT_OVERRIDE: Compacts context at 50% window — preserves more working memory."
    ), h3("settings.local.json — personal overrides (gitignored)")]
    story.append(code(
        '{\n'
        '  "permissions": { "allow": ["Bash(npm run dev)"] },\n'
        '  "env": { "DEBUG": "true" }\n'
        "}"
    ))
    story.append(PageBreak())

    # ── 5. Slash Commands ─────────────────────────────────────────────────────
    story += [h1("5. .claude/commands/ — Slash Commands"), body(
        "Slash commands are project-specific shortcuts that expand into full prompts. "
        "They live as Markdown files in .claude/commands/ and are invoked by typing /command-name."
    ), sp(4)]
    story.append(tbl(
        ["Command", "What it does"],
        [
            ["/review [path]",     "7-category review (security, types, tests, perf, a11y, style, conventions). Run before every PR."],
            ["/deploy [env]",      "Full pipeline: lint -> typecheck -> tests -> audit -> build -> migrate -> smoke tests. Auto-rollback on failure."],
            ["/test-all [flags]",  "Runs unit -> integration -> E2E. Fails if coverage < 80%. Supports --coverage, --watch."],
            ["/bootstrap [flags]", "New-developer setup or CI bootstrap. Supports --skip-db, --ci."],
        ], [4*cm, 13*cm]
    ))
    story += [sp(4), h3("Adding your own slash command"), body(
        "Create any .md file in .claude/commands/ and it is available immediately:"
    )]
    story.append(code(
        "# /db-reset — Reset Development Database\n\n"
        "## Steps\n"
        "1. Run `npx prisma migrate reset --force`\n"
        "2. Run `npm run db:seed`\n"
        "3. Confirm record counts"
    ))
    story.append(PageBreak())

    # ── 6. Skills ─────────────────────────────────────────────────────────────
    story += [h1("6. skills/ — Reusable Skill Definitions"), body(
        "Skills are reusable, named capability definitions that can be referenced by slash commands, agents, "
        "or invoked directly. Unlike one-shot slash commands, skills are designed to be composed."
    ), sp(4)]
    story.append(tbl(
        ["Skill", "Purpose"],
        [
            ["code-review",    "8-step: security, types, conventions, tests, performance, accessibility, report"],
            ["security-audit", "Deep checklist: auth/RLS, input validation, data exposure, secrets, deps, DB safety"],
            ["refactor",       "6 safe patterns: Extract Function, Rename, Remove Dead Code, Simplify, Magic Values, Decompose"],
            ["text-writer",    "Commit messages, PR descriptions, changelogs, API docs, onboarding guides"],
        ], [4*cm, 13*cm]
    ))
    story += [sp(4), h3("Adding a new skill")]
    story.append(code(
        "# Skill: Database Migration\n\n"
        "## Purpose\n"
        "Generate and validate Prisma migrations safely.\n\n"
        "## Steps\n"
        "1. Read prisma/schema.prisma\n"
        "2. Understand the requested change\n"
        "3. Run: npx prisma migrate dev --name <description>\n"
        "4. Verify SQL is non-destructive\n"
        "5. Update src/types/database.ts"
    ))
    story.append(PageBreak())

    # ── 7. Agents ─────────────────────────────────────────────────────────────
    story += [h1("7. agentx/ — Autonomous Agent Definitions"), body(
        "Agents are autonomous workflows that Claude runs end-to-end without step-by-step prompting. "
        "Each .yml file defines a name, tools, trigger, and step sequence."
    ), sp(4)]
    story.append(tbl(
        ["Agent", "Trigger", "What it does"],
        [
            ["code-reviewer.yml",    "PR open/update or /review",    "Diffs changed files, applies code-review skill, outputs report"],
            ["test-writer.yml",      "Manual /write-tests",          "Finds files below 80%, writes co-located tests, verifies they pass"],
            ["security-auditor.yml", "Monday 06:00 UTC or manual",   "npm audit + source scan + security-audit skill -> risk-rated report"],
            ["devops-sre.yml",       "Post-deploy or /deploy",       "Full pipeline with auto-rollback if any step fails"],
        ], [4.5*cm, 4.5*cm, 8*cm]
    ))
    story += [sp(4), h3("Wire code-reviewer to GitHub Actions")]
    story.append(code(
        "# .github/workflows/ai-review.yml\n"
        "on: [pull_request]\n"
        "jobs:\n"
        "  review:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - uses: actions/checkout@v4\n"
        "      - run: claude-code run agentx/code-reviewer.yml"
    ))
    story.append(PageBreak())

    # ── 8. Plugins ────────────────────────────────────────────────────────────
    story += [h1("8. plugins/ — Claude Code Plugin System"), h3("preToolUse — block dangerous actions")]
    story.append(code(
        "async preToolUse({ tool, input }) {\n"
        "  if (tool === 'Write' && input.file_path?.includes('.env')) {\n"
        "    return { block: true, reason: 'Direct .env writes not allowed.' };\n"
        "  }\n"
        "  return { block: false };\n"
        "}"
    ))
    story += [h3("postToolUse — audit logging")]
    story.append(code(
        "async postToolUse({ tool, input, output }) {\n"
        "  if (tool === 'Write') {\n"
        "    fs.appendFileSync('audit.log',\n"
        "      `${new Date().toISOString()} WRITE ${input.file_path}\\n`);\n"
        "  }\n"
        "}"
    ))
    story += [sp(4), body(
        "To add a second plugin: create plugins/my-plugin/index.js with the same structure and add an entry "
        "to plugins/manifest.json. Set enabled: false to disable without deleting."
    ), PageBreak()]

    # ── 9. MCP ────────────────────────────────────────────────────────────────
    story += [h1("9. .mcp.json — MCP Server Integration"), body(
        "MCP (Model Context Protocol) servers give Claude direct, authenticated access to external services "
        "during a session — no more copy-pasting data into chat."
    ), sp(4)]
    story.append(tbl(
        ["Server", "What you can ask Claude"],
        [
            ["GitHub",   '"List open bug issues", "Show diff for PR #42", "Create an issue for the auth bug"'],
            ["Postgres", '"Show users table schema", "How many signups this week?", "Find rows where email is null"'],
        ], [4*cm, 13*cm]
    ))
    story += [
        sp(4),
        body("IMPORTANT: Point the Postgres MCP at a read-only replica or dev database — NOT production."),
        h3("Adding more servers"),
    ]
    story.append(code(
        '"slack": {\n'
        '  "type": "stdio",\n'
        '  "command": "npx",\n'
        '  "args": ["-y", "@anthropic/mcp-slack"],\n'
        '  "env": { "SLACK_TOKEN": "${SLACK_TOKEN}" }\n'
        "}"
    ))
    story.append(PageBreak())

    # ── 10. src/ ──────────────────────────────────────────────────────────────
    story += [h1("10. src/ — Application Source Code"), sp(4)]
    story.append(tbl(
        ["Directory", "Contents", "Conventions"],
        [
            ["src/components/", "React UI by feature domain",      "PascalCase, named exports, no business logic, accessible"],
            ["src/services/",   "Supabase, Prisma, TRPC client",   "Only place that talks to DB or auth"],
            ["src/utils/",      "Pure helpers, Zod validators, logger", "No side effects, 100% coverage target"],
            ["src/types/",      "Shared TS interfaces + DB types", "PascalCase, suffix with Type/Props"],
        ], [4*cm, 5.5*cm, 7.5*cm]
    ))
    story += [sp(4), h3("Using the logger (replaces console.log)")]
    story.append(code(
        "import { logger } from '@/utils/logger';\n\n"
        "logger.info('User signed in', { userId: user.id });   // Good\n"
        "logger.error('Payment failed', { orderId });           // Good\n"
        "console.log(user);                                     // Bad — caught by PreCommit"
    ))
    story += [h3("Path aliases")]
    story.append(code(
        "import { UserType } from '@/types';        // -> src/types/index.ts\n"
        "import { logger }   from '@/utils/logger'; // -> src/utils/logger.ts"
    ))
    story.append(PageBreak())

    # ── 11. tests/ ────────────────────────────────────────────────────────────
    story += [h1("11. tests/ — Test Suite"), sp(4)]
    story.append(tbl(
        ["Layer", "Speed", "Requires", "Run when"],
        [
            ["tests/unit/",        "~1s",  "Nothing",         "After every change"],
            ["tests/integration/", "~10s", "Database",        "Before pushing"],
            ["tests/e2e/",         "~60s", "Running server",  "Before releases"],
        ], [4.5*cm, 2.5*cm, 4*cm, 6*cm]
    ))
    story += [sp(4), h3("Commands")]
    story.append(code(
        "npm run test:unit          # fast, no I/O\n"
        "npm run test:integration   # requires DB\n"
        "npm run test:e2e           # requires running server\n"
        "npm test                   # all three + coverage\n"
        "npm run test:watch         # re-runs on file save\n"
        "npm run test:coverage      # open coverage/index.html"
    ))
    story += [h3("AAA pattern for unit tests")]
    story.append(code(
        "describe('slugify', () => {\n"
        "  it('converts a string to a slug', () => {\n"
        "    const input = 'Hello World!';      // Arrange\n"
        "    const result = slugify(input);      // Act\n"
        "    expect(result).toBe('hello-world'); // Assert\n"
        "  });\n"
        "});"
    ))
    story += [body("Coverage minimum: 80%. Enforced by vitest --coverage."), PageBreak()]

    # ── 12. docs/ ─────────────────────────────────────────────────────────────
    story += [h1("12. docs/ — Documentation"), sp(4)]
    story.append(tbl(
        ["File", "Contents", "Update when"],
        [
            ["docs/architecture.md", "System diagram, data flow, auth flow",  "Adding major new system components"],
            ["docs/api-reference.md","Every TRPC procedure and REST endpoint", "Adding/changing any API procedure"],
            ["docs/onboarding.md",   "Day-1 guide for new developers",         "Setup steps or tooling changes"],
        ], [5*cm, 7*cm, 5*cm]
    ))
    story.append(PageBreak())

    # ── 13. scripts/ ─────────────────────────────────────────────────────────
    story += [h1("13. scripts/ — Shell Scripts"), sp(4)]
    story.append(tbl(
        ["Script", "Usage", "What it does"],
        [
            ["setup.sh",    "bash scripts/setup.sh",                       "Full first-time setup. Safe to re-run."],
            ["deploy.sh",   "bash scripts/deploy.sh [staging|production]", "Full deploy pipeline. Exits on any failure."],
            ["seed-db.sh",  "bash scripts/seed-db.sh",                     "Runs prisma db seed to reset to known state."],
        ], [3.5*cm, 6*cm, 7.5*cm]
    ))
    story += [sp(4), h3("Full reset cycle")]
    story.append(code("npx prisma migrate reset --force && bash scripts/seed-db.sh"))
    story.append(PageBreak())

    # ── 14. Root Config ───────────────────────────────────────────────────────
    story += [h1("14. Root Config Files"), h3("tsconfig.json — strict mode"), body(
        "strict: true and noUncheckedIndexedAccess: true are both enabled. "
        "Array access arr[0] returns T | undefined, not T. All nulls must be handled explicitly. "
        "No implicit any. Do NOT loosen these settings."
    ), h3("Dockerfile — multi-stage build"), sp(4)]
    story.append(tbl(
        ["Stage", "Purpose"],
        [
            ["deps",    "Installs all npm dependencies (cached layer)"],
            ["builder", "Generates Prisma client + runs next build"],
            ["runner",  "Minimal production image, non-root user"],
        ], [3*cm, 14*cm]
    ))
    story += [sp(4)]
    story.append(code(
        "docker build -t my-app:latest .\n"
        "docker run -p 3000:3000 --env-file .env.local my-app:latest"
    ))
    story += [h3(".env.example rules"),
        bullet("Contains every variable name the app needs"),
        bullet("Placeholder values only (your-key-here) — this file IS committed"),
        bullet("Never contains real secrets"),
        bullet("When you add a new env var to the app, add it here first"),
    ]
    story.append(PageBreak())

    # ── 15. Workflow ──────────────────────────────────────────────────────────
    story += [h1("15. Day-to-Day Developer Workflow"), h3("Starting a new feature")]
    story.append(code(
        "git checkout develop && git pull\n"
        "git checkout -b feature/user-profiles\n"
        "claude\n"
        '# "Add a user profile page — name, email, avatar.\n'
        "#  Use UserType from src/types, fetch via TRPC.\"\n"
        "# Claude will: TRPC procedure -> service -> component -> tests (tests first)"
    ))
    story += [h3("Before opening a PR")]
    story.append(code(
        "/review\n"
        "/test-all --coverage\n"
        "npm run lint && npm run typecheck"
    ))
    story += [h3("When coverage drops")]
    story.append(code('/write-tests\n# or: "Run the test-writer agent on src/utils/"'))
    story += [h3("Deploying")]
    story.append(code(
        "/deploy staging\n"
        "/deploy production   # after staging smoke tests pass"
    ))
    story += [sp(4), h3("Quick reference — adding new AI tooling"), sp(4)]
    story.append(tbl(
        ["What you want", "What to create"],
        [
            ["New slash command",                ".claude/commands/my-command.md"],
            ["New reusable AI capability",       "skills/my-skill/SKILL.md"],
            ["New autonomous workflow",          "agentx/my-agent.yml"],
            ["New external service integration", "Entry in .mcp.json"],
            ["New safety guard",                 "Hook in .claude/settings.json or rule in CLAUDE.md"],
            ["New project-wide AI convention",   "Section in CLAUDE.md"],
        ], [8*cm, 9*cm]
    ))

    doc.build(story)
    print(f"PDF saved to: {OUT}")

if __name__ == "__main__":
    build()
