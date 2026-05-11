# AGENTS.md — For Aristotle / AI Agents / Human Contributors

This repository is deliberately thin and truth-preserving.

## Non-negotiables

- Do not widen theorem packets without updating `docs/claim-status.md`, `docs/theorem-ledger.md`, and `docs/paper-lean-notebook-crosswalk.md`.
- Do not call a claim `Lean-proved` unless `lake build` succeeds and the guarded Lean files contain no `sorry` or `admit`.
- Treat SymPy and Wolfram as computational/explanatory companions, not proof authority.
- Keep physical conclusions tagged `Interpretation` until bridges are explicit.
- Preserve the four evidence tags: `Lean-proved`, `Computed here`, `Imported theorem`, `Interpretation`.

## Current v0 focus

The current formalization frontier is the narrow matrix spine:

```text
A(λ), trace, determinant, characteristic polynomial, A² = λI, and branchwise determinant facts.
```

Do not attempt to prove the full arrow-of-time thesis in one pass.

## Required checks

```bash
bash scripts/check_all.sh
```

When Lean is available, `lake build` is mandatory before any Lean-promotion edit.
