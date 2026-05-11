# Claim Status

This board is the canonical human-readable summary of what is proved, computed, imported, and interpreted.

## Allowed Tags

- `Lean-proved`
- `Computed here`
- `Imported theorem`
- `Interpretation`

## Current v0 Status

- The repository is a verification/explainer skeleton.
- The central `A(λ)` matrix identities are checked by SymPy and build in Lean.
- Rows remain conservative in v0; any `Lean-proved` promotion must update all truth surfaces together.
- The final physical sign thesis remains `Interpretation`.

## Status Board

| Claim | Status | Where It Lives |
| --- | --- | --- |
| Constant-curvature translation-bracket model `[P_a, P_b] = λJ_ab` as the paper's algebraic surface | Interpretation | `paper/`, `Spacetime/ConstantCurvature.lean` scaffold |
| `A(λ) = [[0,-λ],[-1,0]]` exact time-evolution matrix | Computed here | `sympy/spacetime_exact_checks.py`, `results/time_evolution_summary.json`, `Spacetime/TimeEvolutionMatrix.lean` scaffold |
| `trace(A)=0`, `det(A)=-λ`, `charpoly(A)=x²-λ` | Computed here | `sympy/spacetime_regression_check.py`, `results/regression_summary.json`, `Spacetime/TimeEvolutionMatrix.lean` scaffold |
| `A(λ)^2 = λI` | Computed here | `sympy/spacetime_exact_checks.py`, `results/time_evolution_summary.json`, `Spacetime/TimeEvolutionMatrix.lean` scaffold |
| `λ>0` branch has negative determinant and real split polynomial roots | Computed here | `sympy/spacetime_matrix_oracle.py`, `results/branch_summary.json` |
| `λ=0` branch has nilpotent/parabolic matrix behavior | Computed here | `sympy/spacetime_matrix_oracle.py`, `results/branch_summary.json` |
| `λ<0` branch has positive determinant, zero trace, and elliptic explainer behavior | Computed here | `sympy/spacetime_matrix_oracle.py`, `results/branch_summary.json` |
| Sphere compactness / finiteness bridge | Imported theorem | future `Spacetime/SignatureBridge.lean` bridge or documentation |
| Wick-rotation / Lorentzian signature bridge as a physical reading | Interpretation | `docs/reader-guide.md`, `docs/proof-visuals.md` |
| `Λ = 1/2(d-1)(d-2)λ`, with `Λ=3λ` in four spacetime dimensions | Computed here | `sympy/spacetime_exact_checks.py`, `Spacetime/SignatureBridge.lean` scaffold |
| `t>0`, `c>0`, and `Λ>0` share the same sign | Interpretation | paper conclusion; formal bridges pending |
| Full arrow-of-time conclusion | Interpretation | paper conclusion; formal bridges pending |

## Discipline

- Do not add a fifth status tag.
- Do not call a scaffolded Lean statement `Lean-proved` unless a real `lake build` is recorded and all truth surfaces are updated together.
- Treat SymPy and Wolfram as exact/explanatory companions, not proof authority.
- Keep physical conclusions separate from algebraic matrix identities.
