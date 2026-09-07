# Ω-Math v0.7 — Research Status

## Current state

The repository contains a typed relational language with explicit syntax, semantics, operator discipline, reduction rules, transformations, invariants/symmetry, path algebra, behavioral equivalence, structural-edit geometry, task-relative sufficient-state construction, and a declared nondeterministic transition layer.

The central discipline remains:

`define → derive → execute → verify → compare → falsify → record`.

## v0.7 mathematical milestone

### M15 — Nondeterministic dynamics

`NONDETERMINISTIC_DYNAMICS.md` extends the transition layer from a function

`T:S×U→S`

to a successor-set relation

`N:S×U→𝒫(S)`.

The language now explicitly represents branching futures rather than silently selecting one successor.

Three concepts are kept separate:

`possible ≠ probable`

`universal preservation ≠ existential preservation`

`branching semantics ≠ deterministic selection`.

### M16 — Branch-collapse counterexample

`EXPERIMENT_NONDETERMINISTIC_001.md` gives a finite executed construction where two systems have the same current observation and the same one-step observable successor set, but differ at the next horizon because one branch remains executable and the other is blocked.

Therefore a one-step summary cannot be promoted to a general two-step sufficient representation.

Status: `EXECUTED / SUPPORTED UNDER DECLARED FINITE MODEL`.

## Existing milestones

### M13 — Task-relative sufficient relational state

A candidate reduction `Q` is sufficient for finite-horizon behavior when

`Q(x)=Q(y) ⇒ B_h(x,u)=B_h(y,u)`

for every admissible input sequence.

### M14 — Structural reduction boundary

Equal source-distance profiles can yield different future trajectories under the same declared dynamics. Structural descriptors therefore require task-specific sufficiency tests.

### M9–M12 — Relational geometry

Structural edit distance, label-independent quotient distance under stated assumptions, exhaustive small-model verification and the geometry signature `Γ_h(C)` remain established/defined at their documented levels.

## Algebraic decision

`PATH CONCATENATION`: `DEFINED`.

`SIGN-PRODUCT SUMMARY`: `DERIVED`.

`SIGN-PRODUCT AS COMPLETE RELATION COMPOSITION`: `REJECTED`.

`PRIMITIVE RELATION REDUCTION`: `OPEN`.

The language does not collapse an ordered relation sequence merely because a scalar summary exists.

## Dynamics decision

`DETERMINISTIC TRANSITION`: `DEFINED`.

`NONDETERMINISTIC TRANSITION`: `DEFINED` as a successor-set relation.

`BRANCHING BEHAVIOR`: `DEFINED` for finite horizons.

`PROBABILISTIC TRANSITION`: `OPEN` — no probabilities are assigned by nondeterminism alone.

`INFINITE-HORIZON SEMANTICS`: `OPEN`.

`FAIRNESS / LIVENESS`: `OPEN`.

## Reduction principle

A reduction is not accepted because it looks structurally rich. It must preserve the exact behavior selected by the declared task.

For branching systems the preservation condition is evaluated on the declared branching behavior object or task predicate.

## Next mathematical tests

1. Exhaustively enumerate small nondeterministic transition systems and verify the recursive branching quotient.
2. Separate universal-safety and existential-reachability quotients.
3. Test whether different branching representations are equivalent under different tasks.
4. Add probability only as an explicit typed extension and compare it with nondeterministic semantics.
5. Test quotient geometry after behavioral reduction.
6. Continue unequal-cardinality and insertion/deletion geometry.
7. Investigate whether relation composition can be derived from transition behavior without imposing a primitive binary sign law.

## Explicitly open

- canonical primitive relation composition;
- canonical path equivalence;
- universal sufficient path profile;
- unrestricted canonical metric;
- general quotient geometry;
- physical time;
- probability;
- energy;
- physical ontology;
- task-independent emergence criterion;
- self-model and causal self-reference;
- independent physical predictions.

## Novelty discipline

The nondeterministic layer is treated as an Ω-Math formalization/integration, not as a claim of inventing nondeterministic transition systems or behavioral equivalence.

Any stronger novelty claim requires explicit comparison with established transition-system, automata, bisimulation and probabilistic formalisms.

## Critical methodological rule

`representable ≠ explained`

`correlated ≠ caused`

`stable ≠ fundamental`

`compressed ≠ equivalent`

`possible ≠ probable`

`emergent candidate ≠ emergence proven`

## Version

**Ω-Math v0.7** — typed relational language extended with explicit nondeterministic dynamics and branching-preserving reduction discipline.
