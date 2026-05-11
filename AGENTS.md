# AGENTS.md — For Aristotle / AI Agents / Human Contributors

This repository is deliberately thin and truth-preserving.

## Non-negotiables

- Do not widen theorem packets without updating `docs/claim-status.md`, `docs/theorem-ledger.md`, and `docs/paper-lean-notebook-crosswalk.md`.
- Do not call a claim `Lean-proved` unless `lake build` succeeds and the guarded Lean files contain no `sorry` or `admit`.
- Treat SymPy and Wolfram as computational/explanatory companions, not proof authority.
- Keep physical conclusions tagged `Interpretation` until bridges are explicit.
- Preserve the four evidence tags: `Lean-proved`, `Computed here`, `Imported theorem`, `Interpretation`.

## Current v0.5 focus

The current formalization frontier is bridge decomposition over the already
proved matrix spine:

```text
A(λ), branch markers, algebraic eigendirections, algebraic split-nullness, and four-dimensional Λ sign arithmetic.
```

Do not attempt to prove the full arrow-of-time thesis in one pass.

For long-running work, use the operational control plane in
`ops/long-horizon/`. Public roadmap language still belongs in `PLANS.md`.

## Required checks

```bash
bash scripts/check_all.sh
```

When Lean is available, `lake build` is mandatory before any Lean-promotion edit.
