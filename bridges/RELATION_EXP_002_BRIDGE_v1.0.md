# REL-EXP-002 ↔ Ω-Math v1.0 — Continuous-Field Bridge Record

**Status:** BRIDGED RESULT / PARTIAL

## Source

- Experiment: `REL-EXP-002-CONTINUOUS-FIELD-RECOVERY`
- Repository: `SmartVoltISA/RELATION-LAB`
- Source revision: `4c46de33d8a65be21dbc53c7eae8d5e8398386da`
- Ω-Math base revision: `00d1ce17b30d1a1fcf671fd2c77d48cd2c63192a`

## Scope

REL-EXP-002 studies recovery of relation structure in a 40-element continuous-like field. The source model uses local and second-neighbor dynamical coupling, state transitions, regularized regression and a Jacobian-like influence matrix.

Ω-Math v1.0 does not define physical/continuous fields, numerical coupling magnitudes, probability, regression, ROC-AUC or Average Precision as primitive semantics. Therefore this bridge records the external experiment result and its provenance without claiming that Ω-Math reproduces the estimator.

## Source result

- Elements: 40
- True relation structure: local + second-neighbor
- ROC-AUC: 0.7548
- Average Precision: 0.4580
- Time-shuffled ROC-AUC: 0.5418
- Time-shuffled Average Precision: 0.1123

The reported result supports feasibility of relation recovery in the tested continuous-like dynamical model, while showing imperfect recovery and a substantial degradation under temporal shuffling.

## Ω-Math representable boundary

The source relation structure can be represented qualitatively as a directed relational graph once its orientation is explicitly declared. The numerical estimator output itself is not imported as Ω-Math primitive semantics.

A minimal qualitative encoding has the form:

```text
entity x0 0
entity x1 1
relation x0 x1 +1 r01
path P = x0->x1
sign P
```

This encoding tests only typed relation/path representation and execution parity. It is not a reconstruction of the 40-element field or its regression estimator.

## Research record

```json
{
  "schema_version": "omega-math.research-record.v1",
  "study_id": "REL-EXP-002",
  "hypothesis_id": "relation-recovery-continuous-field",
  "null_id": "time-shuffled-control",
  "model": "40-element continuous-like field with local and second-neighbor coupling",
  "intervention": "temporal shuffling control",
  "observation": "relation-recovery metrics",
  "metric": {"roc_auc": 0.7548, "average_precision": 0.4580, "shuffled_roc_auc": 0.5418, "shuffled_average_precision": 0.1123},
  "criterion": "compare real temporal structure with shuffled control",
  "horizon": "source experiment",
  "seed": null,
  "source_version": "RELATION-LAB@4c46de33d8a65be21dbc53c7eae8d5e8398386da",
  "status": "SUPPORT",
  "result": {
    "bridge_scope": "PARTIAL",
    "omega_math_reproduction": false,
    "source_conclusion": "supports feasibility within the tested continuous-like dynamical model",
    "limitation": "estimator is not a general relation detector"
  }
}
```

## Result classification

**PARTIAL — external experiment result is recorded; full experiment is not reproduced by Ω-Math v1.0.**

`SUPPORT` in the ResearchRecord refers to the source experiment's declared conclusion within its tested model. `PARTIAL` refers to bridge coverage. These classifications must not be conflated.

## Boundary check

The bridge deliberately does **not** add:

- physical time;
- physical space;
- probability;
- physical energy;
- causality;
- continuous relation magnitude;
- regression semantics;
- statistical estimator semantics.

## Scientific value

REL-EXP-002 strengthens the separation between relational representation and relation recovery. It shows that a richer dynamical system can contain recoverable relation structure, but recovery quality is model- and estimator-dependent. It therefore cannot by itself establish that relation is a universal primitive or that geometry follows from relations.

## Next falsification target

Move from continuous reciprocal propagation to an explicitly **non-reciprocal** system. Test whether directed response relations induce a non-symmetric distance/geometry and whether that structure remains representation-consistent under coordinate changes.
