# Ω-Math — Withheld Reconstruction Experiment v1.0

**Status:** EXEC / SUPPORTED RESULT  
**Purpose:** decisive test of whether the structural kernel can reconstruct a response law without being given constitutive information.

## 1. Frozen structural input

The reconstruction is restricted to:

`STATE + RELATION + DISTINCTION (Δ) + CONSTRAINT + TRANSITION`

No domain-specific coefficient, constitutive equation, material parameter, or unit conversion is supplied to the structural reconstruction.

The candidate structural response form tested is:

`J = g · Δ`

where `g` is deliberately withheld.

## 2. Counterfamily

Three domain labels are used only as independent test cases:

- electrical
- thermal
- fluid

For each domain, the hidden constitutive coefficient is independently selected from:

`g ∈ {0.5, 1.0, 2.0, 4.0}`

The same structural input `Δ ∈ [-3,3]` is used. The generated response is `J = gΔ`.

A zero-intercept least-squares reconstruction of `J = aΔ` is then performed.

## 3. Result: linear counterfamily

For every domain and every hidden coefficient:

| Domain | hidden g | recovered a | RMSE |
|---|---:|---:|---:|
| electrical | 0.5 | 0.5 | 0 |
| electrical | 1.0 | 1.0 | 0 |
| electrical | 2.0 | 2.0 | 0 |
| electrical | 4.0 | 4.0 | 0 |
| thermal | 0.5 | 0.5 | 0 |
| thermal | 1.0 | 1.0 | 0 |
| thermal | 2.0 | 2.0 | 0 |
| thermal | 4.0 | 4.0 | 0 |
| fluid | 0.5 | 0.5 | 0 |
| fluid | 1.0 | 1.0 | 0 |
| fluid | 2.0 | 2.0 | 0 |
| fluid | 4.0 | 4.0 | 0 |

### Interpretation

The structural kernel recovers the **form** `J ∝ Δ`, but the coefficient is exactly the hidden constitutive information. Therefore the kernel cannot identify a unique transmission coefficient from structure alone.

This is a constructive identifiability failure, not a failure of the structural form.

## 4. Adversarial nonlinear counterfamily

The same structural variables were also tested against laws that preserve the same directed relation between difference and response but are not globally linear:

- linear: `J = 2Δ`
- signed quadratic: `J = 2Δ|Δ|`
- threshold: `J = 0` for `|Δ|<1`, otherwise `J = 2Δ`
- saturating: `J = 2 tanh(Δ)`

| Law | Best linear coefficient | RMSE |
|---|---:|---:|
| linear | 2.000 | 0.000 |
| signed quadratic | 4.515 | 2.026 |
| threshold | 1.929 | 0.644 |
| saturating | 0.908 | 0.433 |

The nonlinear cases demonstrate that even the linear response form is not universally reconstructible from `STATE + RELATION + Δ + CONSTRAINT + TRANSITION` alone.

## 5. Gate decision

### G-B — Generic reconstruction

**PARTIAL PASS.**

The experiment supports reconstruction of a structural relation of the form:

`response = operator(structural difference, relation, constraint, state)`

For a restricted linear family, `J = gΔ` is recoverable as a structural form.

### Unique coefficient identification

**REJECTED WITHOUT DOMAIN CLOSURE.**

The counterfamily `g ∈ {0.5,1,2,4}` produces identical structural inputs with different valid responses. Any algorithm returning one universal `g` without additional information would be injecting unstated constitutive assumptions.

### Universal scalar transmission law

**REJECTED.**

The nonlinear counterfamily shows that even the linear constitutive shape requires additional domain assumptions.

## 6. What survives

The experiment strengthens the following architecture:

`UNIVERSAL STRUCTURAL KERNEL`

→ `DERIVED RESPONSE FORM`

→ `CONSTITUTIVE / DOMAIN CLOSURE`

→ `NUMERICAL PARAMETERS`

→ `PHYSICAL INTERPRETATION`

The result does **not** justify promoting `g`, conductivity, resistance, energy, flow, or a universal scalar transmission coefficient into the primitive kernel.

## 7. Reproducibility record

- deterministic seed: `42`
- difference grid: 301 points for adversarial nonlinear test; 121 points for coefficient counterfamily
- linear fit: least squares through origin
- metric: RMSE
- hidden coefficients: fixed before reconstruction
- negative control: nonlinear constitutive laws

## 8. Final statement

**The kernel reconstructs relational structure, not arbitrary domain constitutive closure.**

This is a positive boundary result: it tells Ω-Math what can be universal and exactly where domain information must enter.
