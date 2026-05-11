# Theorem Ledger

This is a target ledger for the Lean scaffold. It is not a claim-promotion board; see `docs/claim-status.md` for current authority status.

## ST-01 — Basic algebraic data

Lean file: `Spacetime/Basic.lean`

Target surfaces:

- `Branch`
- `classifyBranch`
- `Mat2`
- `Mat2.trace`
- `Mat2.det`
- `Mat2.charpoly`
- `Mat2.mul`
- `Mat2.scalar`

Status: build-validated support surface; not a standalone promoted paper claim.

## ST-02 — Constant-curvature bracket surface

Lean file: `Spacetime/ConstantCurvature.lean`

Target surfaces:

- `Generator`
- `BracketTerm`
- `translationBracket`
- `translationBracket_coeff`
- `translationBracket_generator`

Status: scaffolded model of the paper surface, not full Lie-algebra exhaustiveness.

## ST-03 — Signature bridge

Lean file: `Spacetime/SignatureBridge.lean`

Target surfaces:

- `SignatureModel`
- `cosmologicalFromCurvature`
- `cosmologicalFromCurvature_four`

Status: symbolic scaffold. Geometric compactness and Wick-rotation readings remain `Imported theorem` / `Interpretation`.

## ST-04 — Time-evolution matrix

Lean file: `Spacetime/TimeEvolutionMatrix.lean`

Target surfaces:

- `timeEvolutionMatrix`
- `trace_zero`
- `det_eq_neg_lambda`
- `char_poly`
- `square_eq_lambda_identity`
- `zero_branch_square_zero`
- `positive_branch_det_negative`
- `negative_branch_det_positive`

Status: `Lean-proved` for the exact v0.2 matrix spine. This promotion covers the definition of `A(λ)`, trace, determinant, characteristic polynomial, square identity, and determinant/square branch facts only.

## ST-05 — Sign verdict boundary

Lean file: `Spacetime/SignVerdict.lean`

Target surfaces:

- `HyperbolicAlgebraic`
- `ParabolicAlgebraic`
- `EllipticAlgebraic`
- `positiveBranch_hyperbolicAlgebraic`
- `zeroBranch_parabolicAlgebraic`
- `negativeBranch_ellipticAlgebraic`

Status: `Lean-proved` for algebraic branch markers only. Physical sign thesis remains `Interpretation`.
