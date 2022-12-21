import re
from typing import Generator

from aocd.models import Puzzle  # type: ignore[import]

from project_utils import set_on_grid, Coord, StrGrid, get_from_grid


def get_sensors_and_beacons(
        inp: str,
) -> tuple[list[tuple[int, int]], list[tuple[int, int]]]:
    sensors = []
    beacons = []

    patt = re.compile(
        r"Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)"
    )
    for row in inp.split("\n"):
        s_x, s_y, b_x, b_y = [int(x) for x in re.match(patt, row).groups()]
        sensors.append((s_x, s_y))
        beacons.append((b_x, b_y))

    return sensors, beacons


def get_min_max_x_y(coords: list[tuple[int, int]]):
    min_x = max_x = coords[0][0]
    min_y = max_y = coords[0][1]

    for sb in coords:
        if sb[0] < min_x:
            min_x = sb[0]
        if sb[0] > max_x:
            max_x = sb[0]
        if sb[1] < min_y:
            min_y = sb[1]
        if sb[1] > max_y:
            max_y = sb[1]

    return min_x, max_x, min_y, max_y


def get_grid(
        sensors: list[Coord],
        beacons: list[Coord],
        min_x: int,
        max_x: int,
        min_y: int,
        max_y: int,
) -> StrGrid:
    grid: list[list[str]] = [
        ["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)
    ]

    for s in sensors:
        set_on_grid(grid, (s[0], s[1]), "S", min_x, min_y)
    for b in beacons:
        set_on_grid(grid, (b[0], b[1]), "B", min_x, min_y)

    return grid


def generate_diamond_around_point_without_bounds_checking(point: Coord, radius: int) -> Generator[Coord, None, None]:
    curr = (point[0], point[1] - radius)
    while (curr[0] - point[0]) < radius:
        curr = (curr[0] + 1, curr[1] + 1)
        yield curr
    while (curr[1] - point[1]) < radius:
        curr = (curr[0] - 1, curr[1] + 1)
        yield curr
    while -(curr[0] - point[0]) < radius:
        curr = (curr[0] - 1, curr[1] - 1)
        yield curr
    while -(curr[1] - point[1]) < radius:
        curr = (curr[0] + 1, curr[1] - 1)
        yield curr


def generate_diamond_around_point(point: Coord, radius: int, min_x: int, max_x: int, min_y: int, max_y: int) -> \
        Generator[Coord, None, None]:
    for val in generate_diamond_around_point_without_bounds_checking(point, radius):
        if min_x <= val[0] <= max_x and min_y <= val[1] <= max_y:
            yield val


def main() -> None:
    puzzle = Puzzle(year=2022, day=15)
    # sensors, beacons = get_sensors_and_beacons(puzzle.input_data)
    sensors, beacons = get_sensors_and_beacons("""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
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
    min_x, max_x, min_y, max_y = get_min_max_x_y(beacons + sensors)
    grid = get_grid(sensors, beacons, min_x, max_x, min_y, max_y)

    for s in sensors:
        radius = 1
        not_hit_beacon = True
        while not_hit_beacon:
            for p in generate_diamond_around_point(s, radius, min_x, max_x, min_y, max_y):
                if p in beacons:
                    not_hit_beacon = False
                elif get_from_grid(grid, p, min_x, min_y) == ".":
                    # Don't overwrite a B/P on the grid!
                    set_on_grid(grid, p, "#", min_x, min_y)
            radius += 1

    print(sum(char in ["#", "S"] for char in grid[10 - min_y]))


if __name__ == "__main__":
    main()
