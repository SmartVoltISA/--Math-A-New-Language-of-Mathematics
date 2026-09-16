"""Deterministic Ω-Math withheld-reconstruction experiment.

The structural layer receives only a difference Δ and a relation/constraint
context. Constitutive coefficients/laws are generated separately and withheld.
The experiment checks what the structural representation can and cannot identify.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from typing import Callable

import numpy as np


@dataclass(frozen=True)
class LinearCase:
    domain: str
    hidden_g: float
    recovered_g: float
    rmse: float


@dataclass(frozen=True)
class NonlinearCase:
    law: str
    best_linear_g: float
    rmse: float


def fit_through_origin(delta: np.ndarray, response: np.ndarray) -> tuple[float, float]:
    coefficient = float(delta @ response / (delta @ delta))
    residual = response - coefficient * delta
    rmse = float(np.sqrt(np.mean(residual**2)))
    return coefficient, rmse


def run(seed: int = 42) -> dict[str, object]:
    # Seed is part of the reproducibility record even though this deterministic
    # version does not currently sample random observations.
    np.random.default_rng(seed)

    delta_linear = np.linspace(-3.0, 3.0, 121)
    domains = ("electrical", "thermal", "fluid")
    hidden_coefficients = (0.5, 1.0, 2.0, 4.0)

    linear_cases: list[LinearCase] = []
    for domain in domains:
        for g in hidden_coefficients:
            response = g * delta_linear
            recovered, rmse = fit_through_origin(delta_linear, response)
            linear_cases.append(LinearCase(domain, g, recovered, rmse))

    delta_nonlinear = np.linspace(-3.0, 3.0, 301)
    laws: dict[str, Callable[[np.ndarray], np.ndarray]] = {
        "linear": lambda d: 2.0 * d,
        "quadratic_signed": lambda d: 2.0 * d * np.abs(d),
        "threshold": lambda d: np.where(np.abs(d) < 1.0, 0.0, 2.0 * d),
        "saturating": lambda d: 2.0 * np.tanh(d),
    }

    nonlinear_cases: list[NonlinearCase] = []
    for name, law in laws.items():
        response = law(delta_nonlinear)
        coefficient, rmse = fit_through_origin(delta_nonlinear, response)
        nonlinear_cases.append(NonlinearCase(name, coefficient, rmse))

    coefficient_identification_rejected = (
        all(abs(c.recovered_g - c.hidden_g) < 1e-12 for c in linear_cases)
        and len({c.recovered_g for c in linear_cases}) > 1
    )
    nonlinear_linear_form_rejected = any(
        c.law != "linear" and c.rmse > 1e-6 for c in nonlinear_cases
    )

    return {
        "seed": seed,
        "structural_input": ["STATE", "RELATION", "DISTINCTION", "CONSTRAINT", "TRANSITION"],
        "linear_counterfamily": [asdict(c) for c in linear_cases],
        "nonlinear_counterfamily": [asdict(c) for c in nonlinear_cases],
        "decision": {
            "structural_form": "J = g * Δ survives for the restricted linear family",
            "unique_coefficient": "rejected without constitutive/domain closure"
            if coefficient_identification_rejected
            else "not rejected",
            "universal_linear_response": "rejected by nonlinear counterfamily"
            if nonlinear_linear_form_rejected
            else "not rejected",
        },
    }


def main() -> None:
    print(json.dumps(run(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
