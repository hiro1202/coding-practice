# coding-practice

コーディング練習用リポジトリ。

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
└── test.sh                # サンプルケースで解答をテストする
```

## 使い方

新しい問題を始めるとき:

```bash
mkdir -p contests/<contest>/<problem>/tests
cp templates/python.py contests/<contest>/<problem>/main.py
# tests/sample_N.txt と tests/sample_N.expected にサンプルを置く
```

サンプルケースでテスト:

```bash
./test.sh contests/abc464/a
```

手動で実行:

```bash
python3 contests/abc464/a/main.py < contests/abc464/a/tests/sample_1.txt
```
