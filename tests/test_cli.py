import io

from omega_math.cli import main


def test_cli_executes_stdin(capsys, monkeypatch):
    source = 'entity A 0\nentity B 1\nrelation A B +1 rAB\npath P = A->B\nsign P\n'
    monkeypatch.setattr('sys.stdin', io.StringIO(source))
    assert main([]) == 0
    assert capsys.readouterr().out.strip() == '1'
