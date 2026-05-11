#!/usr/bin/env python3
"""Generate simple phase-portrait visuals for the three A(lambda) regimes."""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
VIZ = ROOT / "viz"
VIZ.mkdir(exist_ok=True)


def vector_field(lambda_value: float, name: str, title: str) -> None:
    grid = np.linspace(-2.0, 2.0, 21)
    x, y = np.meshgrid(grid, grid)
    # State vector is (K, P). A(lambda) @ [K, P]^T = [-lambda P, -K].
    u = -lambda_value * y
    v = -x

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.quiver(x, y, u, v)
    ax.axhline(0, linewidth=0.8)
    ax.axvline(0, linewidth=0.8)
    ax.set_xlabel("K")
    ax.set_ylabel("P")
    ax.set_title(title)
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.2, 2.2)
    fig.tight_layout()
    out = VIZ / name
    fig.savefig(out, dpi=160)
    plt.close(fig)
    print(f"Wrote {out}")


vector_field(1.0, "hyperbolic_flow.png", "lambda > 0: hyperbolic branch")
vector_field(0.0, "parabolic_flow.png", "lambda = 0: parabolic branch")
vector_field(-1.0, "elliptic_flow.png", "lambda < 0: elliptic branch")
