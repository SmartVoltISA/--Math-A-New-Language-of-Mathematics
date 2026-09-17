# Ω-038 — Dynamic Graph, Memory and Polarity v1.0

**Status:** EXPERIMENT / PREREGISTERED MODEL
**Core:** Ω-Math v0.9 unchanged
**Purpose:** test whether value-coupled reinforcement plus graph adaptation and memory can produce persistent channel separation, and identify which ingredients are necessary.

## 1. Question

Test the closed research loop:

`objective/value → allocation → update → reinforcement → graph adaptation → memory → polarity`

The experiment must distinguish:

1. concentration without polarity;
2. polarity introduced by an explicit signed/competitive update;
3. persistent structural separation produced by graph adaptation and retention.

No physical interpretation is assumed.

## 2. Hypotheses

**H1:** value-coupled allocation plus an explicit competitive update can generate a signed state, but value sensitivity alone cannot.

**H2:** graph adaptation driven by the current signed state can increase same-polarity connectivity above a non-adaptive baseline.

**H3:** memory/retention can stabilize the resulting separation, but persistence must be measured rather than assumed.

**H4:** polarity is not evidence of a universal law unless the effect survives objective-family, parameter, seed, and update-law controls.

## 3. Null hypotheses

**H0-1:** without an explicit signed/competitive state update, the system does not generate meaningful signed polarity.

**H0-2:** adaptive graph rewiring does not increase same-polarity connectivity relative to the matched non-adaptive baseline.

**H0-3:** retention does not increase polarity persistence relative to the matched low-memory control.

## 4. Domain

Finite undirected weighted graph with `N=40` nodes and weights `A_ij >= 0`.

Node state `x_i` is real-valued. Polarity observable:

`z_i = sign(x_i)`

with zero handled by a preregistered deterministic convention.

The graph is external model structure; no claim is made that it is physical space.

## 5. Cost / allocation

At each step calculate a local same-sign agreement:

`h_i = Σ_j A_ij z_i z_j / Σ_j A_ij`.

Declare:

`J_i = 1 - γ h_i`, with fixed `γ > 0`.

Allocation:

`a_i = exp(-β J_i) / Σ_j exp(-β J_j)`.

The value/objective signal therefore enters only through an explicit allocation rule.

## 6. State update

Competitive treatment:

`x_i(t+1) = (1-δ)x_i(t) + η(a_i(t)-1/N) + ε_i(t)`.

Non-competitive control:

`x_i(t+1) = (1-δ)x_i(t) + η a_i(t) + ε_i(t)`.

The latter is a concentration control and does not impose a signed resource balance.

Noise `ε_i` is fixed by the preregistered seed and amplitude.

## 7. Graph adaptation

Adaptive treatment:

- same-sign edge: increase weight by a declared bounded reinforcement rule;
- opposite-sign edge: decrease weight by the matched decay rule;
- weights remain nonnegative and bounded.

Non-adaptive control keeps the initial graph fixed.

The graph update is a separate law and must not be described as a consequence of objective minimization alone.

## 8. Memory

Compare at least two retention regimes:

- low-memory: larger decay `δ`;
- high-memory: smaller decay `δ`.

Persistence metric is the fraction of nodes whose sign remains unchanged over a declared evaluation window after the driving signal is perturbed.

Memory is operationally defined by state retention; it is not equated with physical time.

## 9. Primary metrics

1. signed-state existence: fraction positive/negative and nonzero magnitude;
2. polarity balance: `|N_+ - N_-|/N`;
3. same-polarity edge fraction;
4. cross-polarity edge fraction;
5. graph modularity/channel separation as secondary diagnostics;
6. sign persistence after perturbation;
7. reinforcement concentration;
8. run-to-run variance;
9. comparison against matched non-adaptive and non-competitive controls.

## 10. Required controls

Minimum factorial comparison:

`competitive × adaptive × memory`

with matched seeds and initial graphs.

Also run a permutation control that destroys the relation between objective signal and node identity while preserving its marginal distribution.

## 11. Falsification

- If non-competitive control produces the same signed separation as competitive treatment, the signed-update mechanism is not supported as necessary.
- If adaptive and fixed graphs have indistinguishable same-sign connectivity, graph adaptation is not supported as the cause of channel separation.
- If high-memory and low-memory regimes have indistinguishable persistence, the memory-stabilization hypothesis is not supported.
- If effects disappear under matched objective-signal permutation, the proposed value coupling is implicated; if they remain, the mechanism is not specific to that signal.

## 12. Reproducibility

Use seeds `0..99`, fixed `N`, `T`, update parameters, initial graph generator, noise law, and graph-update law.

Record raw metrics and hashes before interpretation.

Target Level 2 reproducibility; Level 3 where practical.

## 13. Decision rules

**PASS:** preregistered directional effect is reproduced across the 100-seed family and survives matched control comparison with declared effect-size threshold.

**FAIL:** a mathematical or reproducibility requirement is contradicted.

**OPEN:** effect is model-dependent, unstable, underpowered, or sensitive to untested choices.

A PASS is only for the declared finite model family.

## 14. Critical boundary

This experiment does not test or establish:

`marginal cost ↓ → reinforcement → polarity`

as a universal law.

It tests the stronger mechanistic decomposition:

`value signal + allocation law + competitive update + graph adaptation + memory → persistent structural separation`.

Each arrow is separately controllable.
