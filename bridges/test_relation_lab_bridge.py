from omega_math.parser import Program
from omega_math.runtime import execute_ir


def test_relation_lab_bridge_minimal_contract():
    source = '''
    entity A 0
    entity B 1
    relation A B -1 rAB
    path P = A->B
    sign P
    '''
    program = Program()
    direct = program.run(source)
    bridged = execute_ir(program.to_ir())
    assert direct == bridged
    assert direct == [-1]
