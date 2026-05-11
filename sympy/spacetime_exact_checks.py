#!/usr/bin/env python3
"""Exact symbolic checks for the v0 spacetime-derivation skeleton."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

lambda_ = sp.symbols("lambda", real=True)
x = sp.symbols("x")
A = sp.Matrix([[0, -lambda_], [-1, 0]])
I = sp.eye(2)

summary = {
    "matrix_A": [[str(v) for v in row] for row in A.tolist()],
    "trace": str(A.trace()),
    "determinant": str(A.det()),
    "charpoly_variable": str(x),
    "charpoly": str(sp.expand(A.charpoly(x).as_expr())),
    "square": [[str(v) for v in row] for row in (A * A).tolist()],
    "square_identity_residual": [[str(v) for v in row] for row in sp.simplify(A * A - lambda_ * I).tolist()],
    "cosmological_relation_general": "Lambda = ((d - 1)*(d - 2)/2)*lambda",
    "cosmological_relation_d4": "Lambda = 3*lambda",
}

with (RESULTS / "time_evolution_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("=== Exact Checks ===")
print("A(lambda) =")
sp.pprint(A)
print("trace(A) =", A.trace())
print("det(A) =", A.det())
print("charpoly(A) =", sp.expand(A.charpoly(x).as_expr()))
print("A^2 - lambda*I =")
sp.pprint(sp.simplify(A * A - lambda_ * I))
print(f"Wrote {RESULTS / 'time_evolution_summary.json'}")
