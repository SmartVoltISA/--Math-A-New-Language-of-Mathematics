# Ω-Math Experiment — PATH-DYNAMICS-001

## Question

Is a scalar sign-product or a restricted path profile sufficient to determine future behavior under an explicit transition rule?

## Status

`FORMAL COUNTEREXAMPLE`

## Construction

Use four entities:

`A, B, C, D`

and two paths with the same endpoints and the same three relation signs:

`P1: A -(+1)-> B -(+1)-> C -(+1)-> D`

`P2: A -(+1)-> C -(+1)-> B -(+1)-> D`

Both have:

- length 3;
- sign sequence `(+1,+1,+1)`;
- sign-product `+1`;
- identical endpoint pair `(A,D)`.

They differ only in intermediate relational organization.

## Explicit deterministic propagation rule

At each step, the active entity follows the unique outgoing relation. A node may apply a declared gate:

- `B` passes propagation;
- `C` blocks propagation.

The gate is part of the transition rule, not part of the path sign summary.

Starting from `A`:

- `P1` reaches `B`, passes, then reaches `C` and stops;
- `P2` reaches `C` first and stops immediately.

Thus the future trajectory differs although sign-product, length and endpoint are identical.

## Minimal conclusion

`same sign-product + same length + same endpoints ≠ same behavior`.

A path descriptor that erases intermediate organization cannot be universally behavior-sufficient.

## Relation to behavioral equivalence

The two initial configurations are not behaviorally equivalent for horizon `h >= 1` under the declared propagation rule, despite matching the restricted scalar/path summary.

This is a direct witness that a quotient based only on sign-product (or the listed restricted profile) is not behavior-preserving.

## What is preserved

The result does **not** show that no path profile can ever be sufficient. A profile containing the complete ordered intermediate relational structure may be sufficient for this task. Sufficiency is therefore always relative to:

1. the observation map;
2. the transition rule;
3. the allowed interventions/inputs;
4. the horizon;
5. the information retained by the profile.

## Decision

`PATH -> SIGN PRODUCT` remains a valid scalar summary only.

It is **not** a universal path representation and must not be used as a behavior-preserving reduction without an explicit sufficiency proof.
