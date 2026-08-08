# C - Reverse Permutation
# URL: https://atcoder.jp/contests/abc465/tasks/abc465_c
# 実行: python3 contests/abc465/c/abc465_c.py < contests/abc465/c/tests/sample_1.txt

N = int(input())
S = input()

# A=(1,2,…,N) を作成
A = []

for n in range(1, N + 1):
    A.append(n)

# 並べ替え
for i, s in enumerate(S):
    if s == "o":
        A = A[0:i + 1][::-1] + A[i + 1:]

print(A)
