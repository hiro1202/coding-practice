# C - Plumage Palette
# URL: https://atcoder.jp/contests/abc464/tasks/abc464_c
# 実行: python3 contests/abc464/c/abc464_c.py < contests/abc464/c/tests/sample_1.txt
# 解答日: 2026.9.19
# 結果: TLE
# 実行時間: > 2000 ms
# メモリ: 68156 KiB

N, M = map(int, input().split()) # 何羽, 何日

lst = []
for i in range(N):
    A, D, B = map(int, input().split())
    lst.append([A, D, B])

for d in range(1, M + 1):
    result = []
    for l in lst:
        if l[1] <= d:
            if l[2] not in result:
                result.append(l[2])
        else:
            if l[0] not in result:
                result.append(l[0])

    print(len(result))
