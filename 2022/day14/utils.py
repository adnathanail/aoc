from typing import Generator


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


def normalise_coord(coord: tuple[int, int], min_x: int, min_y: int) -> tuple[int, int]:
    return coord[0] - min_x, coord[1] - min_y


def scan_rock(inp: str, min_x: int, max_x: int, min_y: int, max_y: int) -> list[list[str]]:
    scan: list[list[str]] = [["." for _ in range(min_x, max_x + 1)] for _ in range(min_y, max_y + 1)]

    for row in inp.split("\n"):
        for rock in get_rocks_from_path(
                [(int(point.split(",")[0]), int(point.split(",")[1])) for point in row.split(" -> ")]):
            norm_rock = normalise_coord(rock, min_x, min_y)
            scan[norm_rock[1]][norm_rock[0]] = "#"

    return scan
