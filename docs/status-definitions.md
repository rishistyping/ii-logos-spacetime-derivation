# Status Definitions

This repository uses exactly four claim-status tags.

| Tag | Meaning |
| --- | --- |
| `Lean-proved` | The claim is encoded in Lean, the repository builds with `lake build`, and no `sorry`/`admit` occurs in the guarded Lean surface. |
| `Computed here` | The claim is generated or checked by a repository-local computational artifact, usually SymPy or Wolfram. This is not proof authority. |
| `Imported theorem` | The claim is a standard external mathematical or geometric fact accepted as an input rather than proved in this repository. |
| `Interpretation` | The claim is a paper-level physical, philosophical, or explanatory reading above the formal surface. |

## Lifecycle terms

Development terms such as `scaffolded`, `planned`, `reviewed`, or `pending Lean` are not claim-status tags. They may appear in prose, but the status table must use only the four tags above.

## Promotion rule

A claim moves to `Lean-proved` only after:

1. the relevant Lean theorem exists;
2. `lake build` succeeds locally or in CI;
3. the guarded Lean files contain no `sorry` or `admit`;
4. `docs/claim-status.md`, `docs/theorem-ledger.md`, and `spec/claims.yaml` are updated together.
