import { describe, it, expect, beforeAll, afterAll } from 'vitest';

/**
 * Integration tests for TRPC API endpoints.
 * These tests require a running database and Supabase instance.
 * Set TEST_DATABASE_URL in your .env.test file before running.
 */

beforeAll(async () => {
  // Seed test database
});

afterAll(async () => {
  // Clean up test database
});

describe('Health endpoint', () => {
  it('returns 200 OK', async () => {
    const res = await fetch(`${process.env.NEXT_PUBLIC_APP_URL}/api/health`);
    expect(res.status).toBe(200);
    const body = await res.json();
    expect(body).toMatchObject({ status: 'ok' });
  });
});

// Add endpoint-specific tests here as routes are implemented
