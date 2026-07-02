#!/usr/bin/env bash
# Usage: ./new.sh abc464 c
# 新しい問題のディレクトリを作り、テンプレートを配置する。
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

echo "created: $dir"
echo "次にやること:"
echo "  1. $dir/tests/ に sample_1.txt / sample_1.expected を置く"
echo "  2. $dir/main.py を解く"
echo "  3. ./test.sh $dir でテスト"
