# Ω-Math Frontier Results v1.0

Execution mode: **local Python**, deterministic seeds where applicable.

Date: 2026-09-09

## F-01 — Symmetry and emergent direction

### Model A: deterministic symmetric excitable ring
- 48-node periodic ring.
- Three states: quiescent, excited, refractory.
- Local rule is invariant under rotation and reflection.
- 200 random initial states were paired with their spatial reflections.
- The oriented propagation observable changes sign under reflection.

Observed:
- opposite-sign reflection pairs: **83%** when both members exceeded the |chirality| > 0.05 threshold;
- mean paired signed sum: **0.0**;
- therefore no preferred orientation is selected by the rule itself.

### Model B: exact symmetric initial state + unbiased stochastic triggering
- 96-node periodic ring.
- Initial state: all quiescent (exactly symmetric).
- 500 independent seeds.
- Symmetric local transition rule and unbiased site noise.
- No moving pulse, asymmetric edge, preferred coordinate direction, or directed initialization.

Observed:
- ensemble signed chirality mean: **0.000320**;
- standard error: **0.001411**;
- mean absolute signed chirality: **0.024956**.

Interpretation:
- local directional fluctuations can emerge from a symmetric system;
- the ensemble does not select a preferred sign;
- this is compatible with spontaneous realization-level symmetry breaking, but does **not** establish a fundamental arrow of time/space.

Status: **NOT PROVEN** as a universal/fundamental direction generator.

## F-02 — Physical time

Construct the same relational transition sequence and assign multiple external durations: 3 s, 30 s, 300 s.

All Ω-Math relational states and transitions are identical. Therefore the relational core does not identify a unique physical duration.

Status: **NON-IDENTIFIABLE** without an external clock/coupling rule.

## F-03 — Physical energy

Take an identical transformation chain with positive costs `[1,2,3]` and rescale it by arbitrary positive factors: 1, 10, 0.01, 7.3.

The relational transformation structure is unchanged while the numerical scale changes.

Status: **NON-IDENTIFIABLE**. A physical energy interpretation requires independent calibration or additional conservation/dynamical structure.

## F-04 — Probability

For the realized binary sequence `[1,0,1,1,0,0,1]`, the likelihood is nonzero under Bernoulli p=.1, p=.5 and p=.9.

The realized relational history therefore does not uniquely determine a probability law.

Status: **NOT DERIVABLE** from the deterministic relational core.

## F-05 — Causality

Two models can produce the same observational relation:

- Model A: `X → Y`, with `Y=X`.
- Model B: hidden `U → X` and `U → Y`, with `X=U`, `Y=U`.

Observationally, `Y=X` in both models. Under intervention `do(X=1)`, Model A gives `P(Y=1)=1`, while Model B gives `P(Y=1)=0.5`.

Status: **OBSERVATIONALLY NON-IDENTIFIABLE**; interventions add the required discrimination. Universal causality is not proven.

## F-06 — Physical ontology

The same formal graph/state structure can consistently be interpreted as a physical system, an information-processing system, or an abstract mathematical object.

No purely formal transformation of the current Ω-Math core selects one interpretation.

Status: **NOT PROVEN**. Independent empirical correspondence is required.

## F-07 — Universal metric

A symmetric weighted cycle produces a symmetric shortest-path distance with zero symmetry error. Introducing explicit directional edge costs produces a shortest-path quantity with nonzero symmetry error (maximum observed difference 4 in the test construction).

Therefore metric axioms can be verified for declared symmetric constructions, but symmetry is not guaranteed by the general relational core.

Status: **UNIVERSAL METRIC NOT PROVEN**. The natural generalization for directed systems may be a quasi-metric/directed distance rather than a metric.

## Final frontier verdict

### Confirmed/supportable
- formal typed relational execution;
- deterministic research records and falsification workflow;
- relation recovery in tested model classes;
- intervention-based causal discrimination in tested models;
- operational geometry in tested models;
- operational nonreciprocity under the EXP-002 learning mechanism;
- realization-level directional asymmetry can arise without an explicitly directed initial edge or moving pulse.

### Still open / blocked by identifiability
- fundamental physical time;
- fundamental physical energy;
- probability as a uniquely derived primitive;
- universal causal direction from observation alone;
- physical ontology;
- universal symmetric metric;
- a unique fundamental arrow/direction emerging from complete symmetry.

### Scientific boundary

The work currently supports:

`distinction → relation → structure → path → transformation → observation → dynamics → operational geometry → operational directionality`

It does not yet establish:

`operational structure → physical space/time/energy/probability/causality/ontology`.

Those claims remain gated behind independent empirical correspondence.
