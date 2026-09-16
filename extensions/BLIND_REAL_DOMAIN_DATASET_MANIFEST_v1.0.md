# Ω-Math — Blind Real-Domain Dataset Manifest v1.0

Date: 2026-09-16
Status: CANDIDATE DATASET MANIFEST / NO RESULTS CLAIMED

## Dataset families

### D1 — Thermal transport

NIST reference data include evaluated thermal-conductivity and viscosity values/correlations for fluids and experimental water/steam measurements. The water/steam collection reports thousands of viscosity and thermal-conductivity observations across broad temperature and pressure ranges.

### D2 — Electrical/thermal material transport

NIST reference-material documentation contains paired thermal-conductivity and electrical-resistivity reference values for materials such as tungsten. These are useful because two different transport responses can be examined against a common neutral state/distinction representation.

### D3 — General thermophysical transport

NIST thermophysical reference data expose pressure, density, enthalpy, entropy, heat capacities, speed of sound, viscosity and thermal conductivity across fluids. This provides an independent family with multiple possible response/constraint relationships.

## Source provenance

Primary source family: NIST Standard Reference Data and NIST reference publications.

Relevant references:

- NIST Standard Reference Data overview.
- NIST REFPROP / thermophysical-property documentation.
- NIST experimental water/steam transport-property compilation.
- NIST thermal conductivity/electrical resistivity reference-material documentation.

## Neutralization requirements

Before any Ω-Math reconstruction, each selected table must be converted into a dataset-specific neutral schema. Physical names, units, material names and formula identifiers are removed from the model-facing representation.

The original source and exact mapping are retained in a sealed provenance record outside the blind input.

## Sampling rules

- Preserve original row ordering only when it is physically meaningful and not a hidden label.
- Keep measurement uncertainty when explicitly available, encoded generically as uncertainty bounds.
- Do not fit or smooth data before the blind reconstruction unless the same preprocessing is applied to controls.
- Do not remove outliers using knowledge of the physical domain.
- Split data by source/table before model fitting to prevent leakage.

## Success criterion

The primary result is not low numerical error alone. A successful blind reconstruction must identify a reusable structural relation while correctly reporting what remains unidentified.

## Failure criterion

If the method requires physical labels, units, known constitutive equations or source-specific assumptions to obtain the relation, the result is marked `DOMAIN-LEAK / INVALID` rather than counted as support.

## Status

Candidate datasets identified. No empirical pass/fail claim is made until the neutralization and blind freeze are executed.
