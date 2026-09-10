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

### Process completion standard
- Added `WORK_COMPLETION_STANDARD_v1.0.md` as the repository-wide completion protocol.
- Established the mandatory sequence `make → write → reread → verify → synchronize → validate → self-contain → declare DONE`.
- Established the hard rule `DONE = IMPLEMENTED + WRITTEN + VERIFIED + SYNCHRONIZED + SELF-CONTAINED`.
- Required final verification against the actual stored artifact after the last write; placeholders, missing definitions, stale references, unverified claims, or conversation-only dependencies prevent `DONE`.
- Added the completion rule to `FOUNDATION.md` as principle P8, to `README.md`, and to the canonical index.

### Potential / transition bridge
- Added the graph-derived reversible/dissipative transition research sequence through Experiments 013–018.
- Experiment 018 derives `C=(S-S^T)/2` directly from full ordered graph path continuation and verifies the resulting operator on exact finite graph families and 300 random connected graphs.

### Cross-domain verification
- Added `EXPERIMENT_OMEGA_CROSS_DOMAIN_019.md` defining explicit mappings to harmonic oscillator, diffusion/consensus, damped oscillator and directed-cycle transport.
- Added `EXPERIMENT_OMEGA_CROSS_DOMAIN_020.md` with finite numerical checks of those mappings, including `Phi=Σx_i^4/4`.
- Result: the reversible/dissipative graph architecture reproduces the declared mathematical forms under supplied model semantics.
- Boundary retained: this does not establish a universal physical ontology, physical units, or independent physical predictions.

### Physical vortex bridge
- Added `EXPERIMENT_OMEGA_PHYSICAL_VORTEX_021.md` as a finite physical-bridge check using a steady free vortex with independently specified `rho`, `K`, `r_i`, `r_o`, and `p_o`.
- Verified exactly for the declared model that `Delta_p/rho = Delta_Kinetic = 1.875`, `H=p/rho+u_theta^2/2=10.125` at both selected contours, and radial acceleration is zero.
- Explicitly recorded the critical boundary: pressure difference plus circulation does not imply radial transport; the Ω reversible operator has not thereby derived the fluid pressure field or Navier–Stokes.
- Next falsification target: transient/open vortex with nonzero mass flux and explicit energy-flow/dissipation accounting.

### Existing bridges
- Retained LIGHT and TRANSPORT bridge records and all prior v0.9 verification records.

The v0.9 core remains closed. External-domain evidence may motivate a versioned extension only after formal definition, counterexample testing, sufficiency analysis, and cross-domain verification.
