#!/usr/bin/env bash
# Usage: ./run_samples.sh contests/abc464/a

# -e: コマンドが失敗したら即終了 / -u: 未定義変数の参照をエラーに
# -o pipefail: パイプの途中で失敗しても検知する
set -euo pipefail

# 第1引数(問題ディレクトリ)。未指定なら usage を表示して終了する
dir="${1:?usage: $0 <problem-dir>}"

# 問題ディレクトリ直下の .py から test_*.py を除いたもの = 解答ファイル
solution=$(find "$dir" -maxdepth 1 -name '*.py' ! -name 'test_*')

# 終了コード。1つでも FAIL したら 1 にする
status=0

# tests/ 内のサンプル入力を順に処理する
for input in "$dir"/tests/sample_*.txt; do
    # 期待値ファイルの中身。${input%.txt} は末尾の .txt を削った文字列
    expected=$(cat "${input%.txt}.expected")

    # サンプルを標準入力に流して解答を実行し、出力を受け取る
    # $(...) が末尾の改行を削るので、改行の有無の差は自動で正規化される
    actual=$(python3 "$solution" < "$input")

    # ${input##*/} はパスからファイル名だけを取り出す(basename 相当)
    if [[ "$actual" == "$expected" ]]; then
        echo "PASS ${input##*/}"
    else
        echo "FAIL ${input##*/}: expected [$expected] actual [$actual]"
        status=1
    fi
done

# 全 PASS なら 0、FAIL ありなら 1 を返す(CI や && 連結で使える)
exit "$status"
