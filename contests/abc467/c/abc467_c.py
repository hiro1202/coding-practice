# C - Adjacent Sums (easy)
# https://atcoder.jp/contests/abc467/tasks/abc467_c


def main() -> None:
    """..."""
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    candidates = []

    # 先頭を操作するパターンと操作しないパターンでそれぞれ操作回数を算出する
    for add in range(M):
        A2 = A[:]
        # 先頭に 1 を足すとき、操作回数に 1 を足す
        A2[0] += add
        count = add

        # 左から順に検証する
        for i in range(N - 1):
            if (A2[i] + A2[i + 1]) % M != B[i]:
                # 数値が合わない場合は操作
                A2[i + 1] += 1
                count += 1
        candidates.append(count)

    # 操作回数が少ない方を出力する
    print(min(candidates))


if __name__ == "__main__":
    main()
