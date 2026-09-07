# Ω-Math v0.9 — Transformation Layer

## Purpose

The transformation layer connects static relational structure to dynamics without assuming physical time, energy, probability or metric geometry.

## Transformation

A transformation is a declared mapping between typed states. It must specify domain, admissible outputs, changed/preserved components, controls and whether it is deterministic or branching.

`T:S→S'`

For compatible transformations, ordinary function composition supplies:

`T₂∘T₁:S₀→S₂`.

Identity and associativity hold on declared compatible domains. An inverse exists only when the two-sided inverse conditions are satisfied.

Non-invertibility is not automatically physical irreversibility.

## Change

`COMPARE(S,S')→ChangeRecord` is the comparison layer. Ordinary subtraction is not primitive.

## Transformation classes

Ω distinguishes entity-state, relation, structural, observation, quotient/coarse-graining and dynamical transformations. These descriptions must not be conflated.

## Distance

Given an admissible transformation family `𝒯` and declared cost `c`, a candidate structural distance is

`d_𝒯(S,S') = inf{c(τ): τ∈𝒯(S,S')}`.

Metric status requires verification of the relevant axioms on the declared domain. Transformation cost is not physical energy by definition.

## Information loss

Collapse is described relative to a declared observation/equivalence relation. A quotient or many-to-one transformation is not automatically destruction of the underlying system.

## Symmetry and invariants

Invariants are properties preserved by a declared transformation family. Symmetry is preservation up to a declared equivalence. Label-permutation controls are used to separate structural content from naming artifacts.

## v0.9 closure links

- Exact path equality and empty-path identity are defined in `FRONTIER_CLOSURE_v0.9.md`.
- Infinite-horizon behavioral equivalence is derived from finite horizons.
- Nondeterministic successors are first-class.
- Quotient geometry is conditional; see `QUOTIENT_GEOMETRY_CONDITIONS.md`.
- Physical time, energy and probability remain external/independent semantics.

## Status

`DEFINED / CORE LAYER / v0.9 SYNCHRONIZED`
