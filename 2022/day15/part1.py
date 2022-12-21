from typing import Generator

from aocd.models import Puzzle  # type: ignore[import]

from project_utils import Coord, manhattan_distance, get_min_max_x_y
from utils import get_sensors_and_beacons


def generate_diamond_around_point_without_bounds_checking(
    point: Coord, radius: int
) -> Generator[Coord, None, None]:
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


def generate_diamond_around_point(
    point: Coord, radius: int, min_x: int, max_x: int, min_y: int, max_y: int
) -> Generator[Coord, None, None]:
    for val in generate_diamond_around_point_without_bounds_checking(point, radius):
        if min_x <= val[0] <= max_x and min_y <= val[1] <= max_y:
            yield val


def main() -> None:
    puzzle = Puzzle(year=2022, day=15)
    Y_VAL = 2000000
    sensors, beacons = get_sensors_and_beacons(puzzle.input_data)
    min_x, max_x, min_y, max_y = get_min_max_x_y(beacons + sensors)

    no_beacons: set[Coord] = set()

    for i in range(len(sensors)):
        print("Sensor", sensors[i])
        dist_to_beacon = manhattan_distance(sensors[i], beacons[i])
        if (sensors[i][1] < Y_VAL and sensors[i][1] + dist_to_beacon > Y_VAL) or (
            sensors[i][1] > Y_VAL and sensors[i][1] - dist_to_beacon < Y_VAL
        ):
            print("\tUseful")
            radius = 1
            hit_beacon = False
            while not hit_beacon:
                print(f"\t\tradius {radius}/{dist_to_beacon}")
                for p in generate_diamond_around_point(
                    sensors[i], radius, min_x, max_x, min_y, max_y
                ):
                    if p == beacons[i]:
                        hit_beacon = True
                    elif p[1] == Y_VAL:
                        no_beacons.add(p)
                radius += 1

    print(len(no_beacons))


if __name__ == "__main__":
    main()
