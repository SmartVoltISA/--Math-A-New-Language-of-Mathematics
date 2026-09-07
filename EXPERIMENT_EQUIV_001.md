# Ω-Experiment EQUIV-001 — Minimal Distinction Collapse

## 1. Question

What is the smallest relational structure in which distinct entities become observationally equivalent and previously distinct paths become indistinguishable?

## 2. Construction

Use four distinct entities:

`A=(1,1)`
`B=(2,1)`
`C=(3,1)`
`D=(4,1)`

All entities have the same state:

`s_A=s_B=s_C=s_D=1`.

Identity remains distinct:

`A≠B≠C≠D`.

Choose an observation that sees only state:

`O(e)=s_e`.

Therefore:

`A≈ₒB≈ₒC≈ₒD`.

The quotient has one class:

`E/≈ₒ = {[A]ₒ}`.

## 3. Original structure

Relations:

`A —(+1)→ C`

`B —(−1)→ D`

There are two connected components and two distinct edges.

There are also two distinct one-edge paths:

`P₁ = A,(+1),C`

`P₂ = B,(−1),D`.

`P₁ ≠ P₂`.

## 4. Quotient structure

Since all four endpoints belong to the same observation class:

`Q(A)=Q(B)=Q(C)=Q(D)=X`.

The paths map to:

`Q(P₁)=X,(+1),X`

`Q(P₂)=X,(−1),X`.

Therefore entity distinctions and endpoint distinctions are lost, but the relation signs remain different **if the quotient preserves edge multiplicity and sign labels**.

The two paths are still distinguishable by sign in this representation.

If, instead, the quotient also replaces parallel signed relations by a single unlabeled edge, the two paths become identical and the sign distinction is lost too.

This is an important result: **collapse is not determined by vertex quotienting alone.** The relation-quotient rule matters.

## 5. Structural comparison

| Property | Original | Vertex quotient, signs retained | Vertex + relation collapse |
|---|---:|---:|---:|
| Distinct entities | 4 | 1 class | 1 class |
| Components | 2 | 1 | 1 |
| Relations | 2 | 2 self-relations | potentially 1 |
| Path count represented | 2 | 2 signed paths | potentially 1 |
| Endpoint distinction | preserved | lost | lost |
| Sign distinction | preserved | preserved | potentially lost |
| Identity distinction | preserved | lost observationally | lost observationally |

The exact numerical value of graph degree or cycle rank depends on the chosen graph representation, especially on whether self-loops and parallel edges are retained. Those conventions must therefore be declared before using such quantities as invariants.

## 6. Result

### Confirmed formally

1. Equal state does not imply equal identity.
2. An observation map can erase identity distinctions.
3. A quotient on entities can merge previously distinct endpoints.
4. Distinct paths can become structurally closer or identical after quotienting.
5. Vertex collapse alone does not determine whether relation-sign information survives.

### Not confirmed

- physical collapse;
- irreversible collapse;
- disappearance of the underlying entities;
- gravity;
- black-hole behavior.

## 7. New requirement for Ω-Math

A complete collapse operator cannot be defined only as:

`Q:E→E/≈`.

For a relational system it must specify at least:

`Q_E` — how entities are merged;

`Q_R` — how relations are merged, preserved, or discarded;

`Q_P` — how paths are mapped and when distinct paths become equivalent.

Thus a structural quotient should be treated as a tuple of rules rather than a vertex-only operation.

## 8. Critical observation

The experiment separates two processes that are often confused:

`distinction loss by observation`

and

`structural change of the underlying system`.

The first can happen while the original Ω-system remains completely unchanged.

Therefore a future physical-collapse hypothesis must be based on a change in the system or in an invariant observable of the system, not merely on choosing a coarser description.

## 9. Next test

Construct the smallest dynamic example in which the observation quotient is fixed while the underlying transition law evolves.

Test whether two entities that are observationally equivalent at time `t` remain equivalent at `t+1`.

This will determine whether static observational equivalence is sufficient or whether Ω-Math needs a behavior-preserving equivalence analogous to bisimulation.
