import re

from aocd.models import Puzzle  # type: ignore[import]

from project_utils import get_from_grid, set_on_grid


def get_grid(inp: str) -> tuple[list[list[str]], int, int, int, int]:
    sensors_and_beacons: list[tuple[int, int, int, int]] = []
    patt = re.compile(r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)")
    for row in inp.split("\n"):
        s_x, s_y, b_x, b_y = [int(x) for x in re.match(patt, row).groups()]
        sensors_and_beacons.append((s_x, s_y, b_x, b_y))

    min_x = max_x = min_y = max_y = 0
    for sb in sensors_and_beacons:
        if sb[0] < min_x:
            min_x = sb[0]
        if sb[0] > max_x:
            max_x = sb[0]
        if sb[1] < min_y:
            min_y = sb[1]
        if sb[1] > max_y:
            max_y = sb[1]
        if sb[2] < min_x:
            min_x = sb[2]
        if sb[2] > max_x:
            max_x = sb[2]
        if sb[3] < min_y:
            min_y = sb[3]
        if sb[3] > max_y:
            max_y = sb[3]

    grid: list[list[str]] = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    for sb in sensors_and_beacons:
        set_on_grid(grid, (sb[0], sb[1]), "S", min_x, min_y)
        set_on_grid(grid, (sb[2], sb[3]), "B", min_x, min_y)
    return grid, min_x, max_x, min_y, max_y


def main() -> None:
    puzzle = Puzzle(year=2022, day=15)
    grid, min_x, max_x, min_y, max_y = get_grid("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""")
    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    main()
