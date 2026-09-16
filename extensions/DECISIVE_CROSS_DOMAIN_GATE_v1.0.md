# Ω-Math — Decisive Cross-Domain Gate v1.0

Date: 2026-09-16
Status: EXECUTION SPECIFICATION

## Objective

Determine whether the relational kernel carries predictive structure across independent physical domains without importing domain equations.

## Positive criterion

A POSITIVE result requires all of the following:

1. At least three independent domains.
2. Raw provenance preserved and independently auditable.
3. Physical names, units, known constitutive equations and target labels hidden before reconstruction.
4. Preprocessing frozen before the blind run.
5. Structural reconstruction is performed from state, relation, distinction, constraint and transition information only.
6. The same structural operator family is recovered across domains, with domain-specific constitutive closure kept separate.
7. Predictions are evaluated on withheld observations not used during reconstruction.
8. Performance exceeds preregistered baselines on withheld data.
9. Shuffled-response controls destroy the claimed signal.
10. Nonlinear synthetic controls are not falsely classified as the same linear law.
11. An independent preprocessing audit finds no target leakage.
12. The result survives at least one independent rerun.

A positive result supports: `CROSS-DOMAIN STRUCTURAL GENERALIZATION SUPPORTED`.
It does not establish a universal physical ontology or any specific physical law.

## Negative criterion

A NEGATIVE result requires a valid, leakage-free, preregistered run in which at least one decisive failure occurs, such as:

- the common structural form does not generalize to independent domains;
- withheld-data performance does not exceed the declared baseline;
- shuffled controls retain comparable performance;
- the claimed reconstruction depends on hidden domain information;
- the same kernel requires incompatible ad hoc structures in independent domains.

A negative result rejects the tested generalization claim for the declared protocol. It does not automatically reject every possible formulation of Ω-Math.

## Invalid criterion

The run is INVALID rather than positive/negative if provenance, preprocessing, masking, target leakage, or preregistration cannot be verified.

## Required report

For each domain record:

`provenance → masking hash → preprocessing version → structural input → reconstruction → withheld prediction → baseline → shuffled control → decision`

No domain is revealed to the reconstruction process before the blind result is locked.

## Current NIST reference

NIST SP 260-90 provides independently documented tungsten reference tables containing temperature, thermal conductivity and electrical resistivity values over broad temperature ranges. The source must be preserved before anonymization. See NIST SP 260-90 and the corresponding publication record.

## Decision rule

`POSITIVE` only if every positive criterion passes.
`NEGATIVE` only if the experiment is valid and a decisive negative criterion passes.
`INVALID` otherwise.

No universal promotion is permitted from this gate alone.
