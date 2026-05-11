# Paper / Lean / Notebook Crosswalk

| Paper anchor | Lean target | SymPy artifact | Wolfram / visual surface | Status |
| --- | --- | --- | --- | --- |
| Step 2: translations fail to commute by curvature | `Spacetime/ConstantCurvature.lean` | future bracket artifact | branch funnel panel | Interpretation / scaffold |
| Step 4: general curvature-to-cosmological-constant relation | `Spacetime/SignatureBridge.lean` | `results/lambda_sign_summary.json` | signature bridge panel | Computed here |
| Step 4: four-dimensional `Λ=3λ` and positive-sign arithmetic | `cosmologicalFromCurvature_four`, `cosmologicalFromCurvature_four_positive` | `results/lambda_sign_summary.json` | signature bridge panel | Lean-proved for arithmetic only |
| Step 5: time-evolution matrix on `(K_i,P_i)` plane | `timeEvolutionMatrix` | `results/matrix_oracle_summary.json` | `notebook_preview_time_matrix.svg` target | Lean-proved |
| `trace(A)=0`, `det(A)=-λ`, `charpoly=x²-λ` | `trace_zero`, `det_eq_neg_lambda`, `char_poly` | `results/regression_summary.json` | matrix panel | Lean-proved |
| `A(λ)^2 = λI` | `square_eq_lambda_identity` | `results/time_evolution_summary.json` | matrix panel | Lean-proved |
| Three sign regimes | `positiveBranch_hyperbolicAlgebraic`, `zeroBranch_parabolicAlgebraic`, `negativeBranch_ellipticAlgebraic` | `results/branch_summary.json` | `viz/hyperbolic_flow.png`, `viz/parabolic_flow.png`, `viz/elliptic_flow.png` | Lean-proved for algebraic markers only |
| Step 6: algebraic eigendirections `ℓ+`, `ℓ-` | `ellPlus_eigen`, `ellMinus_eigen`, `ellPlus_ne_ellMinus` | `results/eigendirection_summary.json` | future eigenflow preview | Lean-proved for algebraic eigendirections only |
| Step 6: split quadratic vanishes on `ℓ+`, `ℓ-` | `ellPlus_splitQuadratic_zero`, `ellMinus_splitQuadratic_zero` | `results/null_bridge_summary.json`, `results/invariant_metric_summary.json` | invariant-form preview | Lean-proved for algebraic split form only |
| Step 6: matrix flow scaling on branches | future Lean theorem family | `results/time_flow_summary.json` | flow preview | Computed here |
| Step 6: eigendirections are light rays / horizons | future null-vector bridge theorem family | not asserted as computation | conclusion panel | Interpretation |
| `t>0`, `c>0`, `Λ>0` shared sign thesis | future bridge theorem family | not asserted as computation | conclusion panel | Interpretation |
