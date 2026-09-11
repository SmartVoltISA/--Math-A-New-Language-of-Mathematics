# Ω-Math — Dispersion and Speed Selection

**Status:** conditional mathematical result.

## 1. Minimal normalized system

For

`∂t E = ω curl B`

`∂t B = −ω curl E`

with transverse Fourier modes, the curl eigenvalues are `± i|k|`. Applying the system twice gives

`∂t² E = −ω² curl² E`

and similarly for `B`.

On a transverse plane wave, `curl²` contributes `−|k|²`, so

`Ω² = ω² |k|²`.

Therefore

`Ω = ±|ω||k|`.

## 2. Consequences

The phase speed magnitude is

`|Ω/k| = |ω|`.

The group speed magnitude is

`|dΩ/dk| = |ω|`.

Thus the minimal normalized system has a linear dispersion relation and a wave-speed scale set by the single remaining coupling magnitude `|ω|`.

## 3. What is and is not selected

Selected within the declared class:

- transverse propagating modes;
- linear dispersion;
- equal phase/group speed magnitude;
- one dimensionful or dimensionless coefficient controlling the propagation scale, depending on units.

Not selected:

- a numerical physical value of the speed;
- the interpretation of that speed as `c`;
- physical units;
- Lorentz invariance;
- a spacetime metric;
- electromagnetic interpretation.

## 4. Scale boundary

If time or space is rescaled, the numerical value of `|ω|` changes. Therefore the mathematical structure alone does not establish an absolute physical speed.

An independent dimensional invariant is required before identifying this coefficient with a measured physical constant.

## 5. Comparison with the lattice extension

The earlier local lattice model has

`Ω(k) = −2 sin(k)`

and therefore

`v_g(k) = −2 cos(k)`.

Its bounded, dispersive speed differs from the continuum two-field result. This demonstrates that propagation is not a universal consequence of relation alone; it depends on the chosen spatial operator and continuum/limit assumptions.

## Canonical conclusion

The two-field conservation gate produces a linear propagating continuum sector, but the absolute speed scale remains free until an external dimensional calibration is supplied.

**Evidence class:** Derivation + comparison with executed lattice model.
