# Ω-Math — Physical Experiments Program

Version: 1.0  
Date: 2026-09-09  
Status: PROTOCOLS FOR INDEPENDENT TESTING

## Purpose

This directory translates the Ω-Math algebra-selection problem into physical experiments. The central rule is strict:

> The physical measurement must be defined independently of the candidate Ω-Math algebra.

The experiments do **not** assume that max-min, min-plus, or sum-product is fundamental. They test whether independently measured physical behavior is better predicted by one candidate composition law than by competing laws.

## Candidate algebras

### A — max-min

`(A ∘ B)_ij = max_k min(A_ik, B_kj)`

Natural interpretation to test: bottleneck / limiting-capacity propagation.

### B — min-plus

`(A ∘ B)_ij = min_k (A_ik + B_kj)`

Natural interpretation to test: minimum accumulated cost/time.

### C — sum-product

`(A ∘ B)_ij = Σ_k A_ik B_kj`

Natural interpretation to test: additive superposition / linear transfer.

These interpretations are hypotheses, not definitions of the measurements.

---

# PE-001 — Wave propagation / travel time

## Physical system

A one-dimensional chain of coupled sensors or an acoustic/mechanical waveguide.

Possible implementations:
- acoustic tube with microphones;
- string or rod with accelerometers;
- water-wave channel with optical or pressure sensors.

## Independent measurements

Record, without any Ω-Math preprocessing:
- sensor position;
- excitation time;
- arrival time;
- peak amplitude;
- signal envelope;
- uncertainty of each measurement.

## Procedure

1. Randomize sensor labels.
2. Excite the first location with a short calibrated pulse.
3. Record the complete waveform at all sensors.
4. Repeat from several source locations.
5. Repeat in both directions where physically possible.
6. Reserve source/receiver combinations for a blind held-out test.
7. Only after data lock, construct candidate relational models.

## Primary prediction

Travel times should be approximately additive along serial paths. Therefore min-plus should produce the strongest prediction for earliest arrival time when the medium behaves as a propagation-delay network.

## Expected result if hypothesis is supported

`prediction_error(min-plus) << prediction_error(max-min)` and `prediction_error(min-plus) << prediction_error(sum-product)` on held-out source/receiver pairs.

## Expected null result

No stable separation, or performance depends on the fitting procedure. Then algebra selection is NOT PROVEN.

## Important control

Use a reciprocal homogeneous medium. Directional asymmetry must not be assumed.

---

# PE-002 — Electrical resistor network / conductance

## Physical system

A passive network of resistors with independently measured voltage and current at nodes/branches.

## Independent measurements

Measure:
- resistance values with calibrated instruments;
- applied voltage;
- node voltages;
- branch currents;
- transient response if RC elements are included.

The network topology and component values are recorded before model fitting.

## Procedure

1. Build several networks with different topologies.
2. Randomly choose a subset of node/edge measurements for training.
3. Hold out other measurements.
4. Fit each candidate algebra separately.
5. Predict held-out voltages/currents.
6. Repeat with relabelled nodes and independently rebuilt networks.

## Prediction

For a linear passive network, superposition-like behavior is expected. This makes sum-product a strong candidate for transfer composition.

## Expected result if supported

Sum-product consistently predicts held-out transfer behavior better than max-min and min-plus under the same observation protocol.

## Critical caution

This would support sum-product for this physical model class. It would **not** prove sum-product is universally fundamental.

---

# PE-003 — Bottleneck flow network

## Physical system

A fluid or electrical-current network containing controllable restrictions.

Examples:
- transparent tubing with valves/restrictors;
- low-voltage hydraulic analogue;
- safe laboratory flow network.

## Independent measurements

Measure:
- input flow;
- output flow;
- pressure difference;
- restriction capacity;
- temperature where relevant.

## Prediction

For serial restrictions, the effective capacity is controlled by the weakest link. This gives max-min a direct physical hypothesis.

## Expected result if supported

Max-min predicts held-out effective capacity better than min-plus and sum-product across networks with multiple serial and branching paths.

## Key adversarial test

Construct parallel paths where a sum of capacities can compete with a bottleneck. This prevents the experiment from being trivial.

---

# PE-004 — Coupled oscillators

## Physical system

Two or more mechanical/electrical oscillators coupled by known passive interactions.

Possible implementations:
- pendulums;
- masses and springs;
- low-voltage electronic oscillators.

## Independent measurements

Record:
- displacement/voltage versus time;
- phase;
- frequency;
- coupling configuration;
- damping.

## Goal

Test whether composition of measured transfer responses is better described by one candidate algebra, without defining the measured response through that algebra.

## Expected result

No candidate is assumed in advance. The result is informative only if one algebra wins consistently across independently built systems and held-out conditions.

---

# PE-005 — One physical system, three independent observables

This is the strongest combined experiment.

Use one networked physical system and measure three fundamentally different observables:

1. travel time;
2. signal amplitude/transfer;
3. throughput/capacity.

Then independently test:

`time → min-plus hypothesis`  
`transfer amplitude → sum-product hypothesis`  
`capacity → max-min hypothesis`

## Why this matters

If the same physical structure naturally produces different composition laws for different observables, this is evidence that algebra is tied to the transformation law of the observable rather than being contained in bare topology.

If one algebra dominates all three observables and survives cross-system replication, that becomes a much stronger candidate for deeper status.

---

# Blind-analysis protocol

Every serious physical run should register before measurement:

- hypothesis ID;
- apparatus description;
- topology;
- calibration method;
- sampling rate;
- uncertainty model;
- train/test split;
- candidate algebra definitions;
- primary metric;
- exclusion criteria;
- stopping rule;
- null hypothesis.

The analyst should not change the primary metric after seeing which algebra wins.

## Primary metric

Use held-out predictive error. Prefer normalized RMSE/MAE for continuous observables. Report confidence intervals and paired differences between candidate models.

Secondary metrics may include:
- rank correlation;
- likelihood where justified;
- robustness to calibration uncertainty;
- prediction under relabelling;
- prediction under controlled perturbations.

---

# Required controls

## Negative control

A system or measurement condition in which the proposed relational signal should disappear. The analysis pipeline must not manufacture an algebra preference.

## Positive control

A known physical relation where the measurement pipeline demonstrably detects the expected effect.

## Symmetry control

Use physically reciprocal systems to test whether an apparent directionality is an artefact of sensors, wiring, geometry, or analysis.

## Instrument permutation control

Randomly permute sensor labels after acquisition. Physical predictions must transform covariantly; arbitrary label-dependent conclusions are invalid.

## Calibration perturbation

Repeat the model comparison under realistic calibration uncertainty.

---

# What counts as a result

### PASS — empirical algebra discrimination

One candidate has significantly lower held-out prediction error than competitors, the effect survives controls, and the result replicates on independently rebuilt systems.

### PARTIAL

A candidate wins for one apparatus/observable but not under independent replication or alternate measurement conditions.

### NOT PROVEN

No reliable separation between candidates.

### FAIL

The proposed algebra loses to a competitor or the effect disappears under a declared control.

### INVALID

Measurement leakage, post-hoc metric selection, calibration failure, insufficient data, or another preregistered validity violation.

---

# Expected global outcomes

There are three scientifically useful outcomes.

## Outcome A — Observable-dependent algebra

Different observables consistently favor different algebras.

Interpretation:

`physical system → observable → transformation law → effective algebra`

This would strengthen the Ω-Math distinction between relational carrier and algebra-sensitive observable.

## Outcome B — Cross-domain algebra winner

The same algebra repeatedly wins across unrelated physical systems and observables.

Interpretation: a serious candidate for a deeper universal regularity, but still not automatically a fundamental law.

## Outcome C — No stable winner

Different datasets favor different models, or all candidates perform similarly.

Interpretation: no evidence for a universal algebra. This is a valid and important negative result.

---

# Safety

Use only safe, low-energy laboratory systems and standard measurement equipment. No mains-voltage experiments are required. Electrical demonstrations should use isolated low-voltage supplies and appropriate protection. Flow experiments should use benign fluids at safe pressures.

---

# Replication package expected from an independent tester

Each completed experiment should publish:

1. apparatus diagram;
2. raw measurements;
3. calibration records;
4. preregistration;
5. analysis code;
6. candidate-model definitions;
7. held-out predictions;
8. residual/error tables;
9. controls;
10. exact conclusion: PASS / PARTIAL / NOT PROVEN / FAIL / INVALID.

The raw data must remain sufficient for an independent analyst to rerun the comparison without contacting the original experimenter.

---

# Current status

These are **proposed physical tests**, not completed experiments.

No predicted result is evidence until an independent physical experiment produces it.

The program deliberately separates:

`mathematical possibility → physical hypothesis → preregistered measurement → blind prediction → replication → possible promotion`.
