# Ω-Math — Decisive Positive / Negative Criteria v1.0

Date: 2026-09-16
Status: PREREGISTERED DECISION FRAMEWORK

## Question

Can the Ω-Math structural kernel recover a non-trivial, domain-independent relational architecture from data while constitutive laws, units and domain labels are withheld?

Kernel under test:

`STATE + RELATION + DISTINCTION + CONSTRAINT + TRANSITION`

## Required evidence for a POSITIVE result

A positive result is not a good fit on one dataset. All mandatory gates must pass.

### P1 — Provenance

At least three independent physical domains and at least one independent dataset per domain. Every numeric field must have a source record. No derived target may be introduced without being declared before the blind lock.

### P2 — Blind lock

Domain names, physical units, equation names, constitutive coefficients and target-domain formulas are hidden before reconstruction. Preprocessing is frozen before the blind run.

### P3 — Fixed structural hypothesis

The reconstruction algorithm and candidate structural operator family are fixed before domain reveal. No choosing a model because it works on a revealed domain.

### P4 — Cross-domain structural replication

The same declared structural dependency graph must be recovered in all mandatory domains, with domain-specific parameters allowed only in the declared DOMAIN CLOSURE layer.

### P5 — Out-of-sample evidence

The recovered structure must predict held-out observations better than the preregistered null/baseline without using held-out information during fitting. Selection and preprocessing must remain inside the training procedure where applicable.

### P6 — Negative controls

Shuffled-response controls, independent-response controls and synthetic nonlinear controls must not be classified as positive structural recovery. A method that succeeds equally well on destroyed structure fails the gate.

### P7 — External replication

The result must reproduce on data not used to select the method or thresholds. Internal cross-validation alone is insufficient for the strongest claim.

### P8 — Leakage audit

No physical equation, unit conversion, target-derived feature, source-column identity or post-hoc transformation may leak from the hidden domain into the blind representation.

## POSITIVE decision

`POSITIVE / STRUCTURAL GENERALIZATION SUPPORTED`

only if P1–P8 all pass and the result survives an independent re-run.

This does **not** promote any physical quantity to a primitive. It supports only the declared structural claim.

## Required evidence for a NEGATIVE result

`NEGATIVE / CLAIM FALSIFIED`

if any of the following occurs in a preregistered decisive test:

1. The common structural architecture fails in the required independent domains.
2. The method cannot outperform the preregistered baseline out-of-sample.
3. Destroyed/shuffled controls produce comparable structural recovery.
4. The result depends on domain information or target-derived preprocessing.
5. Independent replication fails under the frozen protocol.

## INCONCLUSIVE state

A result is `INCONCLUSIVE` rather than negative when the protocol cannot make a valid determination because of insufficient data, missing provenance, inadequate independent test data, or a technical failure unrelated to the hypothesis.

## Important distinction

`POSITIVE` means evidence supports the structural claim.

`NEGATIVE` means the decisive test contradicts the structural claim.

`INCONCLUSIVE` means the experiment did not validly discriminate the two.

No p-value alone decides this question. Predictive evaluation must use held-out data, and leakage must be prevented; otherwise apparent performance can be inflated. citeturn0search3turn0search4

## Current pilot status

The first tungsten pilot is **INVALID AS EVIDENCE FOR THE CLAIM** because one anonymized target column (`y2`) is exactly `25 × x1`, while the source table contains temperature as the first column. That target was therefore not an independent raw source field. The pilot can remain as a procedural smoke test, but it cannot count toward P1–P8.

NIST's source table confirms the first rows: temperature 2,3,4,... and tungsten thermal-conductivity values 49.5,74.2,98.9,... with residual resistivity values near 0.988. citeturn2search24

## Decision rule

Do not call the project positive until the full frozen multi-domain experiment passes. Do not call the theory false because this pilot is invalid. The correct current state is `INVALID PILOT → REPEAT WITH CLEAN RAW DATA`.
