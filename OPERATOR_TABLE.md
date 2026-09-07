# Ω-Math v0.8 — Canonical Operator Table

This is the canonical operator inventory. An operator may not silently change type or meaning between documents.

| Operator | Signature | Status | Notes |
|---|---|---|---|
| `DIST` | `Entity × Entity → Distinction` | DEFINED | typed comparison |
| `INCIDENT` | `Entity × Relation → Incidence` | DEFINED | structural query |
| `PATH` | `Relation* → Path` | DEFINED | compatible ordered sequence |
| `CYCLE` | `Path → Cycle ∪ Failure` | DEFINED | declared return criterion |
| `CONCAT` / `⧺` | `Path × Path → Path` | DEFINED | compatible endpoints |
| `SIGN` | `Path → SignSequence / Summary` | DERIVED | product is summary only |
| `COMPARE` | `State × State → ChangeRecord` | DEFINED | not subtraction |
| `TRANSFORM` | `State × Rule/Input → State or Successors` | DEFINED | deterministic or branching |
| `OBSERVE` | `State → Observation` | DEFINED | task-relative |
| `EQUIV` | `Objects × Task → Equivalence` | DEFINED | semantics declared by task |
| `QUOTIENT` | `Object × Equivalence → Quotient` | DEFINED | explicit mapping required |
| `INVARIANT` | `Property × TransformFamily → PreservationTest` | DEFINED | family-relative |
| `BEHAVIOR` | `State × Dynamics × Horizon → Behavior` | DEFINED | trace/tree/task dependent |
| `COST` | `Transformation → [0,∞]` | DEFINED FRAMEWORK | not physical energy by default |
| `DISTANCE` | `State × State → [0,∞]∪{∞}` | DERIVED | minimal declared transformation cost |
| `SYMMETRY` | `State × TransformFamily → Orbit/Action` | DEFINED |
| `RETAIN` | `State × RetentionRule → MemoryCandidate` | DEFINED FRAMEWORK | functional effect must be tested |
| `ORDER` | `TransitionSequence → OrderedIndex` | DERIVED | internal order, not physical time |
| `HORIZON` | `Dynamics × ℕ₀ → FiniteFutureDomain` | DEFINED | discrete depth |
| `BRANCH` | `State × Input → 𝒫(State)` | DEFINED | nondeterministic successors |
| `REACH` | `State × Task × Horizon → Boolean/Set` | DEFINED FRAMEWORK | existential/universal semantics declared |
| `MODEL` | `State → InternalRepresentation` | HYPOTHESIS FRAMEWORK | self-model when causally used |
| `FEEDBACK` | `State/Model × Dynamics → RecurrentDependency` | DEFINED FRAMEWORK |
| `COARSE` | `Structure × Criterion → MacroObject` | DEFINED FRAMEWORK | emergence candidate |

## Reserved / unresolved

The following are not canonical primitives:

`REL_COMPOSE` — primitive relation-to-relation collapse remains OPEN.

`REL_ID` — no primitive identity relation is required while empty-path identity is available as a structural candidate; canonical admission remains OPEN.

`REL_INV` — primitive relation inverse remains OPEN; path reversal is structural and does not imply a relation-state inverse.

`PATH_EQ` — canonical universal path equivalence remains OPEN.

`CAUSE` — causal semantics require explicit intervention/counterfactual criteria.

`PROB` — probability is a separate typed extension, not implied by branching.

`ENERGY` — physical energy is not transformation cost by definition.

`TIME_PHYSICAL` — physical duration is not transition count.

## Admission rule

Every new primitive must declare:

1. input types;
2. output type;
3. domain restrictions;
4. primitive/derived status;
5. semantics;
6. algebraic laws;
7. counterexamples/failure conditions;
8. comparison with existing mathematics;
9. tests.

## Status

`DEFINED / CANONICAL INVENTORY`
