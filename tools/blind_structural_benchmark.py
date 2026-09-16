"""Blind structural benchmark for Ω-Math.

This benchmark deliberately exposes only dimensionless structural observations.
Domain labels and constitutive names are withheld until evaluation.
It tests common response architecture, nonlinear detection and a negative control.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Callable

import numpy as np


@dataclass(frozen=True)
class Case:
    hidden_domain: str
    regime: str
    n: int
    correlation: float
    linear_rmse: float
    structural_pass: bool
    negative_control: bool = False


def fit_origin(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    g = float(x @ y / (x @ x))
    rmse = float(np.sqrt(np.mean((y - g * x) ** 2)))
    return g, rmse


def correlation(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.corrcoef(x, y)[0, 1])


def run() -> dict[str, object]:
    # The structural stage sees only x=distinction, r=coupling indicator,
    # c=constraint indicator and y=response. Domain names are evaluation-only.
    x = np.linspace(-2.0, 2.0, 401)
    r = np.ones_like(x)
    c = np.ones_like(x)

    laws: list[tuple[str, str, Callable[[np.ndarray], np.ndarray]]] = [
        ("domain_A", "linear", lambda d: 0.7 * d),
        ("domain_B", "linear", lambda d: 2.3 * d),
        ("domain_C", "nonlinear", lambda d: 1.4 * d * np.abs(d)),
    ]

    cases: list[Case] = []
    for domain, regime, law in laws:
        y = law(x)
        _, rmse = fit_origin(x, y)
        corr = correlation(x, y)
        # Structural pass means a directed response exists and coupling is active.
        structural = abs(corr) > 0.99 and bool(np.all(r == 1)) and bool(np.all(c == 1))
        cases.append(Case(domain, regime, len(x), corr, rmse, structural))

    # Negative control: preserve x/r/c structure but break the response relation.
    rng = np.random.default_rng(20260916)
    y_negative = rng.normal(0.0, 1.0, size=x.shape)
    _, rmse_negative = fit_origin(x, y_negative)
    corr_negative = correlation(x, y_negative)
    negative_rejected = abs(corr_negative) < 0.15
    cases.append(
        Case(
            "negative_control",
            "independent_response",
            len(x),
            corr_negative,
            rmse_negative,
            structural_pass=not negative_rejected,
            negative_control=True,
        )
    )

    linear_cases = [c for c in cases if not c.negative_control and c.regime == "linear"]
    nonlinear_cases = [c for c in cases if not c.negative_control and c.regime == "nonlinear"]

    common_architecture = all(c.structural_pass for c in linear_cases + nonlinear_cases)
    nonlinear_detected = all(c.linear_rmse > 0.1 for c in nonlinear_cases)
    universal_coefficient_rejected = len({round(fit_origin(x, laws[i][2](x))[0], 8) for i in range(len(laws))}) > 1

    return {
        "protocol": "WITHHELD_REAL_DOMAIN_PROTOCOL_v1.0",
        "visible_structural_inputs": ["STATE", "RELATION", "DISTINCTION", "CONSTRAINT", "TRANSITION"],
        "hidden_domains": True,
        "results": [c.__dict__ for c in cases],
        "gates": {
            "common_structural_architecture": common_architecture,
            "nonlinear_regime_detected": nonlinear_detected,
            "universal_coefficient_rejected": universal_coefficient_rejected,
            "negative_control_rejected": negative_rejected,
        },
        "decision": (
            "STRUCTURAL-PASS: common relational architecture survives; "
            "constitutive coefficients remain domain closure."
            if common_architecture and nonlinear_detected and universal_coefficient_rejected and negative_rejected
            else "FAIL: at least one withheld benchmark gate failed."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
