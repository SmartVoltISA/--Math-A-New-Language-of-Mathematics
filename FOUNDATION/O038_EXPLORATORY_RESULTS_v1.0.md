# Ω-038 — Exploratory Dynamic Graph Results v1.0

**Status:** EXPLORATORY RESULT / NOT A PREREGISTERED PASS
**Experiment:** `O038_DYNAMIC_GRAPH_MEMORY_POLARITY_v1.0.md`
**Core:** Ω-Math v0.9 unchanged

## 1. Execution

A local deterministic numerical exploration was run with 100 seeds (`0..99`) using `N=40`, `T=300`, `η=0.04`, `β=3`, noise amplitude `0.002`, and adaptive graph reinforcement parameter `ρ=0.03`. The graph started as a symmetric dense nonnegative weighted graph. The exploratory implementation used `δ=0.01`.

Because the preregistration intentionally left the exact parameter values of `γ`, `δ` regimes, graph update formula, and evaluation window to be fixed before formal execution, these runs are recorded as exploratory and are **not** declared a preregistered PASS.

## 2. Adaptive graph result

The adaptive model increased same-polarity edge fraction to:

`mean = 0.76115`

`SD = 0.12024`

across 100 seeds.

The matched fixed-graph baseline gave:

`mean = 0.50210`

Therefore the mean difference was:

`Δ = +0.25905`.

In 99 of 100 paired seeds, the adaptive graph had higher same-polarity connectivity than the fixed graph.

## 3. Polarity balance

The positive-node fraction in the adaptive runs had:

`mean = 0.3500`

`SD = 0.0642`.

Thus the system commonly contained both signs rather than collapsing to one sign, but the exact balance varied by seed.

This is evidence of signed separation in this model, not evidence that a universal two-pole state necessarily emerges.

## 4. Interpretation

The strongest exploratory observation is the separation between:

`node-sign state`

and

`graph topology`.

The graph adaptation rule selectively strengthens same-sign connections and weakens opposite-sign connections. Consequently, an initially mixed graph becomes substantially more homophilic.

This demonstrates a self-reinforcing structural loop inside the declared model:

`sign state → graph adaptation → increased same-sign connectivity → altered local objective → allocation/update → sign state`.

The loop is a model construction, not a theorem of nature.

## 5. Controls and limitations

The result is not sufficient to claim that memory causes persistence because only one exploratory retention regime was executed here.

It is also not sufficient to claim that the value signal is necessary, because the objective-family and permutation controls from the preregistration were not all executed in this exploratory pass.

No physical correspondence was tested.

## 6. Decision

**RESULT:** exploratory support for the hypothesis that an explicit signed state plus adaptive same-sign reinforcement can produce substantial structural channel separation in a finite dynamic graph.

**STATUS:** OPEN.

No PASS is assigned to H1–H4 from this exploratory run.

## 7. Next formal test

Before formal execution, freeze:

- `γ`;
- low/high-memory `δ` values;
- exact graph-update equation;
- perturbation protocol;
- persistence window;
- effect-size threshold;
- permutation procedure.

Then execute the full `competitive × adaptive × memory` factorial with matched seeds and record raw outputs before interpretation.
