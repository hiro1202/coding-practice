# C - Plumage Palette
# URL: https://atcoder.jp/contests/abc464/tasks/abc464_c
# 解説: https://atcoder.jp/contests/abc464/editorial/22255
# 実行: python3 contests/abc464/c/abc464_c.py < contests/abc464/c/tests/sample_1.txt
# 解答日: 2026.9.23
# 結果: AC
# 実行時間: 799 ms
# メモリ: 118080 KiB
# メモ: 解説をもとにAIにて生成

import sys
from collections import defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())  # 何羽, 何日

cnt = defaultdict(int)  # 色 -> その色の鳥の数
kinds = 0               # 現在の色の種類数
events = [[] for _ in range(M + 1)]  # events[d] = d日目に起こる (旧色, 新色)

for _ in range(N):
    A, D, B = map(int, input().split())
    # 初期状態として色Aの鳥を追加
    if cnt[A] == 0:
        kinds += 1
    cnt[A] += 1
    events[D].append((A, B))

ans = []
for d in range(1, M + 1):
    for a, b in events[d]:
        # 色Aの鳥を1羽削除
        cnt[a] -= 1
        if cnt[a] == 0:
            kinds -= 1
        # 色Bの鳥を1羽追加
        if cnt[b] == 0:
            kinds += 1
        cnt[b] += 1
    ans.append(kinds)

print("\n".join(map(str, ans)))
