# Ω-Math v0.9 — Reference Runtime

The canonical v0.9 documents define the language semantics. This directory adds a small executable reference implementation without changing the mathematical boundary.

## Design rule

The implementation is subordinate to the specification: types are explicit, entity states and relation states are distinct, relation absence is domain absence, paths preserve order, and summaries are not silently promoted to equivalence.

## Included

- `omega_math/core.py` — typed entities, relations, configurations, states, paths and transformations.
- `omega_math/runtime.py` — executable implementations of the canonical derived operators and verification helpers.
- `omega_math/parser.py` — explicit reference surface syntax.
- `omega_math/cli.py` — command-line execution.
- `tests/test_core.py` — executable conformance checks for core laws and reduction boundaries.
- `examples/basic.omega` — minimal source program.

## Run

```bash
python -m pip install -e .
omega-math examples/basic.omega
python -m pytest
```

The surface syntax is a reference syntax; it is not promoted to a new canonical mathematical layer. Future syntax changes must preserve the typed semantic contract.

## Scope

This runtime does not assign physical meanings to signs, transition indices, transformation cost, geometry, probability or causality. Physical bridges remain external exactly as specified by v0.9.

`specification ≠ implementation ≠ physical theory`
