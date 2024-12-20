import re

prog = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|(don't\(\))|(do\(\))")


def solution(path):
    with open(path) as f:
        memory = f.read()

    enabled = True
    factors = []
    for match in prog.finditer(memory):
        a, b, dont, do = match.groups()
        if dont:
            enabled = False
        elif do:
            enabled = True
        elif enabled and a and b:
            factors.append((int(a), int(b)))

    return sum(a * b for a, b in factors)
