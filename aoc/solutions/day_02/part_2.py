from itertools import pairwise
from typing import Generator


def safe(report: list[int]) -> bool:
    ascending = False
    descending = False
    for a, b in pairwise(report):
        if b > a:
            ascending = True
        elif b < a:
            descending = True
        diff = abs(b - a)
        if (ascending and descending) or (diff < 1 or diff > 3):
            return False
    return True


def subsets(report: list[int]) -> Generator[list[int], None, None]:
    """
    Examples
    --------
    >>> for subset in subsets([0, 1, 2, 3, 4]):
    ...     print(subset)
    [1, 2, 3, 4]
    [0, 2, 3, 4]
    [0, 1, 3, 4]
    [0, 1, 2, 4]
    [0, 1, 2, 3]
    """
    for i in range(len(report)):
        yield report[:i] + report[i + 1 :]


def safe_with_backup(report: list[int]) -> bool:
    if safe(report):
        return True
    for subset in subsets(report):
        if safe(subset):
            return True
    return False


def solution(input_path):
    with open(input_path) as f:
        reports = []
        for row in f.readlines():
            reports.append(list(map(int, row.split())))

    print(sum(safe_with_backup(report) for report in reports))
