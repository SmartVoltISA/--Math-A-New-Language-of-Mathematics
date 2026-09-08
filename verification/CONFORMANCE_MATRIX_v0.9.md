# Ω-Math v0.9 — Executable Conformance Matrix

This matrix records the boundary between the canonical language specification and the reference implementation.

| Canonical operator | Runtime | Text parser | Automated test | v0.9 status |
|---|---|---|---|---|
| DIST | yes | yes | yes | implemented |
| INCIDENT | yes | no | core coverage | implemented |
| PATH | yes | yes | yes | implemented |
| PATH_EQ | yes | yes | yes | implemented |
| CYCLE | yes | yes | yes | implemented |
| CONCAT | yes | API | yes | implemented |
| SIGN | yes | yes | yes | derived |
| COMPARE | yes | no | core coverage | implemented |
| TRANSFORM | yes | API | yes | implemented |
| OBSERVE | yes | API | yes | implemented |
| EQUIV | yes | API | yes | task-relative |
| QUOTIENT | yes | no | yes | derived |
| INVARIANT | yes | no | yes | derived |
| BEHAVIOR | yes | no | yes | derived |
| COST | yes | no | yes | declared cost |
| DISTANCE | yes | no | yes | candidate |
| SYMMETRY | yes | no | yes | derived orbit |
| RETAIN | yes | no | hook | semantic hook |
| ORDER | yes | no | yes | internal order |
| HORIZON | yes | no | yes | finite horizon |
| BRANCH | yes | no | yes | nondeterministic |
| REACH | yes | no | yes | reachability |
| MODEL | yes | no | yes | representation hook |
| FEEDBACK | yes | no | hook | semantic hook |
| COARSE | yes | no | hook | task-relative |

## Explicitly external / not primitive

The following remain intentionally outside the minimal executable primitive core:

- `REL_COMPOSE`
- `REL_ID`
- `REL_INV`
- universal `CAUSE`
- `PROB`
- physical `TIME`
- physical `ENERGY`

Their absence is deliberate and is not treated as an implementation defect.

## Parser boundary

The current parser deliberately exposes only a small reference surface: entity, relation, path, `dist`, `sign`, `cycle`, and `path_eq`. The runtime API is therefore currently richer than the text syntax.

This document makes that asymmetry explicit rather than pretending the parser is complete.

## Verification rule

A canonical operator is considered mechanically conformant only when:

1. its declared type/signature is preserved;
2. its runtime semantics are implemented without adding forbidden physical meaning;
3. at least one deterministic test exercises it;
4. negative/invalid cases are tested where the type system requires rejection.

**Status: WORKING CONFORMANCE RECORD / v0.9**
