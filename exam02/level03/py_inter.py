from termcolor import colored

"""
Write a function that returns a string containing the characters that appear
in both strings, without repetitions. The characters are added in the order
in which they appear in the first string.
"""


def inter(s1: str, s2: str) -> str:
    result = ""

    for char in s1:
        if char in s2:
            if char not in result:
                result += char
    return result


if __name__ == "__main__":
    tests = [
        (
            "hello", "world",
            "lo"
        ),
        (
            "banana", "band",
            "ban"
        ),
        (
            "abcabc", "bc",
            "bc"
        ),
        (
            "abc", "xyz",
            ""
        ),
        (
            "", "abc",
            ""
        )
    ]

    for s1, s2, expected in tests:
        result = inter(s1, s2)

        if result == expected:
            print(colored("PASS", "green"), f" '{s1}', '{s2}' -> '{result}'")
        else:
            print(colored("FAIL", "red"), f" '{s1}', '{s2}'")
            print("     Result:", result)
            print("     Expected:", expected)
