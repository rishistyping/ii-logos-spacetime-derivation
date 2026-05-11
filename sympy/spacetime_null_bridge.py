#!/usr/bin/env python3
"""Computed companion for the algebraic split-null bridge."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

s, a = sp.symbols("s a", positive=True, real=True)
lambda_ = s**2

ell_plus = sp.Matrix([[-s], [1]])
ell_minus = sp.Matrix([[s], [1]])


def split_quadratic(v: sp.Matrix) -> sp.Expr:
    k, p = v
    return sp.simplify(k**2 - lambda_ * p**2)


plus_value = split_quadratic(ell_plus)
minus_value = split_quadratic(ell_minus)

u0, u1 = sp.symbols("u0 u1", real=True)
u = sp.Matrix([[u0], [u1]])
scale_residual = sp.simplify(split_quadratic(a * u) - a**2 * split_quadratic(u))

assert plus_value == 0
assert minus_value == 0
assert scale_residual == 0

summary = {
    "truth_tag": "Computed here",
    "authority_note": "Computed companion for the Lean split-null algebraic bridge; not a physical light-ray proof.",
    "parameterization": {"lambda": "s**2", "assumption": "s > 0"},
    "split_quadratic": "Q(k,p) = k**2 - lambda*p**2",
    "ell_plus": {
        "coordinates_K_P": [str(value) for value in ell_plus],
        "Q_value": str(plus_value),
    },
    "ell_minus": {
        "coordinates_K_P": [str(value) for value in ell_minus],
        "Q_value": str(minus_value),
    },
    "homogeneity": {
        "identity": "Q(a*v) = a**2*Q(v)",
        "residual": str(scale_residual),
    },
}

with (RESULTS / "null_bridge_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("All split-null algebra checks PASSED for lambda = s**2, s > 0.")
print(f"Wrote {RESULTS / 'null_bridge_summary.json'}")
