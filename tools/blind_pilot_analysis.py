"""Blind pilot analysis for the anonymized NIST-derived fixture.

The analysis intentionally knows only column roles (x-like inputs and y-like
responses). It tests whether stable response-vs-drive structure is visible
without restoring physical names or units.
"""
from __future__ import annotations

import csv
import math
from pathlib import Path


def fit_origin(x: list[float], y: list[float]) -> tuple[float, float]:
    denom = sum(v * v for v in x)
    g = sum(a * b for a, b in zip(x, y)) / denom
    rmse = math.sqrt(sum((b - g * a) ** 2 for a, b in zip(x, y)) / len(x))
    return g, rmse


def load(path: Path) -> dict[str, list[float]]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return {name: [float(r[name]) for r in rows] for name in rows[0] if name != "row"}


def main() -> None:
    data = load(Path(__file__).parents[1] / "fixtures" / "BLIND_PILOT_NIST_TUNGSTEN_v1.csv")
    print("columns:", sorted(data))
    for target in ("y1", "y2"):
        for drive in ("x1", "x2"):
            g, rmse = fit_origin(data[drive], data[target])
            print(f"{target} <- {drive}: g={g:.9g}, rmse={rmse:.9g}")


if __name__ == "__main__":
    main()
