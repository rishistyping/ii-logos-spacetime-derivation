#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

echo "== Lean proof-hole text scan =="
if command -v rg >/dev/null 2>&1; then
  SCAN=(rg -n '\bsorry\b|\badmit\b' Spacetime.lean SpacetimeFull.lean Spacetime/*.lean)
else
  SCAN=(grep -RInE --include='*.lean' '\bsorry\b|\badmit\b' Spacetime.lean SpacetimeFull.lean Spacetime)
fi

if "${SCAN[@]}"; then
  echo "Found proof holes in Lean files." >&2
  exit 1
fi
echo "No proof-hole tokens found in Lean files."

if ! command -v lake >/dev/null 2>&1; then
  echo "Lean/Lake is required for Lean-promoted claims." >&2
  exit 1
fi

echo "== Lean build =="
lake build
