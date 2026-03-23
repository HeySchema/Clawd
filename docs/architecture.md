# Architecture

## Overview

My App is a full-stack web application built with Next.js 14 (App Router), TypeScript, and Tailwind CSS. It uses Supabase for authentication and the database layer, Prisma as the ORM, and TRPC for type-safe API communication between client and server.

## High-Level Diagram

```
┌─────────────────────────────────────────────┐
│                  Browser                    │
│   Next.js App Router (React Server + Client)│
└──────────────┬──────────────────────────────┘
               │ TRPC (HTTP batch)
┌──────────────▼──────────────────────────────┐
│           Next.js API Routes                │
│   /api/trpc — TRPC procedure handlers       │
│   /api/health — Health check                │
└──────┬────────────────────┬─────────────────┘
       │ Prisma ORM          │ Supabase Auth SDK
┌──────▼──────┐     ┌────────▼───────┐
│  PostgreSQL  │     │  Supabase Auth │
│  (via Prisma)│     │  (JWT + RLS)   │
└─────────────┘     └────────────────┘
```

## Directory Structure

| Path | Responsibility |
|------|---------------|
| `src/components/` | React UI components (auth, dashboard, search) |
| `src/services/` | Business logic and data access (api, auth, database) |
| `src/utils/` | Pure utility functions (logger, validators, helpers) |
| `src/types/` | Shared TypeScript types and Supabase DB types |
| `src/server/` | TRPC router and procedures |
| `tests/unit/` | Unit tests co-located or mirrored here |
| `tests/integration/` | API integration tests |
| `tests/e2e/` | Playwright end-to-end tests |

## Data Flow

1. User action triggers a React component event handler.
2. Component calls a TRPC procedure via the `api` client (`src/services/api.ts`).
3. TRPC procedure (in `src/server/`) validates input with Zod, calls Prisma via `src/services/database.ts`.
4. Prisma executes a parameterized SQL query against PostgreSQL.
5. Result is returned through TRPC to the component and rendered.

## Authentication Flow

1. User submits credentials via `SignInForm`.
2. `src/services/auth.ts` calls `supabase.auth.signInWithPassword`.
3. Supabase returns a JWT session stored in a secure cookie.
4. Supabase Auth helpers automatically validate the JWT on server-side requests.
5. Row-level security (RLS) in Supabase enforces per-user data access.
