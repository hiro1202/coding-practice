#!/usr/bin/env bash
# Usage: ./new.sh abc464 c
# 新しい問題のディレクトリを作り、解答テンプレートとテストのひな形を配置する。
set -euo pipefail

cd "$(dirname "$0")"

contest="${1:?usage: ./new.sh <contest> <problem>}"
problem="${2:?usage: ./new.sh <contest> <problem>}"
dir="contests/$contest/$problem"

if [ -e "$dir/main.py" ]; then
    echo "error: $dir/main.py は既に存在します" >&2
    exit 1
fi

mkdir -p "$dir/tests"
cp templates/python.py "$dir/main.py"
cp templates/test_python.py "$dir/test_main.py"

echo "created: $dir"
echo "次にやること (TDD):"
echo "  1. $dir/test_main.py に問題ページのサンプルをテストとして写す (RED)"
echo "  2. $dir/main.py の solve() を実装してテストを通す (GREEN)"
echo "  3. $dir/tests/ に sample_N.txt / sample_N.expected を置いて e2e も確認"
echo "  実行: uv run pytest $dir"
