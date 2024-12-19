
from dataclasses import dataclass
from itertools import cycle
from typing import Any


@dataclass(frozen=True, eq=True)
class Vector:
    x: int
    y: int
    def __add__(self, other: Any) -> "Vector":
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        else:
            raise ValueError(f"Type {type(other)} is incompatible with Vector")
        
def make_map(rows: list[str]) -> set:
    obstructions = set()
    for y, row in enumerate(rows):
        for x, element in enumerate(row):
            if element == "^":
                current = Vector(x, y)
            elif element == "#":
                obstructions.add(Vector(x, y))
    return current, obstructions

def make_directions():
    return cycle((Vector(0, -1), Vector(1, 0), Vector(0, 1), Vector(-1, 0)))