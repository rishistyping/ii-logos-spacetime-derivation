#!/usr/bin/env python3
"""Computed invariant-form summary for the time-evolution matrix."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

lambda_, a, b, c = sp.symbols("lambda a b c", real=True)
A = sp.Matrix([[0, -lambda_], [-1, 0]])
G = sp.Matrix([[a, b], [b, c]])
invariance = sp.simplify(A.T * G + G * A)
equations = [sp.Eq(entry, 0) for entry in invariance]
solution = sp.solve(equations, (b, c), dict=True)

canonical_G = sp.Matrix([[1, 0], [0, -lambda_]])
canonical_residual = sp.simplify(A.T * canonical_G + canonical_G * A)

assert canonical_residual == sp.zeros(2, 2)
assert solution

summary = {
    "truth_tag": "Computed here",
    "authority_note": "Computed invariant-form companion for Q(k,p)=k**2-lambda*p**2.",
    "matrix_A": [[str(value) for value in row] for row in A.tolist()],
    "symmetric_form_variables": {"G": [[str(value) for value in row] for row in G.tolist()]},
    "invariance_equation": "A.T*G + G*A = 0",
    "solution_family": [{str(key): str(value) for key, value in item.items()} for item in solution],
    "canonical_form": [[str(value) for value in row] for row in canonical_G.tolist()],
    "canonical_residual": [[str(value) for value in row] for row in canonical_residual.tolist()],
}

with (RESULTS / "invariant_metric_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("All invariant-form checks PASSED.")
print(f"Wrote {RESULTS / 'invariant_metric_summary.json'}")
