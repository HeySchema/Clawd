import { describe, it, expect } from 'vitest';
import { signInSchema, signUpSchema, paginationSchema } from '../../src/utils/validators';

describe('signInSchema', () => {
  it('accepts valid credentials', () => {
    const result = signInSchema.safeParse({ email: 'user@example.com', password: 'secret' });
    expect(result.success).toBe(true);
  });

  it('rejects an invalid email', () => {
    const result = signInSchema.safeParse({ email: 'not-an-email', password: 'secret' });
    expect(result.success).toBe(false);
  });

  it('rejects an empty password', () => {
    const result = signInSchema.safeParse({ email: 'user@example.com', password: '' });
    expect(result.success).toBe(false);
  });
});

describe('signUpSchema', () => {
  const valid = {
    email: 'user@example.com',
    password: 'Password1',
    confirmPassword: 'Password1',
  };

  it('accepts a valid sign-up payload', () => {
    expect(signUpSchema.safeParse(valid).success).toBe(true);
  });

  it('rejects mismatched passwords', () => {
    const result = signUpSchema.safeParse({ ...valid, confirmPassword: 'Different1' });
    expect(result.success).toBe(false);
  });

  it('rejects a weak password (no uppercase)', () => {
    const result = signUpSchema.safeParse({ ...valid, password: 'password1', confirmPassword: 'password1' });
    expect(result.success).toBe(false);
  });
});

describe('paginationSchema', () => {
  it('uses defaults when no input is provided', () => {
    const result = paginationSchema.parse({});
    expect(result).toEqual({ page: 1, limit: 20 });
  });

  it('rejects a limit above 100', () => {
    const result = paginationSchema.safeParse({ limit: 200 });
    expect(result.success).toBe(false);
  });
});
