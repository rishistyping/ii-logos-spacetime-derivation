#!/usr/bin/env python3
"""Regression checks asserting exact symbolic forms with no floating point."""
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

assert A.trace() == 0
assert sp.simplify(A.det() + lambda_) == 0
assert sp.expand(A.charpoly(x).as_expr() - (x**2 - lambda_)) == 0
assert sp.simplify(A * A - lambda_ * I) == sp.zeros(2)
assert A.subs(lambda_, 0) ** 2 == sp.zeros(2)
assert A.subs(lambda_, 1).det() < 0
assert A.subs(lambda_, -1).det() > 0

summary = {
    "status": "passed",
    "checks": [
        "trace(A) == 0",
        "det(A) == -lambda",
        "charpoly(A) == x**2 - lambda",
        "A**2 == lambda*I",
        "lambda=0 gives A**2 == 0",
        "lambda=1 gives det(A) < 0",
        "lambda=-1 gives det(A) > 0",
    ],
}

with (RESULTS / "regression_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("All regression checks PASSED (exact symbolic forms).")
print(f"Wrote {RESULTS / 'regression_summary.json'}")
