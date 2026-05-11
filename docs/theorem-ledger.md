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
- `cosmologicalFromCurvature_four_positive`

Status: `Lean-proved` for four-dimensional arithmetic only: `Λ=3λ` and `λ>0 -> Λ>0`.

The general geometric compactness/finiteness bridge remains `Imported theorem`, and
Wick-rotation / Lorentzian signature interpretation remains `Interpretation`.

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

## ST-06 — Algebraic eigendirections

Lean file: `Spacetime/EigenDirections.lean`

Target surfaces:

- `Vec2`
- `Vec2.zero`
- `Vec2.scale`
- `Vec2.ext`
- `Mat2.mulVec`
- `ellPlus`
- `ellMinus`
- `ellPlus_nonzero`
- `ellMinus_nonzero`
- `ellPlus_eigen`
- `ellMinus_eigen`
- `ellPlus_ne_ellMinus`

Status: `Lean-proved` for algebraic eigenvector/eigendirection facts only.

Physical null-vector/light-cone, redshift, horizon, and arrow-of-time readings remain `Interpretation`.

## ST-07 — Algebraic split-null bridge

Lean file: `Spacetime/NullBridge.lean`

Target surfaces:

- `splitQuadratic`
- `IsSplitNull`
- `splitQuadratic_scale`
- `ellPlus_splitQuadratic_zero`
- `ellMinus_splitQuadratic_zero`
- `ellPlus_isSplitNull`
- `ellMinus_isSplitNull`

Status: `Lean-proved` for algebraic split-quadratic facts only.

Physical light-ray and horizon readings remain `Interpretation`.

## ST-08 — Four-dimensional Lambda sign bridge

Lean file: `Spacetime/SignatureBridge.lean`

Target surfaces:

- `cosmologicalFromCurvature_four`
- `cosmologicalFromCurvature_four_positive`

Status: `Lean-proved` for the four-dimensional arithmetic bridge only.

Observed cosmological interpretation and the full shared-sign thesis (`t>0,c>0,Λ>0`) remain `Interpretation`.

## ST-09 — Split-cone packet

Lean file: `Spacetime/NullConeSplit.lean`

Target surfaces:

- `splitCone`
- `splitCone_scale`
- `splitCone_ellPlus_zero`
- `splitCone_ellMinus_zero`

Status: `Lean-proved` for algebraic split-cone closure under scaling and `ellPlus`/`ellMinus` membership.

## ST-10 — General Lambda sign bridge

Lean file: `Spacetime/SignatureBridge.lean`

Target surfaces:

- `cosmologicalFromCurvature`
- `cosmologicalFromCurvature_general`
- `cosmologicalFromCurvature_nonneg_of_nonneg`
- `cosmologicalFromCurvature_positive_of_positive`

Status: `Lean-proved` for the explicit-assumption packet:
`cosmologicalFromCurvature_general`, `cosmologicalFromCurvature_nonneg_of_nonneg`,
`cosmologicalFromCurvature_positive_of_positive`. No physical sign thesis is promoted.

## ST-11 — Bracket-surface strengthening

Lean file: `Spacetime/ConstantCurvature.lean`

Target surfaces:

- `translationBracket`
- `translationBracket_coeff`
- `translationBracket_generator`
- `translationBracket_scale`

Status: `Lean-proved` for coefficient/generator hygiene lemmas:
`translationBracket_scale`, `translationBracket_zero`, `translationBracket_stable_structure`.
No full Lie-algebra exhaustiveness claim is introduced.
