# Ω-Math — RESULT_POINT_009

## Status

`EXPLORATORY / PRELIMINARY`

This result is not a confirmatory test of the preregistered factorial protocol in `EXPERIMENT_POINT_009.md`. It is the first computational probe of the combined mechanism and is used to select the next controlled experiment.

## Model

- `N = 100` entities
- `E = 300` relations, fixed relation budget
- `120` transitions
- 2D coordinates used only for distance-dependent interaction
- mechanisms represented experimentally by closure, memory, rigidity/persistence, attraction, distance attenuation and redundancy
- state-change propagation measured separately from energy

## Probe result

At the tested combined parameter setting:

- giant connected structure: `99 / 100`
- remaining components: `2`
- detected communities: `8`
- largest detected community: about `20 / 100`
- internal edges of that community: `33`
- external cut edges: `60`
- normalized conductance: about `0.476`

The system therefore became almost globally connected while retaining substantial modular organization. The largest internal regime was not close to the whole system and its interface was not weak enough to qualify as a Point under the protocol criteria.

## Interpretation

The probe separates two quantities that must not be conflated:

`global coherence != Point`

A nearly connected system can still consist of several strongly organized relational modules. Conversely, maximizing closure or cohesion does not by itself produce the required combination:

`one coherent structure + high internal retention + low normalized external coupling + nonzero interface + persistent internal distinctions + recovery`

No evidence for a Point was obtained in this probe.

## What this rules out

It does not support the simple idea that combining all candidate mechanisms at one strong setting automatically generates a Point-like object.

It also does not justify a physical interpretation. Geometry, attraction, memory, rigidity and redundancy remain experimental mechanisms, not Ω-Math primitives.

## Next experiment

The next run should be a controlled parameter search around the intermediate regime between fragmentation and global mixing. In particular, vary memory and rigidity/persistence independently while holding the other mechanisms fixed, then test:

1. giant-component coherence;
2. internal/external relation ratio;
3. normalized interface conductance;
4. lifetime;
5. perturbation recovery;
6. internal state distinguishability;
7. state-change flux across the interface;
8. matched random and component-control nulls.

The target is not the maximum of any single metric. The target is the simultaneous satisfaction of the joint Point criteria.

## Conclusion

`POINT_009: NOT SUPPORTED BY THIS PROBE`

The result is useful because it identifies a real distinction between global connectivity and a Point-like relational boundary, and narrows the next search toward an intermediate, persistent regime rather than maximal closure.
