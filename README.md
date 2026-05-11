# A Brief Derivation of Spacetime

[![Lean](https://img.shields.io/badge/Lean-v0.3%20proved-blue)](https://lean-lang.org/)
[![SymPy](https://img.shields.io/badge/SymPy-exact%20checks-green)](https://www.sympy.org/)
[![Wolfram](https://img.shields.io/badge/Wolfram-notebook%20plan-orange)](https://www.wolfram.com/wolfram-engine/)
[![License](https://img.shields.io/badge/license-Apache--2.0%20%2B%20CC--BY--4.0-15803d)](LICENSE)

This repository is a thin, truth-preserving verification and explainer companion to *A Brief Derivation of Spacetime*.

Lean is the intended proof authority for exact algebraic and matrix identities. SymPy and Wolfram are computational and explanatory companions. Physical interpretations such as the arrow of time and the shared sign of `t`, `c`, and `Λ` remain tagged as `Interpretation` until each bridge is separately formalized.

## Current status

This is a **v0.3 verification skeleton**. The exact matrix spine, algebraic branch markers, and positive-branch algebraic eigendirections have been promoted to `Lean-proved` after `lake build`; physical interpretations remain `Interpretation`.

The current `Lean-proved` matrix spine is:

```text
A(λ) = [[0, -λ],
        [-1,  0]]

trace(A)    = 0
det(A)      = -λ
charpoly(A) = x² - λ
A(λ)²       = λ I
```

The current branch surface is:

| Branch | Lean-proved algebraic fact | Notebook / explainer reading |
| --- | --- | --- |
| `λ > 0` | `det(A) < 0` and the hyperbolic algebraic marker holds | SymPy records real split roots; hyperbolic flow |
| `λ = 0` | `A² = 0` | parabolic / nilpotent limit |
| `λ < 0` | `det(A) > 0`, `trace(A)=0`, and the elliptic algebraic marker holds | elliptic flow |

The current `Lean-proved` eigendirection bridge is algebraic only:

```text
ℓ+ = (-√λ, 1),  A(λ)ℓ+ =  √λ ℓ+    for λ ≥ 0
ℓ- = ( √λ, 1),  A(λ)ℓ- = -√λ ℓ-    for λ ≥ 0
```

For `λ > 0`, Lean also proves `ℓ+ ≠ ℓ-`. The claim that these eigendirections are null/light-cone directions remains `Interpretation`.

## Choose your path

- Paper: [`paper/`](paper/)
- Lean scaffold: [`Spacetime/`](Spacetime/) and [`Spacetime.lean`](Spacetime.lean)
- SymPy exact checks: [`sympy/`](sympy/)
- Wolfram notebook plan: [`wolfram/`](wolfram/)
- Colab-style notebook stub: [`notebooks/spacetime_sympy_colab.ipynb`](notebooks/spacetime_sympy_colab.ipynb)
- Claim status and crosswalks: [`docs/`](docs/)
- Generated result artifacts: [`results/`](results/)
- Visual assets: [`viz/`](viz/)

## Authority model

The repository uses the same four evidence tags as the One Postulate and Cosmological Constant companion repositories:

- `Lean-proved`: only after a successful `lake build` with no proof holes.
- `Computed here`: exact symbolic/computational artifacts generated inside this repository.
- `Imported theorem`: standard outside mathematical/geometric facts accepted as external inputs.
- `Interpretation`: paper-level physical or philosophical readings above the theorem surface.

See [`docs/status-definitions.md`](docs/status-definitions.md) and [`docs/claim-status.md`](docs/claim-status.md).

## Reproduce the current skeleton checks

```bash
uv sync
bash scripts/check_all.sh
```

The combined helper runs the SymPy exact/eigendirection checks, regenerates the
JSON and visual artifacts, scans Lean files for proof holes, and runs
`lake build` when Lean/Lake is installed.

If you are not using `uv`, install the core Python dependencies from
`requirements.txt` and run the same helper.

The notebook dependency surface is optional:

```bash
uv sync --extra notebooks
```

If Lean is unavailable, the helper records that the Lean gate was skipped rather
than supporting additional theorem promotion.

## Build map

```text
paper/                    Paper source and PDF
Spacetime/                Lean scaffold modules
Spacetime.lean            Guarded root
SpacetimeFull.lean        Full-paper interpretation root
sympy/                    Exact symbolic scripts and regression checks
results/                  JSON result artifacts and manifest
viz/                      Generated branch-flow figures
wolfram/                  Notebook plan and builder stub
notebooks/                Python/SymPy notebook stub
docs/                     Claim ledger, theorem ledger, crosswalks, guides
spec/                     Machine-readable claim/equation/symbol specs
scripts/                  Local reproducibility helpers
.github/workflows/        CI skeletons
```

## Release discipline

Before any additional exact claim is promoted to `Lean-proved`, update these surfaces together:

```text
docs/claim-status.md
docs/theorem-ledger.md
docs/paper-lean-notebook-crosswalk.md
spec/claims.yaml
spec/equations.yaml
docs/build-status.md
README.md
```

The final physical sentence — that `t > 0`, `c > 0`, and `Λ > 0` share the same sign — remains `Interpretation` in v0.3.
