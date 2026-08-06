# C - Reverse Permutation
# URL: https://atcoder.jp/contests/abc465/tasks/abc465_c
# 実行: python3 contests/abc465/c/abc465_c.py < contests/abc465/c/tests/sample_1.txt

N = int(input())
S = input()

A = []

for n in range(1, N + 1):
    A.append(n)

for s in S:
    if s == "o":
        # 反転する
        print(A)
