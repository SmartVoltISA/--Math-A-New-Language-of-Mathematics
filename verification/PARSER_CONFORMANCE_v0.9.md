# Ω-Math v0.9 — Reference Parser Conformance

## Purpose

The parser is a deterministic executable reference surface for a deliberately small subset of the canonical Ω-Math v0.9 operator inventory. It is **not** the definition of the language and does not claim to expose every canonical operator through text syntax.

## Supported surface

| Surface form | Canonical operation | Constraint |
|---|---|---|
| `entity A 0` / `entity A 1` | EntityState | only `0` or `1` |
| `relation A B +1 r` / `-1` | RelationState | only `-1` or `+1`; endpoints must exist |
| `path P = A->B->C` | PATH | every adjacent pair must have a declared relation |
| `path E = epsilon(A)` | empty path `ε_A` | identity is anchored at entity `A` |
| `concat R = P + Q` | CONCAT | endpoint compatibility required; empty path is identity |
| `incident A r` | INCIDENT | explicit entity/relation lookup |
| `dist A B` | DIST | typed entity comparison |
| `sign P` | SIGN summary | non-empty path only; product is a summary, not path identity |
| `cycle P` | CYCLE | non-empty closed path |
| `path_eq P Q` | PATH_EQ | exact sequence equality |

## Rejection rules

The parser must reject, rather than reinterpret:

- entity state outside `{0,1}`;
- relation sign outside `{-1,+1}`;
- relation endpoints referencing undeclared entities;
- paths containing undeclared entities or missing relations;
- incompatible path concatenation;
- use of `0` as an implicit relation-absence value;
- duplicate entity/relation/path identifiers;
- unsupported external semantics such as `CAUSE` and `PROB`.

## Intentionally not parsed

The following remain runtime/framework/external concepts and are not assigned accidental surface syntax by this parser:

`COMPARE`, `TRANSFORM`, `OBSERVE`, `EQUIV`, `QUOTIENT`, `INVARIANT`, `BEHAVIOR`, `COST`, `DISTANCE`, `SYMMETRY`, `RETAIN`, `ORDER`, `HORIZON`, `BRANCH`, `REACH`, `MODEL`, `FEEDBACK`, `COARSE`, physical time, physical energy, probability, and universal causal semantics.

Their omission from the parser is an explicit scope decision, not a claim that the corresponding canonical operator is undefined.

## Verification

Automated tests cover valid reference programs, empty-path identity, typed-domain rejection, endpoint rejection, relation-absence rejection, unsupported semantic rejection, and incompatible concatenation.

The canonical semantics remain defined by the v0.9 specification documents and runtime; the parser is only one executable surface over that boundary.
