# Ω-Math — Mathematical Extension Status v1.2

**Status:** canonical extension index after the Hamiltonian, boundary, and transverse-constraint gates.

## Closed conditional gates

1. **Positive quadratic conservation** → metric-skew generator.
2. **Local antisymmetric lattice propagation** → conservative propagating modes.
3. **Isotropic first-order vector operator class** → curl sector selected as the first-order antisymmetric spatial sector, up to scalar/sign.
4. **Two-field transverse conserved coupling** → normalized opposite-sign cross-coupling with one magnitude `|ω|`.
5. **Continuum dispersion** → `Ω² = ω²|k|²` and propagation-speed magnitude `|ω|` within the declared continuum model.
6. **Variational/Hamiltonian audit** → Hamiltonian representation adds structural packaging but no new physical law; global conservation requires admissible pairing and boundary conditions.
7. **Boundary-flux audit** → on a finite domain, `dH/dt` is a boundary-flux term; zero net boundary flux is required for global conservation.

## New constraint result

The transverse condition is **not derived** by the curl dynamics. Instead,

`∂t(∇·E)=0`, `∂t(∇·B)=0`.

Therefore divergence-free initial data define an invariant sector, while arbitrary longitudinal components remain as zero-frequency modes. Transversality must remain an explicit state-space restriction.

The Hamiltonian operator

`P = ω(J ⊗ curl)`

is skew-adjoint under the admissible L2 pairing because `J*=-J` and `curl*=curl`, but it is generally degenerate because curl has a kernel. A globally nondegenerate canonical symplectic structure is therefore **not established** without additional domain, topology, and zero-mode conditions.

## Corrected mathematical statement

The current extension layer supports the following chain:

`positive quadratic invariant`

`→ metric-skew finite-dimensional generator`

`→ local antisymmetric propagation`

`→ isotropic first-order curl sector`

`→ two-field conservative coupling`

`→ continuum dispersion`

`→ Hamiltonian/Poisson representation`

`→ boundary-dependent global conservation`

`→ invariant transverse sector + degenerate Poisson structure`.

Each arrow is conditional on the assumptions declared by its corresponding audit.

## Explicit non-claims

Nothing in v1.2 establishes:

- Maxwell equations;
- electromagnetism;
- a physical identity of `E` and `B`;
- gauge symmetry;
- a physical action principle;
- Lorentz invariance;
- a physical value of the propagation speed;
- physical units or dimensional calibration;
- physical energy, momentum, charge, or time;
- a unique ontology.

## Next mathematical gate

The next gate is to make the domain explicit and test the transverse/zero-mode quotient. The target is a precise theorem describing when `P = ω(J ⊗ curl)` becomes nondegenerate on the reduced state space, and which additional conserved quantities follow from the resulting Hamiltonian structure.

This gate must distinguish carefully between:

- quotienting a kernel;
- restricting to an invariant subspace;
- fixing boundary conditions;
- removing topological harmonic modes.

No physical interpretation should be added until these mathematical distinctions are closed.

**Evidence class:** Derivation / structural audit.
