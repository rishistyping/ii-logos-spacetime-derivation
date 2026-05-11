# Notebook Guide

The notebook surfaces are public explainers, not proof authority.

## Current surfaces

- `notebooks/spacetime_sympy_colab.ipynb`: lightweight Python/SymPy companion stub.
- `wolfram/notebook_plan.md`: frozen notebook contract.
- `wolfram/build_spacetime_notebook.wl`: Wolfram builder stub.

## Rebuild order

```bash
python sympy/spacetime_exact_checks.py
python sympy/spacetime_matrix_oracle.py
python sympy/spacetime_regression_check.py
python sympy/spacetime_visualize.py
```

Then, when a Wolfram runtime is available:

```bash
wolframscript -file wolfram/build_spacetime_notebook.wl
```

## Authority boundary

- Lean: proof authority after build validation.
- SymPy: exact computational companion.
- Wolfram: public-facing explainer.
- Notebook captions must not call a claim `Lean-proved` unless `docs/claim-status.md` does.
