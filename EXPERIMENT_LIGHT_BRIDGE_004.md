# Ω-Math Experiment — LIGHT Bridge 004

## Status

`EXECUTED / ALGEBRAIC BOUNDARY TEST`

## Question

Can the existing Ω v0.9 relation-sign algebra produce a nontrivial loop residual analogous in role to curvature without importing additional algebraic structure?

## Frozen primitives

Relation signs are:

`RelationState = {−1,+1}`.

The existing derived path summary is the sign product:

`Σ(P)=∏ sign(r_i)`.

Path concatenation preserves the ordered relation sequence, while the sign product compresses it to one commutative value.

## Test construction

Use one directed four-cycle:

`A→B→C→D→A`.

Assign two different sign configurations to the same four ordered edges:

`L1 = (+1,+1,−1,−1)`

`L2 = (+1,−1,+1,−1)`.

Both configurations therefore have:

- the same four entities;
- the same four directed edges;
- the same closed-loop topology;
- two `+1` and two `−1` relation states;
- sign product `+1`.

Yet the ordered sign organization around the loop differs.

Because multiplication in `{−1,+1}` is commutative,

`Σ(L1)=Σ(L2)=+1`.

## Result

The existing scalar sign algebra cannot distinguish these two loop assignments.

A task that inspects ordered edge organization can distinguish them, while the scalar summary `Σ` cannot. Hence the sign product is not a sufficient representation for such a loop-sensitive task.

## Stronger boundary

A curvature-like quantity in LIGHT is not merely a sign count/product. It depends on how local field/connection data vary and combine around a loop. The Ω v0.9 core currently retains the ordered path itself, so the information has not been destroyed at the representation level; what is missing is a universally defined operator that maps that ordered local structure to a nontrivial residual.

Thus:

`ordered loop representation: available`

`universal loop-residual operator: not derived`.

## Decision

`PASS — algebraic boundary identified.`

The test does not justify adding `CURVATURE` as a primitive.

It establishes that a curvature-like reduction cannot be obtained universally from the existing scalar sign product. Any future residual operator requires additional declared structure, such as a transport/composition law or another mathematical representation.

## Relation to information-loss rule

This is consistent with the canonical sufficiency condition:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

Here the sign-product map `Q=Σ` identifies `L1` and `L2`, while a task that observes ordered loop organization can distinguish them. Therefore `Σ` is not sufficient for that task.

## Cross-domain caution

No physical gauge theory has been imported into the Ω core by this result. The LIGHT connection/curvature analogy remains an external motivation for asking the question.
