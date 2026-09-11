# Ω-Math — A New Language of Mathematics

Ω-Math is an experimental typed mathematical language built from four primitive values with two different roles:

- `0, 1` — states of entities;
- `−1, +1` — states of relations.

The central research question is whether structure, dynamics, memory, geometry, time and higher-order phenomena can be represented or derived from relations between distinguishable entities.

This repository is a formal research program. It does not assume that nature is proven to have this ontology.

## Core distinction

`EntityState ∈ {0,1}`

`RelationState ∈ {−1,+1}`

These are disjoint typed domains. Relation absence is a domain condition, not a third relation value.

## Minimal object

An elementary Ω-relation is:

`eᵢ —rᵢⱼ→ eⱼ`, where `rᵢⱼ ∈ {−1,+1}`.

A finite configuration is:

`C = (E,D_R,R)`

where `D_R` is the explicit domain of present relations and `R:D_R→{−1,+1}`.

A state may additionally contain explicitly retained variables:

`S=(C,M,X)`.

## Research layers

1. Foundation — entities, relations, distinction, typing.
2. Language — syntax, semantics and operator discipline.
3. Algebra — legal typed operations and relation composition.
4. Structure — paths, cycles, connectivity, boundaries and invariants.
5. Transformation — changes, symmetry, quotient and structural loss.
6. Quantification — transformation costs and derived distance/geometry.
7. Dynamics — transition, order and causality.
8. Memory — retained state with demonstrated functional effect.
9. Emergence — validated higher-level organization.
10. Self-reference / consciousness — explicit hypothesis layers, never primitives.

## Working chain

`distinction → relation → configuration → structure → path → transformation → invariant → equivalence → quotient → metric candidate → dynamics → memory → self-model → feedback → emergence`

This is a research decomposition, not a theorem.

## v0.9 canonical closure

The v0.9 frontier pass closes the remaining **language-design** gaps while preserving explicit boundaries around mathematics not yet derived and physical interpretation.

Canonical integration records:

- `FRONTIER_CLOSURE_v0.9.md` — frontier decisions.
- `STATUS_v0.9.md` — current status.
- `V09_SYNCHRONIZATION_AUDIT.md` — canonical/legacy synchronization map.
- `QUOTIENT_GEOMETRY_CONDITIONS.md` — conditions for quotient-induced distance.
- `WORK_COMPLETION_STANDARD_v1.0.md` — mandatory completion and final-verification protocol.

Path concatenation is the primary sequential operation:

`P ⧺ Q`.

Exact path equality is admitted as representation identity. The empty path is the identity for path concatenation. Primitive relation composition, relation identity and relation inverse remain non-primitive.

Finite-horizon behavioral equivalence extends to infinite horizon by:

`s≈∞s' ⇔ ∀h∈ℕ₀, s≈ₕs'`.

Nondeterministic successor sets are first-class, while branching equivalence is parameterized by explicitly declared task semantics.

## Reduction principle

For a task `F` and reduction `Q`, behavior/task sufficiency requires:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

If this implication fails, the reduction is information-losing for that task. **Compression is not equivalence.**

## Transformation-derived geometry

For admissible transformations `𝒯(S,S')` with declared cost `c`, define the candidate distance:

`d_c(S,S') = inf{c(T):T∈𝒯(S,S')}`.

A metric is accepted only when its axioms follow for the declared domain and transformation family. Quotient-induced distance is additionally conditional; it is not automatically a pseudometric for an arbitrary equivalence relation.

This is a mathematical construction, not a derivation of physical space.

## Mathematical extensions

The v0.9 core is closed for its declared minimal typed-language domain. New mathematical results from Ω-Lab are integrated as **extensions**, not silently promoted into primitives.

Canonical extension register:

- `extensions/CONSERVATION_AND_OPERATOR_SELECTION.md` — positive quadratic conservation and metric-skew operator selection.
- `extensions/SPECTRAL_RELATIONAL_DYNAMICS.md` — spectral classes and dynamical mode taxonomy.
- `extensions/LOCAL_RELATIONAL_PROPAGATION.md` — local graph propagation and dispersion.
- `extensions/DISSIPATION_VS_CONSERVATION.md` — conservative, dissipative and unstable operator classes.
- `extensions/RELATIONAL_CIRCULATION.md` — oriented cycles, circulation and feedback.
- `extensions/VECTOR_RELATIONAL_OPERATORS.md` — conditional curl-sector selection in a restricted isotropic first-order class.
- `extensions/SCALE_AND_TIME.md` — separation of ordinal succession, dimensionless interval and physical duration.
- `extensions/TWO_FIELD_COUPLED_VECTOR_SYSTEM.md` — two-field transverse system selected by locality, isotropy and positive quadratic conservation within the declared class.
- `extensions/TWO_FIELD_COUPLING_AUDIT.md` — executed numerical consistency audit of the two-field reduction.
- `extensions/VARIATIONAL_HAMILTONIAN_AUDIT.md` — Hamiltonian/variational structural audit, including pairing and operator-adjointness conditions.
- `extensions/BOUNDARY_FLUX_AND_GLOBAL_CONSERVATION.md` — finite-domain boundary-flux condition for global conservation.
- `extensions/TRANSVERSE_CONSTRAINT_AND_POISSON_AUDIT.md` — invariant transverse sector, longitudinal zero modes and Poisson degeneracy.
- `extensions/MATHEMATICAL_EXTENSION_STATUS_v1.2.md` — canonical status register after the Hamiltonian and transverse-constraint gates.

The current mathematical bridge is:

`local distinction → local relation → operator → conservation/constraint → spectrum → mode → propagation → field structure`.

The two-field gate is closed conditionally: after positive field-space normalization, the minimal nontrivial transverse sector has the form

`∂t E = ω curl B`

`∂t B = -ω curl E`.

The Hamiltonian audit establishes that the full operator is skew-adjoint because field-space `J` is skew while spatial curl is self-adjoint under the admissible L2 pairing. Global conservation on finite domains depends on boundary flux.

The transverse condition is not derived: divergence is conserved, so divergence-free data define an invariant sector while longitudinal components remain zero-frequency modes. The associated Hamiltonian/Poisson operator is generally degenerate because curl has a kernel.

These are mathematical selection and structural results within restricted classes, not derivations of Maxwell theory or electromagnetism.

Every arrow is conditional on explicitly declared mathematical assumptions. No extension is a claim that physical laws have been derived.

## Method

`define → derive → implement → execute → verify → compare → falsify → record`

Every serious claim states its status: Definition, Derivation, Executed, Supported, Hypothesis, Theorem, Counterexample, or Rejected.

## Completion rule

Work is not considered `DONE` merely because the main change has been implemented.

The required sequence is:

`make → write → reread → verify → synchronize → validate → self-contain → declare DONE`

In compact form:

`DONE = IMPLEMENTED + WRITTEN + VERIFIED + SYNCHRONIZED + SELF-CONTAINED`

The actual stored artifact must be reread after the final write. Empty definitions, placeholders, broken references, stale indexes, unverified claims, or information required only from the conversation prevent a `DONE` status.

The full process standard is `WORK_COMPLETION_STANDARD_v1.0.md`.

## Important rules

Ω-Math must not become a new notation for old mathematics by assumption.

Do not silently identify:

- entity state with relation state;
- absence with a relation value;
- path with a scalar;
- observation with identity;
- stability with emergence;
- correlation with causality;
- connectivity with physical space;
- transformation irreversibility with physical irreversibility;
- transformation cost with physical energy;
- transition count with physical duration.

## Current boundaries / research frontiers

The formal language is closed for its declared domain. The following remain external, conditional, or open research layers:

- unrestricted primitive relation collapse;
- rich/task-independent path equivalence;
- general quotient geometry without compatibility assumptions;
- probability;
- physical time;
- physical energy;
- physical ontology;
- task-independent emergence;
- causal self-model;
- independent physical predictions;
- nondegenerate symplectic reduction of the curl kernel;
- additional conserved quantities from a fully specified reduced phase space.

The mathematical extensions add conditional operator, spectral, propagation, Hamiltonian and scale results without removing these boundaries.

## Repository structure

See the canonical documents, mathematical extensions and experiment records in the repository. v0.8 closure documents are retained as historical records; v0.9 documents define the core frontier status; `extensions/` contains post-closure mathematical structures and results.

## Status

**Ω-Math v0.9 — formally complete as a minimal typed relational language for its declared domain, with a registered and audited mathematical extension layer v1.2.**

This is not a claim of universal mathematical completeness or a completed physical theory.
