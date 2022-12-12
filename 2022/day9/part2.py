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


def drag_knot(leader: Pos, follower: Pos) -> Pos:
    if leader.y - follower.y > 1:
        return Pos(leader.x, leader.y - 1)
    elif leader.y - follower.y < -1:
        return Pos(leader.x, leader.y + 1)
    elif leader.x - follower.x > 1:
        return Pos(leader.x - 1, leader.y)
    elif leader.x - follower.x < -1:
        return Pos(leader.x + 1, leader.y)
    return follower


def main() -> None:
    puzzle = Puzzle(year=2022, day=9)
    inp = puzzle.input_data
    inp = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""
    t_positions = {Pos(0, 0)}
    knot_positions = {
        "1": Pos(0, 0),
        "2": Pos(0, 0),
        "3": Pos(0, 0),
        "4": Pos(0, 0),
        "5": Pos(0, 0),
        "6": Pos(0, 0),
        "7": Pos(0, 0),
        "8": Pos(0, 0),
        "9": Pos(0, 0),
    }
    tail_path = []
    for h_pos in get_head_positions(inp):
        knot_positions["1"] = drag_knot(h_pos, knot_positions["1"])
        knot_positions["2"] = drag_knot(knot_positions["1"], knot_positions["2"])
        knot_positions["3"] = drag_knot(knot_positions["2"], knot_positions["3"])
        knot_positions["4"] = drag_knot(knot_positions["3"], knot_positions["4"])
        knot_positions["5"] = drag_knot(knot_positions["4"], knot_positions["5"])
        knot_positions["6"] = drag_knot(knot_positions["5"], knot_positions["6"])
        knot_positions["7"] = drag_knot(knot_positions["6"], knot_positions["7"])
        knot_positions["8"] = drag_knot(knot_positions["7"], knot_positions["8"])
        knot_positions["9"] = drag_knot(knot_positions["8"], knot_positions["9"])
        if knot_positions["9"] not in t_positions:
            tail_path.append(knot_positions["9"])
        t_positions.add(knot_positions["9"])
    print(len(t_positions))
    print(tail_path)


if __name__ == "__main__":
    main()
