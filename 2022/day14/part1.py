from aocd.models import Puzzle  # type: ignore[import]

from utils import get_scan_size, scan_rock


def main() -> None:
    puzzle = Puzzle(year=2022, day=14)
    inp = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""

    min_x, max_x, min_y, max_y = get_scan_size(inp)
    scan = scan_rock(inp, min_x, max_x, min_y, max_y)

    for row in scan:
        print("".join(row))


if __name__ == "__main__":
    main()
