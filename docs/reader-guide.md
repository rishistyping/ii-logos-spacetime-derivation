# Reader Guide

This repository is a compact companion to *A Brief Derivation of Spacetime*.

## Fast path

1. Read the paper PDF in `paper/`.
2. Read the current status board in `docs/claim-status.md`.
3. Inspect the exact computational matrix artifacts in `results/`.
4. Review the Lean scaffold in `Spacetime/`.
5. Use the visual assets in `viz/` to understand the three sign regimes.

## What is formalized now

The v0 skeleton targets the exact matrix spine around

```text
A(λ) = [[0, -λ], [-1, 0]].
```

The computational artifacts verify trace, determinant, characteristic polynomial, square, and branch behavior.

## What is not formalized now

The full physical arrow-of-time conclusion and the shared sign thesis for `t`, `c`, and `Λ` remain interpretation. Those claims require bridge work beyond the v0 matrix spine.
