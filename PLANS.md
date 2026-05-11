# PLANS.md — v0 to v1.0 Roadmap

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

## v0.6 — Proof-surface audit and bridge taxonomy

Status: next execution target.

The next conservative target is a planning and truth-surface audit, not an
immediate physical promotion:

- add future rows for `ST-09-SPLIT-CONE`, `ST-10-LAMBDA-GENERAL-SIGN`, and `ST-11-BRACKET-SURFACE`;
- classify each row as algebra, arithmetic, imported geometry, or interpretation;
- keep the geometric null/light-cone, horizon, redshift, orientation, and shared-sign thesis unpromoted.

The detailed execution control plane lives in `ops/long-horizon/`.

## v0.7 — Algebraic split-cone packet

Status: planned.

- Add an algebraic cone predicate around `splitQuadratic`.
- Prove only closure and equivalence facts that are internal to the existing
  `Vec2` / `Mat2` style.
- Keep geometric readings below proof status until separate theorem support
  exists.

## v0.8 — Arithmetic and bracket packets

Status: planned.

- Strengthen safe general-dimensional Lambda arithmetic under explicit
  assumptions.
- Improve the symbolic constant-curvature bracket surface without claiming full
  Lie-algebra exhaustiveness.
- Add deterministic computed artifacts only where they clarify the audit trail.

## v0.9 — Public sync pass

Status: planned.

- Align README, public preview, notebook walkthrough, generated visuals, result
  manifest, and truth surfaces.
- Remove version/status drift before any v1.0 release candidate.

## v1.0 — Release readiness

Status: planned.

- Freeze the promoted theorem surface.
- Run local and GitHub validation gates.
- Move package/citation version and release tag only after `main` is green.
