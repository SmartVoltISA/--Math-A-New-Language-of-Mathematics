# Ω-038 — Formal Results v1.2: Common Two-Pole Ensemble Restoration

**Status:** RESULT RECORDED / OPEN INTERPRETATION
**Preregistration:** `O038_FORMAL_PREREGISTRATION_v1.2.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Execution

The frozen v1.2 model was executed for all eight factorial conditions using the same seed-specific initial graph, initial node state, and structural perturbation across each factorial cell.

Seeds: `0..99`.

The initial ensemble was constructed with exactly 20 positive and 20 negative nodes, strong within-sign edges and weaker cross-sign edges. The perturbation flipped 12 node signs, added Normal(0,0.15) state noise, and reduced 30% of edges to 10% of their pre-perturbation weight.

Restoration required a valid two-pole state (`B>=0.20`, `D>=0.10`) for 10 consecutive evaluation steps within 100 recovery steps.

## 2. Results

| Competitive | Adaptive | Memory | Restored / 100 | Restoration rate | Median recovery step |
|---|---|---|---:|---:|---:|
| OFF | OFF | Low | 0 | 0.00 | N/A |
| OFF | OFF | High | 0 | 0.00 | N/A |
| OFF | ON | Low | 100 | 1.00 | 4 |
| OFF | ON | High | 100 | 1.00 | 4 |
| ON | OFF | Low | 0 | 0.00 | N/A |
| ON | OFF | High | 0 | 0.00 | N/A |
| ON | ON | Low | 100 | 1.00 | 4 |
| ON | ON | High | 100 | 1.00 | 4 |

## 3. Primary result

Under this declared finite model and perturbation, **adaptive graph reinforcement is the factor associated with restoration**: every adaptive condition restored the valid two-pole state for all 100 matched seeds, while every nonadaptive condition restored for 0/100.

Pooling over competition and memory:

- adaptive ON: 200/200 restored;
- adaptive OFF: 0/200 restored;
- matched restoration-rate difference: `1.00`.

This exceeds the preregistered descriptive threshold of `0.20`.

Competition did not change the restoration outcome in this experiment: adaptive conditions restored in both competitive states and nonadaptive conditions failed in both competitive states.

Memory level also did not change the binary restoration outcome in this experiment: both low- and high-memory adaptive conditions restored, while both memory levels failed without adaptation.

## 4. What this actually shows

The result is a clean factor-attribution result **for the declared model and perturbation**:

`adaptive relation update → restoration of two-pole structure`

It does not show that competition or memory are unnecessary in general. It shows only that, with this common initial ensemble, parameter set, and perturbation, changing those factors did not alter the binary restoration result.

## 5. Mechanistic observation

The adaptive rule directly reinforces edges whose endpoints currently share a sign and weakens cross-sign edges. After the perturbation, this creates a feedback path that rebuilds the structural separation:

`current sign → edge reinforcement/depression → stronger same-sign topology → local agreement → allocation/state update → current sign`

Thus restoration is not surprising under the declared adaptive rule; the experiment establishes robustness of that mechanism under the specified damage, rather than discovering a law without an encoded restoration mechanism.

## 6. Critical limitation

The experiment still does **not** derive reinforcement from marginal cost. The adaptive reinforcement rule is explicitly encoded as:

`A_ij' = A_ij(1+rho)` for same-sign endpoints and `A_ij' = A_ij(1-rho)` for opposite-sign endpoints.

Therefore the chain

`marginal cost ↓ → reinforcement → polarity`

remains OPEN/HYPOTHESIS.

The next scientifically meaningful step is to replace the explicit reinforcement rule with a rule derived from a declared cost/functional and test whether reinforcement and two-pole restoration emerge without being hard-coded.

## 7. Methodological result

The common-ensemble design fixes the principal confound of v1.1: controls no longer fail merely because they cannot form a valid two-pole state before perturbation. All conditions start from the same valid structure.

The resulting factor attribution is therefore substantially cleaner than v1.1 for the restoration question.

## 8. Decision

**RESULT:** v1.2 executed as preregistered.

**RESULT:** adaptive ON restored 200/200 matched trials; adaptive OFF restored 0/200.

**RESULT:** competition and memory showed no binary restoration effect under these parameters.

**DECISION:** proceed to Ω-039: remove explicit reinforcement and derive the graph update from the objective/cost-functional layer. Test whether reinforcement appears as an emergent consequence rather than an imposed rule.

**STATUS:** OPEN — Ω-039 required.
