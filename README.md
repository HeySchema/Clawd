# My App

A full-stack web application built with Next.js 14, TypeScript, Supabase, Prisma, and TRPC.

## Quick Start

```bash
npm install
cp .env.example .env.local   # fill in your values
npx prisma migrate dev
npm run dev
```

App runs at [http://localhost:3000](http://localhost:3000).

## Documentation

- [Architecture](docs/architecture.md)
- [API Reference](docs/api-reference.md)
- [Onboarding Guide](docs/onboarding.md)

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Production build |
| `npm test` | Run full test suite |
| `npm run lint` | Run ESLint |
| `npm run typecheck` | TypeScript type check |

## Claude Code Commands

| Command | Description |
|---------|-------------|
| `/review` | Code review of staged changes |
| `/test-all` | Run full test suite |
| `/deploy` | Deploy to an environment |
| `/bootstrap` | Set up a fresh environment |