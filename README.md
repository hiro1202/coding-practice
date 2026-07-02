# coding-practice

コーディング練習用リポジトリ。

## 必要なもの

- Python 3.12+
- [uv](https://docs.astral.sh/uv/)（pytest の管理に使用。初回の `uv run pytest` で自動セットアップされる）

## ディレクトリ構成

```
.
├── contests/              # コンテストごとの解答
│   └── abc464/            # コンテスト名
│       └── a/             # 問題ID
│           ├── main.py    # 解答
│           └── tests/     # サンプルケース
│               ├── sample_1.txt        # 入力
│               └── sample_1.expected   # 期待する出力
├── templates/
│   └── python.py          # 新しい問題用のテンプレート
├── test_samples.py        # 全問題をサンプルケースで検証する pytest
├── new.sh                 # 新しい問題のディレクトリを作る
└── test.sh                # pytest の薄いラッパー
```

## 使い方

新しい問題を始めるとき:

```bash
./new.sh abc464 c
# → contests/abc464/c/ に main.py と tests/ ができる
# 問題ページからサンプルをコピーして tests/sample_N.txt / sample_N.expected に貼る
```

テスト:

```bash
./test.sh contests/abc464/a   # 特定の問題だけ
./test.sh                     # 全問題
```

test.sh は pytest のラッパーなので、直接叩いても同じ:

```bash
uv run pytest -k abc464/a     # 特定の問題だけ
uv run pytest -k sample_2     # 特定のサンプルだけ
uv run pytest                 # 全部
```

手動で実行:

```bash
python3 contests/abc464/a/main.py < contests/abc464/a/tests/sample_1.txt
```

## テストの仕組み

`test_samples.py` が `contests/*/*/tests/sample_N.txt` を自動で見つけ、
それぞれを標準入力として `main.py` をサブプロセス実行し、
出力が `sample_N.expected` と一致するかを検証する
（`pytest.mark.parametrize` でサンプル1つ = テストケース1つになる）。

- 実行時間制限 2 秒（AtCoder の標準）を超えるとタイムアウトで落ちる
- 実行時エラー（exit code ≠ 0）は stderr 付きで失敗になる
- サンプルを追加したいときは `sample_4.txt` / `sample_4.expected` を置くだけ
