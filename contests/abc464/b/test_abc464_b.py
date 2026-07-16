import pytest

from abc464_b import main


@pytest.mark.parametrize(
    ("record", "expected"),
    [
        pytest.param(
            "4 5\n.....\n..#..\n.###.\n.....",
            ".#.\n###",
            id="サンプル1"
        ),
        pytest.param(
            "3 4\n#...\n....\n...#",
            "#...\n....\n...#",
            id="サンプル2_切り出し不要"
        ),
        pytest.param(
            "5 6\n......\n......\n...#..\n......\n......",
            "#",
            id="サンプル3_黒1ピクセル"
        ),
        pytest.param(
            "1 1\n#",
            "#",
            id="最小入力_1x1"
        ),
        pytest.param(
            "2 3\n###\n###",
            "###\n###",
            id="全面が黒"
        ),
        pytest.param(
            "1 5\n.#.#.",
            "#.#",
            id="1行のみ_横方向の切り出し"
        ),
        pytest.param(
            "4 1\n.\n#\n#\n.",
            "#\n#",
            id="1列のみ_縦方向の切り出し"
        ),
    ],
)
def test_黒ピクセルの外接矩形を切り出して出力すること(monkeypatch, capsys, record: str, expected: str) -> None:
    lines = iter(record.splitlines())
    monkeypatch.setattr("builtins.input", lambda: next(lines))
    main()
    assert capsys.readouterr().out.strip() == expected
