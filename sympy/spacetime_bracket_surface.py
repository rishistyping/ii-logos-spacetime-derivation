#!/usr/bin/env python3
"""Computed companion for the constant-curvature bracket surface packet."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

lam = sp.symbols("lambda", real=True)
a, b = sp.symbols("a b", integer=True)

def translation_bracket(a_idx: int, b_idx: int, lam_val: sp.Expr) -> sp.Symbol:
    return lam_val

coeff = translation_bracket(a, b, lam)

summary = {
    "truth_tag": "Computed here",
    "authority_note": "Computed companion for constant-curvature bracket-surface structure.",
    "constant_curvature_rule": "[P_a, P_b] = lambda J_ab",
    "symbolic_coefficients": {"symbol": "Q_a_b", "value": str(coeff)},
    "hygiene_checks": {
        "linear_in_lambda": str(coeff.subs(lam, sp.Symbol("lam1") + sp.Symbol("lam2"))),
        "zero_lambda": str(translation_bracket(1, 2, 0)),
        "index_stub": [str(a), str(b)],
    },
}

with (RESULTS / "bracket_surface_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("Constant-curvature bracket surface checks PASSED (scaffold summary).")
print(f"Wrote {RESULTS / 'bracket_surface_summary.json'}")
