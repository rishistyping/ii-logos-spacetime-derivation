#!/usr/bin/env python3
"""Computed companion for the four-dimensional Lambda sign bridge."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

d = sp.symbols("d", integer=True, positive=True)
lambda_ = sp.symbols("lambda", positive=True, real=True)

Lambda = sp.simplify(((d - 1) * (d - 2) * lambda_) / 2)
Lambda_d4 = sp.simplify(Lambda.subs(d, 4))
residual_d4 = sp.simplify(Lambda_d4 - 3 * lambda_)

assert Lambda_d4 == 3 * lambda_
assert residual_d4 == 0

summary = {
    "truth_tag": "Computed here",
    "authority_note": "Computed companion for the Lean four-dimensional arithmetic bridge.",
    "general_relation": "Lambda(d,lambda) = ((d - 1)*(d - 2)/2)*lambda",
    "d4_relation": str(Lambda_d4),
    "d4_residual_against_3_lambda": str(residual_d4),
    "positive_sign_reason": "For lambda > 0, 3*lambda > 0.",
}

with (RESULTS / "lambda_sign_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("All Lambda sign checks PASSED for d = 4 and lambda > 0.")
print(f"Wrote {RESULTS / 'lambda_sign_summary.json'}")
