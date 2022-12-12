from dataclasses import dataclass
from typing import Generator


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
