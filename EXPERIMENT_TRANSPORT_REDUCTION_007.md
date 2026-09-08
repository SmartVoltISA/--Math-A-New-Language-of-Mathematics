# Ω-Math Research Experiment — Transport Reduction 007

## Status

`EXECUTED / STRUCTURAL DERIVATION`

## Question

Does the proposed typed transport layer require a new Ω primitive, or can transport be represented as a typed specialization of the existing transformation layer?

## Starting point

Ω v0.9 already defines a transformation as a declared mapping between typed states/configurations, with ordinary composition on compatible domains. The transport candidate assigns a map

`T_r:X_x→X_y`

to each relation `r:x→y`.

The question is whether this is genuinely new structure or an indexed use of existing transformations.

## Reduction construction

Let each local state set `X_x` be an explicitly declared state domain/substate associated with entity `x`.

For every relation `r:x→y`, declare a transformation

`τ_r : X_x→X_y`.

This is type-compatible with the existing Ω transformation schema.

For a path

`P=(r_1,...,r_n)`,

ordinary transformation composition gives

`τ_P = τ_{r_n}∘...∘τ_{r_1}`.

This is exactly the proposed path-transport rule.

For the empty path,

`τ_{ε_x}=id_{X_x}`

is the identity transformation on the local state domain.

For a closed path `L` based at `x`, the residual predicate is simply

`Nontrivial(L) ⇔ τ_L ≠ id_{X_x}`.

The comparison `≠` is a declared equality test between transformations, not a new arithmetic operation.

## Consequence

The core algebraic mechanism

`relation → local map → ordered composition → loop residual`

does not require a new primitive operation if the model is permitted to declare local state domains and relation-indexed transformations.

Therefore the previous `TRANSPORT_LAYER_v0.1.md` should be interpreted primarily as a **typed construction/schema over the existing Transformation layer**, not automatically as a new primitive type.

## What remains genuinely additional

The reduction does not make every transport feature free. A model must still explicitly declare:

1. the local state domains `X_x`;
2. which transformations are attached to which relations;
3. the admissible domain/codomain of each transformation;
4. the equality/comparison rule for transformations;
5. whether local frame changes are allowed;
6. if frame changes are allowed, which maps are isomorphisms and therefore invertible.

These are model declarations, not automatically new Ω primitives.

## Relation sign remains independent

The Ω relation

`r=(x,y,sign)`

contains only the directed endpoints and sign. The transformation `τ_r` is extra model data attached to that relation.

Therefore:

`relation sign ≠ transport action`.

A relation can have the same sign while carrying different transformations in different models.

## Minimality update

The sequence of reductions is now:

1. `EXPERIMENT_LIGHT_BRIDGE_005`: bijective transport is sufficient.
2. `EXPERIMENT_TRANSPORT_MINIMALITY_006`: arbitrary composable functions are sufficient; bijectivity is not required for residual generation.
3. `EXPERIMENT_TRANSPORT_REDUCTION_007`: such maps can be represented as typed transformations, so a separate `TRANSPORT` primitive is not currently justified.

This is a stronger minimality result than 005 alone.

## Boundary: frame covariance

Gauge/frame-change behavior remains an optional stronger construction. If

`g_x:X_x→X_x`

is invertible, then

`τ'_{xy}=g_y∘τ_{xy}∘g_x^{-1}`.

For a closed loop,

`τ'_L=g_x∘τ_L∘g_x^{-1}`.

Thus identity/non-identity is preserved.

The invertibility requirement belongs specifically to this covariance construction, not to residual generation itself.

## Decision

`PASS — transport is reducible to typed transformations plus explicit local domains.`

`NO NEW PRIMITIVE JUSTIFIED.`

The candidate transport layer remains useful as a documented schema, but the current evidence favors deriving it from existing Ω transformations rather than extending the primitive type system.

## Remaining foundational test

The next check is interaction with Ω equivalence/quotient and information loss: determine when two relation-indexed transformation systems are behaviorally equivalent, and when reducing a transport system to a scalar/sign/path summary provably loses loop behavior.
