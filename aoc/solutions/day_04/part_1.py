from typing import TypeVar

arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

T = TypeVar("T")


def reverse(arr: list[list[T]]) -> list[list[T]]:
    """
    Examples
    --------
    >>> for row in reverse([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1]]):
    ...     print(row)
    [3, 2, 1, 0]
    [7, 6, 5, 4]
    [1, 0, 9, 8]
    """
    return [row[::-1] for row in arr]


def transpose(arr: list[list[T]]) -> list[list[T]]:
    """
    Examples
    --------
    >>> for row in transpose([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 0, 1]]):
    ...     print(row)
    [0, 4, 8]
    [1, 5, 9]
    [2, 6, 0]
    [3, 7, 1]
    """
    return list(list(row) for row in zip(*arr))


def left_diagonal(arr: list[list[T]]) -> list[list[T]]:
    new = []
    for i in range(len(arr) + len(arr[0]) - 1):
        row = []
        for j in range(i + 1):
            try:
                row.append(arr[j][i - j])
            except IndexError:
                pass
        new.append(row)
    return new


def right_diagonal(arr):
    return left_diagonal(reverse(arr))


def search(arr, word="XMAS"):
    return sum("".join(row).count(word) for row in arr)


def solution(path):
    with open(path) as f:
        arr = [list(row.strip()) for row in f.readlines()]

    count = (
        search(arr)
        + search(reverse(arr))
        + search(transpose(arr))
        + search(reverse(transpose(arr)))
        + search(left_diagonal(arr))
        + search(reverse(left_diagonal(arr)))
        + search(right_diagonal(arr))
        + search(reverse(right_diagonal(arr)))
    )

    return count
