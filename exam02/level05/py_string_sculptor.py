"""
Write a function that transforms a string by alternating uppercase
and lowercase only for alphabetic characters.

All other characters remain unchanged and do not count toward the alternation.

The first alphabetic character must be lowercase, the second uppercase,
the third lowercase, and so on.

Spaces reset the alternation
(the next letter after a space becomes lowercase again).
"""


def string_sculptor(text: str) -> str:
    i = 0
    result = ""
    count = 0

    while i < len(text):
        if text[i].isalpha():
            if count % 2 == 0:
                result += text[i].lower()
                count += 1
            else:
                result += text[i].upper()
                count += 1
        elif text[i] == " ":
            result += text[i]
            count = 0
        else:
            result += text[i]
        i += 1
    return result


if __name__ == "__main__":
    print(string_sculptor("hello"))
    print(string_sculptor("Hello World"))
    print(string_sculptor("abc123def"))
    print(string_sculptor("Python3.9!"))
    print(string_sculptor(""))
