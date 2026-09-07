# Ω-Experiment STRUCTURE-004 — Same Counts, Same Degrees, Same Components, Different Geometry of Paths

## 1. Question

Can two relational systems remain distinguishable when the following are identical?

- number of entities;
- entity states;
- number of relations;
- relation-sign counts;
- connected-component count;
- degree sequence;
- cycle rank.

If yes, these aggregate quantities are insufficient to characterize organization.

## 2. Construction

Use six entities, all in state `1`:

`A=(1,1)`
`B=(2,1)`
`C=(3,1)`
`D=(4,1)`
`E=(5,1)`
`F=(6,1)`

For clarity, represent each undirected structural adjacency by two opposite Ω-relations of sign `+1`. Thus every structural adjacency contributes two directed relations.

### Ω₄A

Structural adjacencies:

`A-B, A-C, A-D, A-E, B-C, B-D, C-F`

### Ω₄B

Structural adjacencies:

`A-B, A-C, A-D, A-E, B-C, B-D, C-E, C-F`

The two systems as written above do **not** have equal edge count, so this pair is rejected as an isolated test.

We therefore use the corrected equal-count pair below.

### Ω₄A — final

`A-B, A-C, A-D, A-E, B-C, B-D, C-F`

### Ω₄B — final

`A-B, A-C, A-D, B-C, B-D, C-E, C-F`

Both have 7 structural adjacencies.

Their sorted degree sequences are identical:

`(4,3,3,2,1,1)`.

Both are connected.

Both have cycle rank:

`β₁ = E − V + 1 = 7 − 6 + 1 = 2`.

All relations carry the same sign `+1`.

Thus the obvious aggregate quantities listed in Section 1 are matched.

## 3. The remaining difference

The systems differ in how the terminal low-degree vertices are positioned relative to the central structure.

With perturbation originating at `A`, the shortest-path distance distributions are different.

For Ω₄A:

`{0,1,1,1,1,2}`.

For Ω₄B:

`{0,1,1,1,2,2}`.

Therefore the path geometry from the selected perturbation source differs even though degree sequence, component count, edge count and cycle rank are matched.

## 4. Dynamic test

Use the same explicit propagation rule:

> At each step, every entity directly reached by an outgoing relation from a changed entity copies that changed state at the next step.

Perturb:

`t0: A=0`, all others `=1`.

Because every structural adjacency is represented in both directions, propagation follows the structural adjacency.

The earliest arrival times from `A` are:

### Ω₄A

`A:0`

`B,C,D,E:1`

`F:2`.

### Ω₄B

`A:0`

`B,C,D:1`

`E,F:2`.

Thus the same perturbation produces different temporal profiles.

## 5. Result

This construction isolates a stronger statement than the previous experiments.

The following can all be equal:

`composition`

`relation count`

`sign count`

`component count`

`degree sequence`

`cycle rank`

while the systems still differ in path geometry and in their dynamic response.

Therefore:

`aggregate structure ≠ complete organization`.

A finite list of common graph statistics cannot automatically be declared a complete state description for Ω dynamics.

## 6. Why this matters for equivalence

Suppose an observation map records only:

`N, |R|, degree sequence, component count, β₁`.

Then Ω₄A and Ω₄B are observationally equivalent under that map.

But the perturbation response distinguishes them.

Therefore:

`static aggregate equivalence ≠ behavioral equivalence`.

The missing information is relational arrangement at path level.

## 7. New candidate hierarchy

The experiments now suggest a hierarchy of increasingly discriminating descriptions:

`entity states`

`→ relation counts`

`→ degree structure`

`→ component/cycle statistics`

`→ path geometry`

`→ dynamic response`

This is a research hierarchy, not a theorem that every level strictly contains the previous one for every system.

## 8. Collapse implication

A quotient that preserves only aggregate statistics can merge systems with different future behavior.

Therefore a valid dynamic collapse must specify the behavior it is required to preserve.

This gives a sharper definition target:

> A dynamic structural quotient is acceptable only relative to an explicitly declared class of observations and transitions whose relevant distinctions it preserves.

## 9. Status

`FORMALLY CONSTRUCTED`

The construction demonstrates existence of non-isomorphic structures with matched selected aggregate statistics and different path-distance profiles.

The propagation rule remains an experimental rule, not a physical law.

## 10. Next step

Move from individual graph statistics to a direct object:

`PATH PROFILE(Ω, source)`

and test whether path profiles can serve as a sufficient structural description for the selected dynamics.

Then test whether two systems with identical path profiles can still have different behavior.

If such a counterexample exists, the hierarchy must be extended again.
