# Ω-Math Experiment — Relational Geometry 001

## Status

`EXECUTED / SUPPORTED UNDER DECLARED FINITE MODEL`

## Question

Does allowing relation addition/removal produce a valid structural distance without inserting physical coordinates?

## Model

Use two entities and one undirected relation slot.

Entity states:

`{0,1}`

Relation states:

`{absent, −1, +1}`

A configuration therefore has three typed components.

Elementary unit-cost edits:

- entity-state flip;
- relation add;
- relation remove;
- relation sign flip.

## Exhaustive test

All `2 × 2 × 3 = 12` configurations were enumerated.

For the fixed representation, distance is the minimum number of elementary edits.

### Tests

1. `d(C,C)=0` for all 12 configurations.
2. `d(C,C')≥0` for every pair.
3. `d(C,C')=d(C',C)` because every edit has an equal-cost inverse.
4. Triangle inequality was checked exhaustively over all ordered triples.
5. Relabeling the two entities and taking the minimum over the identity/swap correspondence preserves the metric axioms in this finite model.

## Result

All five tests passed.

The construction therefore gives a genuine finite metric on structural configurations for the declared reversible unit-cost edit system, and a quotient metric under the two-element relabeling group for this model.

## Important limitation

This does not establish a universal metric for Ω-Math.

It establishes only that the proposed construction is mathematically coherent for the declared finite model.

Changing costs, allowing directed edits, changing the relation domain, permitting entity insertion/deletion, or changing the admissible relabeling group creates a different geometry and must be tested separately.

## Interpretation

The significant step is not the numerical value of the distance. It is that the metric can now respond to **topological change**:

`no relation ↔ relation`

rather than only to value changes inside a fixed graph encoding.

No physical distance or physical energy has been assumed.
