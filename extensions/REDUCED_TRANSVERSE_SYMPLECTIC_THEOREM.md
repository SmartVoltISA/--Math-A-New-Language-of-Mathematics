# Ω-Math — Reduced Transverse Symplectic Theorem

**Status:** conditional mathematical result.

## 1. Domain

Fix a periodic three-dimensional domain `T³` and sufficiently regular vector fields with the standard L2 pairing. For every nonzero Fourier mode `k`, impose

`k·E_k = 0`, `k·B_k = 0`,

and remove the zero Fourier mode explicitly.

This domain choice is part of the theorem; it is not derived from the primitive Ω-Math language.

## 2. Curl on the reduced sector

For each nonzero wavevector `k`, the Fourier symbol of curl is

`C(k) = i[k]_×`.

On the transverse plane, `C(k)` is Hermitian/self-adjoint and has eigenvalues

`+|k|, −|k|`.

Therefore `C(k)` is invertible for every `k ≠ 0` on the transverse plane. The zero Fourier sector is excluded by construction.

Thus, subject to the stated regularity and domain conditions, curl is invertible on the reduced nonzero transverse sector.

## 3. Two-field operator

Let `u = (E,B)` and

`P = ω(J ⊗ curl)`,

where `J = [[0,1],[-1,0]]` and `ω ≠ 0`.

On the reduced sector,

`J^{-1} = −J`

and `curl^{-1}` exists. Hence

`P^{-1} = ω^{-1}(J^{-1} ⊗ curl^{-1})`

exists.

Because `P* = −P`, its inverse is also skew-adjoint. The reduced operator therefore defines a nondegenerate skew structure; in the standard linear setting this is the operator form of a symplectic structure.

## 4. Precise conclusion

Under

`periodic domain + transverse sector + zero Fourier mode removed + suitable regularity + ω ≠ 0`,

the previously degenerate Hamiltonian/Poisson operator becomes nondegenerate on the reduced state space.

Therefore:

`global nondegeneracy is not established on the unrestricted space, but is established conditionally on the explicitly reduced transverse nonzero-mode space.`

## 5. Quotient versus restriction

Three operations must not be conflated:

1. **Invariant restriction:** choose transverse initial data and evolve inside that invariant sector.
2. **Kernel removal:** explicitly remove zero/gradient directions so an inverse can exist.
3. **Quotient construction:** identify states differing by kernel directions.

This theorem uses restriction plus explicit zero-mode removal. It does not claim that quotienting by the full curl kernel is automatically well-defined on every domain.

## 6. Topology warning

On domains other than the periodic three-torus, harmonic vector fields and boundary-dependent kernels may survive after imposing `∇·u=0`. The result therefore cannot be generalized to arbitrary domains without an additional Hodge/topology analysis.

## 7. Conserved quantities

The quadratic Hamiltonian

`H = 1/2 ∫ (|E|² + |B|²) dx`

remains conserved when the boundary conditions eliminate net flux.

The reduced symplectic structure does **not by itself** imply a unique additional scalar conserved quantity. Additional invariants require explicit symmetry or modal analysis.

For the translation-invariant periodic linear system, each nonzero Fourier-helicity sector evolves independently as a finite-dimensional oscillator. Modal quadratic amplitudes are consequently conserved, but these are consequences of the specified linear Fourier decomposition, not new universal Ω-Math primitives.

## 8. Gate result

Established conditionally:

- curl is invertible on the transverse nonzero Fourier sector of `T³`;
- `P = ω(J ⊗ curl)` is invertible there for `ω ≠ 0`;
- the inverse is skew-adjoint;
- a nondegenerate symplectic operator representation is available on that reduced state space.

Still open:

- general bounded-domain theorem;
- full Hodge decomposition with boundary conditions;
- topological harmonic sectors;
- a unique action functional;
- physical interpretation;
- gauge theory;
- Lorentz invariance;
- physical calibration.

**Evidence class:** Derivation / structural theorem.
