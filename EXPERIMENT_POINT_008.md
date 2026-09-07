# Ω-Math — EXPERIMENT_POINT_008

## Question

Can a Point-like regime emerge from a **combined mechanism** rather than from relational closure alone?

Candidate factors:

- relational closure;
- memory of previous relations;
- rigidity/persistence of established relations;
- attraction toward nearby/strongly related entities;
- distance-dependent interaction;
- redundant connectivity.

The test does **not** assume that any of these is fundamental. They are experimental candidate mechanisms.

## Motivation

`RESULT_POINT_007` rejected the narrow mechanism:

`closure + redundancy -> single Point`.

The remaining possibility is that coherence is a coupled regime in which several effects stabilize one another. The present experiment therefore tests the joint mechanism rather than increasing one factor in isolation.

## Experimental construction

A finite system of `N=100` entities is initialized in a two-dimensional bookkeeping space. The geometry is experimental only and is not treated as primitive Ω-Math structure.

Each pair can have a relational edge. Edge preference is determined by a combination of:

1. **memory** — persistence of relations that existed previously;
2. **rigidity** — resistance to replacing established relations;
3. **attraction** — preference for relations associated with stronger local interaction;
4. **distance** — attenuation of interaction with increasing geometric separation;
5. **closure** — preference for maintaining already organized local structure.

Total edge count is controlled so that simple increase in relation number cannot explain the result.

## Candidate Point criteria

A regime is Point-like only if several conditions hold simultaneously:

1. one dominant connected structural component;
2. persistent internal relational density;
3. reduced coupling between the dominant structure and exterior entities;
4. a non-empty interface through which changes can propagate outward;
5. persistence under random perturbation;
6. preservation of internal distinguishability;
7. robustness under label permutation;
8. superiority over matched null models.

No single metric is sufficient.

## Null models

At minimum compare against:

- random rewiring with the same number of relations;
- closure-only;
- memory-only;
- rigidity-only;
- attraction/distance-only;
- closure + redundancy (previous mechanism);
- combined mechanism.

The decisive question is whether the combined regime produces a qualitative change not present in the components individually.

## First computational probe

A reduced network simulation was run over a parameter grid for attraction, memory, rigidity and interaction distance, with multiple random seeds.

The strongest connectivity observed in the tested grid produced a giant component of approximately `91.7/100` entities on average, with approximately `7` connected components. This is a promising indication that combined mechanisms can maintain a much larger coherent structure, but it is **not yet evidence for a Point**.

The current probe is insufficient because the boundary/interface and information-flow criteria have not yet been jointly measured, and the geometry introduces an experimental degree of freedom.

## Current result

`PRELIMINARY`

The combined-factor hypothesis remains **OPEN**.

The important observation is methodological: the search should move from single mechanisms to **coupled regimes**, while keeping each candidate factor independently switchable and comparing against matched nulls.

## Next test

Run a factorial experiment with all mechanisms independently enabled/disabled and continuous parameter sweeps. Measure:

- giant-component fraction;
- community fragmentation;
- normalized boundary conductance;
- internal/external relation ratio;
- persistence/lifetime;
- perturbation recovery;
- state distinguishability;
- outward state-change flux through the interface.

The final quantity is deliberately called **state-change flux**, not energy. Energy remains outside the primitive layer until an independent Ω-derived quantity exists.

## Status

`PRELIMINARY / OPEN`

No physical interpretation is claimed.
