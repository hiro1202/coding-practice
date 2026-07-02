"""pytest の共通設定。2つの役割を持つ。

1. `solution` フィクスチャ:
   test_main.py と同じディレクトリの main.py を読み込んで返す。
   手書きのテストから solution.solve(...) の形でロジックを直接テストできる。

2. サンプル入出力の e2e テスト:
   tests/sample_N.txt を自動でテストケースとして収集し、main.py を
   サブプロセス実行して出力が sample_N.expected と一致するか検証する。
   solve() の単体テストでは拾えない入力パースや出力形式のバグを守る。

実行例:
    uv run pytest                     # 全問題
    uv run pytest contests/abc464/a   # 特定の問題（手書き + e2e）
"""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).parent

# AtCoder の標準的な実行時間制限（秒）
TIME_LIMIT = 2


@pytest.fixture
def solution(request: pytest.FixtureRequest):
    """テストファイルと同じディレクトリの main.py をモジュールとして返す。"""
    main_py = request.path.parent / "main.py"
    # 問題ごとに一意なモジュール名を付け、他の問題の main.py と衝突しないようにする
    name = "solution_" + "_".join(request.path.parent.relative_to(ROOT).parts)
    spec = importlib.util.spec_from_file_location(name, main_py)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def pytest_collect_file(file_path: Path, parent: pytest.Collector):
    """tests/sample_N.txt を見つけたら e2e テストケースとして収集する。"""
    if (
        file_path.parent.name == "tests"
        and file_path.suffix == ".txt"
        and file_path.stem.startswith("sample_")
    ):
        return SampleFile.from_parent(parent, path=file_path)


class SampleFile(pytest.File):
    def collect(self):
        yield SampleItem.from_parent(self, name=self.path.stem)


class SampleItem(pytest.Item):
    """sample_N.txt を標準入力として main.py を実行し、.expected と比較する。"""

    def runtest(self) -> None:
        in_file = self.path
        exp_file = in_file.with_suffix(".expected")
        prog = in_file.parents[1] / "main.py"

        if not exp_file.exists():
            pytest.fail(f"期待値ファイルがありません: {exp_file.name}", pytrace=False)

        with in_file.open() as stdin:
            result = subprocess.run(
                [sys.executable, str(prog)],
                stdin=stdin,
                capture_output=True,
                text=True,
                timeout=TIME_LIMIT,
            )

        if result.returncode != 0:
            pytest.fail(
                f"実行時エラー (exit {result.returncode}):\n{result.stderr}",
                pytrace=False,
            )

        expected = exp_file.read_text().rstrip("\n")
        actual = result.stdout.rstrip("\n")
        if actual != expected:
            pytest.fail(
                "出力がサンプルと一致しません\n"
                f"--- expected ---\n{expected}\n"
                f"--- actual ---\n{actual}",
                pytrace=False,
            )

    def reportinfo(self):
        return self.path, None, f"サンプル e2e: {self.name}"
