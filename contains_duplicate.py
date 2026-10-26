# Input: nums = [1, 2, 3, 1]
# Output: true
def check_duplicate(nums: list[int]) -> bool:

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True

    return False


def __main__() -> None:

    input: list[int] = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    output: bool = check_duplicate(input)

    print(output)


def __init__():
    __main__()


if __name__ == "__main__":
    __main__()
