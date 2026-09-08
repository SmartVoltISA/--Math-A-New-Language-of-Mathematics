# EXPERIMENT — LIGHT Bridge 002

## Status

`EXECUTED / FINITE COUNTEREXAMPLE TEST`

## Question

Can locality and loop structure be collapsed to ordinary graph connectivity and scalar path summaries without loss of information?

## Frozen setup

Use four entities `A,B,C,D` and directed relations. Compare two structures with the same entity count and the same relation count.

### Configuration L (local chain)

`A→B`, `B→C`, `C→D`.

### Configuration G (same connectivity class, different declared locality)

Use the same connected relation graph but declare two different locality predicates:

`Loc_L(A,B)=Loc_L(B,C)=Loc_L(C,D)=true`

and all other pairs false.

For a second model define a broader locality predicate that also permits `A,C` and `B,D` local comparison while preserving the same graph connectivity.

## Test 1 — Connectivity vs locality

The underlying graph connectivity is identical in the two models, but the allowed local update neighborhoods differ.

A transition rule that updates only locally admissible neighbors therefore produces different successor sets even though ordinary connectivity is unchanged.

### Decision

`CONNECTIVITY ≠ LOCALITY`.

Locality cannot be replaced universally by graph connectivity.

## Test 2 — Path scalar summary vs loop organization

Let two paths have the same endpoints, length, and sign-product summary, but different intermediate relations. A transition rule may inspect the intermediate entity and accept one path while rejecting the other.

Therefore any proposed universal loop/curvature summary must retain enough ordered intermediate information to preserve the declared observation/transition task.

### Decision

`scalar path summary ≠ path structure`.

This agrees with existing Ω path-dynamics counterexamples.

## Test 3 — What LIGHT actually contributes

The LIGHT repository motivates locality and connection/curvature because electromagnetic theory compares field values locally and derives field strength from an antisymmetric derivative structure. This does not prove that Ω must contain a physical gauge connection.

The finite test instead establishes a weaker but reusable architectural principle:

`locality must be declared when dynamics depend on locality`.

and:

`loop-sensitive behavior requires loop/path information beyond scalar summaries`.

## Result

PASS for the negative claims:

- connectivity is not a universal substitute for locality;
- scalar path summaries are not universal substitutes for ordered loop/path structure.

No new primitive type is justified.

## Next frontier

Define the weakest algebraic structure under which a loop residual is invariant under an allowed change of local representation. If that structure requires a group/action/transport law, record it as an external mathematical extension rather than silently inserting it into Ω primitives.
