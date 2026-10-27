# example
# Input: nums = [1, 2, 3, 1]
# Output: True
# Input: nums = [1, 2, 3, 4, 5, 6]
# Output: False
def check_duplicate_number(nums: list[int]) -> bool:

    i: int = 0
    # 1要素ずつ捜査して線形探索
    for number in range(nums[i]):
        for j in range(nums[i + 1]):
            if i == j:
                return True
            else:
                i += 1

    return False


def __main__():
    Input: list[int] = [1, 2, 3, 4]
    Output = check_duplicate_number(Input)
    print(Output)


def __init__():
    __main__()


if __name__ == "__main__":
    __main__()

