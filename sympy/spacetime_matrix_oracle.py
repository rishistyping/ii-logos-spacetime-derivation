#!/usr/bin/env python3
"""Exact matrix oracle and branch classification for A(lambda)."""
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


def classify_branch(lam_val: int) -> dict[str, str]:
    Av = A.subs(lambda_, lam_val)
    det = sp.simplify(Av.det())
    trace = sp.simplify(Av.trace())
    charpoly = sp.expand(Av.charpoly(x).as_expr())
    if lam_val > 0:
        branch = "positive"
        behavior = "hyperbolic / real split polynomial roots"
    elif lam_val == 0:
        branch = "zero"
        behavior = "parabolic / nilpotent"
    else:
        branch = "negative"
        behavior = "elliptic explainer behavior over real phase plane"
    return {
        "lambda": str(lam_val),
        "branch": branch,
        "behavior": behavior,
        "trace": str(trace),
        "determinant": str(det),
        "charpoly": str(charpoly),
        "eigenvalues": [str(ev) for ev in Av.eigenvals().keys()],
    }

summary = {
    "matrix": [[str(v) for v in row] for row in A.tolist()],
    "trace": str(A.trace()),
    "determinant": str(A.det()),
    "charpoly": str(sp.expand(A.charpoly(x).as_expr())),
    "symbolic_eigenvalues": [str(ev) for ev in A.eigenvals().keys()],
    "branches": {
        "lambda_positive": classify_branch(1),
        "lambda_zero": classify_branch(0),
        "lambda_negative": classify_branch(-1),
    },
}

with (RESULTS / "matrix_oracle_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

branch_summary = {
    name: data for name, data in summary["branches"].items()
}
with (RESULTS / "branch_summary.json").open("w", encoding="utf-8") as f:
    json.dump(branch_summary, f, indent=2)

print(json.dumps(summary, indent=2))
print(f"Wrote {RESULTS / 'matrix_oracle_summary.json'}")
print(f"Wrote {RESULTS / 'branch_summary.json'}")
