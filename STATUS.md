# Ω-Math v0.3 — Research Status

## Current state

The repository now contains a typed structural core plus an explicit transformation layer and tested path/composition semantics.

The current result is deliberately conservative: the signed relation algebra works as a **summary algebra**, while paths remain first-class objects whenever order, intermediate structure, multiplicity or conflict matters.

## Closed milestones in the current cycle

### M1 — Four length-2 signed cases

Enumerated exhaustively:

`(+,+) → +`
`(+,-) → -`
`(-,+) → -`
`(-,-) → +`

The sign-product operation on `{−1,+1}` is closed, commutative and associative.

Status: `DERIVED`.

### M2 — Candidate relation reduction

The sign-product is a valid scalar reduction, but not a universal semantics for sequential relations.

`PATH → SIGN PRODUCT` is therefore retained as a summary map, not as the definition of relation composition.

Status: `COUNTEREXAMPLE / REJECTED AS UNIVERSAL LAW`.

### M3 — Associativity lengths 3–4

For the scalar sign-product summary, associativity follows from the binary operation and therefore extends to arbitrary finite sign sequences.

For full path semantics, associativity belongs to path concatenation itself and does not justify erasing intermediate structure.

Status: `DERIVED` for summary algebra; `DEFINED` for path concatenation.

### M4 — Conflicting parallel paths

Parallel paths cannot be collapsed to one primitive relation without an additional rule for multiplicity, conflict, selection or richer relation state.

Status: `OPEN / NO SILENT COLLAPSE`.

### M5 — Finite-horizon behavioral equivalence

Behavioral equivalence is defined relative to declared observations, inputs/interventions, transition rule, determinism and horizon.

For deterministic finite-horizon behavior:

`x ≈ᵦ,h y` iff the declared observations match through horizon `h` under the same declared inputs.

The equivalence classes are nested:

`≈ᵦ,h+1 ⊆ ≈ᵦ,h`.

At `h=0`, this reduces to observational equivalence.

Status: `DEFINED / DERIVED`.

### M6 — Quotient and invariant preservation

A quotient is behavior- or structure-preserving only relative to explicitly declared observations, transformations and retained quantities.

An invariant must specify the transformation family under which it is preserved:

`I(T(S)) = I(S)`.

Label permutation is a mandatory first representation control for structural claims.

Status: `DEFINED / DERIVED METHODOLOGICAL RULE`.

### M7 — Path-profile sufficiency

A restricted profile containing endpoint, length and sign sequence/product is not universally sufficient for future behavior. PATH-DYNAMICS-001 gives a deterministic counterexample in which intermediate organization changes the trajectory while the restricted profile remains identical.

Status: `COUNTEREXAMPLE`.

## Relation composition decision

`PATH CONCATENATION`: `DEFINED`.

`SIGN-PRODUCT SUMMARY`: `DERIVED`.

`SIGN-PRODUCT AS COMPLETE RELATION COMPOSITION`: `REJECTED` as an information-preserving universal law.

`PRIMITIVE RELATION REDUCTION`: `OPEN`.

The repository must preserve path information until a sufficiency theorem or an explicitly task-relative reduction justifies its removal.

## Structural and behavioral findings retained from earlier work

The topology and structure experiments show that equal entity counts, relation counts, sign counts, degree sequences and selected aggregate graph statistics can still hide different path organization and controlled dynamic responses.

Therefore aggregate graph statistics are not automatically complete state descriptions.

The behavioral-equivalence experiments show:

`static observational equivalence ≠ behavioral equivalence`.

The collapse experiments show:

`observation collapse ≠ system change`.

`vertex quotient ≠ relation quotient ≠ path quotient`.

## Point / boundary status

Executed experiments support, within tested models:

`relations → closure → relational separation → candidate core/interface`.

Closure-only, closure-plus-reconnection, closure-plus-redundancy and combined-factor probes did not establish a unique single Point-like object. Strong closure can fragment; high connectivity alone does not create the required boundary behavior.

Therefore the Point remains `OPEN` and must be tested as an intermediate regime satisfying multiple simultaneous criteria.

## Next layer — quantitative structure

The current dependency barrier has been reached. The next layer can now investigate quantities that are **derived from transformations** rather than inserted as primitives.

Priority order:

1. define admissible transformation costs;
2. derive task-relative transformation distance;
3. test non-negativity, identity of indiscernibles, symmetry and triangle inequality where applicable;
4. identify when directed/asymmetric cost is necessary;
5. test metric invariance under declared symmetries;
6. compare derived quantities with standard graph distance only as an external comparison, not as an assumed definition;
7. investigate whether geometry can emerge as a stable quotient of transformation structure.

## What remains explicitly open

- canonical primitive relation composition;
- canonical path equivalence;
- universal sufficient path profile;
- canonical metric;
- physical time;
- probability;
- energy;
- physical ontology;
- emergence criterion independent of a selected task;
- self-model and causal self-reference;
- physical bridge and empirical predictions.

## Confidence labels

`DEFINED` = introduced by the language.

`DERIVED` = follows formally from current rules.

`EXECUTED` = evaluated by an explicit finite construction or computation.

`SUPPORTED` = survived specified controls.

`COUNTEREXAMPLE` = evidence against a universal claim.

`REJECTED` = claim no longer retained as valid under documented evidence.

`OPEN` = unresolved.

## Critical methodological rule

The ability to express a phenomenon in Ω-Math is not evidence that Ω-Math explains it.

`representable ≠ explained`

`correlated ≠ caused`

`stable ≠ fundamental`

`emergent candidate ≠ emergence proven`

## Physical hypothesis

`H-BH-0` — extreme relational distinguishability collapse may have a physically meaningful correspondence with characteristic black-hole behavior.

Status: `OPEN`.

No physical interpretation is accepted until an Ω quantity is defined independently, mapped to established observables, tested against controls, and used to make predictions not used in its construction.
