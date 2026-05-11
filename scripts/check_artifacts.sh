#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if command -v uv >/dev/null 2>&1; then
  PY=(uv run python)
else
  PY=(python)
fi

echo "== Artifact manifest and drift check =="
"${PY[@]}" scripts/check_truth_surface.py --artifacts-only

git diff --exit-code -- results/ viz/
