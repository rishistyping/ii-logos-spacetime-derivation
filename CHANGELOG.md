# Changelog

## v1.0.0 - 2026-05-11

- Completed the v0.9 proof-surface sync for release readiness.
- Added `ST-09`, `ST-10`, and `ST-11` Lean/Harmonic-independent algebraic packets and synchronized every public proof surface.
- Added deterministic SymPy companion artifacts `split_cone_summary.json` and `bracket_surface_summary.json`.
- Updated `results/manifest.json` and check pipeline to enforce deterministic artifact registration and drift checks.
- Revalidated the full gate (`check_all`) and aligned repository versioning for the first public release candidate.

## v0.5.0 - 2026-05-11

- Added the v0.5 bridge-decomposition control plane.
- Split local and CI validation into Python, artifact, truth-surface, and Lean gates.
- Added Lean proofs for algebraic split-nullness of `ellPlus` and `ellMinus`.
- Added a Lean proof that, in four dimensions, positive `lambda` gives positive symbolic `Lambda`.
- Added deterministic computed artifacts for split-nullness, Lambda sign, branch flow, and invariant form.
- Synchronized public truth surfaces while keeping physical light-cone, horizon, redshift, arrow-of-time, and shared-sign claims interpretive.
