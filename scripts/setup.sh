#!/usr/bin/env bash
set -euo pipefail

echo "==> Installing dependencies..."
npm install

echo "==> Copying environment template..."
if [ ! -f .env.local ]; then
  cp .env.example .env.local
  echo "    Created .env.local — please fill in the required values."
else
  echo "    .env.local already exists, skipping."
fi

echo "==> Generating Prisma client..."
npx prisma generate

echo "==> Running database migrations..."
npx prisma migrate dev --name init

echo "==> Seeding database..."
npm run db:seed

echo "==> Running lint and typecheck..."
npm run lint
npm run typecheck

echo ""
echo "Setup complete! Start the dev server with: npm run dev"
