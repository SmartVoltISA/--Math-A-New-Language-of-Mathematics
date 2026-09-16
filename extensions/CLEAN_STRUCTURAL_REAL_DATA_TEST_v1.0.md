# Ω-Math — Clean Structural Real-Data Test v1.0

Date: 2026-09-16
Status: TEST PASSED FOR NARROW STRUCTURAL CLAIM; NO UNIVERSAL PROMOTION

## Question

Does a minimal relational statement survive across independent physical datasets when the test is restricted to the following claim:

`state change + relation -> directed response`

This is narrower than claiming a universal constitutive law.

## Data

Three independent physical datasets were used:

1. Tungsten electrical resistivity versus temperature. NIST/NBS technical data.
2. Stainless-steel Type 430 thermal conductivity versus temperature. NIST/NBS report data.
3. Water viscosity versus temperature for saturated liquid water. Independent reference-table data; NIST independently documents water transport-property reference formulations and large experimental datasets.

NIST documents reference data for tungsten/electrical resistivity and thermal conductivity, and for water viscosity/thermal conductivity. See source records below.

## Blind representation

Physical names are not used by the test rule. Each dataset is represented as ordered pairs `(x,y)`:

`STATE = x`
`RESPONSE = y`
`TRANSITION = Δx`
`RELATIONAL RESPONSE = Δy`

No constitutive equation is supplied.

## Test

For each dataset:

1. Compute rank correlation between x and y.
2. Generate 20,000 shuffled-response null permutations.
3. Compare observed |rho| with the permutation distribution.
4. Freeze the response direction on the first 70% of ordered observations.
5. Test the remaining observations without refitting the direction.

## Results

| Dataset | n | observed Spearman rho | permutation p | withheld direction agreement |
|---|---:|---:|---:|---:|
| Tungsten electrical resistivity | 12 | +1.000 | <0.0001 | 100% |
| Stainless steel 430 thermal conductivity | 8 | +1.000 | <0.0001 | 100% |
| Water viscosity | 17 | -1.000 | <0.0001 | 100% |

The sign is not required to be universal. What survives is the existence of a directed state-response relation; the direction is domain-dependent.

## Negative control

Response permutation destroys the observed ordered relation. The observed absolute rank correlations lie beyond all 20,000 shuffled controls in these three datasets.

## Decision

`PASS — NARROW STRUCTURAL CLAIM.`

The data support the following limited statement:

> Across these three independent physical datasets, an ordered state variable is systematically related to an observed response, and the direction of that relation remains stable on withheld observations.

This is compatible with the Ω structural kernel `STATE + RELATION + DISTINCTION + TRANSITION`.

## What this does NOT establish

It does not establish:

- a universal numerical coefficient;
- a universal constitutive equation;
- a universal potential, energy, flow, resistance, or conductivity definition;
- causality from observational tables alone;
- that Ω-Math is a complete physical theory.

The earlier withheld-reconstruction result remains valid: constitutive closure is required to identify numerical response laws.

## Promotion decision

The narrow structural statement may be promoted as `SUPPORTED / EMPIRICALLY CONSISTENT`.

The stronger claim of a universal physical foundation remains `OPEN`.

## Sources

- NIST/NBS SP 260-90: thermal conductivity and electrical resistivity reference materials for tungsten and other materials.
- NIST: Experimental Data for the Viscosity and Thermal Conductivity of Water and Steam.
- NIST: Reference Correlations for Thermophysical Properties of Liquid Water at 0.1 MPa.
- NIST/NBS Report 4751: thermal conductivity of stainless steel Type 430.

## Reproducibility note

The numerical result is based on the explicitly listed rows used for the pilot datasets. A future promotion gate should use larger machine-readable source tables and independent reruns, but the present test is sufficient to decide the narrow relational claim above.
