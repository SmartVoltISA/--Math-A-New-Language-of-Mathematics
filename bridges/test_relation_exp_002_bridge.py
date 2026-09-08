from omega_math.parser import Program
from omega_math.research import ResearchRecord
from omega_math.runtime import execute_ir


def test_relation_exp_002_bridge_preserves_typed_snapshot_and_record():
    source = '''
    entity x0 0
    entity x1 1
    relation x0 x1 +1 r01
    path P = x0->x1
    sign P
    '''

    program = Program()
    direct = program.run(source)
    lowered = execute_ir(program.to_ir())

    assert direct == lowered == [1]

    record = ResearchRecord(
        study_id="REL-EXP-002",
        hypothesis_id="relation-recovery-continuous-field",
        null_id="time-shuffled-control",
        model="40-element continuous-like field with local and second-neighbor coupling",
        intervention="temporal shuffling control",
        observation="relation-recovery metrics",
        metric={
            "roc_auc": 0.7548,
            "average_precision": 0.4580,
            "shuffled_roc_auc": 0.5418,
            "shuffled_average_precision": 0.1123,
        },
        criterion="compare real temporal structure with shuffled control",
        horizon="source experiment",
        seed=None,
        source_version="RELATION-LAB@4c46de33d8a65be21dbc53c7eae8d5e8398386da",
        status="SUPPORT",
        result={
            "bridge_scope": "PARTIAL",
            "omega_math_reproduction": False,
        },
    )

    record.validate()
    assert '"bridge_scope":"PARTIAL"' in record.to_json()
    assert '"omega_math_reproduction":false' in record.to_json()
