# Skill: Refactor

## Purpose
Improve code quality, readability, and maintainability without changing observable behavior.

## Trigger
Use this skill when asked to refactor, clean up, simplify, or restructure code.

## Principles
- **No behavior changes** — refactoring must not alter outputs or side effects
- **Smallest safe steps** — one logical change at a time, verified by tests
- **Leave it better** — apply the Boy Scout Rule: leave code cleaner than you found it

## Common Refactoring Patterns

### Extract Function
Move repeated or complex inline logic into a named function in `src/utils/`.

### Rename for Clarity
Rename variables, functions, and types to accurately reflect their purpose.

### Remove Dead Code
Delete unused imports, variables, functions, and feature flags.

### Simplify Conditionals
Replace nested ternaries and complex boolean logic with early returns or named predicates.

### Replace Magic Values
Extract hardcoded strings and numbers into named constants or enums.

### Decompose Component
Split large React components (>200 lines) into smaller, focused sub-components.

## Steps

1. **Read** the target file(s) fully before making any changes
2. **Identify** the specific smell or improvement opportunity
3. **Verify tests exist** — if not, write characterization tests first
4. **Apply** one refactoring pattern at a time
5. **Run tests** — confirm nothing broke
6. **Repeat** until the goal is met

## Constraints
- Do not change public APIs or exported type signatures without explicit permission
- Do not introduce new dependencies during refactoring
- Always run `npm run lint && npm run typecheck` after changes
