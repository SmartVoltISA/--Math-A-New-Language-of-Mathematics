import pytest
from omega_math.core import Entity, Relation, Path, Configuration, State, Transformation
from omega_math.runtime import (
    concat, sign_summary, reverse_path, sufficient, verify_metric,
    quotient, distance, symmetry, model, execute,
)

def R(a,b,s): return Relation(a,b,s)

def test_typed_domains():
    Entity('a',0); Entity('b',1); R('a','b',-1); R('a','b',1)
    with pytest.raises(TypeError): Entity('x',-1)
    with pytest.raises(TypeError): R('a','b',0)

def test_path_identity_and_associativity():
    a,b,c,d='a','b','c','d'; p=Path((R(a,b,1),),a,b); q=Path((R(b,c,-1),),b,c); r=Path((R(c,d,1),),c,d)
    e=Path((),b,b)
    assert concat(e,q)==q
    assert concat(concat(p,q),r)==concat(p,concat(q,r))

def test_sign_is_summary_not_path_identity():
    p=Path((R('a','b',1),R('b','c',1)),'a','c')
    q=Path((R('a','b',-1),R('b','c',-1)),'a','c')
    assert sign_summary(p)==sign_summary(q)==1
    assert p!=q

def test_reversal_does_not_invent_edges():
    p=Path((R('a','b',1),R('b','c',-1)),'a','c')
    assert reverse_path(p).relations == (p.relations[1],p.relations[0])

def test_reduction_witness():
    ok,w=sufficient(lambda x:x%2, lambda x:x, range(4))
    assert not ok and w is not None

def test_metric_verifier():
    d=lambda a,b: abs(a-b)
    assert verify_metric(range(3),d)[0]

def test_quotient_builds_declared_equivalence_classes():
    classes=quotient(range(4), lambda a,b:(a%2)==(b%2))
    assert {frozenset(c) for c in classes} == {frozenset({0,2}),frozenset({1,3})}

def test_distance_is_declared_transformation_cost_not_energy():
    step=Transformation('step', lambda s, _=None:s+1, cost=2.0)
    assert distance(0,3,[step]) == 6.0
    assert distance(0,3,[step],max_steps=2) == float('inf')

def test_symmetry_returns_transformation_orbit():
    flip=Transformation('flip', lambda s, _=None:1-s, cost=1.0)
    assert symmetry(0,[flip]) == frozenset({0,1})

def test_model_is_an_explicit_representation_hook():
    assert model(7, lambda s:s%2) == 1

def test_execute_exposes_all_new_canonical_runtime_operators():
    assert execute('QUOTIENT', [0,1,2], lambda a,b:a%2==b%2)
    assert execute('DISTANCE', 0, 2, [Transformation('step', lambda s,_=None:s+1, cost=1.0)]) == 2.0
    assert execute('SYMMETRY', 0, [Transformation('flip', lambda s,_=None:1-s)]) == frozenset({0,1})
    assert execute('MODEL', 3, lambda s:s*2) == 6
