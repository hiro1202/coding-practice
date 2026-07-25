# A - Obesity
# https://atcoder.jp/contests/abc467/tasks/abc467_a


def main() -> None:
    """..."""
    H, W = map(int, input().split())

    # BMI = W / (H/100)^2 >= 25 を判定したいが、H/100 は float になり誤差が出るため下記で判定
    ok = W * 10000 >= 25 * H * H

    print("Yes" if ok else "No")

if __name__ == "__main__":
    main()
