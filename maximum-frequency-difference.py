# Input: nums = [1, 2, 3, 2, 1]
# Output: 4
def get_maximum_frequency(nums: list[int]):

    # ループで差分を求め、絶対値を管理
    count_list: list[int] = []

    # 要素数の確認
    # 基本的なことが抜けていて、インデックスの位置は要素数 - 1
    # print(len(nums), len(nums) - 1)
    for i in range(len(nums) - 1):
        count_list.append(abs(nums[i] - nums[i + 1]))

    """
    # このループだと期待値と異なる
    for i in range(len(count_list) - 1):
        if count_list[i] == count_list[i + 1]:
            count += 1
    """
    # ハッシュテーブルを使う
    count_hash: dict[int, int] = {}

    # 差分をキー、カウントをValueとする
    for diffence in count_list:
        # print(count_hash.get(diffence))
        count_hash[diffence] = count_hash.get(diffence, 0) + 1

    return max(count_hash.values(), default=0)


def main() -> None:
    nums = [1, 2, 3, 2, 1]

    result: int = get_maximum_frequency(nums)
    print(result)


if __name__ == "__main__":
    main()
