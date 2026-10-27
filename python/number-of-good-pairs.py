# Problem link(https://leetcode.com/problems/number-of-good-pairs/description/)

# 与えられた配列の数値から同じ数値のペア数を返す
def search_number_good_pairs(nums: list[int]):
    
    length: int = len(nums)
    result: int = 0

    # 配列を最初の位置から取得し、取得した数値と他の数値を比較する
    for i in range(length):
        for j in range(i + 1, length):
            if nums[i] == nums[j]:
                result += 1

    return result

def main() -> None:

    nums: list[int] = [1, 2, 3, 1, 1, 3]
    output: int = search_number_good_pairs(nums)

    print(output)


if __name__=="__main__":
    main()

