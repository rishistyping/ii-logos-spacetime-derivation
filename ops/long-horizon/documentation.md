# ExecPlan Documentation Runbook

This runbook summarizes how to operate the repository during the v0.6-v1.0
proof-surface program.

## Project

`ii-logos-spacetime-derivation` is a public verification and explainer
companion to *A Brief Derivation of Spacetime*.

The current v1.0 proof surface promotes:

- exact time-evolution matrix identities;
- algebraic sign-branch markers;
- algebraic eigendirections;
- algebraic split-quadratic facts;
- four-dimensional Lambda arithmetic.

The following remain below proof status:

- geometric null interpretation;
- horizons and redshift;
- arrow orientation;
- `PHYS-01` shared-sign thesis.

## Local Setup

```bash
uv sync --frozen
```

Optional notebook dependencies:

```bash
uv sync --extra notebooks
```

## Verification Commands

```bash
git diff --check
python3 -m py_compile docs/assets/render_readme_assets.py scripts/check_truth_surface.py
bash scripts/check_all.sh
```

For proof milestones, also record:

```bash
lake build
rg -n '\bsorry\b|\badmit\b' Spacetime.lean SpacetimeFull.lean Spacetime/*.lean
```

## Repository Structure

```text
paper/                    Paper source and PDF
Spacetime/                Lean proof-surface modules
sympy/                    Deterministic computed companion scripts
results/                  JSON artifacts and manifest
viz/                      Deterministic visual artifacts
docs/                     Human-readable truth surfaces and guides
docs/assets/              README visual assets and renderer
spec/                     Machine-readable claims, equations, symbols
scripts/                  Local validation gates
ops/long-horizon/         ExecPlan control plane
```

## Planned Packets

- `ST-09-SPLIT-CONE`: algebraic cone predicate around `splitQuadratic`.
- `ST-10-LAMBDA-GENERAL-SIGN`: general-dimensional arithmetic sign bridge with
  explicit assumptions.
- `ST-11-BRACKET-SURFACE`: symbolic bracket-surface strengthening without
  exhaustiveness claims.

## Release Checklist

- Local full gate passes.
- Public truth surfaces are synchronized.
- `results/manifest.json` includes every committed artifact.
- GitHub Actions Python and Lean pass on the feature branch.
- `main` is updated only from a green branch.
- Release tag is created only after `main` is green.

## Troubleshooting

- If artifact drift appears, rerun the relevant producer and inspect whether the
  writer is deterministic across platforms.
- If truth-surface checks fail, inspect the exact line and separate algebraic
  proof language from physical interpretation language.
- If Lean proof work grows beyond a packet-sized module, split the milestone
  before continuing.
