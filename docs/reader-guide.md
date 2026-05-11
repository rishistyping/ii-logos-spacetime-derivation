# Reader Guide

This repository is a compact companion to *A Brief Derivation of Spacetime*.

## Fast path

1. Read the paper PDF in `paper/`.
2. Read `docs/public-reader-preview.md` for the public-facing explanation.
3. Read the current status board in `docs/claim-status.md`.
4. Inspect the exact computational matrix artifacts in `results/`.
5. Review the Lean scaffold in `Spacetime/`.
6. Use the visual assets in `viz/` to understand the three sign regimes.

## What is formalized now

This repository has a public-reader preview and a Lean-proved algebraic surface around

```text
A(λ) = [[0, -λ], [-1, 0]].
```

Lean proves the matrix spine, branch markers, algebraic eigendirections, algebraic split-nullness, and four-dimensional Lambda sign arithmetic. The computational artifacts verify trace, determinant, characteristic polynomial, square, branch behavior, eigendirection residuals, split-null residuals, branch-flow formulas, and invariant form.

## What is not formalized now

The null/light-cone bridge, redshift, horizon interpretation, full physical arrow-of-time conclusion, and shared sign thesis for `t`, `c`, and `Λ` remain interpretation. Those claims require bridge work beyond the current algebraic surface.
