# B - Parking 2
# URL: https://atcoder.jp/contests/abc465/tasks/abc465_b
# 実行: python3 contests/abc465/b/abc465_b.py < contests/abc465/b/tests/sample_1.txt 

X, Y, L, R, A, B = map(int, input().split())

cost = 0

# 経過時間で計算するため A + 1 時から B 時までで計算する
for t in range(A + 1, B + 1):
    if L + 1 <= t <= R:
        cost += X
    else:
        cost += Y

print(cost)
