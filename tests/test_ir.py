import pytest

from omega_math.ir import IRInstruction, IRProgram
from omega_math.parser import Program, ParseError


def test_parser_lowers_reference_program_to_deterministic_ir():
    source = '''
    entity A 0
    entity B 1
    relation A B +1 rAB
    path P = A->B
    path E = epsilon(B)
    concat R = P + E
    incident A rAB
    sign P
    cycle P
    path_eq P P
    dist A B
    '''
    p = Program()
    assert p.run(source) == [True, 1, False, True, 1]
    ir = p.to_ir()
    assert ir.normalized() == (
        ('ENTITY', ('A', 0)),
        ('ENTITY', ('B', 1)),
        ('RELATION', ('A', 'B', 1, 'rAB')),
        ('PATH', ('P', ('A', 'B'))),
        ('EPSILON', ('E', 'B')),
        ('CONCAT', ('R', 'P', 'E')),
        ('INCIDENT', ('A', 'rAB')),
        ('SIGN', ('P',)),
        ('CYCLE', ('P',)),
        ('PATH_EQ', ('P', 'P')),
        ('DIST', ('A', 'B')),
    )


def test_ir_is_immutable_and_validates_arity():
    good = IRProgram((IRInstruction('ENTITY', ('A', 0)),))
    good.validate()
    with pytest.raises(ValueError):
        IRProgram((IRInstruction('ENTITY', ('A',)),)).validate()
    with pytest.raises(ValueError):
        IRProgram((IRInstruction('DIST', ('A', 'B', 'extra')),)).validate()


def test_ir_rejects_unknown_operations():
    with pytest.raises(ValueError):
        IRProgram((IRInstruction('CAUSE', ('A', 'B')),)).validate()


def test_parser_failure_does_not_create_partial_ir_for_invalid_line():
    p = Program()
    with pytest.raises(ParseError):
        p.run('entity A 0\nrelation A B +1 rAB')
    assert p.to_ir().normalized() == (('ENTITY', ('A', 0)),)
