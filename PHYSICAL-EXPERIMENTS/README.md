# Ω-Math — Physical Experiments Program

Version: 1.1  
Date: 2026-09-09  
Status: PROTOCOLS FOR INDEPENDENT TESTING

## Purpose

This directory translates the Ω-Math algebra-selection problem into physical experiments. The central rule is strict:

> The physical measurement must be defined independently of the candidate Ω-Math algebra.

The experiments do **not** assume that max-min, min-plus, or sum-product is fundamental. They test whether independently measured physical behavior is better predicted by one candidate composition law than by competing laws.

A second rule is now mandatory:

> Physical experiments must not be treated as clean mathematical experiments. Raw measurements contain environmental variation, instrument error, calibration uncertainty, finite resolution and uncontrolled disturbances. These effects must be measured, modelled and propagated into the final uncertainty.

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

# PHYSICAL MEASUREMENT LAYER — MANDATORY

The mathematical model must receive a **measurement record**, not an idealized number.

For every observation record store:

`raw signal → calibration → environmental state → corrected estimate → uncertainty`

Never replace this chain by a single clean value without retaining the raw data.

## Environmental variables

Depending on the experiment, record at minimum the variables that can materially affect the measurement:

- air temperature;
- atmospheric pressure;
- relative humidity;
- air density, calculated or independently measured when relevant;
- medium temperature;
- fluid density and viscosity when relevant;
- local acceleration due to gravity when relevant;
- ambient vibration;
- background acoustic/electromagnetic noise;
- supply voltage/current for electrical systems;
- sensor temperature;
- apparatus geometry and thermal expansion;
- timestamp from a calibrated reference clock.

Not every variable is required for every experiment. The protocol must state explicitly which variables are relevant and which were tested and found negligible.

## Air density

For experiments involving propagation through air, do not assume a fixed density. Use the measured temperature, pressure and humidity to estimate air density with a declared physical model, and propagate its uncertainty.

Conceptually:

`rho_air = f(T, p, RH, gas composition)`

The exact equation/model and constants must be frozen during preregistration.

## Other environmental corrections

Examples:

- acoustic propagation: temperature, pressure, humidity, air composition;
- mechanical propagation: temperature, material properties, tension, geometry, gravity;
- fluid flow: pressure, temperature, density, viscosity, tube geometry;
- electrical circuits: component temperature coefficients, supply stability, contact resistance, parasitic capacitance/inductance;
- optical measurements: temperature, refractive index, pressure/humidity where relevant;
- timing: reference-clock accuracy, oscillator drift, cable/sensor latency.

The purpose is not to eliminate the environment. The purpose is to **measure it and include it in the uncertainty budget**.

---

# UNCERTAINTY BUDGET

Every physical experiment must publish an uncertainty budget before the final model comparison.

Separate at least:

1. **Type A uncertainty** — estimated statistically from repeated measurements;
2. **Type B uncertainty** — calibration certificates, instrument resolution, manufacturer specifications, physical constants, environmental-model uncertainty and other justified sources.

For an output `y = f(x1, ..., xn)`, propagate uncertainties using the declared method. For approximately independent inputs:

`u_y^2 ≈ Σ_i (∂f/∂x_i)^2 u_i^2`

If nonlinearities, correlations or large uncertainties make first-order propagation inadequate, use a preregistered Monte Carlo propagation or another justified method.

## Correlated errors

Do not assume independence automatically. Examples:

- common clock error affects many sensors;
- common temperature drift affects many measurements;
- calibration factor shared by a sensor family creates covariance;
- pressure measurement may be correlated with density calculation.

The covariance structure must be retained where known.

## Final result format

Do not report only:

`prediction = 12.37`

Report something like:

`prediction = 12.37 ± 0.08 (expanded uncertainty, k=2)`

or provide a confidence/credible interval using a preregistered statistical definition.

The exact convention must be declared before analysis.

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
- uncertainty of each measurement;
- environmental state at the time of each run.

For acoustic air experiments additionally record:
- air temperature;
- atmospheric pressure;
- relative humidity;
- estimated air density;
- sensor/microphone calibration;
- ambient sound level.

## Procedure

1. Randomize sensor labels.
2. Excite the first location with a short calibrated pulse.
3. Record the complete waveform at all sensors.
4. Record environmental variables synchronously or as close in time as practical.
5. Repeat from several source locations.
6. Repeat in both directions where physically possible.
7. Reserve source/receiver combinations for a blind held-out test.
8. Lock raw data and environmental metadata.
9. Apply only preregistered calibration/correction procedures.
10. Propagate uncertainty into every derived travel-time estimate.
11. Only after data lock construct candidate relational models.

## Physical prediction

For a sufficiently homogeneous propagation medium, travel time along serial segments is expected to be approximately additive. Therefore min-plus is the leading candidate for earliest-arrival composition.

But the test is not:

`clean mathematical travel time → min-plus`.

It is:

`measured travel time + environmental state + uncertainty → held-out prediction`.

## Expected result if hypothesis is supported

`error(min-plus)` should be significantly smaller than competing errors on held-out paths, with the difference remaining larger than the combined experimental uncertainty and surviving environmental corrections.

A stronger result is obtained if the same preference survives changes in temperature, pressure and humidity and independent apparatus rebuilds.

## Expected null result

If candidate differences fall within the uncertainty interval, or the winning algebra changes after reasonable environmental correction, algebra selection is NOT PROVEN.

## Important control

Use a reciprocal homogeneous medium. Directional asymmetry must not be assumed.

---

# PE-002 — Electrical resistor network / conductance

## Physical system

A passive low-voltage network of resistors, optionally with capacitors/inductors, with independently measured voltage and current.

## Independent measurements

Measure:
- component values and tolerances;
- component temperature;
- applied voltage/current;
- node voltages;
- branch currents;
- frequency where AC is used;
- instrument calibration and resolution;
- supply stability;
- contact resistance where material.

## Environmental correction

Component resistance and other parameters may depend on temperature. Measure component temperature and use declared temperature coefficients where justified. Record supply drift and measurement uncertainty.

## Procedure

1. Build several networks with different topologies.
2. Calibrate instruments.
3. Record environmental and electrical state.
4. Randomly choose a subset of measurements for training.
5. Hold out other measurements.
6. Fit each candidate algebra separately.
7. Propagate component and instrument uncertainty.
8. Predict held-out voltages/currents with uncertainty intervals.
9. Repeat with relabelled nodes and independently rebuilt networks.

## Prediction

For a linear passive network, superposition-like behavior is expected. This makes sum-product a strong candidate for transfer composition.

## Expected result if supported

Sum-product consistently predicts held-out transfer behavior better than max-min and min-plus, with a statistically significant and uncertainty-robust margin.

## Critical caution

This supports sum-product only for the tested physical model class. It does not prove sum-product universally fundamental.

---

# PE-003 — Bottleneck flow network

## Physical system

A benign low-pressure fluid network containing controllable restrictions.

Examples:
- transparent tubing with valves/restrictors;
- safe laboratory flow network.

## Independent measurements

Measure:
- input/output flow;
- pressure difference;
- temperature;
- fluid density;
- fluid viscosity;
- restriction geometry/capacity;
- sensor calibration;
- environmental pressure where relevant.

## Prediction

For serial restrictions, effective capacity can be controlled by the weakest link, giving max-min a direct physical hypothesis.

## Expected result if supported

Max-min predicts held-out effective capacity better than min-plus and sum-product across networks with serial and branching paths, with the advantage surviving uncertainty propagation.

## Adversarial test

Construct parallel paths where capacities can add. This prevents a trivial experiment in which max-min is guaranteed by construction.

---

# PE-004 — Coupled oscillators

## Physical system

Two or more mechanical or low-voltage electronic oscillators coupled by known passive interactions.

## Independent measurements

Record:
- displacement/voltage versus time;
- phase;
- frequency;
- coupling configuration;
- damping;
- temperature;
- timing-reference uncertainty;
- sensor calibration.

## Goal

Test whether composition of measured transfer responses is better described by one candidate algebra without defining the measured response through that algebra.

Environmental drift and timing uncertainty must be propagated into phase and frequency estimates.

## Expected result

No candidate is assumed in advance. A meaningful positive result requires one algebra to win consistently across independently built systems and held-out conditions by more than the experimental uncertainty.

---

# PE-005 — One physical system, three independent observables

This is the strongest combined experiment.

Use one networked physical system and measure three fundamentally different observables:

1. travel time;
2. signal amplitude/transfer;
3. throughput/capacity.

Record all relevant environmental variables and their uncertainties for every run.

Then independently test:

`time → min-plus hypothesis`  
`transfer amplitude → sum-product hypothesis`  
`capacity → max-min hypothesis`

The final comparison must use uncertainty-aware held-out predictions, not ideal values.

## Why this matters

If the same physical structure naturally produces different composition laws for different observables, this is evidence that algebra is tied to the transformation law of the observable rather than being contained in bare topology.

If one algebra dominates all three observables and survives cross-system replication with margins larger than experimental uncertainty, that becomes a much stronger candidate for deeper status.

---

# FULL PHYSICAL ERROR MODEL

A useful conceptual decomposition is:

`observed = ideal physical response + environmental variation + instrument error + stochastic noise + model discrepancy`

Do not silently absorb all deviations into random noise. Separate what can be measured from what cannot.

## Environmental variation

If temperature, pressure, humidity or another variable changes during the experiment, record the value and test its influence.

## Instrument uncertainty

Include:
- calibration uncertainty;
- digitization/ADC resolution;
- sensor bandwidth;
- timing resolution;
- systematic offset;
- gain uncertainty;
- latency.

## Model discrepancy

Even a correct physical model may not reproduce reality exactly. Report residuals rather than forcing them into measurement uncertainty.

## Repeated trials

Repeat enough times to estimate the distribution of the measured observable. Do not confuse repeatability with accuracy.

---

# ENVIRONMENTAL ADVERSARIAL TEST

At least one physical experiment should deliberately vary an environmental parameter across a controlled range.

Example for acoustic propagation:

`temperature: low → nominal → high`

while independently recording pressure and humidity.

The candidate algebra must be evaluated against corrected observations under all conditions.

A claimed effect that disappears after proper environmental correction is **FAIL**, not a discovery.

A claimed effect that remains after correction and uncertainty propagation is substantially stronger evidence.

---

# BLIND-ANALYSIS PROTOCOL

Every serious physical run should register before measurement:

- hypothesis ID;
- apparatus description;
- topology;
- calibration method;
- sampling rate;
- environmental variables to record;
- uncertainty model;
- train/test split;
- candidate algebra definitions;
- primary metric;
- exclusion criteria;
- stopping rule;
- null hypothesis;
- correction models and constants;
- uncertainty convention.

The analyst should not change the primary metric or correction model after seeing which algebra wins.

## Primary metric

Use held-out predictive error with uncertainty-aware comparison. Prefer normalized RMSE/MAE for continuous observables. Report confidence intervals and paired differences between candidate models.

Secondary metrics may include:
- rank correlation;
- likelihood where justified;
- robustness to calibration uncertainty;
- prediction under relabelling;
- prediction under controlled perturbations.

---

# REQUIRED CONTROLS

## Negative control

A system or measurement condition in which the proposed relational signal should disappear. The analysis pipeline must not manufacture an algebra preference.

## Positive control

A known physical relation where the measurement pipeline demonstrably detects the expected effect.

## Symmetry control

Use physically reciprocal systems to test whether apparent directionality is an artefact of sensors, wiring, geometry, environment or analysis.

## Instrument permutation control

Randomly permute sensor labels after acquisition. Physical predictions must transform covariantly; arbitrary label-dependent conclusions are invalid.

## Calibration perturbation

Repeat the model comparison under realistic calibration uncertainty.

## Environmental correction control

Compare:
1. raw data;
2. corrected data;
3. uncertainty-expanded predictions.

A candidate should not be declared the winner solely because it fits an uncorrected environmental artefact.

---

# WHAT COUNTS AS A RESULT

### PASS — empirical algebra discrimination

One candidate has significantly lower held-out prediction error than competitors, the effect survives environmental correction and uncertainty propagation, the controls pass, and the result replicates on independently rebuilt systems.

### PARTIAL

A candidate wins for one apparatus/observable but not under independent replication or alternate measurement conditions.

### NOT PROVEN

No reliable separation between candidates, or the difference is comparable to experimental uncertainty.

### FAIL

The proposed algebra loses to a competitor or the effect disappears under a declared control/correction.

### INVALID

Measurement leakage, post-hoc metric selection, calibration failure, invalid environmental correction, insufficient data, or another preregistered validity violation.

---

# EXPECTED GLOBAL OUTCOMES

There are three scientifically useful outcomes.

## Outcome A — Observable-dependent algebra

Different observables consistently favor different algebras after environmental corrections and uncertainty propagation.

Interpretation:

`physical system → observable → transformation law → effective algebra`

This would strengthen the Ω-Math distinction between relational carrier and algebra-sensitive observable.

## Outcome B — Cross-domain algebra winner

The same algebra repeatedly wins across unrelated physical systems and observables with margins larger than experimental uncertainty.

Interpretation: a serious candidate for a deeper universal regularity, but still not automatically a fundamental law.

## Outcome C — No stable winner

Different datasets favor different models, or all candidates perform similarly within uncertainty.

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
4. environmental time series;
5. preregistration;
6. analysis code;
7. candidate-model definitions;
8. held-out predictions;
9. uncertainty budget;
10. residual/error tables;
11. controls;
12. exact conclusion: PASS / PARTIAL / NOT PROVEN / FAIL / INVALID.

The raw data must remain sufficient for an independent analyst to rerun the comparison without contacting the original experimenter.

---

# Current status

These are **proposed physical tests**, not completed experiments.

No predicted result is evidence until an independent physical experiment produces it.

The program deliberately separates:

`mathematical possibility → physical hypothesis → raw measurement → environmental correction → uncertainty propagation → blind prediction → replication → possible promotion`.
