'use client';

import { useState } from 'react';
import { signInSchema, type SignInInput } from '../../utils/validators';
import { signIn } from '../../services/auth';

export function SignInForm() {
  const [errors, setErrors] = useState<Partial<SignInInput>>({});
  const [loading, setLoading] = useState(false);

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
    e.preventDefault();
    const formData = new FormData(e.currentTarget);
    const raw = { email: formData.get('email'), password: formData.get('password') };

    const result = signInSchema.safeParse(raw);
    if (!result.success) {
      const fieldErrors: Partial<SignInInput> = {};
      result.error.errors.forEach((err) => {
        const field = err.path[0] as keyof SignInInput;
        fieldErrors[field] = err.message as never;
      });
      setErrors(fieldErrors);
      return;
    }

    setLoading(true);
    try {
      await signIn(result.data.email, result.data.password);
    } finally {
      setLoading(false);
    }
  }

  return (
    <form onSubmit={handleSubmit} noValidate aria-label="Sign in form">
      <div>
        <label htmlFor="email">Email</label>
        <input id="email" name="email" type="email" autoComplete="email" required />
        {errors.email && <p role="alert">{errors.email}</p>}
      </div>
      <div>
        <label htmlFor="password">Password</label>
        <input id="password" name="password" type="password" autoComplete="current-password" required />
        {errors.password && <p role="alert">{errors.password}</p>}
      </div>
      <button type="submit" disabled={loading}>
        {loading ? 'Signing in…' : 'Sign in'}
      </button>
    </form>
  );
}
