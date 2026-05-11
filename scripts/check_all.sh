#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

bash scripts/check_python.sh
bash scripts/check_artifacts.sh

if command -v uv >/dev/null 2>&1; then
  uv run python scripts/check_truth_surface.py
else
  python scripts/check_truth_surface.py
fi

bash scripts/check_lean.sh
