"""
Write a function that converts a number from one base to another.

It supports bases from 2 to 36 inclusive,
using digits 0-9 and letters A-Z for values 10-35.

Return "ERROR" if the input is invalid (base or digits).
"""


def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if from_base < 2 or from_base > 36 or to_base < 2 or to_base > 36:
        return "ERROR"
    decimal = 0
    result = ""
    for char in number:
        i = 0
        found = False

        for digit in digits:
            if digit == char:
                value = i
                found = True

                if value >= from_base:
                    return "ERROR"

                decimal = decimal * from_base + value

            i += 1
        if not found:
            return "ERROR"

    if decimal == 0:
        return "0"

    while decimal > 0:
        remainder = decimal % to_base
        char = digits[remainder]
        result = char + result
        decimal = decimal // to_base
    return result


if __name__ == "__main__":
    print(number_base_converter("1010", 2, 10))
    print(number_base_converter("FF", 16, 10))
    print(number_base_converter("255", 10, 16))
    print(number_base_converter("123", 10, 2))
    print(number_base_converter("Z", 36, 10))
    print(number_base_converter("35", 10, 36))
    print(number_base_converter("123", 1, 10))
    print(number_base_converter("G", 16, 10))
