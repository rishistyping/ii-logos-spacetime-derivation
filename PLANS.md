# PLANS.md — v0 to v0.5 Roadmap

## v0.1 — Current skeleton

Status: scaffolded.

- Conservative Lean scaffold for the matrix spine.
- Exact SymPy checks for `A(λ)`, trace, determinant, characteristic polynomial, square, and branch examples.
- Result artifacts and visualizations generated.
- Claim-status surfaces downgraded so nothing is called `Lean-proved` before a real `lake build`.

## v0.2 — First Lean promotion gate

- Run `lake build` locally or in CI.
- Fix any Lean API/syntax issues.
- Confirm no `sorry` or `admit` in guarded Lean files.
- Promote only successfully built exact matrix claims to `Lean-proved`.

## v0.3 — Eigen-direction bridge

- Add explicit `ℓ+` and `ℓ-` eigenvector/eigendirection statements.
- Keep geometric and physical readings separate from algebraic facts.

## v0.5 — Physical bridge decomposition

Break the paper's final sign thesis into separate bridge claims before any promotion attempt:

1. algebraic split directions;
2. null-vector / light-cone bridge;
3. curvature-to-`Λ` bridge;
4. arrow-of-time orientation bridge.

Only then consider whether any part of `PHYS-01` can move out of `Interpretation`.
