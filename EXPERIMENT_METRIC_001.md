# Ω-Math Experiment — METRIC-001

## Question

Can a metric be obtained from a declared transformation system without taking distance as a primitive?

## Status

`DERIVED BASELINE`

## Domain

Fix a finite set of possible relation slots `Dᴿ` and let each configuration assign a sign in `{−1,+1}` to every occupied slot.

A primitive transformation flips the sign of exactly one occupied relation slot. Each such flip has cost `1`.

## Derived distance

For configurations `S` and `S'`, define the cost of a transformation sequence as the number of primitive flips. Then

`d(S,S') = min cost(T : S→S')`.

The minimum is exactly the number of relation slots whose signs differ between `S` and `S'`.

## Axioms

### Non-negativity

Every transformation sequence has non-negative integer cost, so `d(S,S') ≥ 0`.

### Identity of indiscernibles

`d(S,S') = 0` iff no relation sign differs, hence `S=S'` within the fixed representation.

### Symmetry

Every sign flip is reversible with the same cost, so reversing a minimum sequence gives

`d(S,S') = d(S',S)`.

### Triangle inequality

A minimum sequence from `S` to `S'` followed by one from `S'` to `S''` is an admissible sequence from `S` to `S''`. Therefore

`d(S,S'') ≤ d(S,S') + d(S',S'')`.

## Result

The transformation-cost construction produces a genuine metric on this fixed finite relation-sign space.

The resulting geometry is the discrete Hamming/hypercube geometry of relation-sign assignments. This is an important **baseline**, not a new physical law.

## Interpretation discipline

The experiment proves only that a metric can emerge from one explicit Ω transformation/cost system.

It does not prove:

- that this is the unique Ω metric;
- that it is fundamental;
- that it represents physical space;
- that transformation cost is physical energy;
- that arbitrary graph geometry follows from it.

## Next test

Replace the fixed-slot sign-flip system by transformations that can add/remove relations and change entity states. Determine which metric properties survive and which depend on the chosen cost model.
