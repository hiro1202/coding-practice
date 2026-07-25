# B - Crop
# https://atcoder.jp/contests/abc464/tasks/abc464_b


def main() -> None:
    """..."""
    # 高さ H・幅 W を取得
    H, W = map(int, input().split())

    # 各行の文字列を H 行読み込む
    # 内包表記は下の for ループを 1 行にまとめたもの
    #   C = []                   # 空の list を初期化
    #   for _ in range(H):
    #       C.append(input())    # list に 1 行ずつ追加
    C = [input() for _ in range(H)]

    # 黒の範囲を表す 上端・下端・左端・右端 を初期化
    u, d = H, -1
    l, r = W, -1

    # 全マスを二重ループで走査し、'#' なら
    # 上=min, 下=max, 左=min, 右=max で範囲を更新
    for i in range(H):
        for j in range(W):
            if C[i][j] == "#":
                u, d = min(i, u), max(i, d)
                l, r = min(j, l), max(j, r)

    # 上端〜下端の各行を、左端〜右端で切り出して出力
    for i in range(u, d + 1):
        print(C[i][l: r + 1])


if __name__ == "__main__":
    main()
