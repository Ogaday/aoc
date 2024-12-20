import re

prog = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")


def clean(memory: str) -> list[tuple[int, ...]]:
    """
    Examples
    --------
    >>> clean("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))")
    [(2, 4), (5, 5), (11, 8), (8, 5)]
    """
    return [tuple(map(int, match.groups())) for match in prog.finditer(memory)]


def solution(path):
    with open(path) as f:
        memory = f.read()

    factors = clean(memory=memory)
    return sum(a * b for a, b in factors)
