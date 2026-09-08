# Ω-Math v1.0 Release Gate

This checklist is the release boundary for v1.0.

## Required

- [x] Typed EntityState / RelationState separation remains explicit.
- [x] Parser lowers the reference surface into deterministic IR.
- [x] IR validates supported operations and exact arity.
- [x] Runtime can execute the reference IR.
- [x] Parser ↔ IR ↔ Runtime differential test exists.
- [x] ResearchRecord has a deterministic machine-readable schema.
- [x] COUNTEREXAMPLE is a machine-checkable result classification.
- [x] Path reversal does not invent inverse relations.
- [x] v0.9 experiments 010–012 remain executable.
- [x] Packaging explicitly discovers `omega_math*`.

## Final verification required before tagging v1.0

1. `python -m pip install -e .`
2. `python -m pytest -q`
3. `python experiments/run_v09_verification.py`
4. Confirm all three commands exit with status 0.
5. Record exact Python, pytest, package, and commit versions.
6. Only then tag/merge v1.0.

## Non-goals

v1.0 does not introduce physical time, physical energy, probability, causality, ontology, or autonomous scientific interpretation as primitive Ω-Math semantics.
