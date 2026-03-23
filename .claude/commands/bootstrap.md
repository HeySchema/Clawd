# /bootstrap — Project Bootstrap

Initialize the project from scratch for a new developer or fresh environment.

## Usage
```
/bootstrap
/bootstrap --skip-db
/bootstrap --ci
```

## Steps Performed

### 1. Install Dependencies
```bash
npm install
```

### 2. Environment Setup
- Copies `.env.example` → `.env.local`
- Prompts for required secret values (or reads from CI secrets)

### 3. Database Setup
```bash
npx prisma generate
npx prisma migrate dev
npm run db:seed
```

### 4. Verify Setup
```bash
npm run lint
npm run typecheck
npm run test:unit
```

### 5. Start Dev Server
```bash
npm run dev
```

## Flags
| Flag | Description |
|------|-------------|
| `--skip-db` | Skip database migration and seed steps |
| `--ci` | Non-interactive mode; read secrets from environment |

## After Bootstrap
The app will be running at `http://localhost:3000`.
See `docs/onboarding.md` for next steps.
