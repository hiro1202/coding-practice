# C - Cantrip
# URL: https://atcoder.jp/contests/abc469/tasks/abc469_c
# 解説: https://atcoder.jp/contests/abc469/editorial/23762
# 実行: python3 contests/abc469/c/abc469_c.py < contests/abc469/c/tests/sample_1.txt
# 解答日: 2026.9.3
# 結果: TLE
# 実行時間: > 2000 ms

N = int(input())
S = input()

for i in range(N):
    ans = 0
    atari = 0
    for j in range(N):
        # J = i まで当たりをカウント
        if j <= i:
            if S[j] == "o":
                ans += 1
                atari += 1
            else:
                ans += 1
            continue
        # J > i 以降は当たりを増減しながら当たりがゼロになるまでお菓子を食べる
        if S[j] == "o":
            ans += 1
        else:
            ans += 1
            atari -= 1
        # 当たりが無くなったらループを抜けて食べたお菓子の数を出力
        if atari == 0:
            break
    print(ans)
