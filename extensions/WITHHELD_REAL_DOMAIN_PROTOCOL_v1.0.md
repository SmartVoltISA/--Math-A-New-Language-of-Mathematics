# Ω-Math — Withheld Real-Domain Reconstruction Protocol v1.0

Date: 2026-09-16
Status: RESEARCH TEST SPECIFICATION

## Purpose

Test whether the Ω-Math structural kernel can recover a common response architecture from independent domain observations when constitutive laws, coefficients, units and domain names are hidden during reconstruction.

This is deliberately stronger than fitting `J = gΔ` to synthetic equations.

## Kernel presented to the reconstructor

Only:

`STATE + RELATION + DISTINCTION + CONSTRAINT + TRANSITION`

The reconstructor may infer a typed structural response of the form:

`J = H(S, R, Δ, C)`

but receives no constitutive coefficient, target-domain equation, physical unit, or domain-specific constant.

## Target families

Use independently sourced observations representing at least:

1. electrical response under a controlled potential difference;
2. thermal response under a controlled temperature difference;
3. fluid response under a controlled pressure difference.

The domain labels are withheld during reconstruction and restored only for evaluation.

## Required controls

### Positive structural control

The three datasets must permit identification of a directed response associated with a relevant asymmetry and coupling relation.

### Coefficient-withholding control

Scale factors must vary independently between datasets. A successful structural reconstruction must not infer one universal numerical coefficient.

### Nonlinear control

At least one target must include a regime where a simple linear constitutive form is insufficient. The reconstructor must be allowed to return `NONLINEAR/DOMAIN-CLOSURE-REQUIRED` rather than forcing linearity.

### Negative control

Construct a dataset where response is statistically independent of the supplied distinction while preserving superficial graph structure. The method must not declare a causal response merely because a relation exists.

### Leakage control

No equation names, units, coefficient values, physical terminology, or target-domain identifiers may appear in the structural input.

## Pass criteria

A run passes the structural gate only if all are true:

1. It identifies a common distinction→response architecture across independent datasets.
2. It preserves explicit typing between state, relation, distinction and response.
3. It does not recover or invent a universal coefficient.
4. It detects the nonlinear counterfamily rather than forcing linearity.
5. It rejects the negative control.
6. Any domain-specific numerical law is classified as DOMAIN CLOSURE rather than universal kernel output.

## Failure criteria

`FAIL` if the method:

- requires a target-domain equation as an input;
- silently uses units to identify the law;
- produces a universal numerical coefficient from heterogeneous datasets;
- converts correlation into causation without the declared transition/control structure;
- forces a linear law onto the nonlinear control;
- accepts the negative control as evidence of directed response.

## Expected result classes

`STRUCTURAL-PASS`

Common relational architecture recovered; domain closure correctly withheld.

`STRUCTURAL-PASS + NONLINEAR`

Common architecture recovered while constitutive form remains domain-specific.

`CONSTITUTIVE-REQUIRED`

Structure identified, but numerical or functional law cannot be inferred without domain closure.

`FAIL`

Structural claim does not survive controls.

`INVALID`

Information leakage or protocol violation.

## Interpretation rule

A successful result does **not** establish that electricity, heat and fluid flow are physically identical. It establishes only that the declared structural representation can encode a common relational pattern without silently importing the domain equations.

A failure does not automatically refute the kernel; it identifies which additional structural variable, transition assumption or domain closure is required.

## Next executable artifact

Implement a blind benchmark with anonymized columns and a frozen reconstruction stage, followed by a reveal/evaluation stage. Record predictions before revealing domain labels and constitutive laws.
