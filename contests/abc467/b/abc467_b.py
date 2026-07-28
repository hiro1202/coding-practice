# B - Keep the Change
# https://atcoder.jp/contests/abc467/tasks/abc467_b


def main() -> None:
    """..."""
    n = int(input())

    ans = 0

    for _ in range(n):
        A, B, S = input().split()
        if S == "keep":
            ans += int(B) - int(A)

    print(ans)


if __name__ == "__main__":
    main()
