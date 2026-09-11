# Ω-Math — Assumption Relaxation Matrix

**Status:** mathematical audit / boundary analysis.

## Purpose

The two-field result must not be treated as uniquely fundamental unless each assumption has been tested for necessity. This document removes the assumptions one at a time and records what is lost.

## Baseline

Baseline class:

`linear + first-order + local + translation-invariant + isotropic + transverse + positive quadratic conservation`

Normalized result:

`∂t E = ω curl B`

`∂t B = −ω curl E`

## Relaxation tests

| Assumption removed | What remains possible | What is no longer selected |
|---|---|---|
| Positive conservation | growth, decay, oscillation | skew field coupling |
| Isotropy | preferred-axis operators | unique curl sector |
| First-order spatial locality | higher-order operators | first-order curl selection |
| Transverse restriction | longitudinal + transverse sectors | purely transverse propagation |
| Linearity | nonlinear conserved systems | linear spectral classification |
| Translation invariance | position-dependent coefficients | global Fourier-mode classification |
| Two-field restriction | larger field spaces | 2×2 coupling reduction |

## Key conclusion

No single assumption alone proves the normalized two-field form. The selection is a joint result of the declared class.

The strongest mathematically identifiable role of each assumption is:

- **local + first-order + isotropic:** restrict the spatial operator sector;
- **transverse:** isolates the propagating vector sector;
- **positive conservation:** restricts field-space evolution to a metric-skew generator;
- **two fields:** reduces the conserved field-space generator to a single 2×2 skew degree of freedom;
- **linearity:** permits exact spectral classification;
- **translation invariance:** permits global Fourier decomposition.

## Falsification targets

The result would require revision if a counterexample were found inside the declared baseline class that simultaneously satisfies all assumptions but is not reducible to the normalized cross-curl form.

A counterexample outside the baseline class does not falsify the theorem; it identifies a boundary of applicability.

## Evidence class

Derivation + boundary classification. The individual countermodel families are mathematical constructions; numerical audits remain in Ω-Lab.
