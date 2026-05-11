#!/usr/bin/env python3
"""Generate deterministic phase-portrait PNGs for the three A(lambda) regimes."""
from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIZ = ROOT / "viz"
VIZ.mkdir(exist_ok=True)

WIDTH = 600
HEIGHT = 600
WORLD_MIN = -2.2
WORLD_MAX = 2.2

BG = (247, 249, 246)
GRID = (220, 226, 219)
AXIS = (44, 56, 70)
POSITIVE = (33, 101, 172)
ZERO = (53, 130, 104)
NEGATIVE = (133, 82, 157)


def blank() -> list[bytearray]:
    row = bytearray(BG * WIDTH)
    return [bytearray(row) for _ in range(HEIGHT)]


def put(px: list[bytearray], x: int, y: int, color: tuple[int, int, int]) -> None:
    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
        index = 3 * x
        px[y][index : index + 3] = bytes(color)


def world_to_pixel(x: float, y: float) -> tuple[int, int]:
    u = (x - WORLD_MIN) / (WORLD_MAX - WORLD_MIN)
    v = (y - WORLD_MIN) / (WORLD_MAX - WORLD_MIN)
    return round(u * (WIDTH - 1)), round((1 - v) * (HEIGHT - 1))


def draw_line(px: list[bytearray], start: tuple[int, int], end: tuple[int, int], color: tuple[int, int, int]) -> None:
    x0, y0 = start
    x1, y1 = end
    dx = abs(x1 - x0)
    dy = -abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx + dy
    while True:
        put(px, x0, y0, color)
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 >= dy:
            err += dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy


def draw_disc(px: list[bytearray], center: tuple[int, int], radius: int, color: tuple[int, int, int]) -> None:
    cx, cy = center
    for y in range(cy - radius, cy + radius + 1):
        for x in range(cx - radius, cx + radius + 1):
            if (x - cx) ** 2 + (y - cy) ** 2 <= radius**2:
                put(px, x, y, color)


def draw_arrow(px: list[bytearray], x: float, y: float, u: float, v: float, color: tuple[int, int, int]) -> None:
    length = math.hypot(u, v)
    if length <= 1e-12:
        draw_disc(px, world_to_pixel(x, y), 2, color)
        return

    scale = 0.22 / length
    x1 = x + scale * u
    y1 = y + scale * v
    start = world_to_pixel(x, y)
    end = world_to_pixel(x1, y1)
    draw_line(px, start, end, color)
    draw_disc(px, end, 2, color)


def write_png(path: Path, px: list[bytearray]) -> None:
    def chunk(kind: bytes, data: bytes) -> bytes:
        payload = kind + data
        return struct.pack(">I", len(data)) + payload + struct.pack(">I", zlib.crc32(payload) & 0xFFFFFFFF)

    raw = b"".join(b"\x00" + bytes(row) for row in px)
    encoded = zlib.compress(raw, level=9)
    png = [
        b"\x89PNG\r\n\x1a\n",
        chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0)),
        chunk(b"IDAT", encoded),
        chunk(b"IEND", b""),
    ]
    path.write_bytes(b"".join(png))


def vector_field(lambda_value: float, name: str, color: tuple[int, int, int]) -> None:
    px = blank()

    for tick in [WORLD_MIN + i * (WORLD_MAX - WORLD_MIN) / 8 for i in range(9)]:
        draw_line(px, world_to_pixel(WORLD_MIN, tick), world_to_pixel(WORLD_MAX, tick), GRID)
        draw_line(px, world_to_pixel(tick, WORLD_MIN), world_to_pixel(tick, WORLD_MAX), GRID)

    draw_line(px, world_to_pixel(WORLD_MIN, 0), world_to_pixel(WORLD_MAX, 0), AXIS)
    draw_line(px, world_to_pixel(0, WORLD_MIN), world_to_pixel(0, WORLD_MAX), AXIS)

    for i in range(21):
        x = -2.0 + i * 0.2
        for j in range(21):
            y = -2.0 + j * 0.2
            u = -lambda_value * y
            v = -x
            draw_arrow(px, x, y, u, v, color)

    out = VIZ / name
    write_png(out, px)
    print(f"Wrote {out}")


vector_field(1.0, "hyperbolic_flow.png", POSITIVE)
vector_field(0.0, "parabolic_flow.png", ZERO)
vector_field(-1.0, "elliptic_flow.png", NEGATIVE)
