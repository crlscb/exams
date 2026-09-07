"""
Write a function that determines whether two strings
are permutations of each other.
Two strings are permutations if they contain the same characters
with the same frequencies.

The function must:

Check that both strings contain exactly the same characters
Count frequencies (case-sensitive)
Return True if they are permutations, False otherwise
Handle empty strings (two empty strings are permutations)
Treat spaces and punctuation as normal characters

"""


def string_permutation_checker(s1: str, s2: str) -> bool:
    i = 0
    found = []

    while i < len(s1):
        if s1[i] not in found:
            if len(s1) == len(s2) and s1.count(s1[i]) == s2.count(s1[i]):
                found.append(s1[i])
            else:
                return False
        i += 1
    return True


if __name__ == "__main__":
    print(string_permutation_checker("abc", "cba"))
    print(string_permutation_checker("abc", "def"))
    print(string_permutation_checker("listen", "silent"))
    print(string_permutation_checker("hello", "bello"))
    print(string_permutation_checker("", ""))
    print(string_permutation_checker("a", ""))
    print(string_permutation_checker("Abc", "abc"))
    print(string_permutation_checker("a gentleman", "elegant man"))
