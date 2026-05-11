# PLANS.md — v0 to v0.5 Roadmap

## v0.1 — Initial public skeleton

Status: complete.

- Conservative Lean scaffold for the matrix spine.
- Exact SymPy checks for `A(λ)`, trace, determinant, characteristic polynomial, square, and branch examples.
- Result artifacts and visualizations generated.
- Claim-status surfaces downgraded so nothing was called `Lean-proved` before a real `lake build`.

## v0.2 — Lean matrix spine promoted

Status: complete.

- `lake build` passes locally and in CI.
- Exact time-evolution matrix claims promoted to `Lean-proved`.
- Algebraic sign-branch marker claims promoted to `Lean-proved`.
- Constant-curvature exhaustiveness, compactness/finiteness, Wick rotation, null/light-cone bridges, and arrow-of-time claims remain unpromoted.
- The physical sign thesis remains `Interpretation`.

## v0.3 — Eigen-direction bridge

Status: complete.

- Add explicit `ℓ+` and `ℓ-` eigenvector/eigendirection statements.
- Add SymPy artifacts for eigenvectors.
- Crosswalk the result to Step 6 of the paper.
- Keep geometric and physical readings separate from algebraic facts.

## v0.4 — Public reader preview

Status: complete.

- Improve public reader experience with a generated notebook preview or lightweight docs page.
- Do not add an interactive web companion yet.
- Keep truth-surface tags visible near any rendered explainer content.

## v0.5 — Physical bridge decomposition

Status: complete.

The paper's final sign thesis is now decomposed into smaller public bridge
claims. Two narrow algebra/arithmetic bridges are promoted; the physical thesis
itself remains interpretive.

1. algebraic split directions: `Lean-proved` as split-quadratic facts;
2. null-vector / light-cone bridge: still `Interpretation`;
3. curvature-to-`Λ` bridge: four-dimensional `Λ = 3λ` and positive-sign arithmetic are `Lean-proved`;
4. arrow-of-time orientation bridge: still `Interpretation`.

Operational control for this build lives in `ops/long-horizon/`.

## v0.6 — Geometric bridge packets

Status: next.

The next conservative target is to decide whether any geometric bridge can be
encoded without promoting the final physical thesis:

- split form to geometric null cone;
- de Sitter horizon interpretation;
- redshift/orientation bridge;
- precise statement of what remains imported versus interpreted.
