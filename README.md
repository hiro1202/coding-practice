# coding-practice

コーディング練習用リポジトリ。テストは自分で書き、TDD で解く。

## 必要なもの

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)（pytest の管理に使用。初回の `uv run pytest` で自動セットアップされる）

## ディレクトリ構成

```
.
├── contests/                 # コンテストごとの解答
│   └── abc464/               # コンテスト名
│       └── a/                # 問題ID
│           ├── main.py       # 解答 (solve = ロジック / main = 入出力)
│           ├── test_main.py  # solve() に対する手書きテスト
│           └── tests/        # サンプル入出力 (e2e 用)
│               ├── sample_1.txt        # 入力
│               └── sample_1.expected   # 期待する出力
├── templates/
│   ├── python.py             # 解答テンプレート
│   └── test_python.py        # テストのひな形
├── conftest.py               # solution フィクスチャ + サンプル e2e の自動収集
└── new.sh                    # 新しい問題のディレクトリを作る
```

## 使い方 (TDD の流れ)

```bash
./new.sh abc464 c
```

で `contests/abc464/c/` に `main.py`・`test_main.py`・`tests/` ができる。あとは:

1. **RED**: 問題ページのサンプルを `test_main.py` にテストとして写す

   ```python
   def test_sample_1(solution):
       assert solution.solve("EEW") == "East"
   ```

2. **GREEN**: `main.py` の `solve()` を実装してテストを通す
3. 境界値など気になるケースをテストに追加する
4. 提出前に `tests/sample_N.txt` / `sample_N.expected` にサンプルを貼り、
   入出力込みの e2e でも確認する

テストの実行:

```bash
uv run pytest contests/abc464/a   # 特定の問題 (手書きテスト + サンプル e2e)
uv run pytest                     # 全問題
uv run pytest -k sample           # e2e だけ、なども -k で絞れる
```

手動で実行:

```bash
python3 contests/abc464/a/main.py < contests/abc464/a/tests/sample_1.txt
```

## テストの仕組み

- `main.py` は「`solve()`（純粋ロジック、標準入出力に触らない）+ `main()`（stdin のパースと出力）」に分ける
- 手書きテスト (`test_main.py`) は `solution` フィクスチャ（`conftest.py` で定義）経由で
  同じディレクトリの `main.py` を読み込み、`solve()` を直接テストする
- `tests/sample_N.txt` は `conftest.py` の `pytest_collect_file` が自動でテストケースとして収集し、
  `main.py` をサブプロセス実行して `sample_N.expected` と比較する。
  `solve()` の単体テストでは拾えない入力パースや出力形式のバグはここで捕まえる
- e2e には実行時間制限 2 秒（AtCoder の標準）と実行時エラー検出付き
