#!/usr/bin/env python3
"""Exact eigendirection checks for the positive curvature branch."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

s = sp.symbols("s", positive=True, real=True)
lambda_ = s**2
A = sp.Matrix([[0, -lambda_], [-1, 0]])

ell_plus = sp.Matrix([[-s], [1]])
ell_minus = sp.Matrix([[s], [1]])

plus_residual = sp.simplify(A * ell_plus - s * ell_plus)
minus_residual = sp.simplify(A * ell_minus - (-s) * ell_minus)

assert plus_residual == sp.zeros(2, 1)
assert minus_residual == sp.zeros(2, 1)
assert ell_plus[1] == 1
assert ell_minus[1] == 1
assert sp.simplify(ell_plus[0] - ell_minus[0]) == -2 * s


def matrix_to_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(value) for value in row] for row in matrix.tolist()]


summary = {
    "parameterization": {
        "lambda": "s**2",
        "assumption": "s > 0",
    },
    "matrix_A": matrix_to_strings(A),
    "ell_plus": {
        "coordinates_K_P": [str(value) for value in ell_plus],
        "eigenvalue": "s",
        "residual": matrix_to_strings(plus_residual),
        "nonzero_witness": "P coordinate is 1",
    },
    "ell_minus": {
        "coordinates_K_P": [str(value) for value in ell_minus],
        "eigenvalue": "-s",
        "residual": matrix_to_strings(minus_residual),
        "nonzero_witness": "P coordinate is 1",
    },
    "distinct_positive_branch": {
        "difference_ell_plus_minus_ell_minus": [str(value) for value in sp.simplify(ell_plus - ell_minus)],
        "reason": "s > 0 implies -2*s != 0",
    },
}

with (RESULTS / "eigendirection_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("All eigendirection checks PASSED for lambda = s**2, s > 0.")
print(f"Wrote {RESULTS / 'eigendirection_summary.json'}")
