# CHANGELOG

## v0.9

### Core closure
- Closed the minimal typed relational language for the declared v0.9 domain.
- Separated entity state `{0,1}` from relation state `{−1,+1}`.
- Canonicalized path algebra, empty path identity, reversal, and exact path equality.
- Formalized finite- and infinite-horizon behavioral equivalence and task-specific nondeterministic semantics.
- Corrected quotient-geometry conditions: quotient distance is not automatically a pseudometric for an arbitrary equivalence relation.
- Kept probability, causal intervention, physical time, physical energy, and physical ontology as external bridges rather than hidden primitives.

### Synchronization
- Synchronized `SEMANTICS.md`, `GLOSSARY.md`, `DYNAMICS.md`, `EMERGENCE.md`, `TYPE_SYSTEM.md`, and canonical examples with v0.9.
- Added `CANONICAL_INDEX_v0.9.md` as the navigation layer for canonical and historical material.

### LIGHT bridge
- Added `LIGHT_STRUCTURAL_BRIDGE_v0.1.md` to compare Ω-Math with the electromagnetic/QFT structure in `SmartVoltISA/LIGHT-`.
- Added `EXPERIMENT_LIGHT_BRIDGE_001.md` as an analytical test of admissibility, locality, and loop-residual candidates.
- Added `EXPERIMENT_LIGHT_BRIDGE_003.md` with an executed finite locality/propagation verification.
- Added `EXPERIMENT_LIGHT_BRIDGE_004.md` with an executed algebraic boundary test for loop residuals.
- Added `EXPERIMENT_LIGHT_BRIDGE_005.md` with an executed finite transport/holonomy boundary test.
- Result: connectivity alone is insufficient to determine locality-dependent propagation; the scalar sign product is insufficient to represent ordered loop structure; a richer transport/composition law is sufficient in a finite external model, but is not derived from Ω v0.9 primitives.

### Transport minimality
- Added `EXPERIMENT_TRANSPORT_MINIMALITY_006.md` to test whether bijectivity is actually required for nontrivial ordered-loop residuals.
- Result: arbitrary composable typed functions with identity and associative composition are sufficient; bijectivity is stronger than necessary for residual generation.
- Separated minimal residual generation from the stronger frame-change/gauge-conjugation requirement, where invertible local frame maps are required.
- Added `TRANSPORT_LAYER_v0.1.md` as a proposed research schema above Ω v0.9; it is not a new primitive.
- Added `EXPERIMENT_TRANSPORT_REDUCTION_007.md`: the transport maps can be represented as typed specializations of the existing Ω transformation layer, so a separate `TRANSPORT` primitive is not currently justified.
- Added `EXPERIMENT_TRANSPORT_QUOTIENT_008.md`: quotient-compatible transport factors through the reduction, but quotienting can erase nontrivial loop residuals; existing task-relative sufficiency machinery is sufficient to express this information-loss boundary.

### Boundary
- Added `EXPERIMENT_LOCALITY_ADMISSIBILITY_BOUNDARY_010.md` with an executed finite verification.
- Result: locality, admissibility, and boundary restrictions can be represented as declared semantic predicates/domain restrictions over existing Ω objects; no new primitive type is justified.
- Strengthened the separation: relation existence, locality, admissibility, and boundary crossing are distinct predicates/constraints and must not be silently identified.
- Added `EXPERIMENT_INTERACTION_REDUCTION_011.md` with an executed exhaustive finite verification of locality/admissibility interaction, boundary restriction, and quotient information loss.
- `EXPERIMENT_POINT_009.md` remains preregistered and untouched because its causal-interface phrase is not operationally defined.

### Causal intervention
- Added `EXPERIMENT_CAUSAL_INTERVENTION_012.md` with an executed finite exhaustive verification.
- Result: explicit interventions are representable as existing typed transformations/inputs; baseline temporal succession can be identical while intervention responses differ; directional models can therefore be interventionally distinguishable without being distinguishable from the chosen baseline trajectory.
- No new `CAUSE` primitive is justified. Causal direction/dependency remains an explicit intervention/comparison semantics and a research frontier.

### Potential / transition bridge
- Added `POTENTIAL_TRANSITION_OPERATOR_v0.1.md` as a research bridge for the candidate operator `dx/dt = (A-D) δPhi/δx`.
- Added `EXPERIMENT_OMEGA_NETWORK_TRANSITION_013.md` with an exact finite three-node verification.
- Result: antisymmetric `A` gives nonzero reversible state motion with zero potential change; positive-semidefinite `D` gives non-increasing potential; both can conserve the closed-network total state quantity when the operator has zero column sum.
- Added `EXPERIMENT_OMEGA_GRAPH_DERIVATION_014.md` and derived both operators from graph incidence and edge coupling: `D=BKB^T`, `A=BCB^T` with `K^T=K>=0` and `C^T=-C`.
- Result: the conservation, antisymmetry and dissipation properties now follow from the relation graph construction for the tested finite model rather than from hand-specified node matrices.
- Added `EXPERIMENT_OMEGA_CYCLE_DERIVED_CIRCULATION_015.md`: constructed `C` from the successor/predecessor order of a closed relation cycle rather than supplying an arbitrary skew matrix.
- Result: for exact finite cycles `n=3,4,5,6,7`, the induced `A=BCB^T` is skew-symmetric, conservative, nonzero, preserves the quadratic potential under the reversible part, and reverses sign with cycle orientation. The `n=3` construction exactly recovers the reversible operator of Experiment 014.
- Added `EXPERIMENT_OMEGA_FINAL_NORMAL_FORM_017.md`: consolidated the verified structure into the final research normal form `dx/dt = B(C-K)B^T grad(Phi)` with `C^T=-C`, `K^T=K>=0`, and `1^T B=0`.
- Result: the reversible/dissipative split, conservation, and potential monotonicity are structurally characterized; a unique `C` cannot be selected from incidence `B` alone on arbitrary multi-cycle graphs without additional ordering/transport/weighting semantics.

The v0.9 core remains closed. External-domain evidence may motivate a versioned extension only after formal definition, counterexample testing, sufficiency analysis, and cross-domain verification.
