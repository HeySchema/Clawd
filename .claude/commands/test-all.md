# /test-all — Run Full Test Suite

Execute the complete test suite (unit, integration, and E2E) and report results.

## Usage
```
/test-all
/test-all --coverage
/test-all --watch
```

## Test Phases

### 1. Unit Tests
```bash
npm run test:unit
```
Runs tests co-located with source files (`*.test.ts`, `*.spec.ts`).

### 2. Integration Tests
```bash
npm run test:integration
```
Tests API endpoints and service interactions.

### 3. End-to-End Tests
```bash
npm run test:e2e
```
Covers critical user flows: authentication, checkout.

## Coverage Requirements
- Minimum **80%** overall code coverage
- Any file below threshold is flagged as a blocker

## Output
- Summary table per phase (passed / failed / skipped)
- Coverage report written to `coverage/`
- Exit code 1 if any phase fails or coverage threshold not met
