# Ω-Math — EXPERIMENT_POINT_009

## Question

Can a stable Point-like boundary emerge from the coupled competition between:

- relational closure;
- memory of established relations;
- rigidity/persistence;
- attraction;
- distance-limited interaction;
- redundant connectivity?

The target is not merely a large connected component. The target is a **single coherent internal regime with a persistent interface**: strongly retained internally, weakly coupled externally, but still capable of transmitting state changes through the interface.

## Hypothesis

The previous experiments suggest that no tested local mechanism is sufficient alone. A Point-like regime may require a coupled balance:

`cohesion + retention + confinement + interface`

The experiment therefore tests whether increasing retention/confinement while preserving nonzero interface produces a stable intermediate regime rather than either fragmentation or unrestricted global mixing.

## Experimental design

Finite system:

- `N = 100` entities;
- fixed total relation budget;
- multiple independent random seeds;
- two-dimensional coordinates used only as an experimental control for distance-dependent interaction.

Each mechanism has an independent switch and continuous strength parameter:

- `M` — memory;
- `G` — rigidity;
- `A` — attraction;
- `D` — distance attenuation;
- `C` — closure;
- `R` — redundancy.

The principal sweep varies `M × G × A × D × C × R` over low/intermediate/high levels while keeping the relation budget fixed.

## Primary observables

For the dominant candidate structure `S`:

1. **coherence** — fraction of entities in the dominant connected component;
2. **internal retention** — fraction of relations retained within `S`;
3. **external coupling** — relation coupling between `S` and exterior;
4. **normalized interface conductance** — external coupling normalized by internal volume/degree;
5. **interface existence** — nonzero boundary coupling;
6. **lifetime** — persistence of the same structural regime across steps;
7. **recovery** — return toward the pre-perturbation regime after random node/edge perturbation;
8. **internal distinguishability** — preservation of non-identical entity states/roles inside `S`;
9. **state-change flux** — state changes crossing the detected interface per transition;
10. **fragmentation** — number and size distribution of internal communities.

## Candidate Point regime

A parameter region is classified as Point-like only if all are simultaneously satisfied:

- dominant structure remains near the whole system;
- internal retention is high;
- normalized external coupling is substantially lower than matched nulls;
- interface remains nonzero;
- internal distinctions persist;
- regime has long lifetime;
- perturbation recovery is positive;
- results survive label permutation;
- combined mechanism outperforms matched component controls.

No single scalar score is allowed to define the Point.

## Critical controls

Compare against:

- random rewiring;
- closure-only;
- memory-only;
- rigidity-only;
- attraction/distance-only;
- closure + redundancy;
- memory + rigidity;
- all mechanisms combined.

Relation count, initial density, seed count and observation horizon are matched.

## Interpretation rule

Three qualitatively different outcomes must be distinguished:

### A. Fragmentation

High internal closure but many disconnected or weakly coordinated cores.

### B. Global mixing

One connected structure, but no persistent boundary because external coupling remains high.

### C. Candidate Point

One coherent structure with high internal retention, suppressed normalized external coupling, a persistent nonzero interface, and preserved internal distinctions.

Only C supports the Point hypothesis.

## State-change flux

Define an experimental interface `∂S` from the relational structure itself. For consecutive states `Ω_t, Ω_{t+1}`, count state changes whose causal propagation crosses `∂S`.

This is called **state-change flux**, not energy. It is a relational/dynamical observable and makes no physical energy claim.

The desired Point regime therefore has:

`internal retention → high`

`external coupling → low`

`interface → nonzero`

`state-change flux → nonzero`

simultaneously.

## Falsification criteria

Reject the coupled-boundary hypothesis if:

- no parameter region satisfies the joint criteria;
- apparent boundary disappears under label permutation;
- the same regime appears in matched random controls;
- high coherence always requires high external coupling;
- nonzero interface always destroys persistence;
- internal distinguishability is lost whenever coherence becomes high.

## Status

`PREREGISTERED / TEST PROTOCOL`

No physical interpretation is assumed. Geometry, attraction, distance, memory and rigidity are experimental candidate mechanisms, not Ω-Math primitives.
