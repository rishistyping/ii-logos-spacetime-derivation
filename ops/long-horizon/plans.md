# ExecPlan: v0.6-v1.0 Proof Surface And Repository Development

This is the internal execution control surface. Public roadmap language lives
in `PLANS.md`; current claim authority lives in `docs/claim-status.md`.

## Current Baseline

- v0.5 is shipped; v1.0 is release-ready after green validation.
- `main` is clean and synced.
- Current promoted surface: matrix spine, branch markers, eigendirections,
  split quadratic facts, and four-dimensional Lambda arithmetic.
- Current unpromoted surface: geometric null reading, horizons, redshift, arrow
  orientation, and `PHYS-01`.

## Architecture Approach

- Keep Lean modules small and bridge-specific.
- Add a new module only when it owns a coherent proof packet.
- Add a matching SymPy producer only when a deterministic computed artifact
  helps audit or explain the packet.
- Move truth surfaces together: README, claim status, theorem ledger, crosswalk,
  specs, manifest, build status, and public preview.

## Milestone Table

| Milestone | Scope | Target surfaces | Acceptance criteria | Validation |
| --- | --- | --- | --- | --- |
| v0.6 Proof-surface audit | Inventory possible bridge packets and classify them before proof work. | `docs/claim-status.md`, `docs/theorem-ledger.md`, `spec/claims.yaml`, `PLANS.md` | Adds future rows for `ST-09`, `ST-10`, and `ST-11` without promoting them. | `git diff --check`; truth-boundary scan; `bash scripts/check_all.sh` |
| v0.7 Algebraic split-cone packet | Add a predicate around `splitQuadratic` and prove basic algebraic closure facts only. | `Spacetime/SplitCone.lean`, `sympy/spacetime_split_cone.py`, `results/split_cone_summary.json` | Packet is promoted only as algebra after Lean build and artifact sync. | `lake build`; `bash scripts/check_all.sh`; artifact drift check |
| v0.8 Arithmetic and bracket packets | Strengthen safe dimension arithmetic and symbolic bracket surface. | `Spacetime/SignatureBridge.lean`, `Spacetime/ConstantCurvature.lean`, new SymPy summaries if useful | General Lambda sign claims require explicit assumptions; bracket claims do not claim exhaustiveness. | `lake build`; proof-hole scan; truth-surface check |
| v0.9 Public sync pass | Align reader docs, notebook walkthrough, visual assets, and result manifest. | README, `docs/`, `notebooks/`, `results/manifest.json` | Public surfaces show the same claim statuses and no stale version drift. | README link check; `bash scripts/check_all.sh`; GitHub Actions |
| v1.0 Release readiness | Freeze the promoted theorem surface and release only if validation is green. | `CHANGELOG.md`, `CITATION.cff`, `pyproject.toml`, tag metadata | Version and tag move only after `main` is green; physical thesis remains below proof status unless separately proved. | local full gate; GitHub Python and Lean; tag workflows |

## Future Claim IDs

- `ST-09-SPLIT-CONE`: algebraic cone predicate and closure facts around
  `splitQuadratic`.
- `ST-10-LAMBDA-GENERAL-SIGN`: arithmetic sign bridge for
  `cosmologicalFromCurvature d λ` under explicit assumptions on `d` and `λ`.
- `ST-11-BRACKET-SURFACE`: symbolic bracket antisymmetry/index hygiene and
  surface checks for `[P_a, P_b] = λJ_ab`.

## Verification Checklist

- [ ] `uv sync --frozen`
- [ ] `git diff --check`
- [ ] `python3 -m py_compile docs/assets/render_readme_assets.py scripts/check_truth_surface.py`
- [ ] `bash scripts/check_all.sh`
- [ ] `lake build`
- [ ] proof-hole scan over `Spacetime.lean`, `SpacetimeFull.lean`, and `Spacetime/*.lean`
- [ ] artifact regeneration plus `git diff --exit-code results/ viz/`
- [ ] truth-surface sync across README, docs, specs, manifest, and build status
- [ ] GitHub Actions Python and Lean green before `main` or tags move

## Risk Register

| Risk | Mitigation |
| --- | --- |
| Overclaiming physical interpretation | Keep boundary terms below proof status unless backed by named Lean declarations and synchronized truth surfaces. |
| Truth-surface drift | Run `scripts/check_truth_surface.py` and update all public surfaces in the same commit. |
| Nondeterministic artifacts | Use deterministic stdlib writers where possible; keep artifact drift checks in CI. |
| Lean scope creep | Keep `Mat2` / `Vec2` style and add only packet-sized modules. |
| Version churn | Do not change package/citation version until release-readiness milestone. |

## Implementation Notes

- The first implementation milestone after this planning refresh should be v0.6
  proof-surface audit, not new theorem code.
- If a future packet cannot be proved cleanly, downgrade it to `Computed here`
  or `Interpretation` and record the reason in the theorem ledger.
