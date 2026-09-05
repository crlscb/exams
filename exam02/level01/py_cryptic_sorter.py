from termcolor import colored

"""
Write a function that sorts a list of strings using a three-level priority:

1. Primary: by length (ascending).
2. Secondary: lexicographically (alphabetical, case-insensitive, ascending).
3. Tertiary: by number of vowels (ascending, only if the length
and lexicographical order are the same).

The function must handle:
- Empty strings and empty lists.
- Mixed uppercase and lowercase letters (treat them as lowercase when sorting).
- Special characters (ignore them when counting vowels).

Forbidden functions: sorted(), list.sort()
"""


def cryptic_sorter(strings: list[str]) -> list[str]:
    disordered = True

    while disordered:
        disordered = False

        for i in range(len(strings) - 1):

            if len(strings[i]) > len(strings[i + 1]):
                strings[i], strings[i + 1] = strings[i + 1], strings[i]
                disordered = True

            elif len(strings[i]) == len(strings[i + 1]):
                if strings[i].lower() > strings[i + 1].lower():
                    strings[i], strings[i + 1] = strings[i + 1], strings[i]
                    disordered = True

                elif strings[i].lower() == strings[i + 1].lower():
                    if count_vowels(strings[i]) > count_vowels(strings[i + 1]):
                        strings[i], strings[i + 1] = strings[i + 1], strings[i]
                        disordered = True
    return strings


def count_vowels(string: str) -> int:
    vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú']
    count = 0

    for char in string:
        if char.lower() in vowels:
            count += 1
    return count


if __name__ == "__main__":
    tests = [
        (
            ["platano", "pera", "frambuesas", "uva"],
            ["uva", "pera", "platano", "frambuesas"]
        ),
        (
            ["b", "aaaa", "cc", "ddd"],
            ["b", "cc", "ddd", "aaaa"]
        ),
        (
            ["Zoo", "agua", "Casa", "mesa"],
            ["Zoo", "agua", "Casa", "mesa"]
        ),
        (
            ["", "a", "", "bb"],
            ["", "", "a", "bb"]
        ),
        (
            [],
            []
        ),
        (
            ["UVA", "uva", "Lua", "LUA"],
            ["Lua", "LUA", "UVA", "uva"]
        )
    ]

    for test, expected in tests:
        result = cryptic_sorter(test)

        if result == expected:
            print(colored("PASS", "green"), test, "->", result)
        else:
            print(colored("FAIL", "red"), test, "->", test)
            print("     Result:", result)
            print("     Expected:", expected)

    vowels_test = [
        ("murciélago", 5),
        ("MURCIÉLAGO", 5),
        ("c@#a!s$4a", 2),
        ("", 0),
        ("rhythm", 0)
    ]

    for test, expected in vowels_test:
        result = count_vowels(test)

        if result == expected:
            print(colored("PASS", "green"), test, "->", result)
        else:
            print(colored("FAIL", "red"), test)
            print("     Result:", result)
            print("     Expected:", expected)
