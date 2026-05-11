# Notebook Guide

The notebook surfaces are public explainers, not proof authority.

## Current surfaces

- `notebooks/spacetime_sympy_colab.ipynb`: lightweight committed-artifact walkthrough.
- `wolfram/notebook_plan.md`: frozen notebook contract.
- `wolfram/build_spacetime_notebook.wl`: Wolfram builder stub.

## Rebuild order

```bash
python sympy/spacetime_exact_checks.py
python sympy/spacetime_matrix_oracle.py
python sympy/spacetime_eigendirections.py
python sympy/spacetime_null_bridge.py
python sympy/spacetime_lambda_sign.py
python sympy/spacetime_flow_scaling.py
python sympy/spacetime_invariant_form.py
python sympy/spacetime_regression_check.py
python sympy/spacetime_visualize.py
```

For a lightweight rendered narrative using the committed artifacts, read `docs/public-reader-preview.md`.

Then, when a Wolfram runtime is available:

```bash
wolframscript -file wolfram/build_spacetime_notebook.wl
```

## Authority boundary

- Lean: proof authority after build validation.
- SymPy: exact computational companion.
- Wolfram: public-facing explainer.
- Notebook captions must not call a claim `Lean-proved` unless `docs/claim-status.md` does.
