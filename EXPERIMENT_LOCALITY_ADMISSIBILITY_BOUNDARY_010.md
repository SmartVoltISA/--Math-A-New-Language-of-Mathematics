# Ω-Math — EXPERIMENT_LOCALITY_ADMISSIBILITY_BOUNDARY_010

## Status

`EXECUTED / FINITE VERIFICATION`

## Question

Can locality, admissibility, and boundary restrictions be represented as declared predicates/constraints over existing Ω objects without introducing new primitive types?

## Frozen core

No new primitive type or value is introduced. The test uses only:

- entities and relations;
- configuration/state;
- paths/reachability;
- declared transformations/transition rules;
- observation of successor/reachable sets;
- quotient/reduction.

## Definitions

For a configuration `C`:

`Loc_C(x,y) ∈ {false,true}` is a declared locality predicate over existing entities.

`Adm_C(r) ∈ {false,true}` is a declared admissibility predicate over an existing relation/transition candidate.

A boundary is represented by a declared domain/interface partition `S ⊂ E`; cross-boundary transitions are a subset of existing transitions and may be admitted or rejected by `Adm_C`.

For nondeterministic dynamics, admissibility restricts the successor set before behavioral equivalence is evaluated. For deterministic dynamics it is a precondition on the declared transformation.

## Finite model

Entities: `E={0,1,2,3}`.

Directed relation candidates:

`R={(0,1),(1,2),(2,3),(0,3)}`.

Initial source: `{0}`.

### Locality controls

`Loc_chain` permits nearest-neighbor pairs only.

`Loc_all` permits all directed pairs needed by the finite model.

Both operate on the same relational configuration; locality is therefore a declared semantic constraint, not identical to graph connectivity.

### Admissibility control

All listed relations are initially admissible. A restricted model removes `(1,2)` from the admissible set while leaving the underlying relation candidate present.

### Boundary control

Take `S={0,1}`. The relation `(1,2)` crosses the interface. Boundary restriction removes this cross-boundary transition from the admissible set while retaining the entities and underlying relation candidate.

## Executed checks

### Check A — connectivity does not determine locality-dependent propagation

With the same source and relation candidates:

- chain locality gives one-step reachable set `{0,1}`;
- broader locality gives one-step reachable set `{0,1,3}`.

Thus connectivity/edge existence does not uniquely determine the propagation neighborhood once locality is an explicit semantic condition.

### Check B — admissibility restricts propagation without changing object types

At horizon 3:

- all listed transitions admitted: `{0,1,2,3}`;
- `(1,2)` inadmissible: `{0,1,3}`.

The difference is produced by a Boolean predicate over existing transition candidates. No new primitive object is required.

### Check C — boundary can be a domain/interface restriction

For `S={0,1}`, rejecting the cross-boundary transition `(1,2)` gives the same restricted reachable set `{0,1,3}` at horizon 3.

The boundary therefore need not be a new primitive type: it can be represented by a declared subset/interface plus an admissibility rule.

### Check D — interaction with quotient/information loss

On local state space `X={0,1,2}`, define `T(0)=1`, `T(1)=0`, `T(2)=2` and quotient `Q(0)=Q(1)=0`, `Q(2)=1`.

Then `T ≠ id_X`, while the induced quotient action is identity: `Q∘T = Q`.

Therefore a quotient may erase a transformation/loop residual even when the pre-quotient dynamics are nontrivial. This is an information-loss effect, not evidence for a missing locality or boundary primitive.

## Verification method

The finite model was executed by exhaustive enumeration of the declared finite sets and direct reachability computation. The quotient masking example was evaluated directly as finite functions.

## Result

`PASS — LOCALITY, ADMISSIBILITY, AND BOUNDARY ARE REPRESENTABLE AS DECLARED SEMANTIC PREDICATES/DOMAIN RESTRICTIONS OVER EXISTING Ω OBJECTS.`

No new Ω primitive type is justified.

The result also strengthens the existing separation:

`relation exists ≠ relation is local ≠ relation is admissible ≠ relation crosses a declared boundary`.

These are distinct predicates/constraints over existing objects and must not be silently identified.

## Limits

This is a finite representational verification, not a derivation of physical locality, causality, spacetime boundaries, or Maxwell boundary conditions.

The result does not prove that every possible physical locality/boundary theory can be encoded without extension. It establishes only that the tested abstract constructions do not require a new primitive type.

`EXPERIMENT_POINT_009.md` remains untouched and remains `PREREGISTERED / TEST PROTOCOL`; its undefined phrase about causal propagation crossing `∂S` is not silently resolved here.
