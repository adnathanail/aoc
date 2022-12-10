from dataclasses import dataclass
from typing import Generator

from aocd.models import Puzzle  # type: ignore[import]


@dataclass(frozen=True)
class Pos:
    x: int
    y: int


def get_head_positions(puzzle_input: str) -> Generator[Pos, None, None]:
    h_pos = Pos(0, 0)
    for line in puzzle_input.split("\n"):
        direction, distance_str = line.split(" ")
        distance = int(distance_str)
        for _ in range(distance):
            match direction:
                case "U":
                    h_pos = Pos(h_pos.x, h_pos.y + 1)
                case "D":
                    h_pos = Pos(h_pos.x, h_pos.y - 1)
                case "L":
                    h_pos = Pos(h_pos.x - 1, h_pos.y)
                case "R":
                    h_pos = Pos(h_pos.x + 1, h_pos.y)
            yield h_pos


def main() -> None:
    puzzle = Puzzle(year=2022, day=9)
    t_positions = {Pos(0, 0)}
    t_pos = Pos(0, 0)
    for h_pos in get_head_positions(puzzle.input_data):
        if h_pos.y - t_pos.y > 1:
            t_pos = Pos(h_pos.x, h_pos.y - 1)
        elif h_pos.y - t_pos.y < -1:
            t_pos = Pos(h_pos.x, h_pos.y + 1)
        elif h_pos.x - t_pos.x > 1:
            t_pos = Pos(h_pos.x - 1, h_pos.y)
        elif h_pos.x - t_pos.x < -1:
            t_pos = Pos(h_pos.x + 1, h_pos.y)
        t_positions.add(t_pos)
    print(len(t_positions))


if __name__ == "__main__":
    main()
