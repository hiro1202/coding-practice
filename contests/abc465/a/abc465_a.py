# A - Supermajority
# https://atcoder.jp/contests/abc465/tasks/abc465_a

A, B = map(int, input().split())

f = False

if A * 3 > B * 2:
    f = True

print("Yes" if f == True else "No")
