from typing import Generator, TypeVar


def find_character(grid: list[str], char: str):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == char:
                return i, j
    raise Exception(f"Can't find '{char}'")


def generate_square_around_point(
        point: tuple[int, int], radius: int, max_i: int, max_j: int
) -> Generator[tuple[int, int], None, None]:
    """
    Given a point e.g. (2, 5) and a radius e.g. 1
    Returns a series of points forming a square centred on that point
      starting in the top left corner, and continuing clockwise around the square

    e.g.
    ........
    ....012.
    ....7.3.
    ....654.
    ........

    If the square would leave the grid, those points are emitted from the return result

    e.g. for radius 3
    ..4.....
    ..3.....
    ..2.....
    ..1.....
    ..0.....
    """
    min_square_i = point[0] - radius
    max_square_i = point[0] + radius
    min_square_j = point[1] - radius
    max_square_j = point[1] + radius

    if min_square_i >= 0:
        for j in range(max(min_square_j, 0), min(max_square_j, max_j) + 1):
            yield min_square_i, j

    if max_square_j <= max_j:
        for i in range(max(min_square_i + 1, 0), min(max_square_i - 1, max_i) + 1):
            yield i, max_square_j

    if max_square_i <= max_i:
        for j in range(min(max_square_j, max_j), max(min_square_j, 0) - 1, -1):
            yield max_square_i, j

    if min_square_j >= 0:
        for i in range(min(max_square_i - 1, max_i), max(min_square_i, -1), -1):
            yield i, min_square_j


def generate_movements_around_point(
        point: tuple[int, int], max_i: int, max_j: int
) -> Generator[tuple[int, int], None, None]:
    """
    Given a point e.g. (2, 5) find the possible squares (u/d/l/r) we can go to,
      respecting the edges of the grid
    """
    if point[0] - 1 >= 0:
        yield point[0] - 1, point[1]

    if point[1] + 1 <= max_j:
        yield point[0], point[1] + 1

    if point[0] + 1 <= max_i:
        yield point[0] + 1, point[1]

    if point[1] - 1 >= 0:
        yield point[0], point[1] - 1


T = TypeVar("T")


def generate_grid(height: int, width: int, default_value: T) -> list[list[T]]:
    return [[default_value for _ in range(width)] for _ in range(height)]


def can_reach_square(start_elevation: str, end_elevation: str) -> bool:
    """
    Given letters of 2 points (which map to elevations)
     return a boolean denoting if you can travel from the start elevation to the end elevation
    """
    if start_elevation == "S":
        start_elevation = "a"
    if end_elevation == "E":
        end_elevation = "z"
    if ord(end_elevation) - ord(start_elevation) <= 1:
        return True
    return ord(start_elevation) > ord(end_elevation)


def show_grid_path(grid, next_step_grid, start_point: tuple[int, int], end_point: tuple[int, int]):
    spiral_map = [list(row) for row in grid]
    spiral_map[end_point[0]][end_point[1]] = "E"

    current_point = start_point
    while current_point != end_point:
        next_point = next_step_grid[current_point[0]][current_point[1]]
        if current_point[0] - next_point[0] == 1:
            spiral_map[current_point[0]][current_point[1]] = "^"
        elif current_point[0] - next_point[0] == -1:
            spiral_map[current_point[0]][current_point[1]] = "v"
        elif current_point[1] - next_point[1] == 1:
            spiral_map[current_point[0]][current_point[1]] = "<"
        elif current_point[1] - next_point[1] == -1:
            spiral_map[current_point[0]][current_point[1]] = ">"
        else:
            raise Exception("Discontinuity")
        current_point = next_point

    for row in spiral_map:
        print("".join(row))
