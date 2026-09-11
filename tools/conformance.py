#!/usr/bin/env python3
"""Independent, offline Ω-Math conformance runner.

No GitHub Actions, network access, or pytest is required. Exit code 0 means
PASS; 1 means FAIL; 2 means INVALID runner/environment.

The synchronization gate checks that the canonical operator registry agrees
with the executable runtime, IR bridge, and canonical operator table. The
textual surface is checked separately because semantic operators may
intentionally have no declarative textual encoding yet.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path as FSPath

ROOT = FSPath(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from omega_math.core import Entity, Relation, Path, dist, incident, sign_summary
from omega_math.ir import IRInstruction, IRProgram, OP_ARITY
from omega_math.operator_registry import OPERATOR_REGISTRY, get_operator, surface_operators
from omega_math.parser import ParseError, Program
from omega_math import runtime


@dataclass
class Check:
    name: str
    ok: bool
    detail: str = ""


def _read_root(name: str) -> str:
    path = ROOT / name
    if not path.is_file():
        raise RuntimeError(f"required synchronization file is absent: {name}")
    return path.read_text(encoding="utf-8")


def _table_operators() -> set[str]:
    """Extract canonical operator names from OPERATOR_TABLE.md table rows."""
    text = _read_root("OPERATOR_TABLE.md")
    found: set[str] = set()
    for line in text.splitlines():
        m = re.match(r"^\|\s*`([A-Z][A-Z0-9_]*)`(?:\s*/|\s*\|)", line)
        if m:
            found.add(m.group(1))
    return found


def _runtime_dispatch_names() -> set[str]:
    """Recover names from the reference dispatch table without executing it."""
    text = _read_root("omega_math/runtime.py")
    marker = 'table = {'
    start = text.find(marker)
    if start < 0:
        raise RuntimeError("runtime dispatch table not found")
    end = text.find("\n    }", start)
    if end < 0:
        raise RuntimeError("runtime dispatch table terminator not found")
    block = text[start:end]
    return set(re.findall(r'"([A-Z][A-Z0-9_]*)"\s*:', block))


def _ir_ops() -> set[str]:
    text = _read_root("omega_math/ir.py")
    start = text.find("OP_ARITY = {")
    if start < 0:
        raise RuntimeError("IR OP_ARITY table not found")
    end = text.find("\n}", start)
    if end < 0:
        raise RuntimeError("IR OP_ARITY terminator not found")
    return set(re.findall(r'^\s*"([A-Z][A-Z0-9_]*)"\s*:', text[start:end], re.MULTILINE))


def check_registry() -> list[Check]:
    checks: list[Check] = []
    names = {s.name for s in OPERATOR_REGISTRY}
    checks.append(Check("registry_unique_names", len(names) == len(OPERATOR_REGISTRY)))

    missing = [s.name for s in OPERATOR_REGISTRY if not hasattr(runtime, s.runtime)]
    checks.append(Check("registry_runtime_symbols", not missing,
                        "missing: " + ", ".join(missing)))

    bad_call_surface = [s.name for s in OPERATOR_REGISTRY if s.ir_op == "CALL" and s.surface is not None]
    checks.append(Check("call_surface_boundary", not bad_call_surface,
                        "unexpected textual surface: " + ", ".join(bad_call_surface)))

    surface = {s.surface for s in surface_operators()}
    expected = {"dist", "incident", "path", "path_eq", "cycle", "concat", "sign"}
    checks.append(Check("surface_inventory", surface == expected,
                        f"got={sorted(surface)} expected={sorted(expected)}"))
    checks.append(Check("registry_lookup", all(get_operator(n).name == n for n in names)))
    return checks


def check_synchronization() -> list[Check]:
    """Cross-check registry, operator table, runtime dispatch and IR."""
    checks: list[Check] = []
    registry = {s.name for s in OPERATOR_REGISTRY}
    table = _table_operators()
    dispatch = _runtime_dispatch_names()
    ir_ops = _ir_ops()

    missing_table = sorted(registry - table)
    extra_table = sorted(table - registry)
    checks.append(Check("sync_registry_vs_operator_table",
                        not missing_table and not extra_table,
                        f"missing={missing_table} extra={extra_table}"))

    runtime_specs = {s.name for s in OPERATOR_REGISTRY if s.ir_op != "CALL"}
    missing_dispatch = sorted(runtime_specs - dispatch)
    extra_dispatch = sorted(dispatch - registry)
    checks.append(Check("sync_direct_runtime_dispatch",
                        not missing_dispatch and not extra_dispatch,
                        f"missing={missing_dispatch} extra={extra_dispatch}"))

    call_specs = {s.name for s in OPERATOR_REGISTRY if s.ir_op == "CALL"}
    checks.append(Check("sync_call_bridge_declared", "CALL" in ir_ops if call_specs else True,
                        "IR CALL operation is absent"))

    # Every non-CALL canonical operator must have a same-named IR opcode.
    missing_ir = sorted(runtime_specs - ir_ops)
    checks.append(Check("sync_registry_vs_ir", not missing_ir,
                        f"missing={missing_ir}"))

    # Registry entries using CALL must have an executable runtime symbol, while
    # direct operators must map one-to-one to their canonical IR opcode.
    bad_mapping = sorted(s.name for s in OPERATOR_REGISTRY
                         if s.ir_op != "CALL" and s.ir_op != s.name)
    checks.append(Check("sync_registry_ir_names", not bad_mapping,
                        f"non-identity IR mappings={bad_mapping}"))

    # The IR must not quietly contain extra canonical-looking operations.
    ir_canonical = {x for x in ir_ops if x not in {"ENTITY", "RELATION", "EPSILON", "CALL"}}
    extra_ir = sorted(ir_canonical - registry)
    checks.append(Check("sync_ir_vs_registry", not extra_ir,
                        f"extra={extra_ir}"))

    # Keep the arity table itself structurally sound for every IR opcode.
    checks.append(Check("ir_arity_table_valid", all(isinstance(v, int) and v >= 0 for v in OP_ARITY.values())))
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

    ir = IRProgram((IRInstruction("CALL", ("DIST", (a, b))),))
    try:
        ir.validate()
        checks.append(Check("call_validation_execution", runtime.execute_ir(ir) == [dist(a, b)]))
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
    source = "\n".join([
        "entity A 0", "entity B 1", "relation A B +1 rAB",
        "path p = A->B", "path e = epsilon(A)",
        "dist A B", "sign p", "path_eq p p", "cycle p",
    ])
    try:
        p = Program()
        results = p.run(source)
        ir = p.to_ir()
        checks.append(Check("parser_reference_surface", results == [1, 1, True, False], repr(results)))
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
    for name, text, needle in cases:
        try:
            Program().run(text)
            checks.append(Check(name, False, "invalid program accepted"))
        except ParseError as exc:
            checks.append(Check(name, needle in str(exc), str(exc)))
    return checks


def check_runtime() -> list[Check]:
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
    out: list[Check] = []
    for group in (check_registry, check_synchronization, check_core_and_ir, check_parser, check_runtime):
        out.extend(group())
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Run offline Ω-Math conformance checks")
    ap.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = ap.parse_args()
    try:
        checks = run()
    except Exception as exc:
        payload = {"status": "INVALID", "checks": [], "error": repr(exc)}
        print(json.dumps(payload, ensure_ascii=False, indent=2) if args.json else f"INVALID\n{exc!r}")
        return 2
    failed = [c for c in checks if not c.ok]
    status = "PASS" if not failed else "FAIL"
    payload = {
        "status": status,
        "checks": [{"name": c.name, "ok": c.ok, "detail": c.detail} for c in checks],
        "summary": {"total": len(checks), "passed": len(checks)-len(failed), "failed": len(failed)},
    }
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        for c in checks:
            suffix = f" — {c.detail}" if c.detail else ""
            print(f"{'PASS' if c.ok else 'FAIL'}  {c.name}{suffix}")
        print(f"\n{status}: {payload['summary']['passed']}/{payload['summary']['total']} checks")
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
