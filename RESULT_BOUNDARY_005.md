# Ω-Math — RESULT_BOUNDARY_005

## Executed test

Two computational constructions were tested without geometric coordinates.

### Test A — closure-biased rewiring

A finite relational system was repeatedly rewired so that local relational closure increased.

The earlier controlled run showed stronger community separation than random rewiring, but maximal closure fragmented the system rather than producing one dominant object.

### Test B — directed inward relational dynamics

A directed system of 80 entities was evolved for 400 rounds. At each update, relation targets preferentially moved toward locally related/reachable entities, with a controlled random component. Seven closure settings were tested from `p=0.40` to `0.95`, with 15 independent runs per setting.

The largest strongly connected component (SCC) was measured as the candidate internally closed core. Incoming and outgoing relations across the SCC interface were measured separately.

## Test B aggregate result

| closure p | largest SCC / N | incoming-to-SCC edge fraction | outgoing-from-SCC edge fraction |
|---:|---:|---:|---:|
| 0.40 | 0.315 | 0.186 | 0.013 |
| 0.50 | 0.381 | 0.221 | 0.009 |
| 0.60 | 0.384 | 0.234 | 0.006 |
| 0.70 | 0.470 | 0.251 | 0.009 |
| 0.80 | 0.404 | 0.265 | 0.007 |
| 0.90 | 0.353 | 0.224 | 0.020 |
| 0.95 | 0.384 | 0.254 | 0.018 |

The peak mean core fraction occurred near `p=0.70`, but the effect was not monotonic and variability remained substantial.

## Main result

The directed dynamics generated a strongly connected internal core together with a persistent interface to entities outside that core.

This gives a stronger structural form of the earlier result:

`relational closure -> internally coherent core + interface`

The core was defined relationally through strong connectivity, not by geometry.

## What this does and does not establish

### Supported, limited

A relational rule can create an internally coherent region without predefined distance, radius, area or spatial coordinates.

The observed core can retain multiple distinct entities; therefore the Point hypothesis does not require:

`e_i = e_j`.

Instead, the candidate transition is:

`external relational differentiation -> internal closure`.

### Not supported

The tests do not show that increasing closure inevitably produces a single Point. Strong closure can instead produce fragmentation into several structures.

Therefore:

`closure -> single Point`

remains OPEN.

### Not yet tested

The desired outward channel was not reproduced as a robust effect. Outgoing core-to-exterior coupling remained small and did not show a clear monotonic relation to closure.

Energy is not an Ω-Math primitive, so no claim about energy escape is made.

## Important consequence

The candidate Point should not be defined as maximum closure.

The simulations instead suggest searching for a critical regime where three properties coexist:

1. one dominant internally coherent structure;
2. a persistent, narrow interface;
3. a non-zero external channel.

This is a stronger and more falsifiable target than simply maximizing closure.

## Information

No physical information or entropy was inserted into the model. Internal identity/state distinctions can remain while external relational description becomes coarser.

Thus:

`internal distinguishability != external distinguishability`.

## Null/control status

The first closure-vs-random experiment contained a random-rewiring null and showed increased modular separation under the closure rule. The second directed construction did not yet include a fully matched null ensemble with identical degree statistics.

Therefore causal attribution remains limited.

## Current conclusion

The combined tests support:

`relations -> closure -> relational separation -> candidate interface`

They do not yet establish:

`candidate interface -> Point`

and they do not establish any physical identification with a black hole.

## Next test

Run a parameter sweep with an explicit competition between:

`internal closure`

and

`fragmentation`

while independently preserving a small external coupling channel. Search for a stable critical window rather than the maximum-closure endpoint. Test robustness against matched degree-preserving and label-permutation nulls.

## Status

`SUPPORTED (LIMITED)` — emergent relational separation/core-interface formation.

`OPEN` — unique Ω-Point.

`OPEN` — outward energy/information channel.

`OPEN` — physical interpretation.
