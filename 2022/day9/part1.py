from aocd.models import Puzzle  # type: ignore[import]

from utils import Pos, get_head_positions


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
