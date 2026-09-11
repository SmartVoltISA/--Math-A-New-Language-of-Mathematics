#!/usr/bin/env python3
"""Independent, offline Ω-Math conformance runner.

No GitHub Actions, network access, or pytest is required. Exit code 0 means
PASS; 1 means FAIL; 2 means INVALID runner/environment.

The synchronization gate checks the canonical manifest against the executable
runtime, IR bridge, operator registry and canonical operator table. The
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
from omega_math.ir import IRInstruction, IRProgram
from omega_math.operator_registry import OPERATOR_REGISTRY, get_operator, surface_operators
from omega_math.parser import ParseError, Program
from omega_math import runtime

MANIFEST_PATH = ROOT / "CONFORMANCE_MANIFEST_v1.0.json"


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


def _manifest() -> dict:
    if not MANIFEST_PATH.is_file():
        raise RuntimeError("required conformance manifest is absent")
    try:
        return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"invalid conformance manifest JSON: {exc}") from exc


def _table_operators() -> set[str]:
    text = _read_root("OPERATOR_TABLE.md")
    found: set[str] = set()
    for line in text.splitlines():
        m = re.match(r"^\|\s*`([A-Z][A-Z0-9_]*)`(?:\s*/|\s*\|)", line)
        if m:
            found.add(m.group(1))
    return found


def _runtime_dispatch_names() -> set[str]:
    text = _read_root("omega_math/runtime.py")
    marker = 'table = {'
    start = text.find(marker)
    if start < 0:
        raise RuntimeError("runtime dispatch table not found")
    end = text.find("\n    }", start)
    if end < 0:
        raise RuntimeError("runtime dispatch table terminator not found")
    return set(re.findall(r'"([A-Z][A-Z0-9_]*)"\s*:', text[start:end]))


def _ir_call_names() -> set[str]:
    text = _read_root("omega_math/ir.py")
    return {"CALL"} if '"CALL": 2' in text else set()


def check_manifest_structure() -> list[Check]:
    m = _manifest()
    checks = [
        Check("manifest_identity", m.get("manifest") == "Ω-Math Conformance Manifest"),
        Check("manifest_version", m.get("version") == "1.0"),
        Check("manifest_canonical", m.get("status") == "CANONICAL"),
        Check("manifest_layers_complete", set(m.get("layers", {})) == {
            "semantic_spec", "surface_syntax", "operator_registry", "ir", "runtime",
            "operator_table", "conformance_runner"
        }),
    ]
    required_files = m.get("layers", {})
    for key, rel in required_files.items():
        checks.append(Check(f"manifest_file_{key}", (ROOT / rel).is_file(), f"missing={rel}"))
    return checks


def check_manifest_against_registry() -> list[Check]:
    m = _manifest()
    manifest_ops = {x["name"]: x for x in m.get("operators", [])}
    registry_ops = {s.name: s for s in OPERATOR_REGISTRY}
    checks = [
        Check("manifest_registry_name_set", set(manifest_ops) == set(registry_ops),
              f"manifest_only={sorted(set(manifest_ops)-set(registry_ops))}; registry_only={sorted(set(registry_ops)-set(manifest_ops))}"),
    ]
    mismatches = []
    for name in sorted(set(manifest_ops) & set(registry_ops)):
        item, spec = manifest_ops[name], registry_ops[name]
        expected = {"status": spec.status, "surface": spec.surface, "ir": spec.ir_op, "runtime": spec.runtime}
        actual = {k: item.get(k) for k in expected}
        if actual != expected:
            mismatches.append(f"{name}: actual={actual} expected={expected}")
    checks.append(Check("manifest_registry_metadata", not mismatches, "; ".join(mismatches)))
    checks.append(Check("manifest_surface_set", set(m.get("surface_operators", [])) ==
                        {s.surface for s in surface_operators()},
                        "manifest surface inventory differs from registry"))
    return checks


def check_registry() -> list[Check]:
    names = {s.name for s in OPERATOR_REGISTRY}
    missing = [s.name for s in OPERATOR_REGISTRY if not hasattr(runtime, s.runtime)]
    bad_call_surface = [s.name for s in OPERATOR_REGISTRY if s.ir_op == "CALL" and s.surface is not None]
    surface = {s.surface for s in surface_operators()}
    expected = {"dist", "incident", "path", "path_eq", "cycle", "concat", "sign"}
    return [
        Check("registry_unique_names", len(names) == len(OPERATOR_REGISTRY)),
        Check("registry_runtime_symbols", not missing, "missing: " + ", ".join(missing)),
        Check("call_surface_boundary", not bad_call_surface,
              "unexpected textual surface: " + ", ".join(bad_call_surface)),
        Check("surface_inventory", surface == expected,
              f"got={sorted(surface)} expected={sorted(expected)}"),
        Check("registry_lookup", all(get_operator(n).name == n for n in names)),
    ]


def check_synchronization() -> list[Check]:
    m = _manifest()
    registry = {s.name for s in OPERATOR_REGISTRY}
    table = _table_operators()
    dispatch = _runtime_dispatch_names()
    checks = []

    checks.append(Check("sync_registry_vs_operator_table", registry == table,
                        f"missing={sorted(registry-table)} extra={sorted(table-registry)}"))

    direct = {s.name for s in OPERATOR_REGISTRY if s.ir_op != "CALL"}
    checks.append(Check("sync_direct_runtime_dispatch", direct <= dispatch,
                        f"missing={sorted(direct-dispatch)}"))

    call_specs = {s.name for s in OPERATOR_REGISTRY if s.ir_op == "CALL"}
    checks.append(Check("sync_call_bridge_declared", "CALL" in _ir_call_names() if call_specs else True,
                        "IR CALL operation is absent"))

    bad_mapping = sorted(s.name for s in OPERATOR_REGISTRY if s.ir_op != "CALL" and s.ir_op != s.name)
    checks.append(Check("sync_registry_ir_names", not bad_mapping,
                        f"non-identity IR mappings={bad_mapping}"))

    manifest_layers = m.get("layers", {})
    checks.append(Check("sync_manifest_runner_path", manifest_layers.get("conformance_runner") == "tools/conformance.py"))
    return checks


def check_core_and_ir() -> list[Check]:
    a, b, c = Entity("A", 0), Entity("B", 1), Entity("C", 0)
    r1 = Relation("A", "B", 1, key="r1")
    r2 = Relation("B", "C", -1, key="r2")
    p = Path((r1, r2), "A", "C")
    eps = Path((), "A", "A")
    checks = [
        Check("entity_domain", all(x.state in (0, 1) for x in (a, b, c))),
        Check("relation_domain", r1.sign in (-1, 1) and r2.sign in (-1, 1)),
        Check("epsilon_identity", eps.length == 0 and eps.source == eps.target == "A"),
        Check("path_sign", sign_summary(p) == -1),
        Check("distance_boundary", dist(a, b) != dist(a, a)),
        Check("incident_endpoint", incident(a, r1) is True and incident(c, r1) is False),
    ]
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
    source = "\n".join([
        "entity A 0", "entity B 1", "relation A B +1 rAB",
        "path p = A->B", "path e = epsilon(A)",
        "dist A B", "sign p", "path_eq p p", "cycle p",
    ])
    checks: list[Check] = []
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
    a, b = Entity("A", 0), Entity("B", 1)
    probes = {
        "DIST": lambda: runtime.execute("DIST", a, b),
        "PATH": lambda: runtime.execute("PATH", (Relation("A", "B", 1, key="r"),)),
        "CYCLE": lambda: runtime.execute("CYCLE", Path((), "A", "A")),
        "CONCAT": lambda: runtime.execute("CONCAT", Path((), "A", "A"), Path((), "A", "A")),
        "HORIZON": lambda: runtime.execute("HORIZON", 2),
        "ORDER": lambda: runtime.execute("ORDER", ["x", "y"]),
    }
    checks = []
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
    for group in (check_manifest_structure, check_manifest_against_registry, check_registry,
                  check_synchronization, check_core_and_ir, check_parser, check_runtime):
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
