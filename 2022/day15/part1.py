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

    no_beacons_x_vals: set[int] = set()

    for i in range(len(sensors)):
        print("Sensor", sensors[i])
        dist_to_beacon = manhattan_distance(sensors[i], beacons[i])
        if (
                sensors[i][1] == Y_VAL
                or (sensors[i][1] < Y_VAL < sensors[i][1] + dist_to_beacon)
                or (sensors[i][1] > Y_VAL > sensors[i][1] - dist_to_beacon)
        ):
            print(f"\tradius {dist_to_beacon}")
            points_on_y_val = [
                p
                for p in generate_diamond_around_point(
                    sensors[i], dist_to_beacon, min_x, max_x, min_y, max_y
                )
                if p[1] == Y_VAL
            ]
            if len(points_on_y_val) == 1:
                no_beacons_x_vals.add(points_on_y_val[0][0])
            elif len(points_on_y_val) == 2:
                x_1, x_2 = points_on_y_val[0][0], points_on_y_val[1][0]
                start_x, end_x = sorted([x_1, x_2])
                for x in range(start_x, end_x + 1):
                    no_beacons_x_vals.add(x)
            elif len(points_on_y_val) != 0:
                raise Exception(f"Can't intersect y={Y_VAL} more than twice!")
    print(len([x_val for x_val in no_beacons_x_vals if (x_val, Y_VAL) not in beacons]))


if __name__ == "__main__":
    main()
