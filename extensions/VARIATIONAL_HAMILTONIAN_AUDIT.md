# Ω-Math — Variational / Hamiltonian Audit

**Status:** conditional mathematical formulation.

## 1. Objective

Determine whether a variational or Hamiltonian formulation adds constraints beyond the already established positive-conservation / metric-skew structure of the normalized two-field system.

## 2. Canonical transverse system

`∂t E = ω curl B`

`∂t B = −ω curl E`

with transverse fields and suitable boundary conditions.

## 3. Quadratic Hamiltonian

Define

`H = 1/2 ∫ (E·E + B·B) dx`.

The evolution preserves `H` because the curl operator is formally skew-adjoint under boundary conditions that eliminate the surface term:

`∫ E·curl B dx = ∫ B·curl E dx`.

Hence

`dH/dt = ω∫ E·curl B dx − ω∫ B·curl E dx = 0`.

This reproduces the conserved positive quadratic structure already obtained from the operator audit.

## 4. Hamiltonian interpretation

Introduce the field-space antisymmetric operator

`J = [[0, 1],[-1, 0]]`

and the quadratic functional gradient

`δH/δ(E,B) = (E,B)`.

The normalized system can be represented schematically as

`∂t (E,B) = ω (J ⊗ curl) (δH/δ(E,B))`.

The evolution operator is antisymmetric with respect to the appropriate pairing, so the Hamiltonian representation is compatible with conservation.

## 5. Does the formulation add a new constraint?

For the present linear quadratic model, **no independent physical constraint is obtained** merely by rewriting the already conserved system in Hamiltonian language.

The Hamiltonian formulation packages:

- the positive quadratic invariant;
- the antisymmetric generator;
- the resulting conservative flow.

It does not determine, by itself:

- the physical interpretation of the fields;
- the numerical propagation speed;
- Lorentz symmetry;
- gauge symmetry;
- sources;
- nonlinear dynamics;
- physical units;
- physical time or energy.

## 6. Variational formulation

A first-order action may be constructed by choosing a suitable symplectic potential and Hamiltonian. Such a construction is not unique because canonical transformations and boundary terms can change the representation without changing the equations of motion.

Therefore existence of an action is weaker than uniqueness of the underlying physical ontology.

## 7. Boundary conditions

The conservation identity depends on boundary conditions or decay assumptions that make the curl integration-by-parts surface contribution vanish. For finite domains, boundary flux must be treated explicitly.

Thus global conservation is not purely a local algebraic statement; the domain and boundary structure are part of the mathematical model.

## 8. New mathematical information

The audit does identify one useful structural distinction:

`local conservative operator` → `global conserved functional` requires an admissible pairing/domain/boundary condition.

This prevents silently promoting a local skew relation into an unrestricted global conservation law.

## Canonical conclusion

For the current two-field linear model, Hamiltonian/variational language is primarily a **repackaging and structural audit**, not a new derivation of the dynamics. The genuinely new constraint is the explicit dependence of global conservation on the functional pairing and boundary conditions.

**Evidence class:** Derivation / structural audit.

**Not established:** physical action principle, Maxwell Lagrangian, gauge theory, Lorentz invariance, or physical ontology.
