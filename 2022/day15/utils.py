import re

from project_utils import Coord


def get_sensors_and_beacons(
    inp: str,
) -> tuple[list[Coord], list[Coord]]:
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
