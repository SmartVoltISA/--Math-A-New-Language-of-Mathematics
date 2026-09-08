import pytest
from omega_math.core import Entity, Relation, Path, Configuration, State
from omega_math.runtime import concat, sign_summary, reverse_path, sufficient, verify_metric

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
