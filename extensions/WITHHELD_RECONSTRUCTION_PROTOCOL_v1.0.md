# Ω-Math — Withheld Reconstruction Protocol v1.0

Date: 2026-09-16
Status: RESEARCH PROTOCOL

## Purpose

Test whether the universal structural kernel predicts nontrivial response structure when constitutive information is withheld, rather than merely restating information supplied as an input.

## Kernel

`K = STATE + RELATION + DISTINCTION + CONSTRAINT + TRANSITION`

## Reconstruction target

The reconstruction must predict a relation of the form

`response = H(Δ, R, C, S)`

without importing the target-domain constitutive equation into the definition of `H`.

## Mandatory separation

### Structural inputs

- state variables;
- relation topology;
- declared distinction/difference;
- admissible constraints;
- transition rule class.

### Domain closure

- units;
- constitutive coefficients;
- material parameters;
- boundary conditions;
- calibration constants.

Domain closure may be supplied only after the structural prediction has been frozen.

## Minimal experiment family

Construct at least two systems with identical structural kernel and different constitutive coefficients:

`J₁ = g₁ Δ`,
`J₂ = g₂ Δ`,
`g₁ ≠ g₂`.

The structural layer must reconstruct the common response architecture while failing to identify the numerical coefficient unless additional closure data are supplied.

## Falsification criteria

The reconstruction fails if it:

1. silently inserts `g` into the primitive relation;
2. changes operator type to hide a scalar coefficient;
3. predicts a unique coefficient where multiple admissible values exist;
4. confuses graph connectivity with physical transmission magnitude;
5. uses target-domain equations as premises while claiming cross-domain derivation.

## Positive criterion

A successful structural reconstruction must produce a nontrivial invariant relation shared by multiple domains and must survive an adversarial counterfamily in which constitutive coefficients vary independently.

## Output classes

- `STRUCTURAL-PASS`: architecture reconstructed, coefficient intentionally unresolved;
- `CONSTITUTIVE-REQUIRED`: additional descriptor required and explicitly identified;
- `FAIL`: structural prediction does not survive the counterfamily;
- `INVALID`: assumptions or typing were not fixed before execution.

## Decision rule

No new primitive is admitted from this experiment alone. Promotion requires independent evidence, reproducibility and comparison against existing mathematics.

**Core boundary:** structural reconstruction is not physical law identification.
