from omega_math.cli import main


def test_cli_identifies_v1_reference_interface(capsys):
    assert main([]) == 0
    out = capsys.readouterr()
    assert out.out == ''


def test_cli_executes_stdin(capsys, monkeypatch):
    source = 'entity A 0\nentity B 1\nrelation A B +1 rAB\npath P = A->B\nsign P\n'
    monkeypatch.setattr('sys.stdin', __import__('io').StringIO(source))
    assert main([]) == 0
    assert capsys.readouterr().out.strip() == '1'
