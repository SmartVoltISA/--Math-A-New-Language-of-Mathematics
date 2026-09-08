import json
import pytest

from omega_math.parser import Program
from omega_math.research import ResearchRecord, SCHEMA_VERSION, counterexample
from omega_math.runtime import execute_ir


def make_record(status="COUNTEREXAMPLE", observed=-1):
    return ResearchRecord(
        study_id="E0-demo",
        hypothesis_id="H-SIGN-PLUS",
        null_id="H0-SIGN-UNSPECIFIED",
        model={"path": ["A", "B"], "relations": [-1]},
        intervention={"type": "none"},
        observation={"operator": "SIGN", "value": observed},
        metric={"name": "sign", "value": observed},
        criterion={"expected": 1},
        horizon=1,
        seed=0,
        source_version="0.9.0",
        status=status,
        result={"expected": 1, "observed": observed},
    )


def test_research_record_is_deterministic_and_valid():
    record = make_record()
    record.validate()
    payload = record.to_dict()
    assert payload["schema_version"] == SCHEMA_VERSION
    assert json.loads(record.to_json()) == payload
    assert record.to_json() == make_record().to_json()


def test_counterexample_requires_counterexample_status():
    assert counterexample(make_record()).status == "COUNTEREXAMPLE"
    with pytest.raises(ValueError):
        counterexample(make_record("SUPPORT"))


def test_deliberately_false_hypothesis_is_machine_detected():
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

    observed = lowered[0]
    expected = 1
    status = "COUNTEREXAMPLE" if observed != expected else "SUPPORT"
    record = make_record(status=status, observed=observed)
    checked = counterexample(record)
    assert checked.result == {"expected": 1, "observed": -1}


def test_invalid_status_is_rejected():
    with pytest.raises(ValueError):
        make_record("MAYBE").validate()
