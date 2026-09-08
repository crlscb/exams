"""
Write a function that creates a simple cipher by shifting
the letters of a string by a given amount.
Non-alphabetic characters must remain unchanged.
"""


def whisper_cipher(text: str, shift: int) -> str:
    new_text = ""
    i = 0

    while i < len(text):
        if text[i].isalpha():
            if text[i].islower():
                new_text += chr(
                    (ord(text[i]) - ord("a") + shift) % 26 + ord("a")
                )
            else:
                new_text += chr(
                    (ord(text[i]) - ord("A") + shift) % 26 + ord("A")
                )
        else:
            new_text += text[i]
        i += 1
    return new_text


if __name__ == "__main__":
    print(whisper_cipher("hello", 3))
    print(whisper_cipher("Hello World!", 1))
    print(whisper_cipher("xyz", 3))
    print(whisper_cipher("ABC123def", 5))
    print(whisper_cipher("", 10))
    print(whisper_cipher("abc", -3))
