# Ω-Math v0.4 — Canonical Examples

These examples are deliberately small. They define the intended reading of the language without assigning physical meanings to the signs.

## 1. Two distinct entities with equal state

`A=(A,0)`

`B=(B,0)`

Then:

`A ≠ B`

but

`state(A)=state(B)=0`.

Equal state is not identity.

## 2. Present positive relation

`A —(+1)→ B`

This means a directed relation is present and its current primitive relation state is `+1`.

It does not mean attraction, force, causation or positive arithmetic unless a model explicitly defines that interpretation.

## 3. Absent relation

If `(A,C) ∉ D_R`, then no relation is modeled from `A` to `C`.

It is not represented as `0`, `−1` or `+1`.

## 4. Path

`A —(+1)→ B —(−1)→ C`

is a path with ordered sign sequence:

`(+1,−1)`

and scalar sign summary:

`Σ(P)=−1`.

The summary does not erase the fact that the intermediate entity is `B`.

## 5. Two paths with the same summary

`P1: A —(+1)→ B —(+1)→ C`

`P2: A —(−1)→ B —(−1)→ C`

Both have sign-product `+1`.

They are not thereby the same path, same relation or same behavior.

## 6. Parallel paths

If both

`A —(+1)→ B`

and

`A —(−1)→ B`

are modeled as distinct relational instances, the language does not silently replace them with a third primitive sign. Multiplicity and conflict require an explicit richer representation or reduction rule.

## 7. Transformation

Let `T_flip` change one relation sign and leave all other declared components unchanged.

Then:

`T_flip(S)=S'`.

If the transformation has unit cost, repeated flips produce a transformation-cost distance on the fixed relation-slot representation.

## 8. Observation versus identity

Let

`O(A)=0`
`O(B)=0`.

Then

`A ≈_O B`

but not necessarily

`A=B`.

## 9. Behavioral distinction

Two states can satisfy

`O(x)=O(y)`

while

`O(T(x)) ≠ O(T(y))`.

Then they are observationally equivalent at horizon `0` but not behaviorally equivalent at horizon `1`.

## 10. Reduction witness

If

`Q(x)=Q(y)`

but

`F(x)≠F(y)`,

then `Q` is not sufficient for task `F`.

This is the canonical Ω pattern for rejecting an unjustified structural collapse.

## Status

`DEFINED / REFERENCE EXAMPLES`
