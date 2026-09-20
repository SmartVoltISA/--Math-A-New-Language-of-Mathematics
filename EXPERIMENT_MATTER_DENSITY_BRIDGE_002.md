# Ω-Math Experiment — MATTER Density Bridge 002

## Status

**EXECUTED / FINITE + MULTI-SEED CONTROL VERIFICATION**

Date: 2026-09-20  
Seed family: 0–11 for random-sign controls

## Question

Does the tested chain

`H_R → ψ_R → |ψ_R|²`

produce a well-defined, conserved relational density that survives fixed coarse-graining and shows reproducible dependence on relational structure?

This experiment deliberately stops before assigning physical probability, matter density, or gravity.

## Frozen construction

Graph: finite 20×20 square lattice, open boundaries.

Preferred operator from MATTER/H_R Bridge 001:

`H_R = D - A_R`

with typed relation signs `r_ij ∈ {-1,+1}`.

Evolution:

`i dψ/dt = H_R ψ`

Initial state:

- normalized delta-localized state at the lattice center;
- `||ψ(0)||² = 1`.

Local relational weight:

`q_i(t)=|ψ_i(t)|²`.

Coarse-graining was fixed before comparison:

- non-overlapping 2×2 lattice blocks;
- block mass `Q_b = Σ_{i∈b} q_i`;
- no fitted kernel width;
- no fitted parameters;
- no physical units assigned.

Measured quantities:

- total norm `Σ_i q_i`;
- microscopic participation ratio `PR = 1/Σ_i q_i²`;
- coarse participation ratio `PR_block = 1/Σ_b Q_b²`;
- maximum coarse block mass;
- coarse-grained Shannon entropy.

## Controls

### C1 — all-positive topology

All relation signs are +1 on the fixed square lattice.

### C2 — random-sign topology-preserving control

Same 20×20 topology and same number of edges, with independent ±1 relation signs.

Twelve independent seeds were tested.

### C3 — topology-randomized control

Same number of edges but randomized endpoint topology; relation signs all +1.

This separates sign effects from connectivity effects.

## 1. Conservation check

For every finite Hermitian run, the norm remained numerically constant.

Representative 20×20 runs:

- all-positive: norm deviation ≈ 4×10^-15;
- random-sign: norm deviation ≈ 2×10^-14;
- topology-randomized: norm deviation ≈ 2×10^-14.

Therefore:

**PASS — `Σ_i |ψ_i|²` is conserved by the declared finite relational dynamics.**

This is Hilbert-norm conservation of the model. It is **not** a derivation of the Born rule.

## 2. Fixed coarse-grained density exists

The block masses

`Q_b(t)=Σ_{i∈b}|ψ_i(t)|²`

are non-negative and satisfy

`Σ_b Q_b = 1`

up to numerical precision.

Thus the model provides a mathematically defined normalized coarse-grained density measure without inserting a physical mass law.

## 3. All-positive propagation

For the 20×20 all-positive lattice, starting from the central delta state:

| t | microscopic PR | block PR | max block mass | entropy |
|---:|---:|---:|---:|---:|
| 0 | 1.00 | 1.00 | 1.0000 | 0.000 |
| 2 | 49.82 | 19.69 | 0.1009 | 3.209 |
| 5 | 159.21 | 54.30 | 0.0597 | 4.296 |
| 10 | 222.09 | 74.95 | 0.0277 | 4.452 |
| 20 | 229.52 | 76.68 | 0.0254 | 4.455 |

The localized state spreads over the lattice while total norm remains fixed.

## 4. Random-sign propagation

For one representative random-sign realization:

| t | microscopic PR | block PR | max block mass | entropy |
|---:|---:|---:|---:|---:|
| 0 | 1.00 | 1.00 | 1.0000 | 0.000 |
| 2 | 13.20 | 7.59 | 0.3050 | 2.543 |
| 5 | 41.27 | 23.10 | 0.1036 | 3.582 |
| 10 | 60.25 | 29.81 | 0.1010 | 3.953 |
| 20 | 108.08 | 46.07 | 0.0941 | 4.263 |

The same topology with random relation signs spreads substantially less in this finite run.

This reproduces the localization/propagation distinction already observed in MATTER/H_R Bridge 001, now measured after the explicit map `ψ → |ψ|²`.

## 5. Multi-seed random-sign verification

Twelve independent random-sign realizations were run to `t=20`.

Random-sign mean ± standard deviation:

- microscopic PR: `121.67 ± 33.76`;
- block PR: `54.46 ± 11.46`;
- maximum block mass: `0.0632 ± 0.0278`;
- lowest eigenvalue: `0.3181 ± 0.0522`.

All-positive reference at `t=20`:

- microscopic PR: `229.52`;
- block PR: `76.68`;
- maximum block mass: `0.0254`;
- lowest eigenvalue: approximately `0`.

The sign-dependent difference is therefore not an artifact of a single random seed in this tested sample.

## 6. Topology-randomized control

A topology-randomized graph with the same edge count and all-positive relation signs was also evolved.

At `t=20`:

- microscopic PR ≈ 148.77;
- block PR ≈ 70.70;
- maximum block mass ≈ 0.0361.

Its behavior differs from both the regular all-positive lattice and the random-sign lattice.

Therefore:

**PASS — both topology and relation signs can alter the coarse-grained density dynamics.**

The experiment does not yet identify which structural feature would be physically fundamental.

## 7. What this closes

The mathematical bridge

`H_R → ψ_R → |ψ_R|² → fixed coarse-grained relational density Q_b`

is now explicitly constructed and numerically verified in finite models.

The result has three parts:

1. Hermitian relational dynamics conserves total norm.
2. `|ψ_R|²` defines a non-negative normalized relational weight.
3. Fixed block coarse-graining produces a stable, directly measurable density field whose propagation/localization depends on topology and relation signs.

## 8. What this does NOT close

The following remain OPEN:

`|ψ_R|² → physical probability`

`Q_b → physical mass density`

`Q_b → gravitational source`

`relational density → observed galaxy rotation curves`

No physical mass unit, gravitational constant, probability postulate, measurement rule, or dark-matter target was inserted.

Therefore this experiment is not evidence that the constructed density is actual matter or dark matter.

## 9. Decision

**PASS:** finite relational dynamics gives a conserved non-negative density measure after `ψ → |ψ|²`.

**PASS:** fixed, parameter-free 2×2 coarse-graining gives reproducible mesoscopic density measures.

**PASS:** topology-randomized and sign-randomized controls change the resulting density dynamics.

**OPEN:** whether a physically meaningful coarse-grained field can be selected without arbitrary coarse-graining choices.

**OPEN:** whether the relational density has any physical correspondence to matter.

**NO CLAIM:** no gravitational interpretation is made.

## 10. Next decisive bridge

The next step is not yet a galaxy fit.

It is:

`coarse-grained ρ_R → effective field/dynamical response`

with a preregistered field equation or response functional and explicit null controls.

The required order remains:

`FACT → CHECK → RESULT → DECISION → FIXATION`.

## Final result

The MATTER chain has advanced to:

`typed relation → H_R → spectrum → ψ_R → |ψ_R|² → coarse-grained relational density`.

This bridge is **mathematically verified in finite models**.

Its physical interpretation remains **OPEN**.
