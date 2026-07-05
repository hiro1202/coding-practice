import pytest

from abc464_a import main


@pytest.mark.parametrize(
    ("record", "expected"),
    [
        pytest.param("EEWEW", "East", id="Eが多い"),
        pytest.param("WWWWWWW", "West", id="Wのみ"),
        pytest.param("E", "East", id="最小入力_E"),
        pytest.param("W", "West", id="最小入力_W"),
    ],
)
def test_兵力が多い方の軍名を出力すること(monkeypatch, capsys, record: str, expected: str) -> None:
    monkeypatch.setattr("builtins.input", lambda: record)
    main()
    assert capsys.readouterr().out.strip() == expected
