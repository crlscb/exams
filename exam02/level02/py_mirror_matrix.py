from termcolor import colored

"""
Write a function that horizontally mirrors a 2D matrix by reversing each row.

The function must:

Take a 2D list (matrix) of integers as input
Return a new 2D list where each row is horizontally reversed
Handle matrices of any size (square or rectangular)
Preserve the original order of the rows
Not modify the original matrix
"""


def mirror_matrix(matrix: list[list[int]]) -> list[list[int]]:
    new_matrix = []

    for row in matrix:
        new_matrix.append(row[::-1])

    return new_matrix


if __name__ == "__main__":
    tests = [
        (
            [[1, 2, 3], [4, 5, 6]],
            [[3, 2, 1], [6, 5, 4]]
        ),
        (
            [[2, 1], [3, 4], [5, 6]],
            [[1, 2], [4, 3], [6, 5]]
        ),
        (
            [[7]],
            [[7]]
        ),
        (
            [[1, 2, 3, 4]],
            [[4, 3, 2, 1]]
        ),
        (
            [[-1, -2], [-3, -4]],
            [[-2, -1], [-4, -3]]
        )
    ]

    for matrix, expected in tests:
        result = mirror_matrix(matrix)

        if result == expected:
            print(colored("PASS", "green"), matrix, "->", result)
        else:
            print(colored("FAIL", "red"), matrix)
            print("     Result:", result)
            print("     Expected:", expected)
