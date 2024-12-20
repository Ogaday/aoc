from contextlib import contextmanager
import importlib.resources
from pathlib import Path
from typing import Generator


DEFAULT_INPUT_DIR = Path("inputs")


def day_name(day: int) -> str:
    """Generate a string with the padded name of the day.

    Examples
    --------
    >>> day_name(day=1)
    'day_01'
    >>> day_name(day=10)
    'day_10'

    Warnings
    --------
    This performs no validation of the day itself.
    """
    padded_day = str(day).zfill(2)
    return f"day_{padded_day}"


@contextmanager
def example_path(day: int) -> Generator[Path, None, None]:
    """Generate a path for the example input for a given day.

    Examples
    --------
    >>> with example_path(day=3) as path:
    ...     print(path.name)
    day_03.txt

    Warnings
    --------
    This will return a path, but does not guarantee that the path exists.
    """
    with importlib.resources.path("aoc.examples", day_name(day)).with_suffix(
        ".txt"
    ) as path:
        yield path


@contextmanager
def input_path(
    day: int, directory: Path = DEFAULT_INPUT_DIR
) -> Generator[Path, None, None]:
    """
    Examples
    --------
    >>> with input_path(day=1) as path:
    ...     print(path)
    inputs/day_01.txt
    >>> with input_path(day=11, directory=Path("/tmp")) as path:
    ...     print(path)
    /tmp/day_11.txt
    """
    path = (directory / day_name(day=day)).with_suffix(".txt")
    yield path
