# Ω-Math — Geometry from Transformation Cost

## Purpose

This document defines a route by which quantitative distance may be **derived from transformations** rather than inserted as a primitive geometric axiom.

It is a construction framework, not a claim that physical space has been derived.

## 1. Admissible transformations

Let `S` and `S'` be configurations in a declared state domain `𝒮`.
Let `𝒯(S,S')` be the set of admissible transformations taking `S` to `S'`.

The admissible set must be specified before measuring distance. Different admissible sets define different notions of structural accessibility.

## 2. Transformation cost

Let

`c : 𝒯 → [0,∞]`

assign a non-negative cost to each admissible transformation.

No physical energy interpretation is allowed unless separately established.

## 3. Derived directed distance

Define

`d_c(S,S') = inf { c(T) : T ∈ 𝒯(S,S') }`.

If no admissible transformation exists, the value may be `∞`.

This quantity is derived from the transformation system plus its cost, not introduced as primitive geometry.

## 4. When a metric follows

`d_c` is a metric only if the declared transformation/cost system establishes:

1. `d_c(S,S') ≥ 0`;
2. `d_c(S,S') = 0` iff `S` and `S'` are identical at the selected resolution;
3. `d_c(S,S') = d_c(S',S)`;
4. `d_c(S,S'') ≤ d_c(S,S') + d_c(S',S'')`.

The triangle inequality follows when transformations compose and their costs are subadditive. Symmetry requires reversible equal-cost transformations; it must not be assumed.

## 5. Directed geometry

If reversal is impossible or has a different cost, the natural object is a directed distance/quasi-metric rather than a metric.

This is compatible with Ω-Math because relation direction and transformation direction are retained rather than silently symmetrized.

## 6. Symmetry and invariance

For a symmetry transformation family `G`, a structural distance should satisfy the appropriate invariance condition, for example:

`d_c(gS,gS') = d_c(S,S')`.

Whether this holds is a theorem to be tested from the cost and transformation definitions.

## 7. Geometry as quotient

A geometric space may be sought by identifying configurations that are equivalent under a declared relation `≈` and then studying the induced distance on equivalence classes:

`D([S],[S']) = inf { d_c(x,y) : x∈[S], y∈[S'] }`.

Well-definedness requires proof that the quotient and distance are compatible. A quotient must not erase distinctions that the selected dynamics still use.

## 8. Comparison with ordinary graph distance

Graph shortest-path distance may be used as an external comparison baseline. It must not be inserted as the Ω definition of distance.

Questions for comparison:

- when does transformation distance equal graph distance?
- when does it differ because relation signs matter?
- when does it become directed?
- which structural information is lost by the scalar distance?

## 9. Falsification targets

The construction fails as a useful geometric layer if, for the intended transformation family:

- zero-cost distinct states occur without an accepted equivalence;
- triangle inequality systematically fails without a directed/generalized interpretation;
- the result is dominated by arbitrary encoding choices;
- label permutations alter structural distances;
- no stable quotient or invariant geometry can be obtained;
- physical mappings require hidden imported spatial assumptions.

## Status

`DEFINED FRAMEWORK / METRIC OPEN`.

No physical space, physical time, energy or fundamental metric has been derived by this document.
