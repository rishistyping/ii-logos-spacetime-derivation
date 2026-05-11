#!/usr/bin/env python3
"""Computed matrix-flow summaries for the three A(lambda) branches."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
RESULTS.mkdir(exist_ok=True)

t, s, omega = sp.symbols("t s omega", positive=True, real=True)
I = sp.eye(2)


def matrix_to_strings(matrix: sp.Matrix) -> list[list[str]]:
    return [[str(sp.simplify(value)) for value in row] for row in matrix.tolist()]


def verify_flow(A: sp.Matrix, flow: sp.Matrix) -> tuple[sp.Matrix, sp.Matrix]:
    differential_residual = sp.simplify(flow.diff(t) - A * flow)
    initial_residual = sp.simplify(flow.subs(t, 0) - I)
    assert differential_residual == sp.zeros(2, 2)
    assert initial_residual == sp.zeros(2, 2)
    return differential_residual, initial_residual


A_pos = sp.Matrix([[0, -s**2], [-1, 0]])
flow_pos = sp.cosh(s * t) * I + (sp.sinh(s * t) / s) * A_pos
pos_diff, pos_init = verify_flow(A_pos, flow_pos)

ell_plus = sp.Matrix([[-s], [1]])
ell_minus = sp.Matrix([[s], [1]])
plus_scaling = sp.simplify(flow_pos * ell_plus - sp.exp(s * t) * ell_plus)
minus_scaling = sp.simplify(flow_pos * ell_minus - sp.exp(-s * t) * ell_minus)
minus_scaling = minus_scaling.applyfunc(lambda value: sp.simplify(value.rewrite(sp.exp)))
assert plus_scaling == sp.zeros(2, 1)
assert minus_scaling == sp.zeros(2, 1)

A_zero = sp.Matrix([[0, 0], [-1, 0]])
flow_zero = I + t * A_zero
zero_diff, zero_init = verify_flow(A_zero, flow_zero)

A_neg = sp.Matrix([[0, omega**2], [-1, 0]])
flow_neg = sp.cos(omega * t) * I + (sp.sin(omega * t) / omega) * A_neg
neg_diff, neg_init = verify_flow(A_neg, flow_neg)

summary = {
    "truth_tag": "Computed here",
    "authority_note": "Computed matrix-flow companion. Physical horizon/redshift readings are not promoted here.",
    "positive_branch": {
        "lambda": "s**2",
        "flow_formula": "exp(tA) = cosh(s*t)I + sinh(s*t)/s A",
        "differential_residual": matrix_to_strings(pos_diff),
        "initial_residual": matrix_to_strings(pos_init),
        "ell_plus_scaling_residual": [str(value) for value in plus_scaling],
        "ell_minus_scaling_residual": [str(value) for value in minus_scaling],
    },
    "zero_branch": {
        "lambda": "0",
        "flow_formula": "exp(tA) = I + tA",
        "differential_residual": matrix_to_strings(zero_diff),
        "initial_residual": matrix_to_strings(zero_init),
    },
    "negative_branch": {
        "lambda": "-omega**2",
        "flow_formula": "exp(tA) = cos(omega*t)I + sin(omega*t)/omega A",
        "differential_residual": matrix_to_strings(neg_diff),
        "initial_residual": matrix_to_strings(neg_init),
    },
}

with (RESULTS / "time_flow_summary.json").open("w", encoding="utf-8") as f:
    json.dump(summary, f, indent=2)

print("All branch flow checks PASSED.")
print(f"Wrote {RESULTS / 'time_flow_summary.json'}")
