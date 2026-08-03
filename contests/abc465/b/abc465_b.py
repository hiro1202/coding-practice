# B - Parking 2
# URL: https://atcoder.jp/contests/abc465/tasks/abc465_b
# 実行: python3 contests/abc465/b/abc465_b.py < contests/abc465/b/tests/sample_1.txt 

X, Y, L, R, A, B = map(int, input().split())

a_b = []

for t in range(A + 1, B + 1):
    a_b.append(t)

cost = 0

for t in a_b:
    if t >= L + 1 and t <= R:
        cost += X
    else:
        cost += Y

print(cost)
