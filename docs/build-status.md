# Build Status

## Current environment note

This v0.3 truth-surface pass was validated locally on 2026-05-11 with Python 3.11, `uv`, Lean/Lake, and the pinned Lean 4.7.0 toolchain.

The Lean entrypoint is `lakefile.lean` for compatibility with the pinned Lean/Lake release.

## Last local checks recorded during the v0.3 promotion

- Python exact checks: passing
- Python matrix oracle: passing
- Python eigendirection checks: passing
- Python regression checks: passing
- Python visualization generation: passing
- Lean proof-hole scan: passing; no `sorry` or `admit` in `Spacetime.lean`, `SpacetimeFull.lean`, or `Spacetime/*.lean`
- Lean build: passing via `lake build`
- Truth-surface promotion: exact matrix spine, algebraic branch markers, and algebraic eigendirections promoted to `Lean-proved`; physical bridge claims remain `Interpretation`.

## Commands

```bash
bash scripts/check_all.sh
```

When Lean is available, record the output of:

```bash
lake build
rg -n '\bsorry\b|\badmit\b' Spacetime.lean SpacetimeFull.lean Spacetime/*.lean
```

Future promotions must rerun this gate before any additional rows move to `Lean-proved`.
