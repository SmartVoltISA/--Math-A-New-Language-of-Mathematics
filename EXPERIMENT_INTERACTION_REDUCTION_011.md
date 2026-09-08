# Ω-Math — EXPERIMENT_INTERACTION_REDUCTION_011

## Status

`EXECUTED / FINITE EXHAUSTIVE VERIFICATION`

## Question

Can the combined action of locality, admissibility, boundary restriction, transformation, and quotient be represented entirely with existing Ω objects and task-relative reduction semantics?

## Frozen core

No new primitive type or operator is introduced. The model uses:

`Relation → declared Loc/Adm predicates → Transformation/transition → Path/REACH → Observation/Quotient`.

A boundary is represented by a declared subset/interface and its crossing predicate.

## Finite model

`E={0,1,2,3}` with relation candidates

`R={(0,1),(1,2),(2,3),(0,3)}`.

Each candidate is independently marked by two Boolean predicates:

- `Loc(r)` — locality admission;
- `Adm(r)` — transition admissibility.

The effective transition condition is their conjunction:

`Eff(r) = Loc(r) ∧ Adm(r)`.

For boundary `S={0,1}`, crossing is independently identified by source/target membership; it is not itself a relation state.

## Exhaustive verification

All `2^4 = 16` locality masks and all `2^4 = 16` admissibility masks were enumerated, for horizons `h=0,1,2,3`.

Total reachability cases checked:

`16 × 16 × 4 = 1024`.

For every case,

`REACH(Loc,Adm,h) = REACH(Eff,h)`

where `Eff` is the pointwise conjunction of the two declared predicates.

No discrepancy was found.

## Boundary check

For `S={0,1}`, `(1,2)` is the cross-boundary candidate. Rejecting that candidate through the admissibility predicate produces the same finite propagation result as explicitly applying the boundary restriction before transformation.

With all other candidates enabled, horizon-3 reachability changes from

`{0,1,2,3}`

to

`{0,1,3}`.

Thus the boundary operation is representable as a restriction on an existing transition domain.

## Counterexample: connectivity alone is insufficient

With all relation candidates present, horizon-1 reachability from `0` is `{0,1,3}` when all candidates are permitted.

Suppressing the `(0,3)` candidate through locality gives `{0,1}` while the underlying relation configuration remains unchanged.

Therefore the same connectivity structure can support different propagation semantics when locality is declared separately.

## Quotient interaction

Let `X={0,1,2}` and

`T(0)=1, T(1)=0, T(2)=2`.

Let

`Q(0)=Q(1)=0, Q(2)=1`.

Then `T ≠ id_X`, but

`Q∘T = Q`.

The quotient therefore erases the transformation residual. This is exactly the existing information-loss/sufficiency boundary: the reduction is not sufficient for a task that observes the pre-quotient transformation, although it is sufficient for a task that observes only the quotient state.

## Structural conclusion

The tested composition is fully expressible as:

`declared predicate/domain restriction`
`→ existing Transformation`
`→ existing Path/REACH`
`→ existing Observation`
`→ existing Equivalence/Quotient`.

No separate primitive `INTERACTION`, `LOCALITY`, `ADMISSIBILITY`, or `BOUNDARY` is justified by this finite model.

## Important qualification

The experiment establishes representability of the tested abstract constructions. It does not derive physical locality, causal structure, spacetime boundaries, interaction laws, or Maxwell boundary conditions.

Likewise, the result does not prove that every possible domain-specific interaction theory can be encoded without extension.

## Result

`PASS — THE COMBINED INTERACTION/RESTRICTION CHAIN REDUCES TO EXISTING Ω TRANSFORMATION + PATH/REACH + OBSERVATION/QUOTIENT MACHINERY.`

The v0.9 primitive core remains unchanged.
