"""
Write a function that merges two sorted lists into a single sorted list.
"""


def shadow_merge(list1: list[int], list2: list[int]) -> list[int]:
    new_list = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            new_list.append(list1[i])
            i += 1
        else:
            new_list.append(list2[j])
            j += 1

    while i < len(list1):
        new_list.append(list1[i])
        i += 1
    while j < len(list2):
        new_list.append(list2[j])
        j += 1

    return new_list


if __name__ == "__main__":
    print(shadow_merge([1, 3, 5], [2, 4, 6]))
    print(shadow_merge([1, 2, 3], [4, 5, 6]))
    print(shadow_merge([1], [2, 3, 4]))
    print(shadow_merge([], [1, 2, 3]))
    print(shadow_merge([1, 1, 2], [1, 3, 3]))
