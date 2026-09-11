# Ω-Math — Two-Field Coupling Audit

**Audit type:** numerical consistency check of the two-field conservation reduction.

## Objective

Check the algebraic claim used in `TWO_FIELD_COUPLED_VECTOR_SYSTEM.md`:

`K G + Gᵀ K = 0`, with `K=Kᵀ>0`, implies that `G` is similar to a real 2×2 skew-symmetric matrix and therefore has purely imaginary or zero eigenvalues.

## Numerical protocol

- Seed: `42`
- Trials: `1000`
- Field dimension: `2`
- Generate random real `A`.
- Construct `K=AᵀA+0.1I`, guaranteeing positive definiteness.
- Set `J=[[0,1],[-1,0]]`.
- Construct `G=K^(-1/2) J K^(1/2)`.
- Evaluate the conservation residual `||KG+GᵀK||₂`.
- Evaluate the largest absolute real part of the eigenvalues of `G`.

## Result

Observed over all 1000 trials:

- maximum conservation residual ≈ `2.26×10⁻¹⁴`;
- maximum absolute real eigenvalue component ≈ `8.81×10⁻¹⁶`.

Both are at floating-point roundoff scale for this calculation.

## Independent analytic check

Because

`B=K^(1/2) G K^(-1/2)`

satisfies

`B+Bᵀ=0`,

`B` is real skew-symmetric. In two dimensions,

`B=ωJ`,

so

`spec(B)={+iω,-iω}`.

Similarity preserves eigenvalues, hence

`spec(G)={+iω,-iω}`.

The zero case is included when `ω=0`.

## Interpretation

The numerical audit supports the algebraic reduction. It does **not** establish any physical interpretation of the fields, the invariant, the coefficient `ω`, or the propagation mechanism.

**Evidence class:** Executed + Supported.
