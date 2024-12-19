from dataclasses import dataclass
from itertools import cycle
from typing import Any

from aoc.solutions.day_06.common import make_directions, make_map

class CycleError(Exception):
    """Raise when a cycle is detected."""
    def __init__(self, positions):
        self.positions = positions

def get_positions(current, obstructions, directions=None):
    directions = directions or make_directions()
    x_min, x_max = 0, max(v.x for v in obstructions) + 1
    y_min, y_max = 0, max(v.y for v in obstructions) + 1
    positions = set()
    seen = set()
    direction = next(directions)
    
    while (x_min <= current.x < x_max) and (y_min <= current.y < y_max):
        if (current, direction) in seen:
            raise CycleError(positions)
        seen.add((current, direction))
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
    start, obstructions = make_map(rows)
    original_path = get_positions(current=start, obstructions=obstructions)
    new_obstructions = set()
    for point in original_path - {start}:
        try:
            get_positions(current=start, obstructions=obstructions | {point})
        except CycleError:
            new_obstructions.add(point)
    return len(new_obstructions)



