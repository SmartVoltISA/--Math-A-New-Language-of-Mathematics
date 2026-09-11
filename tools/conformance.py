#!/usr/bin/env python3
"""Independent, offline Ω-Math conformance runner.

This runner deliberately does not require GitHub Actions, network access, or
pytest. It checks the executable reference layer and the registry/surface
boundary using deterministic probes. Exit code 0 means PASS; non-zero means
FAIL or INVALID.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path as FSPath

# Make the repository root importable when invoked as `python tools/conformance.py`.
ROOT = FSPath(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from omega_math.core import Entity, Relation, Path, concat, dist, incident, sign_summary
from omega_math.ir import IRInstruction, IRProgram
from omega_math.operator_registry import OPERATOR_REGISTRY, get_operator, surface_operators
from omega_math.parser import ParseError, Program
from omega_math import runtime


@dataclass
class Check:
    name: str
    ok: bool
    detail: str = ""


def check_registry() -> list[Check]:
    checks: list[Check] = []
    names = [s.name for s in OPERATOR_REGISTRY]
    checks.append(Check("registry_unique_names", len(names) == len(set(names))))

    runtime_missing = []
    for spec in OPERATOR_REGISTRY:
        if not hasattr(runtime, spec.runtime):
            runtime_missing.append(spec.name)
    checks.append(Check("registry_runtime_symbols", not runtime_missing,
                        "missing: " + ", ".join(runtime_missing)))

    bad_ir = []
    for spec in OPERATOR_REGISTRY:
        if spec.ir_op == "CALL" and spec.surface is not None:
            bad_ir.append(spec.name)
    checks.append(Check("call_surface_boundary", not bad_ir,
                        "CALL operators unexpectedly have textual surface: " + ", ".join(bad_ir)))

    surface = {s.surface for s in surface_operators()}
    expected = {"dist", "incident", "path", "path_eq", "cycle", "concat", "sign"}
    checks.append(Check("surface_inventory", surface == expected,
                        f"got={sorted(surface)} expected={sorted(expected)}"))

    lookup_ok = all(get_operator(n).name == n for n in names)
    checks.append(Check("registry_lookup", lookup_ok))
    return checks


def check_core_and_ir() -> list[Check]:
    checks: list[Check] = []
    a, b, c = Entity("A", 0), Entity("B", 1), Entity("C", 0)
    r1 = Relation("A", "B", 1, key="r1")
    r2 = Relation("B", "C", -1, key="r2")
    p = Path((r1, r2), "A", "C")
    eps = Path((), "A", "A")

    checks.append(Check("entity_domain", all(x.state in (0, 1) for x in (a, b, c))))
    checks.append(Check("relation_domain", r1.sign in (-1, 1) and r2.sign in (-1, 1)))
    checks.append(Check("epsilon_identity", eps.length == 0 and eps.source == eps.target == "A"))
    checks.append(Check("path_sign", sign_summary(p) == -1))
    checks.append(Check("distance_boundary", dist(a, b) != dist(a, a)))
    checks.append(Check("incident_endpoint", incident(a, r1) is True and incident(c, r1) is False))

    call = IRInstruction("CALL", ("DIST", (a, b)))
    ir = IRProgram((call,))
    try:
        ir.validate()
        result = runtime.execute_ir(ir)
        checks.append(Check("call_validation_execution", result == [dist(a, b)]))
    except Exception as exc:
        checks.append(Check("call_validation_execution", False, repr(exc)))

    bad = IRProgram((IRInstruction("CALL", ("", (a, b))),))
    try:
        bad.validate()
        checks.append(Check("call_rejects_empty_name", False, "invalid CALL accepted"))
    except (TypeError, ValueError):
        checks.append(Check("call_rejects_empty_name", True))
    return checks


def check_parser() -> list[Check]:
    checks: list[Check] = []
    text = "\n".join([
        "entity A 0",
        "entity B 1",
        "relation A B +1 rAB",
        "path p = A->B",
        "path e = epsilon(A)",
        "dist A B",
        "sign p",
        "path_eq p p",
        "cycle p",
    ])
    try:
        p = Program()
        results = p.run(text)
        ir = p.to_ir()
        checks.append(Check("parser_reference_surface", results == [True, 1, True, False]))
        checks.append(Check("parser_ir_valid", ir.normalized() == tuple((i.op, i.args) for i in ir.instructions)))
    except Exception as exc:
        checks.append(Check("parser_reference_surface", False, repr(exc)))
        checks.append(Check("parser_ir_valid", False, repr(exc)))

    cases = [
        ("singleton_path_rejected", "entity A 0\npath p = A", "non-empty path"),
        ("zero_relation_rejected", "entity A 0\nentity B 1\nrelation A B 0", "unsupported syntax"),
        ("ambiguous_parallel_relation_rejected",
         "entity A 0\nentity B 1\nrelation A B +1 r1\nrelation A B -1 r2\npath p = A->B",
         "ambiguous relation"),
    ]
    for name, source, needle in cases:
        try:
            Program().run(source)
            checks.append(Check(name, False, "invalid program accepted"))
        except ParseError as exc:
            checks.append(Check(name, needle in str(exc), str(exc)))
    return checks


def check_runtime_surface() -> list[Check]:
    checks: list[Check] = []
    a, b = Entity("A", 0), Entity("B", 1)
    probes = {
        "DIST": lambda: runtime.execute("DIST", a, b),
        "PATH": lambda: runtime.execute("PATH", (Relation("A", "B", 1, key="r"),)),
        "CYCLE": lambda: runtime.execute("CYCLE", Path((), "A", "A")),
        "CONCAT": lambda: runtime.execute("CONCAT", Path((), "A", "A"), Path((), "A", "A")),
        "HORIZON": lambda: runtime.execute("HORIZON", 2),
        "ORDER": lambda: runtime.execute("ORDER", ["x", "y"]),
    }
    for name, fn in probes.items():
        try:
            fn()
            checks.append(Check(f"runtime_{name.lower()}", True))
        except Exception as exc:
            checks.append(Check(f"runtime_{name.lower()}", False, repr(exc)))
    try:
        runtime.execute("NOT_A_CANONICAL_OPERATOR")
        checks.append(Check("runtime_unknown_operator_rejected", False, "unknown operator accepted"))
    except KeyError:
        checks.append(Check("runtime_unknown_operator_rejected", True))
    return checks


def run() -> list[Check]:
    checks: list[Check] = []
    for group in (check_registry, check_core_and_ir, check_parser, check_runtime_surface):
        checks.extend(group())
    return checks


def main() -> int:
    ap = argparse.ArgumentParser(description="Run offline Ω-Math conformance checks")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = ap.parse_args()

    try:
        checks = run()
    except Exception as exc:
        payload = {"status": "INVALID", "checks": [], "error": repr(exc)}
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print("INVALID")
            print(repr(exc))
        return 2

    failed = [c for c in checks if not c.ok]
    status = "PASS" if not failed else "FAIL"
    payload = {
        "status": status,
        "checks": [{"name": c.name, "ok": c.ok, "detail": c.detail} for c in checks],
        "summary": {"total": len(checks), "passed": len(checks) - len(failed), "failed": len(failed)},
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for c in checks:
            print(f"{'PASS' if c.ok else 'FAIL'}  {c.name}" + (f" — {c.detail}" if c.detail else ""))
        print(f"\n{status}: {payload['summary']['passed']}/{payload['summary']['total']} checks")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
