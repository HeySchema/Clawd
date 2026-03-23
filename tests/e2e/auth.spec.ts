import { test, expect } from '@playwright/test';

/**
 * E2E tests for the authentication flow.
 * Requires the dev server to be running: npm run dev
 */

const TEST_EMAIL = 'e2e-test@example.com';
const TEST_PASSWORD = 'TestPassword1';

test.describe('Sign In', () => {
  test('user can sign in with valid credentials', async ({ page }) => {
    await page.goto('/sign-in');
    await page.getByLabel('Email').fill(TEST_EMAIL);
    await page.getByLabel('Password').fill(TEST_PASSWORD);
    await page.getByRole('button', { name: 'Sign in' }).click();
    await expect(page).toHaveURL('/dashboard');
  });

  test('shows error for invalid credentials', async ({ page }) => {
    await page.goto('/sign-in');
    await page.getByLabel('Email').fill('wrong@example.com');
    await page.getByLabel('Password').fill('wrongpassword');
    await page.getByRole('button', { name: 'Sign in' }).click();
    await expect(page.getByRole('alert')).toBeVisible();
  });
});

test.describe('Sign Up', () => {
  test('user can create a new account', async ({ page }) => {
    await page.goto('/sign-up');
    await page.getByLabel('Email').fill(`new-${Date.now()}@example.com`);
    await page.getByLabel('Password').fill(TEST_PASSWORD);
    await page.getByLabel('Confirm Password').fill(TEST_PASSWORD);
    await page.getByRole('button', { name: 'Sign up' }).click();
    await expect(page).toHaveURL('/dashboard');
  });
});
