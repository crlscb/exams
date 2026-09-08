"""
Write a function that rotates an array to the right by k positions.
Rotating to the right by k positions means that the last k elements
are moved to the beginning of the array.

"""


def twist_sequence(arr: list[int], k: int) -> list[int]:
    new_list = []
    i = 0

    if len(arr) == 0:
        return new_list

    k = k % len(arr)
    end = len(arr) - k

    while end < len(arr):
        new_list.append(arr[end])
        end += 1
    while i < len(arr) - k:
        new_list.append(arr[i])
        i += 1
    return new_list


if __name__ == "__main__":
    print(twist_sequence([1, 2, 3, 4, 5], 2))
    print(twist_sequence([1, 2, 3], 1))
    print(twist_sequence([1, 2, 3, 4], 0))
    print(twist_sequence([1, 2, 3], 5))
    print(twist_sequence([], 3))
