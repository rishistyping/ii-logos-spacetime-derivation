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

## ExecPlan control plane

`PLANS.md` remains the public roadmap. The v0.6-v1.0 execution plan is tracked
under `ops/long-horizon/`, which is the repository's ExecPlan surface:

- `prompt.md`: mission, hard requirements, target packets, and proof boundary.
- `plans.md`: milestone table, risk register, validation checklist, and future claim IDs.
- `implement.md`: execution contract, validation discipline, and merge rules.
- `documentation.md`: operator runbook, repo map, setup, verification, and release checklist.

## Current v1.0 live frontier

The current frontier is not a broad physical proof. It is the narrow matrix and bridge spine:

```text
A(λ), trace, determinant, characteristic polynomial, square, sign-regime classification, algebraic eigendirections, algebraic split-nullness, ST-09 split-cone closure, ST-10 general Lambda sign arithmetic, ST-11 bracket-surface hygiene, and four-dimensional Lambda sign arithmetic.
```

The final physical arrow-of-time sign thesis remains interpretation until bridge theorems are separately encoded.
