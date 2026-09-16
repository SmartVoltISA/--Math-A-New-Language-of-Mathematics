# Ω-Math — Real-Domain Data Sources v1.0

Date: 2026-09-16
Status: SOURCE AUDIT / READY FOR BLIND BENCHMARK CONSTRUCTION

## Objective

Build the first withheld reconstruction benchmark from independently documented measurement/reference data rather than generated equations.

## Source A — Thermal

NIST SRD 81 provides heat-transmission measurements for insulating and building materials. Its field definitions explicitly include `Delta T`, thermal conductance, conductivity, resistance and resistivity. The database contains measured records rather than only a theoretical equation.

Source: NIST SRD 81 — Heat Transmission Properties of Insulating and Building Materials.

Reference: https://srdata.nist.gov/insulation/Search/DatabaseSearch

Supporting documentation also states that the database contains 2,175 thermal-conductivity records collected with NIST guarded-hot-plate apparatus. This is suitable for a controlled difference→response reconstruction after the physical labels are stripped.

## Source B — Fluid

NIST's flow-and-pressure measurement program describes controlled pressure sources driving fluids through microcapillaries while flow is recorded. It also describes viscosity measurements across temperature, concentration and shear-rate conditions.

Source: NIST Flow and Pressure.

Reference: https://www.nist.gov/noac/technology/fluid-measurements/flow-and-pressure

NIST also publishes evaluated fluid transport properties including viscosity and thermal conductivity over defined conditions.

## Source C — Electrical / material transport

NIST documents standard-reference measurements covering both thermal conductivity and electrical resistivity materials. This provides a path to an independently sourced electrical/material transport family without importing a textbook constitutive equation into the reconstruction stage.

Source: NBS/NIST SP 260-46 — Thermal conductivity and electrical resistivity standard reference materials.

Reference: https://doi.org/10.6028/NIST.SP.260-46

## Important limitation

The present source audit establishes availability and suitability of reference measurements. It does **not** yet claim that the raw records have been downloaded, anonymized, normalized or executed through the blind reconstruction pipeline.

## Data-preparation rule

Before reconstruction, create an anonymized table containing only structural roles:

`state_id, relation_id, distinction, constraint_flags, response, replicate/group_id`

Remove or encode separately:

- physical domain name;
- physical units;
- variable names such as voltage, temperature or pressure;
- constitutive equation;
- material-specific coefficient;
- source-specific interpretation.

The reveal file retains the original metadata and is not exposed to the reconstruction stage.

## Evaluation rule

The benchmark must distinguish:

`STRUCTURAL-PASS`
`CONSTITUTIVE-REQUIRED`
`NEGATIVE-CONTROL-PASS`
`LEAKAGE/INVALID`
`FAIL`

The purpose is not to prove that electrical, thermal and fluid phenomena are physically identical. The purpose is to test whether the same typed relational architecture can be recovered without silently importing domain physics.
