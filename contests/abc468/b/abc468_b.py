# B - Corridor Watch
# URL: https://atcoder.jp/contests/abc468/tasks/abc468_b
# 実行: python3 contests/abc468/b/abc468_b.py < contests/abc468/b/tests/sample_1.txt

M, D = map(int, input().split())
S = input()

ans = 0

for i, s in enumerate(S):
    if s == "G":
        continue

    flg = True

    # ±D の範囲内に G があれば False
    for j in range(-D, D + 1):
        # インデックスエラーを回避
        if i + j < 0 or i + j >= M:
            continue

        if S[i + j] == "G":
            flg = False

    if flg == True:
        ans += 1

print(ans)
