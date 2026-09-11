# Ω-Math — Transverse Constraint and Poisson Audit

**Status:** conditional mathematical result / open constraint gate.

## 1. Objective

Determine whether the transverse conditions used in the two-field curl model are consequences of the dynamics, or an independent restriction of the state space. Then determine whether the Hamiltonian operator defines a nondegenerate symplectic structure or only a degenerate Poisson-type structure.

## 2. Canonical system

`∂t E = ω curl B`

`∂t B = −ω curl E`.

Taking divergence and using `∇·curl = 0` gives

`∂t(∇·E) = 0`,

`∂t(∇·B) = 0`.

Therefore divergence-free initial data remain divergence-free. But the equations do not force the divergence to vanish for arbitrary initial data. The transverse condition is therefore an **invariant state-space restriction, not a dynamically derived constraint**.

## 3. Fourier-space interpretation

For a nonzero Fourier mode `k`, decompose each vector into longitudinal and transverse parts:

`E = E_parallel + E_perp`, with `k·E_perp = 0`,

and similarly for `B`.

Because `k × E_parallel = 0` and `k × B_parallel = 0`,

`∂t E_parallel = 0`,

`∂t B_parallel = 0`.

Thus the longitudinal sector is a zero-frequency invariant sector, while the transverse sector carries the nontrivial curl dynamics.

## 4. Hamiltonian / Poisson operator

Let `u = (E,B)` and

`P = ω (J ⊗ curl)`, with `J = [[0,1],[-1,0]]`.

Under the admissible L2 pairing,

`J* = −J`,

`curl* = curl`,

so

`P* = −P`.

Thus `P` is a skew-adjoint Hamiltonian/Poisson-type operator.

However, curl has a kernel containing gradient fields on standard domains, and additional zero modes may occur depending on topology and boundary conditions. Consequently `P` is generally **degenerate** on the unrestricted vector-field space.

A degenerate skew operator does not define a globally nondegenerate symplectic form. Therefore:

`Hamiltonian operator established; global canonical symplectic nondegeneracy not established.`

## 5. Transverse restriction and zero modes

Restricting to a suitable transverse subspace removes the obvious longitudinal gradient kernel for nonzero Fourier modes. On a periodic domain, however, the zero Fourier mode still satisfies `curl = 0`, so transversality alone does not guarantee invertibility.

Further domain/topology and zero-mode conditions are required before claiming a genuinely nondegenerate symplectic structure.

## 6. What is actually derived?

Derived:

1. divergence is conserved by the canonical curl dynamics;
2. divergence-free initial data define an invariant transverse sector;
3. longitudinal modes are zero-frequency modes of the curl generator;
4. the full Hamiltonian/Poisson operator is skew-adjoint under the admissible pairing;
5. the unrestricted operator is generally degenerate because curl has a kernel.

Not derived:

- divergence-free constraints as universal axioms;
- gauge symmetry;
- a physical Gauss law;
- Maxwell equations;
- physical electromagnetic interpretation;
- a globally nondegenerate canonical symplectic form.

## 7. Gate result

The transverse assumption must remain explicitly marked as an **additional state-space restriction**. It cannot be promoted to a consequence of the minimal curl dynamics.

The next mathematical question is narrower and testable: under explicit domain choices, can the transverse/zero-mode quotient produce a well-defined nondegenerate symplectic structure, and what additional conserved quantities follow from that structure?

**Evidence class:** Derivation / structural audit.
