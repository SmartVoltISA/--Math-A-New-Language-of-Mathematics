# Ω-Math v0.9 — Synchronization Audit

## Purpose

The v0.9 frontier closure exists, but several legacy documents still identify earlier versions as current. This audit separates the canonical v0.9 state from historical documents and prevents version drift from being mistaken for mathematical contradiction.

## Canonical v0.9 integration records

1. `FRONTIER_CLOSURE_v0.9.md` — canonical frontier decisions.
2. `STATUS_v0.9.md` — canonical v0.9 status summary.
3. `QUOTIENT_GEOMETRY_CONDITIONS.md` — corrected conditions for quotient-induced distance.

These documents are the integration layer until legacy canonical filenames are synchronized.

## Legacy documents requiring synchronization

- `README.md` — still labels the project v0.4 and lists already-closed frontiers as open.
- `CHANGELOG.md` — currently ends at v0.4.
- `OPERATOR_TABLE.md` — v0.8; its unresolved list predates exact path equality and infinite-horizon closure.
- `FOUNDATION.md` — v0.4 document version.
- `REDUCTION_RULES.md` — v0.4 document version.
- `TRANSFORMATION.md` — v0.2 document version.
- `BEHAVIORAL_EQUIV.md` — v0.1 document version.
- `RELATION_COMPOSITION.md` — v0.2 document version.
- `LANGUAGE_CLOSURE_v0.8.md` and `V08_COMPLETION_INDEX.md` — historical v0.8 closure records.

Legacy version numbers are not themselves errors: they become dangerous only when the file is presented as the current canonical specification.

## v0.9 decisions that supersede older wording

- exact path equality is admitted at the representation level;
- empty path is the identity for path concatenation;
- infinite-horizon equivalence is derived as the intersection of finite-horizon equivalences;
- nondeterministic successor sets are first-class;
- branching equivalence is task-semantics dependent;
- fairness/liveness are explicit predicates over infinite runs;
- relation identity/inverse and primitive relation-to-relation collapse remain non-primitive;
- continuous state sets are permitted only when their additional structure is explicitly declared;
- probability requires an independently declared kernel;
- causal claims require explicit intervention semantics;
- physical time and energy remain external empirical bridges;
- quotient geometry requires explicit compatibility conditions.

## Mathematical correction

The earlier wording that unconditionally called

`d_Q([x],[y]) = inf{d(x',y'): x'~x, y'~y}`

a quotient pseudodistance was too strong. For an arbitrary equivalence relation, triangle inequality is not automatic. The corrected status is **quotient-distance candidate**, promoted to pseudometric/metric only after the required compatibility and separation conditions are established. See `QUOTIENT_GEOMETRY_CONDITIONS.md`.

## Canonical status boundary

`Ω-Math v0.9 = formally complete minimal typed relational language for the declared domain.`

This means language closure, not universal mathematics, physical ontology, or a finished theory of nature.

## Synchronization rule

When legacy and v0.9 documents disagree, use the v0.9 integration records above for current status. Legacy documents must not be silently edited into new mathematics; synchronization should preserve their historical version or explicitly mark them superseded.

## Audit result

**Architecture: coherent.**

**Documentation: previously desynchronized.**

**Critical mathematical correction: quotient geometry conditionally valid, not automatic.**

**Current closure: v0.9, with explicit external/empirical boundaries.**
