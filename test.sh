#!/usr/bin/env bash
# Usage: ./test.sh contests/abc464/a
# Runs main.py against every tests/sample_N.txt and diffs with sample_N.expected
set -euo pipefail

dir="${1:?usage: ./test.sh <problem-dir>}"
prog="$dir/main.py"
pass=0
fail=0

for in_file in "$dir"/tests/sample_*.txt; do
    [ -e "$in_file" ] || { echo "no test files in $dir/tests"; exit 1; }
    exp_file="${in_file%.txt}.expected"
    got="$(python3 "$prog" < "$in_file")"
    want="$(cat "$exp_file")"
    name="$(basename "$in_file" .txt)"
    if [ "$got" = "$want" ]; then
        echo "PASS $name"
        pass=$((pass + 1))
    else
        echo "FAIL $name"
        echo "  input:    $(tr '\n' ' ' < "$in_file")"
        echo "  expected: $want"
        echo "  got:      $got"
        fail=$((fail + 1))
    fi
done

echo "----"
echo "$pass passed, $fail failed"
[ "$fail" -eq 0 ]
