from dataclasses import dataclass
from itertools import cycle
from typing import Any

from aoc.solutions.day_06.common import make_directions, make_map

def get_path(current, obstructions, directions=None):
    directions = directions or make_directions()
    x_min, x_max = 0, max(v.x for v in obstructions) + 1
    y_min, y_max = 0, max(v.y for v in obstructions) + 1
    positions = set()
    direction = next(directions)
    while (x_min <= current.x < x_max) and (y_min <= current.y < y_max):
        new = current + direction
        if new in obstructions:
            direction = next(directions)
        else:
            positions.add(current)
            current = new
    return positions

def solution(path):
    with open(path) as f:
        rows = f.readlines()
    current, obstructions = make_map(rows)
    positions = get_path(current, obstructions)
    return len(positions)

