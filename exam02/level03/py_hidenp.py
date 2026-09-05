from termcolor import colored
"""
Write a function that checks whether the string 'small' is a
subsequence of 'big'. A subsequence means that all characters in 'small'
appear in 'big' in the same order, but not necessarily consecutively.
The function is case-sensitive.
"""


def hidenp(small: str, big: str) -> bool:
    i = 0

    if len(small) < 1:
        return True

    for char in big:
        if small[i] == char:
            i += 1
            if i == len(small):
                return True

    return False


if __name__ == "__main__":
    tests = [
        (
            "abc", "a1b2c3",
            True
        ),
        (
            "ace", "abcde",
            True
        ),
        (
            "aec", "abcde",
            False
        ),
        (
            "", "abc",
            True
        ),
        (
            "abc", "ab",
            False
        ),
        (
            "aaaa", "aaa",
            False
        ),
        (
            "sing", "subsequence testing",
            True
        )
    ]

    for small, big, expected in tests:
        result = hidenp(small, big)

        if result == expected:
            print(colored("PASS", "green"), small, big, "->", result)
        else:
            print(colored("FAIL", "red"), small, big)
            print("     Result:", result)
            print("     Expected:", expected)
