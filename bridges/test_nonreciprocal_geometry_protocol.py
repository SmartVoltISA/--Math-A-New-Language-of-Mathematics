from omega_math.core import Entity, Relation, Path


def test_nonreciprocal_relations_are_not_reversed_implicitly():
    a = Entity("A", 0)
    b = Entity("B", 1)
    forward = Relation("rAB", a, b, 1)
    reverse = Path((forward,)).reverse()

    assert forward.source == a
    assert forward.target == b
    assert reverse.relations == ()


def test_explicit_reverse_relation_remains_distinct():
    a = Entity("A", 0)
    b = Entity("B", 1)
    forward = Relation("rAB", a, b, 1)
    backward = Relation("rBA", b, a, -1)

    assert forward.source != backward.source
    assert forward.target != backward.target
    assert forward.key != backward.key
