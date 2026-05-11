# Claim Status

This board is the canonical human-readable summary of what is proved, computed, imported, and interpreted.

## Allowed Tags

- `Lean-proved`
- `Computed here`
- `Imported theorem`
- `Interpretation`

## Current v0.5 Status

- The repository is a conservative verification/explainer companion.
- The exact `A(λ)` matrix spine is `Lean-proved`.
- The algebraic sign-branch markers that build in Lean are `Lean-proved`.
- The positive-branch algebraic eigendirections are `Lean-proved`.
- The split-quadratic bridge for those eigendirections is `Lean-proved`.
- The four-dimensional `Λ = 3λ` and positive-sign arithmetic bridge is `Lean-proved`.
- SymPy remains the exact computational companion and artifact generator.
- The final physical sign thesis remains `Interpretation`.

## Status Board

| Claim | Status | Where It Lives |
| --- | --- | --- |
| Constant-curvature translation-bracket model `[P_a, P_b] = λJ_ab` as the paper's algebraic surface | Interpretation | `paper/`, `Spacetime/ConstantCurvature.lean` scaffold |
| `A(λ) = [[0,-λ],[-1,0]]` exact time-evolution matrix | Lean-proved | `Spacetime/TimeEvolutionMatrix.lean::timeEvolutionMatrix`, `sympy/spacetime_exact_checks.py`, `results/time_evolution_summary.json` |
| `trace(A)=0`, `det(A)=-λ`, `charpoly(A)=x²-λ` | Lean-proved | `Spacetime/TimeEvolutionMatrix.lean::trace_zero`, `det_eq_neg_lambda`, `char_poly`; `sympy/spacetime_regression_check.py`, `results/regression_summary.json` |
| `A(λ)^2 = λI` | Lean-proved | `Spacetime/TimeEvolutionMatrix.lean::square_eq_lambda_identity`, `sympy/spacetime_exact_checks.py`, `results/time_evolution_summary.json` |
| `λ>0` branch has negative determinant and satisfies the hyperbolic algebraic marker | Lean-proved | `Spacetime/TimeEvolutionMatrix.lean::positive_branch_det_negative`, `Spacetime/SignVerdict.lean::positiveBranch_hyperbolicAlgebraic`; `results/branch_summary.json` records the split-root explainer artifact |
| `λ=0` branch has square-zero/parabolic algebraic matrix behavior | Lean-proved | `Spacetime/TimeEvolutionMatrix.lean::zero_branch_square_zero`, `Spacetime/SignVerdict.lean::zeroBranch_parabolicAlgebraic`; `results/branch_summary.json` |
| `λ<0` branch has positive determinant, zero trace, and satisfies the elliptic algebraic marker | Lean-proved | `Spacetime/TimeEvolutionMatrix.lean::negative_branch_det_positive`, `trace_zero`, `Spacetime/SignVerdict.lean::negativeBranch_ellipticAlgebraic`; `results/branch_summary.json` |
| For `λ≥0`, `ℓ+ = (-√λ,1)` and `ℓ- = (√λ,1)` are nonzero eigenvectors with eigenvalues `√λ` and `-√λ`; for `λ>0` they are distinct | Lean-proved | `Spacetime/EigenDirections.lean::ellPlus_eigen`, `ellMinus_eigen`, `ellPlus_nonzero`, `ellMinus_nonzero`, `ellPlus_ne_ellMinus`; `sympy/spacetime_eigendirections.py`, `results/eigendirection_summary.json` |
| For `λ≥0`, `ℓ+` and `ℓ-` vanish against `Q(k,p)=k²-λp²`, and `Q(rv)=r²Q(v)` | Lean-proved | `Spacetime/NullBridge.lean::splitQuadratic`, `splitQuadratic_scale`, `ellPlus_splitQuadratic_zero`, `ellMinus_splitQuadratic_zero`; `sympy/spacetime_null_bridge.py`, `results/null_bridge_summary.json` |
| Sphere compactness / finiteness bridge | Imported theorem | future `Spacetime/SignatureBridge.lean` bridge or documentation |
| Wick-rotation / Lorentzian signature bridge as a physical reading | Interpretation | `docs/reader-guide.md`, `docs/proof-visuals.md` |
| General `Λ = 1/2(d-1)(d-2)λ` relation | Computed here | `sympy/spacetime_lambda_sign.py`, `results/lambda_sign_summary.json` |
| In four spacetime dimensions, `Λ=3λ`; if `λ>0`, then `Λ>0` | Lean-proved | `Spacetime/SignatureBridge.lean::cosmologicalFromCurvature_four`, `cosmologicalFromCurvature_four_positive`; `sympy/spacetime_lambda_sign.py`, `results/lambda_sign_summary.json` |
| `ST-09-SPLIT-CONE`: cone-closure packet for `Q(k,p)=k²-λp²` is `Lean-proved` on the algebraic split form | Lean-proved | `Spacetime/NullConeSplit.lean`, `results/split_cone_summary.json` |
| `ST-10-LAMBDA-GENERAL-SIGN`: safe general-dimensional `Λ` arithmetic bridge with explicit assumptions is `Lean-proved` | Lean-proved | `Spacetime/SignatureBridge.lean` |
| `ST-11-BRACKET-SURFACE`: constant-curvature bracket-surface hygiene and algebraic split rules are `Lean-proved` | Lean-proved | `Spacetime/ConstantCurvature.lean`, `results/bracket_surface_summary.json` |
| Eigenspaces are null/light-cone directions | Interpretation | Step 6 of the paper; bridge theorem pending |
| `t>0`, `c>0`, and `Λ>0` share the same sign | Interpretation | paper conclusion; formal bridges pending |
| Full arrow-of-time conclusion | Interpretation | paper conclusion; formal bridges pending |

## Discipline

- Do not add a fifth status tag.
- Do not call a scaffolded Lean statement `Lean-proved` unless a real `lake build` is recorded and all truth surfaces are updated together.
- Treat SymPy and Wolfram as exact/explanatory companions, not proof authority.
- Keep physical conclusions separate from algebraic matrix identities.
- Do not read the `Lean-proved` matrix and branch rows as proof of the later physical bridge claims.
