# Input s : "leetcode"
# Output: {'l': 1, 'e': 3, 't': 1, 'c': 1, 'o': 1, 'd': 1}
# Input: s = ""
# Output: {}
def count_chars(s: str) -> dict[str, int]:

    chars_counter_dict: dict[str, int] = {}

    # 入力内容からKeyを作成、同じ値の場合は、カウントする
    for i in range(len(s)):
        if s[i] in chars_counter_dict:
            chars_counter_dict[s[i]] += 1

    return chars_counter_dict


def __main__() -> None:
    s: str = "leetcode"

    chars_counter_dict: dict[str, int] = count_chars(s)
    print(chars_counter_dict)


def __init__():
    __main__()


if __name__ == "__main__":
    __init__()