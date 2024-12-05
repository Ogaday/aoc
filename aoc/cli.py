from argparse import ArgumentParser
import importlib
import importlib.resources
from pathlib import Path
from typing import Callable, Optional

from aoc.io import DEFAULT_INPUT_DIR, day_name, example_path, input_path


def import_solution(day: int, part: int) -> Callable[[Path], int]:
    """
    Raises
    ------
    AttributeError
        If the module doesn't define a solution method.
    ModuleNotFoundError
        If the solution module doesn't exist.
    """
    solutions = importlib.import_module(f"aoc.solutions.{day_name(day)}.part_{part}")
    return getattr(solutions, "solution")

def solve(day: int, part: int, input_path: Path) -> int:
    sol = import_solution(day=day, part=part)
    return sol(input_path)

def solve_example(day: int, part: int):
    with example_path(day=day) as path:
        return solve(day=day, part=part, input_path=path)

class CLI:
    def __init__(self):
        self.parser = ArgumentParser(prog="aoc", description="Advent of Code solutions.")
        self.parser.add_argument("-d", "--day", type=int)
        self.parser.add_argument("-p", "--part", type=int)
        self.parser.add_argument("-i", "--input-path", type=Path, default=None)
        self.parser.add_argument("--input-directory", type=Path, default=DEFAULT_INPUT_DIR)
        self.parser.add_argument("-e", "--example", action="store_true")

    def __call__(self, args: Optional[list] = None):
        parsed = self.parser.parse_args(args)
        if not (parsed.day and parsed.part):
            self.parser.print_help()
            return

        if parsed.example:
            print(solve_example(day=parsed.day, part=parsed.part))
            return

        if parsed.input_path is None:
            parsed.input_path = input_path(day=parsed.day, directory=parsed.input_directory)
        
        print(solve(day=parsed.day, part=parsed.part, input_path=parsed.input_path))
        return

if __name__ == "__main__":
    cli = CLI()
    cli()