# A - Decisive Battle
# https://atcoder.jp/contests/abc464/tasks/abc464_a


def main() -> None:
    """東軍(E)と西軍(W)の兵力を比較し、多いほうの軍を出力する。"""
    record = input().strip()

    east_count = record.count("E")
    west_count = record.count("W")

    # 入力文字列の長さは奇数と保証されており E と W が同数になることはないため、
    # 東軍が多くなければ必ず西軍が多い。
    if east_count > west_count:
        print("East")
    else:
        print("West")


if __name__ == "__main__":
    main()
