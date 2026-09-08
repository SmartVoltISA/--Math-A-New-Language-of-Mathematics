import json

from omega_math.parser import Program
from omega_math.research import ResearchRecord
from omega_math.runtime import execute_ir


SOURCE_REVISION = "5c1b6522d90763e89e61a9c7ae2ceb57c9e00265"
OMEGA_MATH_REVISION = "9c4fc0a301f0721df9a80436cbbda72069c404e7"


def test_rel_exp_001_qualitative_snapshot_bridge():
    source = """
    entity A 0
    entity B 1
    relation A B -1 rAB
    path P = A->B
    sign P
    """

    program = Program()
    direct = program.run(source)
    lowered = execute_ir(program.to_ir())
    assert direct == lowered == [-1]

    record = ResearchRecord(
        study_id="REL-EXP-001-QUAL-SNAPSHOT",
        hypothesis_id="REL-EXP-001",
        null_id="REL-EXP-001-QUAL-NULL",
        model={"relation": "A->B", "mode": "qualitative-snapshot"},
        intervention={"type": "none"},
        observation={"operator": "SIGN", "value": lowered[0]},
        metric={"name": "relation_sign", "value": lowered[0]},
        criterion={"expected": -1},
        horizon=1,
        seed=0,
        source_version=f"RELATION-LAB@{SOURCE_REVISION};OMEGA-MATH@{OMEGA_MATH_REVISION}",
        status="SUPPORT",
        result={"observed": lowered[0], "scope": "qualitative-snapshot"},
    )

    record.validate()
    assert json.loads(record.to_json()) == record.to_dict()
    assert record.result["observed"] == -1
    assert record.result["scope"] == "qualitative-snapshot"
