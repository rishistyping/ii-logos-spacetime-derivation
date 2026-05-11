# Contributing to ii-logos-spacetime-derivation

This is a **thin verification/explainer repository**. Please keep changes minimal and truth-preserving.

## Guidelines
- Lean is the sole proof authority for algebraic identities.
- Physical interpretations must remain tagged **Interpretation** until bridges are formalized.
- Always update `docs/claim-status.md`, `docs/theorem-ledger.md`, and `docs/paper-lean-notebook-crosswalk.md` together.
- Run the combined validation helper before any PR.
- Follow the exact pattern of `ii-logos-cosmological-constant` and `ii-logos-one-postulate`.

## Workflow
1. Fork or branch from main
2. Make changes in the appropriate layer (Lean / sympy / docs)
3. Update all truth surfaces
4. `uv sync && bash scripts/check_all.sh`
5. Open PR with clear claim impact

Thank you for keeping the record straight.
