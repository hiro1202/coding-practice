#!/usr/bin/env bash
# Usage: ./test.sh [contests/abc464/a]
# 引数なしなら全問題、問題ディレクトリを渡すとその問題だけテストする。
# 実体は pytest なので、直接 `uv run pytest -k abc464/a` でも同じ。
set -euo pipefail

cd "$(dirname "$0")"

if [ $# -eq 0 ]; then
    exec uv run pytest
fi

dir="${1%/}"            # 末尾の / を除去
dir="${dir#contests/}"  # contests/ プレフィックスを除去 (abc464/a 形式でも渡せる)
exec uv run pytest -k "$dir"
