# Ω-Math — Reciprocity Defect Noise Robustness Audit v1.0

Date: 2026-09-09
Execution: local Python, deterministic RNG.

## Objective
Test whether the declared reciprocity defect remains statistically discriminative when the measured response matrix is contaminated by observation noise.

## Candidate

`rho(R) = ||R-R^T||_F / ||R+R^T||_F`

The ideal structural value is exactly zero for a symmetric response matrix. Under noisy observation, the measured value need not be zero.

## Protocol

For each noise level `sigma` in `{0.01, 0.03, 0.1, 0.2, 0.3, 0.5, 1.0}`, generate 500 paired 20-node systems:

- directed response: `R = exp(-A)` from a positive random directed matrix `A`;
- reciprocal control: `S=(A+A^T)/2`, with response `Rs=exp(-S)`;
- identical response construction for both members;
- independent zero-mean Gaussian observation noise added to each measured response;
- negative entries clipped to a positive numerical floor;
- `sigma` is expressed relative to the mean response magnitude.

## Results

| sigma | directed mean rho | symmetric mean rho | P(directed > symmetric) | symmetric 95% quantile |
|---:|---:|---:|---:|---:|
| 0.01 | 0.292763 | 0.006550 | 1.000 | 0.007098 |
| 0.03 | 0.292699 | 0.019558 | 1.000 | 0.021162 |
| 0.10 | 0.298282 | 0.065522 | 1.000 | 0.071280 |
| 0.20 | 0.315148 | 0.129358 | 1.000 | 0.141249 |
| 0.30 | 0.337347 | 0.189688 | 1.000 | 0.207548 |
| 0.50 | 0.384477 | 0.291899 | 1.000 | 0.317254 |
| 1.00 | 0.478214 | 0.446055 | 0.830 | 0.488450 |

## Decision

The candidate remains strongly discriminative through 50% noise in this declared observation model. At 100% noise, separation degrades substantially and is no longer universally reliable in this sample.

This is the correct statistical interpretation: noise does not invalidate the exact structural invariant; it limits recovery of that invariant from noisy measurements.

## Boundary

This experiment does not establish a universal noise model, estimator optimality, or physical robustness. It establishes only robustness under the explicitly declared additive observation-noise model.

## Status

**PASS — robustness gate for the declared noise model.**

The candidate remains a mathematical invariant of the declared response matrix. The noisy case is treated as an estimation problem rather than redefining the invariant.
