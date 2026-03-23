#!/usr/bin/env bash
set -euo pipefail

echo "==> Seeding database..."
npx prisma db seed

echo "Database seeded successfully."
