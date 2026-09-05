from termcolor import colored

"""
Write a function that checks whether a string is a palindrome,
ignoring spaces and uppercase/lowercase, and considering only
alphabetic characters in the comparison.
"""


def echo_validator(text: str) -> bool:
    letters = []

    for char in text:
        if char.isalpha():
            letters.append(char.lower())

    if letters != letters[::-1]:
        return False

    return True


if __name__ == "__main__":
    tests = [
        ("radar", True),
        ("hello", False),
        ("A man a plan a canal Panama", True),
        ("Race! Car", True),
        ("123", True),
        ("", True),
        ("Reconocer", True),
        ("House", False)
    ]

    for text, expected in tests:
        result = echo_validator(text)

        if result == expected:
            print(colored("PASS", "green"), f"'{text}' -> {result}")
        else:
            print(colored("FAIL", "red"), f"'{text}'")
            print("     Result:", result)
            print("     Expected:", expected)
