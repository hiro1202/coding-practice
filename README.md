# coding-practice

コーディング練習用リポジトリ。Python 3.12+ / [uv](https://docs.astral.sh/uv/)。

```
contests/abc464/a/
├── abc464_a.py       # 解答（リポジトリ全体で一意な名前にする）
├── test_abc464_a.py  # テスト
└── tests/            # サンプル入出力 (sample_1.txt / sample_1.expected)
```

```bash
python3 contests/abc464/a/abc464_a.py < contests/abc464/a/tests/sample_1.txt
uv run pytest                     # 全問題
uv run pytest contests/abc464/a   # 特定の問題
```
