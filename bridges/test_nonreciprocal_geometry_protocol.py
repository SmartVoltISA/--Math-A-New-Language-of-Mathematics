from omega_math.core import Entity, Relation, Path, reverse_path


def test_nonreciprocal_relations_are_not_reversed_implicitly():
    a = Entity("A", 0)
    b = Entity("B", 1)
    forward = Relation(a, b, 1, "rAB")

    try:
        reverse_path(Path((forward,)))
    except ValueError as exc:
        assert "does not invent edges" in str(exc)
    else:
        raise AssertionError("reverse_path must reject an implicit inverse")


def test_explicit_reverse_relation_remains_distinct():
    a = Entity("A", 0)
    b = Entity("B", 1)
    forward = Relation(a, b, 1, "rAB")
    backward = Relation(b, a, -1, "rBA")

    assert forward.src == a and forward.dst == b
    assert backward.src == b and backward.dst == a
    assert forward.key != backward.key
