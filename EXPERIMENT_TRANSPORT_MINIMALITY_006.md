# Ω-Math Research Experiment — Transport Minimality 006

## Status

`EXECUTED / FINITE ALGEBRAIC VERIFICATION`

## Question

Is bijectivity actually required for a transport law to generate a nontrivial ordered-loop residual?

## Motivation

`EXPERIMENT_LIGHT_BRIDGE_005.md` demonstrated that bijective local transports are sufficient for nontrivial holonomy. The phrase “weakest additional structure” was intentionally left open. This experiment tests that minimality claim directly.

## Frozen Ω boundary

The Ω v0.9 primitive types are unchanged:

- `EntityState = {0,1}`
- `RelationState = {−1,+1}`
- `Path` remains an ordered compatible sequence of relations.

No transport is promoted to an Ω primitive by this experiment.

## Minimal candidate

Let each vertex/entity `x` carry a set `X_x`.

For each directed relation `r:x→y`, assign an arbitrary function

`T_r : X_x → X_y`.

No injectivity or surjectivity is assumed.

For compatible paths,

`T_{P⧺Q} = T_Q ∘ T_P`.

For every entity `x`, the empty path has identity transport

`T_{ε_x} = id_{X_x}`.

Function composition supplies associativity automatically.

Thus the minimal algebraic package needed for ordered transport is:

1. typed local state sets;
2. typed maps along relations;
3. composability by matching source/target fibers;
4. identity maps on each fiber;
5. ordinary function composition.

Invertibility is not part of this minimal package.

## Finite non-bijective counterexample

Take a closed four-cycle

`A→B→C→D→A`

with the common local state set

`X={0,1,2}`.

Assign:

- `T_AB(0)=0, T_AB(1)=0, T_AB(2)=0` (constant; non-bijective);
- `T_BC(x)=(x+1) mod 3`;
- `T_CD=id`;
- `T_DA=id`.

The loop transport is

`H = T_DA ∘ T_CD ∘ T_BC ∘ T_AB`.

Therefore

`H(0)=1`, `H(1)=1`, `H(2)=1`.

Hence

`H ≠ id_X`.

The loop has a nontrivial residual although one transport is explicitly non-bijective.

## Associativity verification

For arbitrary composable functions,

`(T_3∘T_2)∘T_1 = T_3∘(T_2∘T_1)`.

A finite exhaustive Python check over a representative set of functions on `X={0,1,2}` found no associativity discrepancy.

The associativity result is structural: it follows from ordinary function composition, not from a special numerical rule.

## Cross-domain verification: deterministic finite automata

A deterministic finite automaton assigns a transition function

`δ_a : Q→Q`

to each input symbol `a`.

For a word `w=a_1...a_n`, the induced map is

`δ_w = δ_{a_n}∘...∘δ_{a_1}`.

This is the same typed composition law as the transport construction, but its interpretation is automata-state evolution rather than local transport on a network.

Choose `Q={0,1,2}` with

- `δ_a(x)=0` for every `x`;
- `δ_b(x)=(x+1) mod 3`.

Then

`δ_{ab}=δ_b∘δ_a`

is the constant map to `1`, and therefore is not the identity transformation.

Thus the same algebraic structure appears independently in finite-state computation.

## What this establishes

`PASS` — bijectivity is stronger than necessary for a nontrivial ordered residual.

The minimal sufficient algebraic structure for the residual itself is a typed family of composable functions with identity and associative composition.

`NOT DERIVED` — this does not prove that this structure is the unique mathematically minimal foundation in every formal sense. It establishes a strictly weaker sufficient structure than the bijective model of LIGHT Bridge 005.

## Important separation

Two different requirements must not be conflated:

### A. Residual generation

For

`H(L) ≠ id`

to be meaningful, arbitrary composable maps are sufficient.

### B. Local frame/gauge change

The transformation

`T'_{xy}=g_y∘T_{xy}∘g_x^{-1}`

requires the `g_x` to be bijections (isomorphisms) so that `g_x^{-1}` exists.

Therefore bijectivity belongs to the **frame-change/invariance layer**, not to the minimal transport-composition layer.

## Consequence

The candidate research hierarchy should be split:

`typed fibers → composable maps → identity → composition → path transport → loop residual`

and, only when required,

`fiber isomorphisms → frame change → conjugation invariance`.

No `CURVATURE` primitive is justified.

No change to the Ω v0.9 core is justified by this experiment.

## Decision

`PASS — minimal transport algebra reduced.`

The next research task is to test whether this typed-map layer can be integrated with Ω paths and transformations without duplication or hidden coercion, and whether its laws remain valid for heterogeneous local state spaces.
