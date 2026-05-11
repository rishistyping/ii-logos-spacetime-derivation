# v0.5 Implementation Log

Use this file for concise implementation state. It should describe what changed,
what remains, and which validation gate owns the next decision.

## Current Scope

- `Spacetime/NullBridge.lean` owns algebraic split-null proofs.
- `Spacetime/SignatureBridge.lean` owns the four-dimensional Lambda sign proof.
- `sympy/` owns deterministic computed artifacts.
- `scripts/check_*.sh` and `scripts/check_truth_surface.py` own validation.
- `docs/` and `spec/` own public truth surfaces.

## Merge Discipline

- Keep implementation commits small enough to audit.
- Run `git diff --check` before every commit.
- Run `bash scripts/check_all.sh` before publishing.
- Do not tag `v0.5.0` until local checks and GitHub Actions are green.

## Proof Boundary

The v0.5 release may say that algebraic split-nullness and the four-dimensional
Lambda sign bridge are Lean-proved. It may not say that physical light rays,
horizons, redshift, arrow of time, or the shared-sign thesis are Lean-proved.
