# Ω-Math — Full Research Gate Map v1.0

Date: 2026-09-16
Status: CURRENT COMPLETE PASS / NO UNJUSTIFIED PROMOTION

## Scope

This document consolidates the current closed core, implementation hardening, mathematical extension layer and remaining research gates after the full-stack pass.

## A. Canonical core

The minimal typed kernel remains:

`STATE + RELATION + DISTINCTION + CONSTRAINT + TRANSITION`

The v0.9 operator inventory remains synchronized. Entity states are exactly integer `0|1`; relation signs are exactly integer `-1|+1`. Configuration rejects duplicate entity identifiers and duplicate explicit relation keys. Transformation cost obeys `[0,∞]`. These are implementation contracts, not new mathematical primitives.

## B. Structural reconstruction

Established as a structural response architecture:

`response = H(Δ,R,C,S)`

Not established:

`H ⇒ unique numerical constitutive coefficient`.

The executed withheld reconstruction experiment (`extensions/WITHHELD_RECONSTRUCTION_EXPERIMENT_v1.0.md`) confirms the identifiability boundary on a deterministic counterfamily: the same structural input admits multiple hidden coefficients `g`, while the structural form `J = gΔ` survives within the restricted linear family.

Important scope limit: this is a methodological/synthetic gate experiment, not yet empirical validation using independently sourced physical datasets.

## C. Connector status

The following remain connector/derived families rather than universal primitives:

`POTENTIAL-LIKE, TRANSMISSION, RESISTANCE, FLOW, TRANSFER, IMPULSE, INERTIA, VISCOSITY, STIFFNESS, ELASTICITY, THRESHOLD, HYSTERESIS, MEMORY, FEEDBACK`.

Their forms can be reconstructed conditionally from state, relation, difference and constraints, but their numerical realization requires domain closure or additional laws.

## D. Conservation

For the audited two-field curl system,

`local antisymmetric dynamics + admissible pairing + zero net boundary flux`

is sufficient for the derived quadratic conservation statement. Without boundary control, local antisymmetry does not imply global conservation. fileciteturn92file0

## E. Transverse/Hamiltonian gate

Divergence-free data define an invariant sector but are not forced for arbitrary initial data. The unrestricted curl operator is generally degenerate because of its kernel. Therefore global symplectic nondegeneracy requires an explicit reduced phase space. fileciteturn93file0

## F. General-domain gate

The universal implication

`transverse ⇒ curl invertible`

is rejected. A valid general theorem must specify domain, boundary conditions, function space, kernel treatment and regularity. Harmonic/topological sectors remain explicit DOMAIN CLOSURE data.

## G. Quotient geometry

Quotient distance is retained as a candidate. Metric status requires explicit compatibility, symmetry, separation and triangle checks. Mathematical quotient geometry does not imply physical space.

## H. Time/scale

Transition order/count does not determine physical duration. A dimensional clock requires an additional scale-setting structure.

## I. Variational uniqueness

A Hamiltonian/Poisson representation can be established conditionally in the audited reduced sector. A unique canonical physical action is not established. Any future uniqueness result must show that competing admissible formulations are excluded by internal assumptions rather than by importing target-domain physics.

## J. Complete gate table

| Gate | Current status |
|---|---|
| Core typing | CLOSED |
| Cost positivity | CLOSED |
| Registry/runtime synchronization | CLOSED by static audit; fresh execution belongs to STAND |
| Generic structural reconstruction | PARTIAL / FORM SURVIVES |
| Unique constitutive coefficient | REJECTED WITHOUT DOMAIN CLOSURE |
| Universal transmission scalar | REJECTED |
| Reduced T³ symplectic sector | CONDITIONAL CLOSED |
| General bounded-domain Hodge theorem | OPEN / DOMAIN-SPECIFIC |
| Boundary-dependent conservation | CONDITIONAL CLOSED |
| Quotient metric | CONDITIONAL / CANDIDATE |
| Physical time calibration | OPEN / REQUIRES SCALE |
| Physical units | OPEN |
| Unique physical action | OPEN |
| Emergence/COARSE promotion | OPEN / TASK-RELATIVE |

## K. Executed decisive gate

The withheld reconstruction gate has now been executed as a deterministic synthetic experiment.

Result:

1. The restricted structural form `J = gΔ` survives.
2. The hidden coefficient is not identifiable from the structural kernel.
3. Adversarial nonlinear laws reject promotion of linear response to a universal law.
4. The experiment therefore supports the separation between UNIVERSAL STRUCTURE and DOMAIN CLOSURE.

The executable record is `tools/withheld_reconstruction.py`.

## L. Next decisive empirical gate

Do not add another primitive.

Run the same withheld-reconstruction protocol on independently sourced equations or datasets from at least three genuinely different physical domains, with units, constitutive coefficients and domain labels hidden from the structural stage. The structural stage must attempt reconstruction from normalized relational inputs only; the closure stage may then reveal units and constitutive laws.

Required negative controls:

- arbitrary hidden coefficients;
- nonlinear constitutive laws;
- threshold/saturation cases;
- shuffled relation controls;
- at least one case where the candidate structural form is intentionally false.

A successful result is **not** recovery of a universal coefficient. The target is recovery of a common structural dependency plus correct abstention when domain closure is insufficient.

## M. Final architecture

```text
UNIVERSAL STRUCTURAL KERNEL
    STATE
    RELATION
    DISTINCTION
    CONSTRAINT
    TRANSITION
             ↓
DERIVED DYNAMICS
    CHANGE / RESPONSE / FLOW
             ↓
CONNECTOR LAYER
    POTENTIAL / TRANSMISSION / RESISTANCE / TRANSFER
             ↓
DOMAIN CLOSURE
    CONSTITUTIVE LAW / UNITS / PARAMETERS / BOUNDARY / CALIBRATION
             ↓
HIGHER STRUCTURES
    INVARIANT / SYMMETRY / MEMORY / FEEDBACK / COARSE
```

## Decision

No new universal primitive is justified by the current evidence. The project has passed the synthetic identifiability gate and should now move to empirical withheld reconstruction rather than vocabulary expansion.
