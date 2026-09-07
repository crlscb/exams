"""
Write a function that checks whether two strings are anagrams.

They must contain exactly the same letters in the same quantities,
ignoring uppercase/lowercase and spaces.
"""


def anagram(s1: str, s2: str) -> bool:
    i = 0
    found = []
    s1_clean = ""
    s2_clean = ""

    for char in s1:
        if char != " ":
            s1_clean += char.lower()
    for char in s2:
        if char != " ":
            s2_clean += char.lower()

    while i < len(s1_clean):
        if s1_clean[i] not in found:
            if (
                len(s1_clean) == len(s2_clean) and
                s1_clean.count(s1_clean[i]) ==
                s2_clean.count(s1_clean[i])
            ):
                found.append(s1_clean[i])
            else:
                return False
        i += 1
    return True


if __name__ == "__main__":
    print(anagram("hello", "olleh"))
    print(anagram("listen", "silent"))
    print(anagram("rail safety", "fairy tales"))
    print(anagram("hello", "world"))
    print(anagram("hello", "helloo"))
    print(anagram("aab", "abb"))
    print(anagram("Hello", "olleh"))
    print(anagram("", ""))
