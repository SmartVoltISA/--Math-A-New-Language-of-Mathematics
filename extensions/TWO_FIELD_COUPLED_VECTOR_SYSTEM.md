# Ω-Math — Two-Field Coupled Vector System

**Status:** conditional mathematical theorem/model class; not a derivation of Maxwell equations or physical electromagnetism.

## 1. Gate

We test the next mathematical gate from `MATHEMATICAL_EXTENSION_STATUS_v1.0.md`:

> Construct the minimal two-field coupled vector system satisfying locality, positive conservation, isotropy and transverse propagation. Determine which coupling structure is selected and which degrees of freedom remain free.

The analysis is deliberately restricted to a linear, first-order, translation-invariant, rotationally covariant vector-field class.

## 2. General local isotropic first-order form

Let `E(x,t), B(x,t) ∈ R^3`. In Fourier space, a first-order isotropic local operator acting on a vector has the form

`M(k) = a(k²) I + b(k²) kkᵀ + c(k²) [k]×`,

where `[k]×v = k × v`.

For the minimal first-order spatial sector, retain the term linear in `k`:

`M(k) = a₀ I + b₀ kkᵀ + c₀ [k]×`.

The `I` and `kkᵀ` sectors do not produce the required antisymmetric transverse propagation by themselves. The curl sector is the unique first-order isotropic antisymmetric sector, up to scalar normalization/sign.

## 3. Two-field transverse reduction

After restricting to the transverse subspace (`k·E = k·B = 0`), the minimal propagation sector is

`∂t E = α curl E + β curl B`

`∂t B = γ curl E + δ curl B`.

Thus the field-label coupling is represented by

`G = [[α, β], [γ, δ]]`.

For a transverse Fourier mode, `curl` has eigenvalues `± i|k|`, so the temporal spectrum is determined by the eigenvalues of `G` multiplied by `± i|k|`.

## 4. Positive quadratic conservation

Take a positive quadratic invariant

`Q = 1/2 ∫ uᵀ K u dx`,

with `u=(E,B)` and constant symmetric positive-definite field metric `K`.

Exact conservation for the first-order system requires the full generator to be skew with respect to `K`. In the reduced two-field sector this becomes

`K G + Gᵀ K = 0`.

Therefore `K^{1/2} G K^{-1/2}` is an ordinary real skew-symmetric 2×2 matrix. Every real skew-symmetric 2×2 matrix has the form

`ω J`,  where `J=[[0,1],[-1,0]]`.

Hence, after a positive field-space change of coordinates, the conserved two-field transverse sector is necessarily

`∂t E' = ω curl B'`

`∂t B' = -ω curl E'`.

This is the minimal normalized exchange form.

## 5. What is selected

Within the declared class, the combination

`locality + first-order isotropy + transverse sector + positive quadratic conservation`

selects:

1. the curl sector as the antisymmetric first-order spatial operator;
2. a two-dimensional field-space skew generator;
3. one independent coupling magnitude `|ω|` after normalization;
4. opposite-sign cross-coupling in the normalized two-field basis.

The sign of `ω` is convention-dependent under orientation/time-reversal conventions.

## 6. What remains free

The mathematical constraints do **not** uniquely determine:

- the physical interpretation of `E` and `B`;
- the physical units or dimensional scale of `ω`;
- the absolute spatial scale;
- the physical meaning of the conserved quadratic form;
- boundary/initial conditions;
- nonlinear terms;
- sources and charges;
- gauge structure;
- Lorentz invariance;
- a physical value of propagation speed;
- quantization;
- whether the fields correspond to electromagnetism.

In particular, a rescaling of space, time, fields, or the quadratic metric can change coefficients without changing the mathematical structure.

## 7. Countermodels / failure boundaries

### No positive conservation
A general `G` can have real eigenvalues. The resulting modes can grow or decay rather than oscillate.

### No isotropy
Preferred-axis couplings can propagate while breaking rotational covariance.

### No transverse restriction
Longitudinal sectors can remain or behave differently; transverse propagation is no longer a complete description.

### Symmetric spatial operator
A Laplacian-type operator gives diffusion/relaxation rather than the antisymmetric propagating sector.

### Nonlinear extension
Conservation may survive in nonlinear systems, but the linear spectral selection above no longer proves the nonlinear dynamics.

## 8. Relation to Ω-Lab

This extension consolidates the mathematical content of:

- `REL-PULSE-01_AUTONOMOUS_RELATIONAL_OSCILLATION.md`
- `REL-PULSE-02_CONSERVATION_FEEDBACK_SELECTION.md`
- `REL-PULSE-03_SPATIAL_PROPAGATING_MODE.md`
- `REL-PULSE-04_CURL_SELECTION_AUDIT.md`

Those experiments provide executed numerical checks for the component results. This document states the combined mathematical gate and keeps the physical interpretation outside Ω-Math.

## 9. Canonical conclusion

**Result:** Within the declared linear first-order isotropic transverse class, positive quadratic conservation reduces the two-field coupling to a metric-skew 2×2 generator. After field normalization, the minimal nontrivial form is an antisymmetric cross-coupling through the curl operator.

**Evidence class:** Derivation + executed component audits.

**Not established:** Maxwell theory, electromagnetism, light, or any physical ontology.
