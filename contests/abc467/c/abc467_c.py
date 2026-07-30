# C - Adjacent Sums (easy)
# https://atcoder.jp/contests/abc467/tasks/abc467_c


def main() -> None:
    """..."""
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    candidates = []

    # 操作回数 = 0 で初期化
    # (A[i] + A[i + 1]) % M = B[i] の判定をする
    # False なら操作回数に 1 を足す（A[i] に 1 を足す操作が必要になるため）
    # これを最後まで回して、操作回数を出力する

if __name__ == "__main__":
    main()
