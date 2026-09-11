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
- Synchronized canonical semantics, dynamics, examples, type system and navigation.
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
- Added `EXPERIMENT_OMEGA_OPEN_TRANSIENT_VORTEX_022.md` with explicit open-system energy accounting: boundary flux, pressure work, storage change and dissipation.
- Added `EXPERIMENT_OMEGA_AXISYMMETRIC_VORTEX_023.md` with a finite radial+axial field, geometry-derived incidence/continuation operators, finite kinetic storage and dissipation proxy.
- Experiment 023 result: radial+axial graph construction, skew reversible operator and positive dissipation measure all pass; physical pressure/velocity prediction remains NOT_PROVEN.

### Flow falsification and construction sequence
- Ω-028 verifies compatibility of an energy-consistent incompressible flow discretization with a skew/reversible plus PSD dissipative split, while explicitly retaining the boundary that this is representation rather than an independent Navier–Stokes derivation.
- Ω-030 falsifies the stronger claim that an independently specified axisymmetric pointwise convection operator is automatically recovered by metric-weighted skew projection. The measured operator mismatch is order-one relative to the physical operator norm.
- Ω-031 constructs conservative cylindrical transport directly from geometry and face fluxes, without post-hoc skew projection.
- Ω-032 extends that construction to the vector cylindrical convective term, including the `u_θ²/r` and `u_r u_θ/r` curvature terms. Discrete kinetic-energy power cancels to numerical precision.
- Ω-033 verifies pressure-work compatibility using the same divergence-free face-flux geometry; pressure power is numerically zero in the closed configuration.
- Ω-034 constructs an independent symmetric positive geometry-derived viscous operator. The minimum eigenvalue is within numerical roundoff of zero and the quadratic dissipation is positive.
- Ω-035 combines convection, pressure and viscosity into one complete instantaneous kinetic-energy accounting check. Reversible powers are approximately zero and viscous power is negative.
- Ω-036 repeats the vector conservative construction on 4×4 through 12×12 grids and retains the declared conservation/energy tolerances.
- The sequence strengthens the Ω physical bridge but does not yet establish a new physical law, a complete Navier–Stokes derivation, or independent pressure/vortex prediction.

### Existing bridges
- Retained LIGHT and TRANSPORT bridge records and all prior v0.9 verification records.

The v0.9 core remains closed. External-domain evidence may motivate a versioned extension only after formal definition, counterexample testing, sufficiency analysis, and cross-domain verification.
