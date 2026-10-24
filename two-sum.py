# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Input: nums = [3,3], target = 6
# Output: [0,1]
def get_index_of_two_sum(nums: list[int], target: int) -> list[int]:

    # 二重ループで記載する
    for f in range(len(nums)):
        # ここの内部ループの処理がわからなかった
        for s in range(f + 1, len(nums)):
            if nums[f] + nums[s] == target:
                return [f, s]

    return []


def __main__():
    #  nums: list[int] = [2, 7, 11, 15]
    nums: list[int] = [3, 2, 4]
    target: int = 9

    result: list[int] = get_index_of_two_sum(nums, target)

    print(result)


if __name__ == "__main__":
    __main__()

