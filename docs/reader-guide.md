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

The v0.4 repository has a public-reader preview and a v0.3 Lean-proved algebraic surface around

```text
A(λ) = [[0, -λ], [-1, 0]].
```

Lean proves the matrix spine, branch markers, and algebraic eigendirections. The computational artifacts verify trace, determinant, characteristic polynomial, square, branch behavior, and eigendirection residuals.

## What is not formalized now

The null/light-cone bridge, redshift, horizon interpretation, full physical arrow-of-time conclusion, and shared sign thesis for `t`, `c`, and `Λ` remain interpretation. Those claims require bridge work beyond the current algebraic surface.
