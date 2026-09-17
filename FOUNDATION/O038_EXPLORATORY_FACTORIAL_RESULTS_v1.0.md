# Ω-038 — Exploratory Factorial Results v1.0

**Status:** EXPLORATORY RESULT / NOT PREREGISTERED PASS
**Experiment:** `O038_DYNAMIC_GRAPH_MEMORY_POLARITY_v1.0.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Execution status

A deterministic numerical factorial exploration was executed with 100 seeds (`0..99`) for all eight combinations of:

- competitive update: off/on;
- graph adaptation: off/on;
- high-memory retention: off/on.

Parameters used for this exploratory execution were frozen for the run as:

`N=40`, `T=300`, `η=0.04`, `β=3.0`, `γ=0.5`, `ρ=0.03`, noise amplitude `0.002`.

Memory parameter:

- low memory: `δ=0.12`;
- high memory: `δ=0.01`.

The initial graph was a symmetric dense nonnegative weighted graph generated from each fixed seed. The same seed was reused across matched factorial conditions.

**Important:** the original Ω-038 preregistration did not freeze all of these numerical choices before the run. Therefore this document remains exploratory and does not upgrade Ω-038 to a preregistered PASS.

## 2. Factorial results

Metrics are means over 100 seeds; SD is sample standard deviation where reported.

| Competitive | Adaptive | Memory | Same-sign edge fraction | Positive-node fraction | Sign persistence |
|---|---|---|---:|---:|---:|
| OFF | OFF | Low | 0.9151 | 0.9558 | 0.8903 |
| OFF | OFF | High | 0.6933 | 0.8155 | 0.6048 |
| OFF | ON | Low | 0.9269 | 0.9543 | 0.8880 |
| OFF | ON | High | 0.9657 | 0.8870 | 0.6030 |
| ON | OFF | Low | 0.5019 | 0.5050 | 0.4883 |
| ON | OFF | High | 0.5092 | 0.4998 | 0.5340 |
| ON | ON | Low | 0.5312 | 0.5020 | 0.4958 |
| ON | ON | High | 0.9320 | 0.4545 | 0.5393 |

## 3. Primary observation

The strongest separation occurs in the combination:

`competitive + adaptive + high-memory`

where same-sign connectivity reaches approximately `0.9320`, while the positive-node fraction remains near balanced (`0.4545`).

This differs qualitatively from the non-competitive cases, where the positive-node fraction approaches a near-unipolar state (`≈0.89–0.96`).

Thus high same-sign connectivity alone is not sufficient evidence for two-pole organization: a trivial one-sign collapse can also produce high same-sign connectivity.

## 4. Critical control discovered

The factorial run reveals a metric problem that must be fixed before formal claims about polarity persistence:

**same-sign connectivity can be inflated by global sign collapse.**

Therefore the next formal metric family must jointly require:

1. nontrivial occupancy of both signs;
2. high within-sign connectivity;
3. low cross-sign connectivity;
4. persistence after perturbation;
5. comparison against a sign-shuffled null preserving the positive/negative counts.

A useful separation score candidate is therefore conditional on both-sign occupancy rather than using same-sign fraction alone.

## 5. Mechanistic interpretation

Within this implementation, the combination of competitive resource balance and adaptive graph reinforcement produces the clearest transition from mixed connectivity toward a two-channel signed structure.

The observed loop is:

`competitive allocation → signed state → same-sign reinforcement / opposite-sign decay → graph separation → altered local agreement → allocation → signed state`

High memory changes retention of the signed state and therefore changes the dynamics of the loop, but the present exploratory metric does not establish memory as necessary or sufficient.

## 6. What is NOT established

The run does not establish:

- a universal law of polarity formation;
- that memory is necessary for polarity;
- that adaptive graph rewiring is universally necessary;
- that marginal cost itself causes reinforcement;
- physical correspondence;
- causality outside the declared update equations.

## 7. Required next formal test

Freeze the following **before execution**:

- all numerical parameters;
- exact graph update equation;
- exact perturbation protocol;
- persistence window;
- both-sign occupancy threshold;
- separation metric;
- sign-shuffled null;
- objective permutation control;
- effect-size threshold;
- multiple-testing family.

Then rerun 100 fixed matched seeds and evaluate the full factorial.

## 8. Decision

**RESULT:** strong exploratory evidence that competitive signed updating plus adaptive graph reinforcement can generate a highly separated two-sign structure in the declared finite model.

**DISCOVERY:** the current same-sign metric is confounded by one-sign collapse and must not be used alone as a polarity metric.

**STATUS:** OPEN.

The next formal experiment must test whether the two-sign separation survives the anti-collapse control and whether memory/adaptation/competition each contribute independently.
