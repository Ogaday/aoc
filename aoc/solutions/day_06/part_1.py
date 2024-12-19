from dataclasses import dataclass
from itertools import cycle
from typing import Any

from aoc.solutions.day_06.common import make_directions, make_map

def solution(path):
    with open(path) as f:
        rows = f.readlines()
    directions = make_directions()
    current, obstructions = make_map(rows)
    x_min, x_max = 0, len(rows[0])
    y_min, y_max = 0, len(rows)
    positions = set()
    direction = next(directions)
    while (x_min <= current.x < x_max) and (y_min <= current.y < y_max):
        new = current + direction
        if new in obstructions:
            direction = next(directions)
        else:
            positions.add(current)
            current = new
    return len(positions)

