"""contests/ 以下の全問題をサンプルケースで検証する。

各問題の tests/sample_N.txt を標準入力として main.py を実行し、
出力が tests/sample_N.expected と一致することを確認する。

実行例:
    uv run pytest                 # 全問題
    uv run pytest -k abc464/a     # 特定の問題だけ
    uv run pytest -k sample_2     # 特定のサンプルだけ
"""

import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent

# AtCoder の標準的な実行時間制限（秒）
TIME_LIMIT = 2


def collect_cases():
    """contests/<contest>/<problem>/tests/sample_N.txt を全部集める。"""
    for in_file in sorted(ROOT.glob("contests/*/*/tests/sample_*.txt")):
        problem_dir = in_file.parents[1]
        case_id = f"{problem_dir.parent.name}/{problem_dir.name}/{in_file.stem}"
        yield pytest.param(problem_dir / "main.py", in_file, id=case_id)


@pytest.mark.parametrize(("prog", "in_file"), list(collect_cases()))
def test_sample(prog: Path, in_file: Path) -> None:
    exp_file = in_file.with_suffix(".expected")
    assert exp_file.exists(), f"期待値ファイルがありません: {exp_file}"

    with in_file.open() as stdin:
        result = subprocess.run(
            [sys.executable, str(prog)],
            stdin=stdin,
            capture_output=True,
            text=True,
            timeout=TIME_LIMIT,
        )

    assert result.returncode == 0, f"実行時エラー:\n{result.stderr}"

    expected = exp_file.read_text().rstrip("\n")
    actual = result.stdout.rstrip("\n")
    assert actual == expected
