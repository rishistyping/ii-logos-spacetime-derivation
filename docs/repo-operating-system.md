# Repo Operating System

This repository follows the One Postulate / Cosmological Constant companion pattern with stricter v0 truth discipline.

## Truth surfaces

Keep these synchronized:

```text
README.md
docs/claim-status.md
docs/theorem-ledger.md
docs/paper-lean-notebook-crosswalk.md
docs/notebooks.md
docs/build-status.md
spec/claims.yaml
spec/equations.yaml
results/manifest.json
ops/long-horizon/*.md
```

## Evidence lanes

- Lean: intended proof authority after `lake build` succeeds.
- SymPy: exact computational oracle and artifact generator.
- Wolfram: public explainer and visualization companion.
- Docs/specs: proof-boundary and crosswalk surfaces.

## Promotion checklist

Before any claim is promoted to `Lean-proved`:

- [ ] `lake build` succeeds.
- [ ] `rg -n '\bsorry\b|\badmit\b' Spacetime.lean SpacetimeFull.lean Spacetime/*.lean` returns no proof holes.
- [ ] `python sympy/spacetime_regression_check.py` passes.
- [ ] `docs/claim-status.md` is updated.
- [ ] `docs/theorem-ledger.md` is updated.
- [ ] `spec/claims.yaml` is updated.
- [ ] `docs/build-status.md` records the validation.

## Operational control plane

`PLANS.md` remains the public roadmap. The larger incremental build plan is
tracked under `ops/long-horizon/`:

- `prompt.md`: mission, non-goals, and authority order.
- `plans.md`: execution waves.
- `implement.md`: implementation state and merge discipline.
- `documentation.md`: truth-surface sync requirements.

## Current v0.5 live frontier

The current frontier is not a broad physical proof. It is the narrow matrix spine:

```text
A(λ), trace, determinant, characteristic polynomial, square, sign-regime classification, algebraic eigendirections, algebraic split-nullness, and four-dimensional Lambda sign arithmetic.
```

The final physical arrow-of-time sign thesis remains interpretation until bridge theorems are separately encoded.
