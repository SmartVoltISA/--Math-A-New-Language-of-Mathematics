# Ω-Math v0.9 — Mathematical Audit 003

## Scope

Third mathematical and synchronization audit after v0.9 frontier closure and canonical-layer synchronization.

The audit checks whether the current canonical documents agree on the same typed language, path semantics, equivalence semantics, reduction rule, dynamics boundary, and quotient-geometry conditions.

This record supersedes the *action list* of `V09_MATH_AUDIT_002.md`; it does not erase historical records.

## 1. Canonical document authority

`CANONICAL_INDEX_v0.9.md` defines the current authoritative layer.

The following older files remain historical:

- `PATH_ALGEBRA.md`
- `EQUIVALENCE.md`
- `STATUS.md`
- other explicitly versioned pre-v0.9 records.

No historical document is allowed to silently override a v0.9 canonical document.

**Status: PASS**

## 2. Type separation

The canonical type system keeps entity states `{0,1}` distinct from relation states `{−1,+1}`.

The following coercions remain forbidden unless explicitly introduced as derived operations:

- relation sign as arithmetic addition/subtraction;
- absence as a third relation value;
- path as a scalar;
- transformation cost as physical energy;
- transition order as physical time.

This prevents several common category errors in later derivations.

**Status: PASS**

## 3. Path semantics

The current canonical path layer defines:

- paths as ordered relation sequences with compatible endpoints;
- empty path `ε_e` as a path-level identity where concatenation is defined;
- concatenation as the primitive sequential composition of paths;
- no primitive relation identity;
- no primitive relation inverse;
- no requirement for primitive relation composition.

A path may have a derived sign sequence and derived sign product, but these summaries do not replace the path.

The legacy `PATH_ALGEBRA.md` wording that requires at least one relation is therefore historical/stale and does not control v0.9 semantics.

**Status: PASS / LEGACY CONFLICT EXPLICITLY CONTAINED**

## 4. Equivalence hierarchy

The canonical layer distinguishes:

- identity equality;
- state equality;
- static observational equivalence;
- finite-horizon behavioral equivalence;
- infinite-horizon behavioral equivalence;
- task-specific nondeterministic equivalence.

For deterministic systems with fixed observation, admissible inputs/interventions and horizon, finite-horizon equivalence is an equivalence relation. Infinite-horizon equivalence is the intersection of the finite-horizon relations.

No claim is made that static observational equivalence is sufficient for dynamic behavior.

**Status: PASS**

## 5. Nondeterministic semantics

For nondeterministic systems the successor set is retained rather than silently selecting one successor.

Behavioral equivalence must declare its criterion, for example:

- trace/output equivalence;
- branching-sensitive equivalence;
- existential reachability;
- universal safety.

Therefore deterministic recursive signatures cannot be promoted to a universal nondeterministic equivalence without additional assumptions.

**Status: PASS / SCOPE EXPLICIT**

## 6. Reduction and sufficiency

The canonical sufficiency condition is:

`Q(x)=Q(y) ⇒ F(x)=F(y)`.

This is the required fiber-constancy condition for the task `F` to factor through the representation `Q` on its image.

It is task-relative. A descriptor can be sufficient for one transition/observation task and insufficient for another.

Existing counterexamples support this boundary for reduced path/geometric descriptors.

**Status: PASS / FINITE COUNTEREXAMPLES CONSISTENT**

## 7. Quotient geometry

The representative-infimum construction

`d_Q([x],[y]) = inf{d(x',y'): x'~x, y'~y}`

is retained only as a candidate in the general case.

Triangle inequality and separation are not automatic for an arbitrary equivalence relation. A sufficient compatible setting includes quotienting by an isometry/group action, subject to the precise construction used. Otherwise the properties must be established for the concrete finite system.

The recorded finite counterexample is therefore treated as a mathematical boundary condition, not an implementation defect.

**Status: PASS / COUNTEREXAMPLE VERIFIED**

## 8. Transformation-derived distance

For

`d_c(x,y)=inf{c(T):T∈T(x,y)}`

the metric properties require explicit assumptions:

- composable admissible transformations;
- subadditive costs for triangle inequality;
- reversibility/equal cost for symmetry;
- exclusion of zero-cost distinct states, or an explicit quotient identifying them, for separation.

Thus no universal metric follows merely from assigning costs to transformations.

**Status: PASS / CONDITIONS EXPLICIT**

## 9. Geometry versus dynamics

Current experiments establish that increasingly rich static descriptors can still fail to determine behavior under a controlled transition rule.

In particular, the repository contains finite evidence for:

- same coarse structural counts but different topology;
- same source-distance profile but different behavior;
- same unsigned geometry/topology with different relation signs but different propagation;
- same path endpoints/length/sign summary but different intermediate organization and behavior.

These results do not prove that all geometry is insufficient. They establish only that the tested summaries are not universally sufficient for the tested tasks.

**Status: SUPPORTED / SCOPE-BOUNDED**

## 10. Dynamics boundary

The current canonical dynamics layer separates:

- transition order from physical time;
- model memory from physical memory;
- feedback recurrence from causality;
- transformation cost from physical energy;
- stable macro-patterns from a universal definition of emergence.

Probability, causal intervention, physical time and physical energy remain explicit bridges rather than hidden meanings of the primitive language.

**Status: PASS**

## 11. Point/boundary research

The point-like/cohesive regime remains a research hypothesis, not a primitive theorem.

Operational tests may combine closure, retention, confinement, interface persistence, perturbation recovery and redundancy, but no physical interpretation is accepted without an independent mapping to observables.

Potential normalized measures must declare their domain guards before execution; a zero denominator is an invalid/undefined case, not an implicit zero.

**Status: PASS / PRE-REGISTRATION DISCIPLINE REQUIRED**

## 12. Physical interpretation boundary

The current formal language does not derive:

- spacetime;
- gravity;
- black holes;
- physical energy;
- physical causality;
- empirical time;
- quantum mechanics.

Such claims remain external hypotheses/bridges requiring independent empirical or mathematical support.

**Status: PASS**

## 13. Remaining documentation actions

No mathematical repair to the v0.9 core is required by this audit.

Recommended documentation hygiene:

1. keep `EQUIVALENCE.md` and `PATH_ALGEBRA.md` explicitly historical;
2. keep `STATUS_v0.9.md` as the current status authority;
3. keep canonical experiment records distinct from exploratory drafts;
4. update future audits rather than rewriting historical audit conclusions;
5. add a new experiment only when it tests a genuinely unresolved boundary.

## 14. Final decision

The current v0.9 layer is internally coherent under its declared scope.

The main mathematical boundary is now clear:

`primitive language → derived representations → task-specific sufficiency → verified behavior`.

No tested low-dimensional summary has been promoted to a universal representation merely because it works on selected examples.

The project therefore proceeds above the closed language layer rather than reopening the primitive core.

`complete language ≠ complete mathematics ≠ complete physics`

**AUDIT-003: PASS — CORE CLOSED / RESEARCH FRONTIER OPEN**
