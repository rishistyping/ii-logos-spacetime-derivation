#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

if command -v uv >/dev/null 2>&1; then
  PY=(uv run python)
else
  PY=(python)
fi

echo "== Python exact and artifact checks =="
"${PY[@]}" sympy/spacetime_exact_checks.py
"${PY[@]}" sympy/spacetime_matrix_oracle.py
"${PY[@]}" sympy/spacetime_eigendirections.py
"${PY[@]}" sympy/spacetime_null_bridge.py
"${PY[@]}" sympy/spacetime_lambda_sign.py
"${PY[@]}" sympy/spacetime_flow_scaling.py
"${PY[@]}" sympy/spacetime_invariant_form.py
"${PY[@]}" sympy/spacetime_regression_check.py
"${PY[@]}" sympy/spacetime_visualize.py
