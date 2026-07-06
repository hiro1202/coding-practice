import pytest

from abc464_a import main


@pytest.mark.parametrize(
    ("record", "expected"),
    [
        #
    ],
)
def test_兵力が多い方の軍名を出力すること(monkeypatch, capsys, record: str, expected: str) -> None:
    monkeypatch.setattr("builtins.input", lambda: record)
    main()
    assert capsys.readouterr().out.strip() == expected
