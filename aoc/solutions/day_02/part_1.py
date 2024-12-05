from itertools import pairwise

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


with open("inputs/day_02.txt") as f:
    reports = []
    for row in f.readlines():
        reports.append(list(map(int, row.split())))

print(sum(safe(report) for report in reports))
