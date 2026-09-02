# B - Isolated Seats
# URL: https://atcoder.jp/contests/abc469/tasks/abc469_b
# 解説: https://atcoder.jp/contests/abc469/editorial/23758
# 実行: python3 contests/abc469/b/abc469_b.py < contests/abc469/b/tests/sample_1.txt
# 解答日: 2026.9.1
# 結果: AC
# 実行時間: 58 ms

N = int(input())
S = input()

pre = "x"
ans = 0

for i in range(N):
  if pre == "x" and S[i] == "x":
    # 最後の文字なら +1
    if i == N - 1:
      ans += 1
    # 最後以外なら次の文字が x だった場合 +1
    elif S[i + 1] == "x":
      ans += 1
  pre = S[i]

print(ans)
