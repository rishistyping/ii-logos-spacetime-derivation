#!/usr/bin/env python3
"""Computed companion for the split-cone packet."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

s, a, k0, p0 = sp.symbols("s a k0 p0", positive=True, real=True)
lam = s**2

def split_quadratic(vk: sp.Symbol, vp: sp.Symbol) -> sp.Expr:
    return sp.simplify(vk**2 - lam * vp**2)

ell_plus = sp.Matrix([[-s], [1]])
ell_minus = sp.Matrix([[s], [1]])

Q_plus = split_quadratic(ell_plus[0], ell_plus[1])
Q_minus = split_quadratic(ell_minus[0], ell_minus[1])

generic_k, generic_p = sp.symbols("k p", real=True)
generic_Q_scaled = split_quadratic(a * generic_k, a * generic_p)
generic_Q = split_quadratic(generic_k, generic_p)
scale_residual = sp.simplify(generic_Q_scaled - a**2 * generic_Q)

assert Q_plus == 0
assert Q_minus == 0
assert scale_residual == 0

summary = {
    "truth_tag": "Computed here",
    "authority_note": "Computed companion for algebraic split-cone closure; does not promote physical light-cone interpretation.",
    "parameterization": {"lambda": "s**2", "assumption": "s > 0"},
    "cone_predicate": "splitCone(lam,v) := splitQuadratic(lam,v)=0",
    "split_quadratic": {
        "expression": "Q(k,p) = k**2 - lam*p**2",
        "lambda_substitution": "lam = s**2",
    },
    "ell_plus": {
        "coordinates_K_P": [str(value) for value in ell_plus],
        "Q_value": str(Q_plus),
    },
    "ell_minus": {
        "coordinates_K_P": [str(value) for value in ell_minus],
        "Q_value": str(Q_minus),
    },
    "homogeneity": {
        "identity": "Q(a*v) = a**2*Q(v)",
        "residual": str(scale_residual),
    },
}

with (RESULTS / "split_cone_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("Split-cone algebra checks PASSED for lambda = s**2, s > 0.")
print(f"Wrote {RESULTS / 'split_cone_summary.json'}")
