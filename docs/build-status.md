# Build Status

## Current environment note

This v0 skeleton was validated locally on 2026-05-11 with Python 3.11, `uv`, Lean/Lake, and the pinned Lean 4.7.0 toolchain.

The Lean entrypoint is `lakefile.lean` for compatibility with the pinned Lean/Lake release.

## Last local checks recorded during this skeleton patch

- Python exact checks: passing
- Python matrix oracle: passing
- Python regression checks: passing
- Python visualization generation: passing
- Lean proof-hole scan: passing; no `sorry` or `admit` in `Spacetime.lean`, `SpacetimeFull.lean`, or `Spacetime/*.lean`
- Lean build: passing via `lake build`

## Commands

```bash
bash scripts/check_all.sh
```

When Lean is available, record the output of:

```bash
lake build
rg -n '\bsorry\b|\badmit\b' Spacetime.lean SpacetimeFull.lean Spacetime/*.lean
```

Only after that gate is green should rows move to `Lean-proved`.
