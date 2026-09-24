# C - Plumage Palette
# URL: https://atcoder.jp/contests/abc464/tasks/abc464_c
# 解説: https://atcoder.jp/contests/abc464/editorial/22255
# 実行: python3 contests/abc464/c/abc464_c.py < contests/abc464/c/tests/sample_1.txt
# 解答日: 2026.9.24
# 結果: AC
# 実行時間: 585 ms
# メモリ: 110040 KiB
# メモ: 解説をもとにAIにて生成

import sys

# 以降のinput()をreadlineに差し替え（読むのは呼んだ時）。余計な処理がない分速い
input = sys.stdin.readline

N, M = map(int, input().split())  # 何羽, 何日

# 色ごとの鳥の数。毎日数え直すとO(NM)でTLEなので差分で更新する
# [0] * 4 → [0, 0, 0, 0]（0が4個並んだリスト）。色は1〜NなのでN+1個作り、添字=色で使う
cnt = [0] * (N + 1)
# 色の種類数。cntが0↔1をまたぐ時だけ増減すればいい
kinds = 0
# events[d] = d日目の(旧色, 新色)。日付でバケツ分けすればソート不要
# M=3 → [[], [], [], []]（空リストが4個）。[[]] * 4 だと全部同じリストを共有するので内包表記で作る
events = [[] for _ in range(M + 1)]

for _ in range(N):
    A, D, B = map(int, input().split())
    # 初日前の状態を作る
    if cnt[A] == 0:
        kinds += 1
    cnt[A] += 1
    events[D].append((A, B))
# sample_1 だとループ後はこうなる
# cnt    = [0, 1, 1, 1, 1, 1, 1]（色1〜6が1羽ずつ）
# kinds  = 6
# events = [[], [(4, 6)], [], [(1, 2), (3, 5), (6, 6)], [], [(5, 1)], [(2, 5)], []]

ans = []
for d in range(1, M + 1):
    # その日に変わる鳥だけ処理するので全体でO(N+M)
    for a, b in events[d]:
        # 色変化 = aを1羽削除 + bを1羽追加（a==bでも元に戻るので場合分け不要）
        cnt[a] -= 1
        if cnt[a] == 0:
            kinds -= 1
        if cnt[b] == 0:
            kinds += 1
        cnt[b] += 1
    ans.append(kinds)

# printを毎回呼ぶと遅いので1回でまとめて出力
print("\n".join(map(str, ans)))
