#!/usr/bin/env python3
"""Compile real Lean modules, then delete each declared import one at a time.

This is a compiler-backed module-import necessity probe. It is not a theorem-level
dependency extractor. The upstream source commit and corpus are pinned.
"""
from __future__ import annotations

import re
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = REPO_ROOT / "openai-math"
LEAN_ROOT = UPSTREAM / "lean"
PINNED_COMMIT = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
IMPORT_RE = re.compile(r"^\s*import\s+([A-Za-z0-9_.]+)\s*$")

TARGETS = (
    "OAI/NumberTheory/PiExponent/Main.lean",
    "OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixInterpolation.lean",
    "OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixGeometry.lean",
    "OAI/NumberTheory/PiExponent/Approximation/InterpolationConsequence.lean",
    "OAI/NumberTheory/PiExponent/Ampleness/AdmissibleBlowupGeometry.lean",
    "OAI/NumberTheory/PiExponent/Approximation/DeterminantContradiction.lean",
    "OAI/NumberTheory/PiExponent/Approximation/FormalMatrixSurjectivity.lean",
    "OAI/NumberTheory/PiExponent/Approximation/WeightedSliceDegree.lean",
    "OAI/NumberTheory/PiExponent/Approximation/AdmissibleMatrixFrame.lean",
    "OAI/NumberTheory/PiExponent/Approximation/WeightedGlobalSectionBound.lean",
    "OAI/NumberTheory/PiExponent/Jets/AdmissibleJetPackets.lean",
    "OAI/NumberTheory/PiExponent/Statement.lean",
)


def run(command: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command, cwd=cwd, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT, check=False, timeout=300,
    )


def main() -> int:
    commit = run(["git", "-C", str(UPSTREAM), "rev-parse", "HEAD"], cwd=REPO_ROOT)
    if commit.returncode != 0 or commit.stdout.strip() != PINNED_COMMIT:
        print(f"UPSTREAM_PIN_FAIL actual={commit.stdout.strip()!r} expected={PINNED_COMMIT}")
        return 2

    files = [(rel, LEAN_ROOT / rel) for rel in TARGETS]
    if any(not path.is_file() for _, path in files):
        missing = [rel for rel, path in files if not path.is_file()]
        print(f"CORPUS_MISSING {missing}")
        return 2

    original_sources = {rel: path.read_text(encoding="utf-8") for rel, path in files}
    import_edges: list[tuple[str, str, int]] = []
    for rel, source in original_sources.items():
        for line_no, line in enumerate(source.splitlines(keepends=True), 1):
            match = IMPORT_RE.match(line.rstrip("\r\n"))
            if match:
                import_edges.append((rel, match.group(1), line_no))

    print(f"PINNED_UPSTREAM_COMMIT {PINNED_COMMIT}")
    print(f"MODULES {len(files)}")
    print(f"DECLARED_IMPORT_EDGES {len(import_edges)}")

    # Confirm each source file compiles before testing mutations.
    for rel, path in files:
        result = run(["lake", "env", "lean", rel], cwd=LEAN_ROOT)
        if result.returncode != 0:
            print(f"BASELINE_COMPILE_FAIL module={rel}")
            print(result.stdout[-5000:])
            return 3
        print(f"BASELINE_COMPILE_PASS module={rel}")

    removal_passes = 0
    removal_fails = 0
    for rel, path in files:
        original = original_sources[rel]
        lines = original.splitlines(keepends=True)
        import_indices = [
            (i, IMPORT_RE.match(line.rstrip("\r\n")).group(1))
            for i, line in enumerate(lines)
            if IMPORT_RE.match(line.rstrip("\r\n"))
        ]
        for index, imported in import_indices:
            mutated = lines[:index] + lines[index + 1:]
            path.write_text("".join(mutated), encoding="utf-8")
            try:
                result = run(["lake", "env", "lean", rel], cwd=LEAN_ROOT)
            finally:
                path.write_text(original, encoding="utf-8")
            if result.returncode == 0:
                removal_passes += 1
                print(f"IMPORT_REMOVAL_COMPILES module={rel} import={imported}")
            else:
                removal_fails += 1
                tail = " ".join(result.stdout.strip().split())[-700:]
                print(f"IMPORT_REMOVAL_BREAKS module={rel} import={imported} diagnostic={tail}")

    # A valid but potentially redundant import should still compile. This tests
    # whether Lean's compiler itself rejects extra imports (it normally does not).
    main_rel = TARGETS[0]
    main_path = LEAN_ROOT / main_rel
    main_original = original_sources[main_rel]
    extra = "import OAI.NumberTheory.PiExponent.Statement\n"
    main_path.write_text(extra + main_original, encoding="utf-8")
    try:
        extra_result = run(["lake", "env", "lean", main_rel], cwd=LEAN_ROOT)
    finally:
        main_path.write_text(main_original, encoding="utf-8")
    print(f"EXTRA_VALID_IMPORT_{'ACCEPTED' if extra_result.returncode == 0 else 'REJECTED'}")
    if extra_result.returncode != 0:
        print(extra_result.stdout[-3000:])

    print(f"SUMMARY removal_compiles={removal_passes} removal_breaks={removal_fails} total={len(import_edges)}")
    print("INTERPRETATION compiler-backed direct-import necessity only; not elaborator theorem-dependency extraction")
    return 0 if extra_result.returncode == 0 else 4


if __name__ == "__main__":
    raise SystemExit(main())
