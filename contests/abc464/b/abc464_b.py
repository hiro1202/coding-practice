# B - Crop
# https://atcoder.jp/contests/abc464/tasks/abc464_b


def main() -> None:
    """..."""
    # 高さ H・幅 W を取得

    # グリッド(各行の文字列)を H 行読み込む

    # 黒の範囲を表す 上端・下端・左端・右端 を初期化

    # 全マスを二重ループで走査し、'#' なら
    # 上=min, 下=max, 左=min, 右=max で範囲を更新

    # 上端〜下端の各行を、左端〜右端で切り出して出力


if __name__ == "__main__":
    main()
