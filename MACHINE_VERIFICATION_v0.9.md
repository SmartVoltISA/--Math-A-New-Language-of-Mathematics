# Ω-Math v0.9 — Machine Verification

## Purpose

The reference runtime is now paired with executable finite verification for the newest closure experiments. The specification remains authoritative; executable code is a conformance instrument, not a replacement for the mathematical definitions.

## Executed suite

`experiments/run_v09_verification.py` reproduces the frozen finite claims of:

- `EXPERIMENT_LOCALITY_ADMISSIBILITY_BOUNDARY_010.md`;
- `EXPERIMENT_INTERACTION_REDUCTION_011.md`;
- `EXPERIMENT_CAUSAL_INTERVENTION_012.md`.

`tests/test_experiments_v09.py` contains the same checks under pytest.

## Frozen results

- Experiment 010: locality/admissibility/boundary finite checks PASS.
- Experiment 011: all `16 × 16 × 4 = 1024` locality/admissibility/horizon cases PASS; quotient masking check PASS.
- Experiment 012: all `256 × 256 × 4 = 262144` model/start cases are enumerated; the frozen counts are `28672` baseline-identical cases and `25344` interventionally distinguishable cases.

## Reproducibility

Run:

```bash
python -m pip install -e .
python experiments/run_v09_verification.py
python -m pytest
```

The suite must fail loudly on any mismatch. No undefined normalization is silently mapped to zero, and no physical interpretation is introduced by the test harness.

## Boundary

Machine verification does **not** imply that every historical experiment in the repository has already been mechanized. The remaining work is incremental mechanization of older experiment records and deeper parser/semantic coverage. It also does not promote probability, physical time, physical energy, or a universal causal primitive into Ω-Math v0.9.

`specification → implementation → executable verification → recorded result`

`complete language ≠ complete mathematics ≠ complete physics`
