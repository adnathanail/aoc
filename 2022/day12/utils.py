from typing import Generator, TypeVar, Optional


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
    if point[0] >= 1:
        yield point[0] - 1, point[1]

    if point[1] + 1 <= max_j:
        yield point[0], point[1] + 1

    if point[0] + 1 <= max_i:
        yield point[0] + 1, point[1]

    if point[1] >= 1:
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


def show_grid_path(
    grid, next_step_grid, start_point: tuple[int, int], end_point: tuple[int, int]
):
    # spiral_map = [list(row) for row in grid]
    spiral_map = [["." for _ in row] for row in grid]
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


def traverse_grid(
    grid: list[str], end_point: tuple[int, int]
) -> tuple[list[list[int]], list[list[Optional[tuple[int, int]]]]]:
    # 2D array with same dimensions as the grid, holding the current known minimum number of steps to E
    #  initialise to width * height as this is theoretically the longest possible trail
    min_distance_grid: list[list[int]] = generate_grid(
        len(grid), len(grid[0]), len(grid) * len(grid[0])
    )
    min_distance_grid[end_point[0]][
        end_point[1]
    ] = 0  # The end square is 0 steps away from itself

    # 2D array with same dimensions as the grid, holding the coordinate of the next step in the shortest path
    #  from a given location to E
    next_step_grid: list[list[Optional[tuple[int, int]]]] = generate_grid(
        len(grid), len(grid[0]), None
    )

    distances_changed_this_iteration = True
    while distances_changed_this_iteration:
        distances_changed_this_iteration = False
        update_radius = 1
        squares_checked_this_radius = True
        while squares_checked_this_radius:
            squares_checked_this_radius = False
            distances_changed_this_square = True
            while distances_changed_this_square:
                distances_changed_this_square = False
                for coord in generate_square_around_point(
                    end_point, update_radius, len(grid) - 1, len(grid[0]) - 1
                ):
                    squares_checked_this_radius = True
                    for neighbour in generate_movements_around_point(
                        coord, len(grid) - 1, len(grid[0]) - 1
                    ):
                        if (
                            can_reach_square(
                                grid[coord[0]][coord[1]],
                                grid[neighbour[0]][neighbour[1]],
                            )
                            and min_distance_grid[coord[0]][coord[1]]
                            > min_distance_grid[neighbour[0]][neighbour[1]] + 1
                        ):
                            distances_changed_this_square = True
                            distances_changed_this_iteration = True
                            min_distance_grid[coord[0]][coord[1]] = (
                                min_distance_grid[neighbour[0]][neighbour[1]] + 1
                            )
                            next_step_grid[coord[0]][coord[1]] = neighbour
            update_radius += 1
    return min_distance_grid, next_step_grid
