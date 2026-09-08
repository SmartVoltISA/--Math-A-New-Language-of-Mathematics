# Ω-Math v0.9 — Runtime Conformance Matrix

This record maps the canonical operator inventory to the reference runtime. It does not change the mathematical specification.

| Operator | Runtime | `execute()` | Status |
|---|---|---:|---|
| `DIST` | `dist` | yes | covered |
| `INCIDENT` | `incident` | yes | covered |
| `PATH` | `path` | yes | covered |
| `PATH_EQ` | `path_eq` | yes | covered |
| `CYCLE` | `cycle` | yes | covered |
| `CONCAT` | `concat` | yes | covered |
| `SIGN` | `sign_summary` | yes | covered |
| `COMPARE` | `compare` | yes | covered |
| `TRANSFORM` | `transform` | yes | covered |
| `OBSERVE` | `observe` | yes | covered |
| `EQUIV` | `equiv` | yes | covered |
| `QUOTIENT` | `quotient` | yes | covered for finite declared domains |
| `INVARIANT` | `invariant` | yes | covered |
| `BEHAVIOR` | `behavior` | yes | covered for finite executable dynamics |
| `COST` | `cost` | yes | framework; not physical energy |
| `DISTANCE` | `distance` | yes | declared transformation-cost candidate |
| `SYMMETRY` | `symmetry` | yes | finite orbit under declared transformations |
| `RETAIN` | `retain` | yes | framework hook; functional effect remains a test |
| `ORDER` | `order` | yes | internal order only |
| `HORIZON` | `horizon` | yes | discrete transition depth |
| `BRANCH` | `branch` | yes | successor-set wrapper |
| `REACH` | `reach` | yes | finite horizon; task semantics supplied by goal/transition |
| `MODEL` | `model` | yes | representation hook; causal/use claim remains external |
| `FEEDBACK` | `feedback` | yes | framework hook; recurrence semantics remain task-specific |
| `COARSE` | `coarse` | yes | framework hook; emergence claim remains controlled/tested |

## Explicitly outside the primitive runtime

The following remain intentionally unavailable as primitive operators:

- `REL_COMPOSE`
- `REL_ID`
- `REL_INV`
- `CAUSE`
- `PROB`
- `ENERGY`
- `TIME_PHYSICAL`

Their absence is conformant with `OPERATOR_TABLE.md` and the v0.9 frontier boundary.

## Important distinction

Runtime presence means that a reference implementation exists for the declared computational framework. It does **not** mean that every natural-language theorem, physical interpretation, or emergence/causality claim has been proved.

Machine verification remains finite and domain-specific. The canonical documents remain authoritative for semantics.

## Verification additions in this branch

`tests/test_core.py` covers the newly exposed `QUOTIENT`, `DISTANCE`, `SYMMETRY`, and `MODEL` operators in addition to the earlier core checks.

`experiments/run_v09_verification.py` and `tests/test_experiments_v09.py` cover the frozen finite verification records for experiments 010–012.

## Status

`MACHINE CONFORMANCE RECORD / v0.9 / BRANCH omega-math-verification-v09`
