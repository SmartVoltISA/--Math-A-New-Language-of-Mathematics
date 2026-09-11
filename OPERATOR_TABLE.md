# Ω-Math v0.9 — Canonical Operator Table

This is the canonical operator inventory. An operator may not silently change type or meaning between documents.

| Operator | Signature | Status | Notes |
|---|---|---|---|
| `DIST` | `Entity × Entity → Distinction` | DEFINED | typed comparison |
| `INCIDENT` | `Entity × Relation → Incidence` | DEFINED | structural query |
| `PATH` | `Relation* → Path` | DEFINED | ordered compatible sequence |
| `PATH_EQ` | `Path × Path → Boolean` | DERIVED / ADMITTED | exact sequence equality only |
| `CYCLE` | `Path → Cycle ∪ Failure` | DEFINED | declared return criterion |
| `CONCAT` / `⧺` | `Path × Path → Path` | DEFINED | compatible endpoints; empty path is identity |
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
| `QUOTIENT_DISTANCE` | `Quotient × BaseDistance → [0,∞]∪{∞}` | DERIVED | quotient-distance candidate; compatibility required |
| `SYMMETRY` | `State × TransformFamily → Orbit/Action` | DEFINED |
| `RETAIN` | `State × RetentionRule → MemoryCandidate` | DEFINED FRAMEWORK | functional effect must be tested |
| `ORDER` | `TransitionSequence → OrderedIndex` | DERIVED | internal order, not physical time |
| `HORIZON` | `Dynamics × ℕ₀ → FiniteFutureDomain` | DEFINED | discrete depth |
| `BRANCH` | `State × Input → 𝒫(State)` | DEFINED | nondeterministic successors |
| `REACH` | `State × Task × Horizon → Boolean/Set` | DEFINED FRAMEWORK | existential/universal semantics declared |
| `MODEL` | `State → InternalRepresentation` | HYPOTHESIS FRAMEWORK | self-model when causally used |
| `FEEDBACK` | `State/Model × Dynamics → RecurrentDependency` | DEFINED FRAMEWORK |
| `COARSE` | `Structure × Criterion → MacroObject` | DEFINED FRAMEWORK | emergence candidate |

## Derived closures

- `ε_e` is the identity of path concatenation: `ε_e⧺P=P` and `P⧺ε_e=P`.
- `s≈∞s' ⇔ ∀h∈ℕ₀, s≈ₕs'` is derived from finite-horizon equivalence.
- Rich path equivalence is task-relative and is not identified with exact sequence equality.
- Quotient geometry is a derived construction subject to explicit compatibility/separation conditions; see `QUOTIENT_GEOMETRY_CONDITIONS.md`.

## Non-primitive / external modules

`REL_COMPOSE` — primitive relation-to-relation collapse is not required; path formation is the sequential composition layer.

`REL_ID` — not a primitive relation; empty-path identity is sufficient for path concatenation.

`REL_INV` — not a primitive relation; path reversal does not imply a reverse edge.

`CAUSE` — causal semantics require explicit intervention/counterfactual criteria.

`PROB` — probability requires an independently declared probabilistic kernel.

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

`DEFINED / CANONICAL INVENTORY / v0.9 SYNCHRONIZED`
