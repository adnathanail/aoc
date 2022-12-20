from aocd.models import Puzzle  # type: ignore[import]

from utils import get_scan_size, scan_rock, drop_sand


def main() -> None:
    puzzle = Puzzle(year=2022, day=14)

    min_x, max_x, min_y, max_y = get_scan_size(puzzle.input_data)
    # The sand could extend a maximum of the height to the left and right
    min_x = min(min_x, 500 - max_y)
    max_x = max(max_x, 500 + max_y)

    scan = scan_rock(puzzle.input_data, min_x, max_x, min_y, max_y, max_y + 2)

    i = 0
    while drop_sand(scan, (500, 0), min_x, min_y):
        i += 1

    print(i)


if __name__ == "__main__":
    main()
