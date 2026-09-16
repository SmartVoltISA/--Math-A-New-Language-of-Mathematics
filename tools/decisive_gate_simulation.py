"""Deterministic simulation of the decisive blind-gate decision logic.

This is a protocol/control test, not evidence about physical universality.
It verifies that the gate can return POSITIVE, NEGATIVE, or INVALID without
ambiguity under preregistered conditions.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Run:
    domains: int
    withheld_gain: bool
    shuffle_destroyed: bool
    nonlinear_control_clean: bool
    leakage_free: bool
    independent_rerun: bool


def decide(run: Run) -> str:
    if not run.leakage_free:
        return "INVALID"
    positive = (
        run.domains >= 3
        and run.withheld_gain
        and run.shuffle_destroyed
        and run.nonlinear_control_clean
        and run.independent_rerun
    )
    if positive:
        return "POSITIVE"
    return "NEGATIVE"


def main() -> None:
    cases = {
        "all_gates_pass": Run(3, True, True, True, True, True),
        "withheld_failure": Run(3, False, True, True, True, True),
        "shuffle_failure": Run(3, True, False, True, True, True),
        "leakage": Run(3, True, True, True, False, True),
        "insufficient_domains": Run(2, True, True, True, True, True),
    }
    for name, case in cases.items():
        print(f"{name}: {decide(case)}")


if __name__ == "__main__":
    main()
