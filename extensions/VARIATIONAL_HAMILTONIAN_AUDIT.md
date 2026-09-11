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

For the standard L2 pairing, curl is formally **self-adjoint**, not skew-adjoint, when the boundary contribution is removed:

`∫ E·curl B dx = ∫ B·curl E dx`.

Therefore

`dH/dt = ω∫ E·curl B dx − ω∫ B·curl E dx = 0`.

The antisymmetry responsible for Hamiltonian conservation belongs to the full field-space operator `J ⊗ curl`, where `J = [[0,1],[-1,0]]` is skew and curl is self-adjoint under the stated domain/boundary assumptions.

This reproduces the conserved positive quadratic structure already obtained from the operator audit.

## 4. Hamiltonian interpretation

Introduce the field-space antisymmetric operator

`J = [[0, 1],[-1, 0]]`

and the quadratic functional gradient

`δH/δ(E,B) = (E,B)`.

The normalized system can be represented schematically as

`∂t (E,B) = ω (J ⊗ curl) (δH/δ(E,B))`.

Under an admissible L2 domain, `J ⊗ curl` is skew-adjoint because the tensor factors have opposite adjoint character: `J* = −J` and `curl* = curl`.

Thus the Hamiltonian representation is compatible with conservation.

## 5. Does the formulation add a new constraint?

For the present linear quadratic model, **no independent physical constraint is obtained** merely by rewriting the already conserved system in Hamiltonian language.

The Hamiltonian formulation packages:

- the positive quadratic invariant;
- the antisymmetric field-space generator;
- the self-adjoint spatial curl operator;
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

A first-order action may be constructed by choosing a suitable symplectic or Poisson structure and Hamiltonian. Such a construction is not unique because canonical changes of variables and boundary terms can change the representation without changing the equations of motion.

For the present `(E,B)` variables, this point must not be overstated: because curl has a kernel outside the strictly transverse quotient/subspace, the operator `J ⊗ curl` need not be globally invertible. A genuinely nondegenerate symplectic formulation therefore requires an additional domain/constraint analysis. It is safer at this stage to call the representation Hamiltonian/Poisson-like rather than assert a globally nondegenerate canonical symplectic form.

## 7. Boundary conditions

The conservation identity depends on boundary conditions or decay assumptions that make the curl integration-by-parts surface contribution vanish. For finite domains, boundary flux must be treated explicitly.

Thus global conservation is not purely a local algebraic statement; the domain and boundary structure are part of the mathematical model.

## 8. New mathematical information

The audit identifies two useful structural distinctions:

`local conservative operator` → `global conserved functional` requires an admissible pairing/domain/boundary condition.

`skew field-space structure × self-adjoint spatial operator` → `skew full evolution operator`.

It also exposes a new open issue: `curl` has a nontrivial kernel on general vector-field domains, so the Hamiltonian operator can be degenerate unless the transverse/quotient structure is handled explicitly.

## Canonical conclusion

For the current two-field linear model, Hamiltonian/variational language is primarily a **repackaging and structural audit**, not a new derivation of the dynamics. The genuinely new constraints/information are:

1. global conservation depends on the functional pairing and boundary conditions;
2. the full Hamiltonian operator is skew because field-space antisymmetry combines with spatial curl self-adjointness;
3. a globally nondegenerate symplectic formulation is not established because the curl operator may have a kernel.

**Evidence class:** Derivation / structural audit.

**Not established:** physical action principle, Maxwell Lagrangian, gauge theory, Lorentz invariance, or physical ontology.
