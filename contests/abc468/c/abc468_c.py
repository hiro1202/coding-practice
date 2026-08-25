# C - Between P and Q
# URL: https://atcoder.jp/contests/abc468/tasks/abc468_c
# 実行: python3 contests/abc468/c/abc468_c.py < contests/abc468/c/tests/sample_1.txt
# 解答日: 2026.8.23
# 結果: AC
# 実行時間: 170 ms

from itertools import permutations

N = int(input())
# permutations はタプルを返すので、比較相手の P, Q もタプルにしておく
# （list と tuple は < で比較できずエラーになる）
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

ans = 0
for perm in permutations(range(1, N + 1)):  # [1, 2, ..., N] の並べ替えを辞書順に生成
    if P < perm < Q:
        ans += 1

print(ans)
