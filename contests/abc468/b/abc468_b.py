# B - Corridor Watch
# URL: https://atcoder.jp/contests/abc468/tasks/abc468_b
# 実行: python3 contests/abc468/b/abc468_b.py < contests/abc468/b/tests/sample_1.txt

M, D = map(int, input().split())
S = input()

ans = 0

for i in range(M):
    # G を探す範囲を定める
    # 0 以上、M - 1 以下にすることでインデックスエラーを回避
    left = max(0, i - D)
    right = min(M - 1, i + D)

    watched = False

    # ±D の範囲内に G があれば True
    for j in range(left, right + 1):
        if S[j] == "G":
            watched = True
            break

    if not watched:
        ans += 1

print(ans)
