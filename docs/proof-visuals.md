# Proof Visuals

The skeletal visual layer should compress the argument without adding proof authority.

## Current assets

- `docs/public-reader-preview.md`
- `viz/hyperbolic_flow.png`
- `viz/parabolic_flow.png`
- `viz/elliptic_flow.png`

The `viz/` images are generated from `sympy/spacetime_visualize.py` and illustrate the three regimes of the exact matrix

```text
A(λ) = [[0, -λ], [-1, 0]].
```

The public reader preview combines those images with Mermaid diagrams and visible truth tags. It does not add proof authority.

The v0.5 computed artifact layer also includes split-null, Lambda-sign,
branch-flow, and invariant-form JSON summaries in `results/`. Those files are
audit trails for the visual narrative, not physical proof objects.

## Target v1 assets

- `wolfram/assets/notebook_hero_overview.svg`
- `wolfram/assets/notebook_preview_branches.svg`
- `wolfram/assets/notebook_preview_time_matrix.svg`
- `wolfram/assets/notebook_preview_eigenflow.svg`
- `wolfram/assets/notebook_preview_crosswalk.svg`

## Boundary

Visuals are not proof objects. They are `Computed here` or `Interpretation` surfaces, depending on the row in `docs/claim-status.md`.
