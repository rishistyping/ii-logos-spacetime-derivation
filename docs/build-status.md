# Build Status

## Current environment note

This v0.5 truth-surface pass was validated locally on 2026-05-11 with Python 3.11, `uv`, Lean/Lake, and the pinned Lean 4.7.0 toolchain.

The Lean entrypoint is `lakefile.lean` for compatibility with the pinned Lean/Lake release.

This file records validated status. Future execution plans live in
`ops/long-horizon/` and do not change current claim authority by themselves.

## Last local checks recorded during the v0.5 promotion

- Python exact checks: passing
- Python matrix oracle: passing
- Python eigendirection checks: passing
- Python split-null bridge checks: passing
- Python Lambda sign checks: passing
- Python branch-flow scaling checks: passing
- Python invariant-form checks: passing
- Python regression checks: passing
- Python visualization generation: passing
- Artifact manifest and drift checks: passing
- Truth-surface consistency check: passing
- Lean proof-hole scan: passing; no `sorry` or `admit` in `Spacetime.lean`, `SpacetimeFull.lean`, or `Spacetime/*.lean`
- Lean build: passing via `lake build`
- Truth-surface promotion: exact matrix spine, algebraic branch markers, algebraic eigendirections, algebraic split-nullness, and four-dimensional Lambda sign arithmetic promoted to `Lean-proved`; physical bridge claims remain `Interpretation`.

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
