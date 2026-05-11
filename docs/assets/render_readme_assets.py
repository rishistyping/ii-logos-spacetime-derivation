#!/usr/bin/env python3
"""Render README visual assets from deterministic SVG sources.

The script writes SVG files with no external Python dependencies. On macOS it
also uses `sips` to rasterize the SVGs to the PNG files used by the README.
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ASSET_DIR = Path(__file__).resolve().parent

NAVY = "#0F233F"
INK = "#172033"
MUTED = "#5D6572"
PARCHMENT = "#F6F1E7"
SAGE = "#E8EDE5"
GREEN = "#15803D"
TEAL = "#0F766E"
GOLD = "#B88A2E"
BLUE = "#334155"
ROSE = "#8B3A4A"


def svg_header(width: int, height: int) -> str:
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#FBF7EE"/>
      <stop offset="0.55" stop-color="{PARCHMENT}"/>
      <stop offset="1" stop-color="#E8EDE5"/>
    </linearGradient>
    <filter id="softShadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="18" stdDeviation="20" flood-color="#0F233F" flood-opacity="0.12"/>
    </filter>
    <style>
      .brand {{ font-family: Avenir Next, Helvetica Neue, Arial, sans-serif; font-weight: 700; letter-spacing: 8px; }}
      .title {{ font-family: Avenir Next, Helvetica Neue, Arial, sans-serif; font-weight: 800; letter-spacing: 0; }}
      .body {{ font-family: Avenir Next, Helvetica Neue, Arial, sans-serif; font-weight: 500; letter-spacing: 0; }}
      .mono {{ font-family: SFMono-Regular, Menlo, Consolas, monospace; font-weight: 650; letter-spacing: 0; }}
      .small {{ font-size: 30px; fill: {MUTED}; }}
    </style>
  </defs>
"""


def end_svg() -> str:
    return "</svg>\n"


def text(x: int, y: int, value: str, size: int, color: str = INK, cls: str = "body", anchor: str = "start") -> str:
    return f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" class="{cls}" text-anchor="{anchor}">{value}</text>'


def rounded_rect(x: int, y: int, w: int, h: int, fill: str, stroke: str = NAVY, r: int = 24, sw: int = 4) -> str:
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def arrow(x1: int, y1: int, x2: int, y2: int, color: str = MUTED, width: int = 5) -> str:
    return f"""<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"/>
<path d="M {x2} {y2} l -18 -10 l 4 10 l -4 10 z" fill="{color}"/>"""


def render_hero() -> str:
    width, height = 3000, 1200
    parts = [svg_header(width, height)]
    parts.append(f'<rect width="{width}" height="{height}" fill="url(#paper)"/>')
    parts.append(f'<circle cx="2380" cy="250" r="520" fill="{SAGE}" opacity="0.75"/>')
    parts.append(f'<circle cx="2560" cy="760" r="360" fill="#DDE8DF" opacity="0.55"/>')
    parts.append(f'<path d="M 0 940 C 520 840 860 1030 1350 910 C 1900 770 2290 910 3000 760 L 3000 1200 L 0 1200 Z" fill="#E1E8DF" opacity="0.62"/>')
    parts.append(text(180, 190, "II LOGOS", 48, TEAL, "brand"))
    parts.append(text(180, 335, "A Brief Derivation", 118, NAVY, "title"))
    parts.append(text(180, 470, "of Spacetime", 118, NAVY, "title"))
    parts.append(text(186, 565, "The sign is structural. The magnitude is empirical.", 48, BLUE, "body"))
    parts.append(text(186, 630, "The bridge is tracked claim by claim.", 48, BLUE, "body"))

    # Central proof card.
    parts.append(f'<g filter="url(#softShadow)">')
    parts.append(rounded_rect(1720, 300, 920, 560, "#FBF9F1", NAVY, 34, 5))
    parts.append(text(1815, 405, "v0.5 proof boundary", 42, NAVY, "title"))
    parts.append(text(1815, 505, "A(λ)² = λI", 54, GREEN, "mono"))
    parts.append(text(1815, 590, "Q(ℓ+) = Q(ℓ-) = 0", 46, TEAL, "mono"))
    parts.append(text(1815, 675, "Λ = 3λ,  λ > 0 ⇒ Λ > 0", 42, GOLD, "mono"))
    parts.append(text(1815, 770, "Physical arrow: Interpretation", 36, ROSE, "body"))
    parts.append("</g>")

    # Abstract curvature/grid motif.
    for offset in range(0, 7):
        y = 900 + offset * 28
        parts.append(f'<path d="M 1660 {y} C 1910 {y-110} 2170 {y+80} 2700 {y-40}" fill="none" stroke="{NAVY}" stroke-width="3" opacity="0.18"/>')
    parts.append(f'<line x1="1680" y1="885" x2="2680" y2="885" stroke="{NAVY}" stroke-width="3" opacity="0.28"/>')
    parts.append(f'<line x1="2180" y1="410" x2="2180" y2="1010" stroke="{NAVY}" stroke-width="3" opacity="0.28"/>')
    parts.append(end_svg())
    return "\n".join(parts)


def render_verification_story() -> str:
    width, height = 1600, 900
    nodes = [
        (90, 350, 210, 125, "Paper", "source", TEAL),
        (350, 350, 210, 125, "Lean", "proof authority", GREEN),
        (610, 350, 260, 125, "SymPy / Wolfram", "computed companions", GOLD),
        (920, 350, 210, 125, "Visuals", "reader layer", BLUE),
        (1180, 350, 210, 125, "Checks", "rerunnable gate", TEAL),
    ]
    parts = [svg_header(width, height), f'<rect width="{width}" height="{height}" fill="url(#paper)"/>']
    parts.append(text(800, 110, "Verification Story", 62, NAVY, "title", "middle"))
    parts.append(text(800, 165, "Public narrative, proof authority, computed companions, and release gates.", 30, MUTED, "body", "middle"))
    for i, (x, y, w, h, label, sub, accent) in enumerate(nodes):
        parts.append(f'<g filter="url(#softShadow)">')
        parts.append(rounded_rect(x, y, w, h, "#FBF9F1", NAVY, 24, 4))
        parts.append(f'<rect x="{x}" y="{y}" width="{w}" height="12" rx="6" fill="{accent}"/>')
        parts.append(text(x + w // 2, y + 58, label, 34, NAVY, "title", "middle"))
        parts.append(text(x + w // 2, y + 96, sub, 24, MUTED, "body", "middle"))
        parts.append("</g>")
        if i < len(nodes) - 1:
            parts.append(arrow(x + w + 24, y + h // 2, nodes[i + 1][0] - 24, y + h // 2, MUTED, 4))
    parts.append(rounded_rect(330, 640, 940, 118, SAGE, TEAL, 22, 3))
    parts.append(text(800, 692, "Inspectable v0.5 result", 32, NAVY, "title", "middle"))
    parts.append(text(800, 732, "algebra proved; interpretation labeled", 28, MUTED, "body", "middle"))
    parts.append(end_svg())
    return "\n".join(parts)


def render_bridge_funnel() -> str:
    width, height = 1600, 900
    steps = [
        ("Positive metric", TEAL),
        ("Curvature bracket", BLUE),
        ("λ branch split", GOLD),
        ("de Sitter signature", TEAL),
        ("time matrix", GREEN),
        ("eigendirections", GREEN),
        ("split form", GREEN),
        ("interpretation boundary", ROSE),
    ]
    parts = [svg_header(width, height), f'<rect width="{width}" height="{height}" fill="url(#paper)"/>']
    parts.append(text(800, 105, "Bridge Decomposition Funnel", 58, NAVY, "title", "middle"))
    parts.append(text(800, 160, "The README visualizes the paper's route without moving the proof boundary.", 29, MUTED, "body", "middle"))
    start_x, start_y = 120, 250
    top_w, h, gap = 1360, 52, 16
    for i, (label, color) in enumerate(steps):
        w = top_w - i * 125
        x = start_x + (top_w - w) // 2
        y = start_y + i * (h + gap)
        parts.append(f'<path d="M {x} {y} H {x+w} L {x+w-46} {y+h} H {x+46} Z" fill="#FBF9F1" stroke="{NAVY}" stroke-width="4"/>')
        parts.append(f'<path d="M {x} {y} H {x+w} L {x+w-46} {y+h} H {x+46} Z" fill="{color}" opacity="0.13"/>')
        parts.append(text(800, y + 35, label, 28, NAVY if i < 7 else ROSE, "title", "middle"))
    parts.append(text(800, 830, "Lean-proved: matrix spine, eigendirections, split form, Λ arithmetic", 27, GREEN, "body", "middle"))
    parts.append(text(800, 866, "Interpretation: geometric light-cone reading, horizon, redshift, arrow thesis", 25, ROSE, "body", "middle"))
    parts.append(end_svg())
    return "\n".join(parts)


ASSETS = {
    "logos-spacetime-hero": (render_hero, 3000, 1200),
    "verification-story": (render_verification_story, 1600, 900),
    "bridge-decomposition-funnel": (render_bridge_funnel, 1600, 900),
}


def write_assets() -> None:
    sips = shutil.which("sips")
    for name, (renderer, _width, _height) in ASSETS.items():
        svg_path = ASSET_DIR / f"{name}.svg"
        png_path = ASSET_DIR / f"{name}.png"
        svg_path.write_text(renderer(), encoding="utf-8")
        if sips:
            subprocess.run(
                [sips, "-s", "format", "png", str(svg_path), "--out", str(png_path)],
                check=True,
                stdout=subprocess.DEVNULL,
            )
            print(f"Wrote {png_path.relative_to(ASSET_DIR.parent.parent)}")
        else:
            print(f"Wrote {svg_path.relative_to(ASSET_DIR.parent.parent)}; install sips-compatible renderer for PNG export")


if __name__ == "__main__":
    write_assets()
