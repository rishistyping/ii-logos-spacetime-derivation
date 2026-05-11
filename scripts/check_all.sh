#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if command -v uv >/dev/null 2>&1; then
  PY=(uv run python)
else
  PY=(python)
fi

echo "== Python exact checks =="
"${PY[@]}" sympy/spacetime_exact_checks.py
"${PY[@]}" sympy/spacetime_matrix_oracle.py
"${PY[@]}" sympy/spacetime_eigendirections.py
"${PY[@]}" sympy/spacetime_regression_check.py
"${PY[@]}" sympy/spacetime_visualize.py

if command -v rg >/dev/null 2>&1; then
  echo "== Lean proof-hole text scan =="
  if rg -n '\bsorry\b|\badmit\b' Spacetime.lean SpacetimeFull.lean Spacetime/*.lean; then
    echo "Found proof holes in Lean files." >&2
    exit 1
  else
    echo "No sorry/admit found in Lean files."
  fi
else
  echo "ripgrep not installed; skipping proof-hole text scan."
fi

if command -v lake >/dev/null 2>&1; then
  echo "== Lean build =="
  lake build
else
  echo "Lean/Lake not installed; skipping lake build. Do not promote Lean-proved claims from this run."
fi
