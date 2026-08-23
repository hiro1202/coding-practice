# C - Between P and Q
# URL: https://atcoder.jp/contests/abc468/tasks/abc468_c
# 実行: python3 contests/abc468/c/abc468_c_slow.py < contests/abc468/c/tests/sample_1.txt
# 解答日: 2026.8.23
# 結果: AC
# 実行時間: 1918 ms（自作の再帰 permutations 版。itertools 版の abc468_c.py より約6倍遅い）

def permutations(arr):
    """arr の並べ替えを1つずつ返す"""
    # 終了条件: 0〜1個なら並べ替えようがないので1通りだけ返す
    if len(arr) <= 1:
        yield list(arr)  # yield: 1個返すが関数は終わらない
        return

    for i in range(len(arr)):  # 先頭に置く要素を1つずつ入れ替える
        # i番目を抜いた残りのリストを作成
        rest = arr[:i] + arr[i + 1:]

        for tail in permutations(rest):  # 残りを再帰で並べ替え
            yield [arr[i]] + tail


N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

arr = list(range(1, N + 1))  # [1, 2, ..., N]

ans = 0
for perm in permutations(arr):
    # リストの < は辞書順比較（左から比べて最初に差がついた所で決まる）
    if P < perm < Q:
        ans += 1

print(ans)
