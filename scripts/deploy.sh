#!/usr/bin/env bash
set -euo pipefail

ENVIRONMENT="${1:-staging}"

echo "==> Deploying to: $ENVIRONMENT"

echo "==> Running pre-flight checks..."
npm run lint
npm run typecheck
npm test
npm audit --audit-level=high

echo "==> Building application..."
npm run build

echo "==> Running database migrations..."
npx prisma migrate deploy

echo "==> Building Docker image..."
IMAGE_TAG="my-app:$(git rev-parse --short HEAD)"
docker build -t "$IMAGE_TAG" .

echo "==> Pushing image to registry..."
docker push "$IMAGE_TAG"

echo "==> Deployment complete: $IMAGE_TAG -> $ENVIRONMENT"

echo "==> Running smoke tests..."
HEALTH_URL="${NEXT_PUBLIC_APP_URL:-http://localhost:3000}/api/health"
curl -sf "$HEALTH_URL" | jq .

echo "==> Tagging release..."
VERSION=$(node -p "require('./package.json').version")
git tag "v${VERSION}" && git push origin "v${VERSION}"

echo ""
echo "Deploy successful!"
