#!/usr/bin/env bash
set -euo pipefail

TARGET_DIR="${1:-.}"
cd "$TARGET_DIR"

echo "== Frontend Audit =="
echo "Dir: $(pwd)"

# Detect package manager
PM="npm"
if [ -f "pnpm-lock.yaml" ]; then PM="pnpm"; fi
if [ -f "yarn.lock" ]; then PM="yarn"; fi

echo "Package manager: $PM"

echo ""
echo "== Install deps =="
if [ "$PM" = "pnpm" ]; then
  pnpm install
elif [ "$PM" = "yarn" ]; then
  yarn install --frozen-lockfile || yarn install
else
  npm ci || npm install
fi

run_cmd () {
  local cmd="$1"
  if jq -e ".scripts[\"$cmd\"]" package.json >/dev/null 2>&1; then
    echo ""
    echo "== Run: $cmd =="
    if [ "$PM" = "pnpm" ]; then pnpm run "$cmd"
    elif [ "$PM" = "yarn" ]; then yarn "$cmd"
    else npm run "$cmd"
    fi
  else
    echo ""
    echo "== Skip: $cmd (not defined) =="
  fi
}

run_cmd lint
run_cmd test
run_cmd build

echo ""
echo "== Suggestions =="
echo "- If this is a Next.js app, consider running: next build && next lint"
echo "- If bundle size is a concern, run a bundle analyzer (Next or Vite plugin)."
echo "- Review Core Web Vitals budgets (LCP/INP/CLS) for critical routes."

echo ""
echo "Done."
