# v0.5 Execution Plans

This file is the internal execution control surface. Public roadmap language
lives in `PLANS.md`.

## Wave v0.4.1 - Reliability Baseline

- Add operational control docs under `ops/long-horizon/`.
- Split validation into Python, Lean, artifact, and truth-surface gates.
- Harden CI with read-only permissions, concurrency, timeouts, frozen `uv`
  sync, artifact drift checks, and truth-surface checks.

## Wave v0.5.1 - Claim Decomposition

- Add explicit public claim rows for:
  - `ST-07-SPLIT-NULL`
  - `ST-08-LAMBDA-SIGN`
- Keep physical bridge readings interpretive.

## Wave v0.5.2 - Null Algebra Bridge

- Add `Spacetime/NullBridge.lean`.
- Prove algebraic split-nullness of `ellPlus` and `ellMinus`.
- Generate `results/null_bridge_summary.json`.

## Wave v0.5.3 - Lambda Sign Bridge

- Extend `Spacetime/SignatureBridge.lean`.
- Prove the four-dimensional sign bridge
  `0 < lambda -> 0 < cosmologicalFromCurvature 4 lambda`.
- Generate `results/lambda_sign_summary.json`.

## Wave v0.5.4 - Flow and Invariant Artifacts

- Generate deterministic summaries for branch flow scaling and the invariant
  split quadratic form.
- Upgrade `results/manifest.json` to schema v2.

## Wave v0.5.5 - Truth-Surface Sync and Release

- Synchronize README, docs, specs, build status, and release notes.
- Run the final local validation gate.
- Push only after the integration branch is green.
