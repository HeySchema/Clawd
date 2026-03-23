# API Reference

All API communication goes through TRPC procedures. Each procedure is fully type-safe end-to-end.

## Base URL

```
/api/trpc
```

## Health Check

```
GET /api/health
```

**Response:**
```json
{ "status": "ok", "timestamp": "2024-01-15T12:00:00.000Z" }
```

---

## Authentication Procedures

### `auth.signIn`

Sign in with email and password.

**Input:**
```ts
{ email: string; password: string }
```

**Output:**
```ts
{ user: UserType; session: AuthSessionType }
```

---

### `auth.signUp`

Create a new user account.

**Input:**
```ts
{ email: string; password: string; confirmPassword: string }
```

**Output:**
```ts
{ user: UserType }
```

---

### `auth.signOut`

Invalidate the current session.

**Input:** none

**Output:**
```ts
{ success: true }
```

---

## Error Format

All TRPC errors follow this shape:

```ts
{
  error: {
    message: string;
    code: 'BAD_REQUEST' | 'UNAUTHORIZED' | 'NOT_FOUND' | 'INTERNAL_SERVER_ERROR';
    data: { zodError?: ZodError; httpStatus: number }
  }
}
```
