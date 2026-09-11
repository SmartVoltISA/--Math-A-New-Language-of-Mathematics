# Ω-Math — Surface Syntax v1.0

**Status:** reference surface specification.

This document fixes the concrete textual syntax accepted by the deterministic reference parser. It is deliberately smaller than the semantic operator inventory: an operator can be semantically canonical without being directly expressible in the current textual surface.

## 1. Lexical rules

- Input is UTF-8 text.
- One statement occupies one line.
- Leading/trailing whitespace is ignored.
- Blank lines are ignored.
- A line whose first non-whitespace character is `#` is a comment.
- Names are non-whitespace tokens (`\S+`).
- Entity states are exactly `0` or `1`.
- Relation states are exactly `+1` or `-1`.

## 2. Declarations

### Entity

```text
entity <name> <state>
```

Example:

```text
entity A 0
entity B 1
```

Entity names are unique within a program.

### Relation

```text
relation <src> <dst> <sign> [<relation-key>]
```

Example:

```text
relation A B +1 rAB
relation B C -1 rBC
```

Endpoints must already be declared. Relation keys are unique. If a key is omitted, the parser generates a deterministic internal key; explicit keys are recommended whenever a relation may need to be identified independently of its endpoints.

## 3. Paths

### Empty path

```text
path <name> = epsilon(<entity>)
```

This is the unique surface form for an empty path and represents the path identity at that entity.

### Non-empty path

```text
path <name> = <entity>-><entity>->...
```

At least two entities are required. Every consecutive pair must have exactly one matching relation in the current reference surface.

If several relations connect the same ordered pair, the path is rejected as **ambiguous** rather than selecting one silently. This prevents hidden information loss.

An empty path written as `path P = A` is rejected; use `epsilon(A)`.

## 4. Sequential composition

```text
concat <name> = <path> + <path>
```

The two paths must be endpoint-compatible. The empty path acts as the identity when its endpoint matches the adjoining path endpoint.

The `+` in this statement is **path concatenation syntax**, not arithmetic addition and not the `+1` relation state.

## 5. Queries

### Incidence

```text
incident <entity> <relation-key>
```

Returns whether the entity is an endpoint of the selected relation.

### Entity distinction

```text
dist <entity> <entity>
```

Returns `0` for equal entity objects and `1` otherwise.

This is a typed distinction operation, not a physical metric.

### Path sign summary

```text
sign <path>
```

Returns the derived product of relation signs. It is undefined for the empty path.

### Cycle predicate

```text
cycle <path>
```

Returns true exactly when the path is non-empty and its source equals its target.

### Exact path equality

```text
path_eq <path> <path>
```

Compares the complete ordered path representation. Equal sign summaries are not sufficient for equality.

## 6. Program model

The reference parser is sequential. A declaration must precede every object that depends on it.

A successful parse produces:

1. a symbol environment of entities, relations and paths;
2. an ordered IR instruction stream;
3. query results in source order.

The IR is validated independently after lowering.

## 7. Error semantics

A malformed or semantically invalid statement raises `ParseError` with its source line number.

The reference surface rejects, among other cases:

- entity state outside `{0,1}`;
- relation sign outside `{−1,+1}`;
- missing relation endpoints;
- duplicate entity/path/relation keys;
- missing path relations;
- ambiguous parallel relations in node-defined paths;
- singleton non-empty paths;
- incompatible concatenation;
- `CAUSE` or probability syntax without an explicitly admitted external semantics;
- implicit relation absence represented by `0`.

## 8. Surface syntax versus semantic language

The semantic Ω-Math language contains a broader operator inventory (`TRANSFORM`, `OBSERVE`, `EQUIV`, `QUOTIENT`, `INVARIANT`, `BEHAVIOR`, `DISTANCE`, `SYMMETRY`, `RETAIN`, `ORDER`, `HORIZON`, `BRANCH`, `REACH`, `MODEL`, `FEEDBACK`, `COARSE`, etc.). Their reference semantics are implemented in `omega_math/runtime.py`, but they are not all textual statements in v1.0.

This distinction is intentional:

`semantic operator ≠ surface syntax ≠ primitive`.

A future surface construct must lower to an explicitly validated IR operation before it becomes part of the conformance grammar.

## 9. Design invariant

The parser must never resolve ambiguity by silently choosing a relation, invent an inverse edge, reinterpret `0` as relation absence, or coerce entity and relation states into ordinary arithmetic.

The guiding rule is:

`explicit structure > implicit convenience`.

**Evidence class:** Definition / implementation contract.
