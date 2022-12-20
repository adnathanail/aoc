from typing import Generator, Optional
from project_utils import get_from_grid, set_on_grid


def get_scan_size(inp):
    min_x = 500
    max_x = 500
    min_y = 0
    max_y = 0
    for row in inp.split("\n"):
        for point in row.split(" -> "):
            point_split = point.split(",")
            x, y = int(point_split[0]), int(point_split[1])
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x
            if y < min_y:
                min_y = y
            if y > max_y:
                max_y = y
    return min_x, max_x, min_y, max_y


def get_rocks_from_path(path: list[tuple[int, int]]) -> Generator[tuple[int, int], None, None]:
    current_point = path.pop(0)
    yield current_point
    while len(path) > 0:
        target_point = path.pop(0)
        while current_point != target_point:
            if current_point[0] == target_point[0]:
                if current_point[1] < target_point[1]:
                    current_point = (current_point[0], current_point[1] + 1)
                elif current_point[1] > target_point[1]:
                    current_point = (current_point[0], current_point[1] - 1)
                else:
                    raise Exception("current_point != target_point")
            elif current_point[1] == target_point[1]:
                if current_point[0] < target_point[0]:
                    current_point = (current_point[0] + 1, current_point[1])
                elif current_point[0] > target_point[0]:
                    current_point = (current_point[0] - 1, current_point[1])
                else:
                    raise Exception("current_point != target_point")
            else:
                raise Exception("lines must be straight")
            yield current_point


def scan_rock(inp: str, min_x: int, max_x: int, min_y: int, max_y: int, floor: Optional[int] = None) -> list[list[str]]:
    scan: list[list[str]] = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]
    if floor is not None:
        scan.extend([["." for _ in range(min_x, max_x + 1)] for _ in range(floor - max_y - 1)])
        scan.append(["#" for _ in range(min_x, max_x + 1)])

    for row in inp.split("\n"):
        for rock in get_rocks_from_path(
                [(int(point.split(",")[0]), int(point.split(",")[1])) for point in row.split(" -> ")]):
            set_on_grid(scan, rock, "#", min_x, min_y)

    return scan


def get_potential_new_sand_positions(sand_coord) -> Generator[tuple[int, int], None, None]:
    yield sand_coord[0], sand_coord[1] + 1
    yield sand_coord[0] - 1, sand_coord[1] + 1
    yield sand_coord[0] + 1, sand_coord[1] + 1


def drop_sand(scan: list[list[str]], sand_coord: tuple[int, int], min_x: int, min_y: int) -> bool:
    """
    Returns True when sand successfully rested on something
    """
    at_rest = False
    while not at_rest:
        # There is already sand at the source, so all other sand is blocked
        if get_from_grid(scan, sand_coord, min_x, min_y) == "o":
            return False
        for potential_new_coord in get_potential_new_sand_positions(sand_coord):
            try:
                if get_from_grid(scan, potential_new_coord, min_x, min_y) == ".":
                    sand_coord = potential_new_coord
                    break
            except IndexError:
                # Tried to access outside of the minimally sized 2D array, therefore sand will never hit another rock
                return False
        else:
            at_rest = True

    set_on_grid(scan, sand_coord, "o", min_x, min_y)
    return True
