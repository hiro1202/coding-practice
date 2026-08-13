# A - Maximal Value
# URL: https://atcoder.jp/contests/abc468/tasks/abc468_a
# 実行: python3 contests/abc468/a/abc468_a.py < contests/abc468/a/tests/sample_1.txt

N = int(input())
A = list(map(int, input().split()))

c = 0

for i in range(N - 2):
    if A[i] < A[i + 1] > A[i + 2]:
        c += 1

print(c)
