"""main.py の solve() に対するテスト。

TDD の進め方:
1. 問題ページのサンプルをテストとして写す（solve() が未実装なので RED）
2. main.py の solve() を実装してテストを通す（GREEN）
3. 境界値など気になるケースを追加する

`solution` は conftest.py が提供するフィクスチャで、
同じディレクトリの main.py を読み込んだモジュール。

書き方の例（ABC464 A なら）:

    def test_sample_1(solution):
        assert solution.solve("EEW") == "East"
"""


def test_sample_1(solution):
    # TODO: 問題ページのサンプル1を写す
    assert solution.solve() == ...
