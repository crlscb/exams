"""
Write a function that counts how many consecutive pairs of valid digits
there are in a string.

A valid pair is two adjacent digits where the second is exactly one greater
than the first.

A 9 followed by 0 is NOT a valid pair.
"""


def pattern_tracker(text: str) -> int:
    i = 0
    count = 0
    while i < len(text) - 1:
        if text[i].isdigit() and text[i + 1].isdigit():
            if int(text[i + 1]) - int(text[i]) == 1:
                count += 1
        i += 1
    return count


if __name__ == "__main__":
    print(pattern_tracker("123"))
    print(pattern_tracker("12a34"))
    print(pattern_tracker("987654321"))
    print(pattern_tracker("01234567"))
    print(pattern_tracker("abc"))
    print(pattern_tracker("1a2b3c4"))
    print(pattern_tracker("112233"))
