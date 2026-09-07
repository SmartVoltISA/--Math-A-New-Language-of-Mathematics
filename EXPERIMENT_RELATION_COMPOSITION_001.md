# Ω-Experiment RELATION-COMPOSITION-001 — Exhaustive Length-3 Reduction Test

## Question

Can primitive relation signs be reduced along length-3 paths without losing distinctions relevant to the path itself or to an explicitly defined propagation behavior?

## Primitive space

Relation signs:

`R = {−1,+1}`.

For a length-3 path

`P = (r₁,r₂,r₃)`

there are exactly `2³ = 8` ordered sign sequences.

A candidate scalar reduction is sign product:

`σ(P)=r₃ r₂ r₁`.

## Exhaustive cases

| Path signs | Product |
|---|---:|
| `(+,+,+)` | `+` |
| `(+,+,−)` | `−` |
| `(+,-,+)` | `−` |
| `(+,-,−)` | `+` |
| `(−,+,+)` | `−` |
| `(−,+,−)` | `+` |
| `(−,−,+)` | `+` |
| `(−,−,−)` | `−` |

Thus four length-3 sign sequences map to `+1` and four map to `−1`.

## Immediate consequence

The map

`P → σ(P)`

is many-to-one.

For example:

`(+,+,−)` and `(+,-,+)` have the same product `−1` but different ordered sign sequences.

Therefore the product is a summary, not an injective encoding of the path.

## Structural counterexample

Construct two paths with the same endpoints and the same product:

`P₁: A —(+1)→ B —(+1)→ C —(−1)→ D`

`P₂: A —(+1)→ B —(−1)→ C —(+1)→ D`.

Both have:

`σ(P₁)=σ(P₂)=−1`.

But the sign change occurs at a different position in the path. If a transition rule is sensitive to intermediate relation states, the two paths can produce different behavior while their scalar products remain equal.

## Reversal

For a reversed path, the ordered sequence is reversed. Sign multiplication gives the same scalar product because multiplication is commutative:

`r₃ r₂ r₁ = r₁ r₂ r₃`.

Therefore product reduction cannot encode directional ordering of signs.

This does not mean reversed paths are behaviorally equivalent; it means only that this scalar summary cannot distinguish them.

## Decision

`PATH → SIGN PRODUCT` is **NOT INFORMATION-PRESERVING**.

`SIGN PRODUCT` remains a valid derived summary when the only required observable is parity of negative relations.

It must not be promoted to the universal Ω path-composition law.

## Next test

Construct minimal transition systems in which two paths have equal sign product but different intermediate organization, then test whether the declared dynamics distinguishes them. The smallest successful example will establish that sign-product equivalence is insufficient for behavioral equivalence.

## Status

`FORMALLY CONSTRUCTED / COUNTEREXAMPLE`
