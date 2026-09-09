# Ω-Math — External Observation Algebra Discrimination Hard Gate v1.0

Date: 2026-09-09  
Execution: local Python, deterministic seed `20260909`, 300 trials per external model.

## Objective

Close the previous gate: determine whether competing Ω-Math algebras can be empirically discriminated when the observation is defined by an external model rather than by the candidate algebra itself.

Candidate algebras:

- max-min: `(A∘B)_ij = max_k min(A_ik,B_kj)`;
- min-plus: `(A∘B)_ij = min_k(A_ik+B_kj)`;
- sum-product: `(A∘B)_ij = Σ_k A_ikB_kj`.

The measurement definitions below do not invoke these candidate formulas.

## External model A — continuous-time diffusion

A directed continuous-time random walk was generated from an independently defined generator
`L = W^T - diag(row_sum(W))`.

The externally observable transition operators were calculated as
`T(t)=exp(tL)`.

The candidate prediction was `T(dt) ∘ T(dt)` and was compared directly with the independently generated observable `T(2dt)`.

Trials: 300, `N=6`.

Mean relative error:

| Candidate | Mean error |
|---|---:|
| max-min | ≈ 0.0674 |
| min-plus | ≈ 0.9055 |
| sum-product | ≈ 0 |

Winner count: **sum-product 300/300**.  
Correct-model numerical error is at machine precision because the external transition operator is a semigroup.

Result: **PASS — external observation discriminates the candidate algebras for this model class.**

## External model B — travel time

Positive edge travel times were independently generated. The observed two-edge travel time was defined as the earliest arrival through any intermediate node:
`τ_2(i,j)=min_k(τ(i,k)+τ(k,j))`.

This is an external transport observable, not a candidate-algebra output.

Trials: 300, `N=8`.

Mean relative error:

| Candidate | Mean error |
|---|---:|
| max-min | ≈ 2.43 |
| min-plus | 0 |
| sum-product | ≈ 36.18 |

Winner count: **min-plus 300/300**.

Result: **PASS — an independently defined travel-time observable selects min-plus for this model class.**

## External model C — bottleneck capacity

Positive edge capacities were independently generated. The observed two-edge route capacity was defined as the best bottleneck route:
`B_2(i,j)=max_k min(B(i,k),B(k,j))`.

Again, the observable is defined as a transport/capacity quantity, not by choosing an Ω-Math algebra first.

Trials: 300, `N=8`.

Mean relative error:

| Candidate | Mean error |
|---|---:|
| max-min | 0 |
| min-plus | ≈ 0.574 |
| sum-product | ≈ 1.71 |

Winner count: **max-min 300/300**.

Result: **PASS — an independently defined bottleneck observable selects max-min for this model class.**

## Adversarial synthesis

The three external systems produce three different empirical winners:

`diffusion → sum-product`  
`travel time → min-plus`  
`bottleneck capacity → max-min`

This is the decisive result of the gate.

It simultaneously establishes two points:

1. **Algebra is empirically testable.** An independently defined observable can discriminate competing composition laws.
2. **No single algebra is forced by relational structure alone.** Different independently defined observables/model classes select different algebras on the same general relational carrier.

Therefore the correct architecture is not “discover the one algebra hidden inside relations”. It is:

`relational carrier → semantic/measurement class → admissible algebra → prediction → external test`.

The algebra is a hypothesis tied to an observable/model class until cross-domain evidence demonstrates a deeper common law.

## Important limitation

These are synthetic but externally specified model classes, not measurements of nature. The result therefore does **not** prove that physical systems universally use any of the three algebras.

It does prove that the previous identifiability obstacle is not fundamental: once the observation is genuinely independent of the candidate algebra, algebra selection can become an empirical question.

## Promotion decision

### Ω-Math

**PROMOTE** the external-observation layer as a required methodological boundary for empirical algebra selection.

Candidate algebras must be represented explicitly and tested against observables whose definitions do not already contain the candidate operation.

### FUNDAMENT

**DO NOT promote** max-min, min-plus, or sum-product as universal/fundamental.

The current evidence instead supports a stronger methodological principle:

> A composition algebra is physically meaningful only insofar as an independently specified observable repeatedly discriminates it against competing algebras.

## Next hard gate

Move from synthetic external models to real or independently sourced physical measurements, with preregistered observation definitions, held-out prediction, competing algebra families, null controls, and cross-domain replication.
