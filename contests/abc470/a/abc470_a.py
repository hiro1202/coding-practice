# A - Fizz
# URL: https://atcoder.jp/contests/abc470/tasks/abc470_a
# 実行: python3 contests/abc470/a/abc470_a.py < contests/abc470/a/tests/sample_1.txt
# 解答日: 2026.9.17
# 結果: AC
# 実行時間: 55ms

N = int(input())

for n in range(1, N + 1):
  if n % 3 == 0:
    print("Fizz")
  else:
    print(n)
