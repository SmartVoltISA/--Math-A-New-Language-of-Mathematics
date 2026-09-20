# Ω-Math Experiment — MATTER / H_R Bridge 001

## Status

**EXECUTED / FINITE + RANDOM CONTROL VERIFICATION**

Date: 2026-09-20  
Seed: 42

## Question

Can a Hamiltonian-like operator be constructed directly from the typed Ω relation state

`r_ij ∈ {-1,+1}`

without inserting the Schrödinger equation's operator by hand?

## Frozen boundary

Ω-Math primitives remain:

`EntityState={0,1}`  
`RelationState={-1,+1}`

The following are **extensions**, not new Ω primitives:

- graph incidence;
- signed adjacency;
- signed graph Laplacian;
- complex amplitude `ψ`;
- Hilbert-space norm;
- `ħ`.

No physical interpretation is admitted automatically.

## 1. Candidate operators

Three constructions were compared.

### A — signed adjacency

For an undirected relation graph:

`H_A[i,j]=r_ij`

for present edges and zero otherwise.

Because `H_A=H_A^T`, it is Hermitian and generates norm-preserving evolution

`i dψ/dt = H_A ψ`

in the finite model.

### B — signed Laplacian

Define

`A_R[i,j]=r_ij`

on edges and zero otherwise, and

`D[i,i]=degree(i)`.

Then

`H_R = D - A_R`.

This is the preferred candidate because it uses:

`relation signs + connectivity/boundary structure → operator`.

For every real symmetric signed graph:

`H_R=H_R^T`.

Therefore `i dψ/dt=H_R ψ` is norm-preserving in the finite model.

### C — signed incidence product

The tempting construction

`H=B R B^T`

with diagonal `R=diag(r_e)` was tested and **rejected as the canonical candidate**.

Reason: unlike the signed Laplacian, its spectrum is not invariant under the natural node-sign gauge transformation of edge signs. Therefore it introduces representation dependence that is not present in the intended signed-graph equivalence.

This is a useful negative result, not an error to hide.

## 2. Exact 1D test

A periodic 1D cycle with `n=64` and all relation signs `+1` was tested.

For the signed Laplacian:

`λ(k)=2-2 cos(k)=4 sin²(k/2)`.

Numerical spectrum matched the analytic spectrum with maximum absolute error:

`2.22 × 10^-15`.

Maximum eigenvalue:

`4.0`.

For Schrödinger-type evolution `ω=λ/ħ`, the small-`k` dispersion is quadratic:

`λ(k)≈k²`.

Thus this construction naturally produces a **nonrelativistic / Schrödinger-like quadratic dispersion**, not a light-like linear dispersion.

This is a structural match to the role of a Hamiltonian operator, not a derivation of quantum mechanics.

## 3. Sign control on a cycle

For a 64-node cycle, two sign configurations were compared.

### Product of edge signs = +1

A random sign arrangement with the same topology was gauge-equivalent to the all-positive cycle.

Maximum spectral difference:

`0.0`.

### Product of edge signs = -1

Changing the global cycle parity shifted the spectrum; the lowest eigenvalue became approximately:

`0.00240909`.

Therefore the relation signs are not merely decorative: the global signed topology can change the allowed spectrum.

## 4. Two-channel real form

For any symmetric `H_R`, define

`J_R = [[0,H_R],[-H_R,0]]`.

Numerical verification on a 20×20 signed lattice:

- `||H_R-H_R^T||∞ = 0`;
- `||J_R+J_R^T||∞ = 0`;
- maximum absolute real part of eigenvalues of `J_R`:
  approximately `1.89×10^-15`.

So the real two-channel system is skew-symmetric and norm/energy preserving in the finite model.

This reproduces the already established Ω two-channel structure:

`∂t E = H_R B`

`∂t B = -H_R E`

up to the declared scale factor `1/ħ`.

## 5. Norm conservation

A 20×20 random signed relational lattice was evolved spectrally for 2000 steps with `dt=0.01`.

Initial state was normalized.

Maximum observed norm error:

`4.44 × 10^-16`.

Therefore:

**PASS — finite Hermitian relational operator gives norm-preserving evolution.**

This is a mathematical property of the constructed operator.

It does not establish the physical Born rule.

## 6. 2D sign/topology control

A 20×20 square lattice was tested with identical topology.

### All-positive relations

Median eigenvector inverse participation ratio:

`0.00656`.

### Random ±1 relation signs

Median IPR:

`0.01545`.

95th percentile:

`0.05547`.

Maximum observed IPR:

`0.19654`.

The random-sign system therefore produced substantially more spatially concentrated eigenmodes than the all-positive control.

This is evidence that signed relational structure can alter spectral organization and localization properties.

It is **not** evidence for physical particles or dark matter.

## 7. Wave-packet propagation control

A delta-localized initial state was evolved on the same 20×20 lattice.

All-positive relations spread substantially:

- at `t=4`: participation ratio ≈ 100;
- at `t=8`: ≈ 201;
- at `t=20`: ≈ 189.

A random signed lattice remained much more concentrated:

- at `t=4`: ≈ 34;
- at `t=8`: ≈ 73;
- at `t=20`: ≈ 85.

The exact values are finite-size/model dependent, but the control demonstrates a robust qualitative distinction between unsigned and signed relational dynamics.

## 8. What has now been closed

The previous MATTER anchor required:

`RELATIONS → H_R`.

A concrete minimal bridge now exists:

`typed signed relations + topology → signed graph operator H_R → spectrum → ψ_R dynamics`.

For the preferred construction:

`H_R=D-A_R`.

The chain is therefore:

`relation → signed operator → Hermitian spectrum → norm-preserving amplitude dynamics`.

## 9. What remains OPEN

The following bridges are **not** established:

`|ψ_R|² → physical probability`

`ρ_R → physical matter density`

`ρ_R → gravitational source`

and the physical meanings/values of:

`ħ`, mass, spatial units, energy units and measurement operators.

Also unresolved:

- whether a unique operator is selected by Ω rather than by model choice;
- whether nonlinear/self-interaction is required for stable localized structures;
- whether a 3D relational model produces an independently measurable long-range response;
- whether any such response matches gravitational observations without inserting the target law.

## 10. Decision

**PASS:** a minimal relation-defined Hermitian operator can be constructed.

**PASS:** the operator produces real spectrum and norm-preserving Schrödinger-type evolution.

**PASS:** relation-sign organization changes spectral structure and localization.

**FAIL / REJECTED as canonical:** `B R B^T` is not gauge-invariant under the natural node-sign transformation.

**OPEN:** physical quantum interpretation.

**OPEN:** matter interpretation.

**OPEN:** gravitational interpretation.

## 11. Next decisive bridge

The next experiment should not jump directly to dark matter.

It should test:

`H_R → ψ_R → |ψ_R|² → coarse-grained ρ_R`.

Required controls:

1. all-positive relation control;
2. random-sign control;
3. topology-preserving sign shuffle;
4. topology-randomized control;
5. finite-size scaling;
6. localization metric;
7. propagation metric;
8. stability of localized modes;
9. parameter-free or preregistered coarse-graining;
10. negative control where relational signs are destroyed.

Only after that:

`ρ_R → effective field → gravitational observable`.

## Final result

The matter bridge has advanced from a formal analogy to a tested mathematical construction:

`±1 relation → H_R → spectrum → ψ_R → norm-preserving dynamics`.

The result is **mathematically verified in finite models**.

It is **not yet a physical derivation of quantum mechanics, matter, or dark matter**.
