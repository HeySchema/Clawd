# /deploy — Deployment Helper

Guide through a safe, step-by-step deployment to the target environment.

## Usage
```
/deploy [environment]
/deploy staging
/deploy production
```

## Pre-flight Checks (run automatically)
1. `npm run lint` — lint must pass
2. `npm run typecheck` — no type errors
3. `npm test` — full test suite green
4. `npm audit` — no critical vulnerabilities
5. Verify `.env` variables are set for target environment
6. Confirm branch is up-to-date with `develop` (or `main` for production)

## Deployment Steps
1. Build the application: `npm run build`
2. Run database migrations: `npx prisma migrate deploy`
3. Push Docker image to registry
4. Update the deployment manifest
5. Roll out to target environment
6. Run smoke tests post-deploy
7. Tag the release commit

## Rollback Plan
If any step fails, the deploy halts and instructions for rollback are printed.
