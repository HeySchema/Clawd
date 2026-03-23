# Developer Onboarding

Welcome to My App! This guide will get you up and running in minutes.

## Prerequisites

- Node.js 20+
- npm 10+
- Docker (for local PostgreSQL)
- A Supabase account (or run Supabase locally)

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/your-org/my-app.git
cd my-app
```

### 2. Install dependencies

```bash
npm install
```

### 3. Set up environment variables

```bash
cp .env.example .env.local
```

Open `.env.local` and fill in the required values. See comments in the file for guidance.

### 4. Start the database

```bash
docker compose up -d
```

### 5. Run database migrations

```bash
npx prisma migrate dev
npm run db:seed
```

### 6. Start the development server

```bash
npm run dev
```

The app is now running at [http://localhost:3000](http://localhost:3000).

---

## Running Tests

```bash
npm run test:unit        # Unit tests
npm run test:integration # Integration tests (requires running DB)
npm run test:e2e         # Playwright E2E tests (requires dev server)
npm test                 # All tests + coverage report
```

## Code Quality

```bash
npm run lint       # ESLint
npm run typecheck  # TypeScript compiler check
```

Both must pass before opening a PR.

## Project Structure

See [architecture.md](./architecture.md) for a detailed overview.

## Getting Help

- Check existing issues on GitHub
- Ask in `#engineering` Slack channel
- Run `/bootstrap` in Claude Code for automated setup
