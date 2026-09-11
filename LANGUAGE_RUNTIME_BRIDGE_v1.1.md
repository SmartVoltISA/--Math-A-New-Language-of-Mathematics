# Ω-Math Language Runtime Bridge v1.1

## Purpose

This document records the boundary between the canonical semantic operator inventory, the executable reference runtime, the intermediate representation (IR), and the concrete textual parser.

The rule is:

`semantic operator ≠ surface syntax ≠ primitive`

An operator can be semantically defined and executable without already having a textual encoding.

## 1. Canonical registry

`omega_math/operator_registry.py` is the machine-readable inventory of the canonical operators.

Each entry records:

- operator name;
- signature;
- semantic status;
- textual surface, when one exists;
- IR opcode;
- reference runtime function.

The registry is metadata only. It does not duplicate runtime semantics.

## 2. Current textual surface

The reference parser currently has a deliberately small, fully executable surface:

- `entity`
- `relation`
- `path`
- `epsilon`
- `concat`
- `incident`
- `dist`
- `sign`
- `cycle`
- `path_eq`

These constructs lower to validated v1 IR and are covered by parser conformance tests.

## 3. Runtime operator layer

The reference runtime additionally implements the canonical higher-level operators:

`COMPARE`, `TRANSFORM`, `OBSERVE`, `EQUIV`, `QUOTIENT`, `INVARIANT`, `BEHAVIOR`, `COST`, `DISTANCE`, `SYMMETRY`, `RETAIN`, `ORDER`, `HORIZON`, `BRANCH`, `REACH`, `MODEL`, `FEEDBACK`, `COARSE`.

Many of these require executable rules, predicates, dynamics or task functions. Arbitrary Python callables are not silently serialized into textual syntax.

## 4. IR CALL bridge

IR v1.1 adds:

`CALL(operator_name, operands)`

This is an in-memory bridge for runtime operators whose operands may be executable objects.

Validation requires:

- a non-empty operator name;
- operands represented as a tuple;
- exactly two top-level CALL arguments.

Execution resolves the operator through the canonical runtime dispatch table.

This does **not** make `CALL` a new mathematical primitive. It is an implementation-level IR instruction.

## 5. Deliberate non-feature

The parser must not invent syntax such as serialized Python lambdas for:

`TRANSFORM`, `OBSERVE`, `EQUIV`, `INVARIANT`, `BEHAVIOR`, `REACH`, `MODEL`, `FEEDBACK`, or similar operators.

A future textual form must be declarative, typed, deterministic in parsing, and lowerable to validated IR.

## 6. Conformance requirement

For every future surface operator:

`surface text → parser → IR → runtime → result`

must be covered by tests.

For every runtime-only operator, the implementation must remain callable through the reference runtime and/or validated `CALL` IR without claiming textual support.

## 7. Next gate

The next language implementation gate is a declarative rule/task layer. It should introduce only named, typed, non-arbitrary executable declarations and then promote selected runtime operators into textual syntax one family at a time.

No syntax is promoted merely because a Python implementation exists.

**Status: IMPLEMENTED / AUDITABLE / v1.1 bridge**
