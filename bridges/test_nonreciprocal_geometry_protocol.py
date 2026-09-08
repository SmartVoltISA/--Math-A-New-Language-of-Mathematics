from omega_math.core import Entity, Relation, Path


def test_nonreciprocal_relations_are_not_reversed_implicitly():
    a = Entity("A", 0)
    b = Entity("B", 1)
    forward = Relation(a.id, b.id, 1, "rAB")
    path = Path((forward,))

    assert forward.src == a.id
    assert forward.dst == b.id
    assert path.relations == (forward,)
    assert not hasattr(path, "reverse")


def test_explicit_reverse_relation_remains_distinct():
    a = Entity("A", 0)
    b = Entity("B", 1)
    forward = Relation(a.id, b.id, 1, "rAB")
    backward = Relation(b.id, a.id, -1, "rBA")

    assert forward.src != backward.src
    assert forward.dst != backward.dst
    assert forward.key != backward.key
