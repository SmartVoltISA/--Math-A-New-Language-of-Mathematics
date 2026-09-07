# Ω-Math — EXPERIMENT_POINT_006

## Objective

Test whether a single Point-like object can emerge as a stable regime when inward closure competes with fragmentation, while a narrow non-zero boundary interface remains.

## Model

Finite undirected relational system with `N=100` entities and fixed relation count `E=300`.

No geometry, coordinates, distances, radius, area, gravity or energy are supplied.

At each transition, one relation is rewired. Candidate rewiring is selected from two classes:

- closure move: increases local common-neighbor closure;
- dispersal move: prevents unlimited isolation by preserving a small probability of external reconnection.

The control parameter `p` is the probability of accepting closure pressure. A second parameter `q` controls retention of a small external interface.

The experiment sweeps a grid of `p,q` values and repeats each point over independent random seeds.

## Candidate Point

At each time step identify the largest structurally coherent component `K` and search for a boundary set `B` separating `K` from the remainder.

A candidate Point regime requires simultaneously:

1. `K/N` remains close to 1 for a sustained interval;
2. internal edge fraction of `K` is high;
3. normalized external conductance of `K` is low;
4. at least one non-zero interface to the exterior persists;
5. internal node distinctions remain nontrivial;
6. the regime survives small perturbations;
7. the result is absent or significantly weaker in matched random-rewiring controls.

## Important correction

The previous experiment showed that strong closure can create community separation but can also fragment the system. Therefore maximum closure is not assumed to be the Point.

The present experiment explicitly searches for an intermediate stable regime.

## Tests

### A. Parameter sweep

Search the full `(p,q)` grid for a stable Point-like window rather than selecting a parameter from a single run.

### B. Seed replication

Use multiple independent seeds for every candidate parameter region.

### C. Perturbation

After a candidate regime forms, randomly rewire a small fraction of relations and measure recovery.

### D. Label invariance

Permute entity labels and verify invariant measurements.

### E. Null topology

Compare against degree-preserving random rewiring.

### F. Fragmentation control

Measure number and size distribution of components. A state with many comparable components is classified as fragmentation, not a Point.

## Information test

Use a specified observation map that hides internal labels and compare:

- internal distinguishable configurations;
- externally distinguishable configurations;
- boundary-level equivalence classes.

A candidate Point is stronger if external compression increases while internal structural distinctions remain measurable.

No physical information or entropy is assumed.

## Energy test

Not performed in the Ω-only stage because energy is not yet defined as a primitive or independently derived observable.

The protocol records this as an explicit unresolved dimension rather than inferring energy from graph activity.

## Interpretation rules

`Point candidate`: all criteria pass across replications and controls.

`Boundary only`: separation appears, but no single dominant stable object exists.

`Fragmentation`: closure produces multiple isolated structures.

`Null-equivalent`: result is reproduced by matched controls.

`No effect`: no systematic regime detected.

## Falsification

The Point hypothesis is weakened if the parameter sweep produces only boundary/community formation or fragmentation, with no stable single dominant regime.

It is not falsified merely because this particular graph family fails; that result constrains the mechanism and requires testing other relational dynamics.

## Status

`PROTOCOL`
