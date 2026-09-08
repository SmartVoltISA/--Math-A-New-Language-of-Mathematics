# Ω-Math Experiment — LIGHT Bridge 005

## Status

`EXECUTED / FINITE ALGEBRAIC VERIFICATION`

## Question

What is the weakest additional mathematical structure required to turn an ordered loop into a nontrivial residual, rather than merely a scalar sign summary?

## Motivation

LIGHT's gauge structure separates a local connection from its curvature/field strength. The Ω v0.9 tests established that the ordered path is representable, while the scalar sign product is not sufficient for loop-sensitive tasks. This experiment asks whether a minimal transport law explains the missing operation without promoting physical gauge structure to an Ω primitive.

## Frozen Ω boundary

The v0.9 primitive relation state remains:

`RelationState = {−1,+1}`.

No physical connection, gauge field, curvature, vector space, or differential form is added to Ω.

## Minimal external transport model

Let each entity carry a local finite state set

`X = {0,1,2}`.

For each directed relation `r : x→y`, assign a bijective transport map

`T_r : X→X`.

Composition of transports along a path is ordinary function composition. The identity transport is the identity map on `X`.

For a closed path

`L = (r_1,...,r_n)`

based at `x`, define its holonomy

`H(L) = T_{r_n} ∘ ... ∘ T_{r_1}`.

A loop has a trivial residual when `H(L)=id`; it has a nontrivial residual when `H(L)≠id`.

## Finite counterexample

Use the closed four-cycle

`A→B→C→D→A`.

Assign:

- `T_AB = (0 1)`;
- `T_BC = (1 2)`;
- `T_CD = id`;
- `T_DA = id`.

The resulting loop transport is

`H = (1 2) ∘ (0 1)`,

which maps

`0→2`, `1→0`, `2→1`.

Therefore

`H ≠ id`.

The loop has a nontrivial residual even though every edge may carry the same Ω relation sign `+1`.

## Why order matters

The two local transports `(0 1)` and `(1 2)` do not commute. Reversing their order gives a different permutation.

Thus the residual depends on ordered composition, not on an additive/counting summary of edge labels.

This supplies the missing structural ingredient identified by LIGHT:

`local comparison → transport → ordered composition → loop holonomy/residual`.

## Representation versus primitive

The test does **not** show that Ω must add `TRANSPORT` or `CURVATURE` as primitive types.

It shows a precise boundary:

- Ω v0.9 already represents the loop/path;
- scalar relation signs do not contain enough algebra to generate nontrivial noncommutative transport;
- a richer transport/composition structure can generate a loop residual;
- that richer structure is an external mathematical extension unless independently derived from Ω primitives.

## Gauge-change invariance check

If local frames are changed by bijections `g_x` at each entity, each edge transport changes by

`T'_{xy} = g_y ∘ T_{xy} ∘ g_x^{-1}`.

For a closed loop based at `x`, the holonomy changes by conjugation:

`H'(L) = g_x ∘ H(L) ∘ g_x^{-1}`.

Therefore the property

`H(L)=id`

is invariant under local frame changes. The exact permutation representative is not invariant, but trivial/nontrivial holonomy is.

This is the finite abstract analogue of the distinction between representation-dependent connection data and a loop-level invariant. It is an analogy, not a derivation of electromagnetism.

## Decision

`PASS — transport law is sufficient to produce a nontrivial loop residual in a finite external algebra.`

`NOT DERIVED — transport law is not derivable from Ω v0.9 scalar relation signs alone.`

## Consequence for Ω

The next possible extension is not `CURVATURE` as a primitive. The mathematically cleaner candidate is a typed **transport/composition layer** with explicitly declared state space, composability, identity and transformation laws.

Such an extension must remain outside v0.9 until it passes:

1. minimality;
2. type separation;
3. associativity/identity checks;
4. information-loss analysis;
5. cross-domain verification;
6. comparison with existing mathematics.

## Final boundary

`relation sign → loop residual` is insufficient.

`relation + declared transport algebra → loop residual` is sufficient in the tested finite model.

Therefore LIGHT has not yet found a missing primitive in Ω, but it has identified a concrete mathematical layer above the current core that is worth investigating.
