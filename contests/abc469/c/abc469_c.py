# C - Cantrip
# URL: https://atcoder.jp/contests/abc469/tasks/abc469_c
# 解説: https://atcoder.jp/contests/abc469/editorial/23762
# 実行: python3 contests/abc469/c/abc469_c.py < contests/abc469/c/tests/sample_1.txt
# 解答日: 2026.9.9
# 結果: AC
# 実行時間: 164 ms

import sys

# 前提1：x の総数 < k のとき、すべてのお菓子を食べることができる
# 前提2：k 個目の x の位置までお菓子を食べることができる

data = sys.stdin.read().split()
N = int(data[0])
S = data[1]

# x の位置をリスト化
# 例：xoxx -> [1, 3, 4]
# 　　k = 1 なら 1 つ、K = 2 なら 3 つお菓子を食べることができる
xs = [i + 1 for i, c in enumerate(S) if c == "x"]  
M = len(xs)  # x の総数

ans = []
for k in range(1, N + 1):
    if M < k:
        ans.append(N)          # 前提1
    else:
        ans.append(xs[k - 1])  # 前提2

# print を N 回呼ぶと遅いので、改行コードを入れて出力を1回にまとめる
# write() は末尾に改行コードがつかないためつける
# join() は str でないと TypeError になるため str に変換
sys.stdout.write("\n".join(map(str, ans)) + "\n")
