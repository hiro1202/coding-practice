# C - Between P and Q
# URL: https://atcoder.jp/contests/abc468/tasks/abc468_c
# 実行: python3 contests/abc468/c/abc468_c.py < contests/abc468/c/tests/sample_1.txt

def permutations(arr):
    if len(arr) <= 1:
        yield list(arr)
        return
    for i in range(len(arr)):
        rest = arr[:i] + arr[i+1:]
        for tail in permutations(rest):
            yield [arr[i]] + tail


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

arr = list()

for n in range(1,  N + 1):
    arr.append(n)

ans = 0

for perm in permutations(arr):
    if P < perm < Q:
        ans += 1

print(ans)
