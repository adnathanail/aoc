from typing import Generator, TypeVar, Optional

from aocd.models import Puzzle  # type: ignore[import]


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
    return [[width * height for _ in range(width)] for _ in range(height)]


def can_reach_square(start_square: str, end_square: str) -> bool:
    if start_square == "S":
        return True
    if end_square == "E":
        return start_square == "z"
    if ord(end_square) - ord(start_square) <= 1:
        return True
    return ord(start_square) > ord(end_square)


def main() -> None:
    puzzle = Puzzle(year=2022, day=12)
    grid = puzzle.input_data.split("\n")
    grid = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi""".split("\n")

    start = find_character(grid, "S")
    end = find_character(grid, "E")

    min_distance_grid = generate_grid(len(grid), len(grid[0]), len(grid) * len(grid[0]))
    min_distance_grid[end[0]][end[1]] = 0  # The end square is 0 steps away from itself

    # next_step_grid: list[list[Optional[tuple[int, int]]]] = generate_grid(
    #     len(grid), len(grid[0]), None
    # )

    distances_changed_this_iteration = True
    while distances_changed_this_iteration:
        print("Iteration")
        distances_changed_this_iteration = False
        update_radius = 1
        squares_checked_this_radius = True
        while squares_checked_this_radius:
            print(f"\tUpdate radius {update_radius}")
            squares_checked_this_radius = False
            distances_changed_this_square = True
            while distances_changed_this_square:
                print("\t\tSquare")
                distances_changed_this_square = False
                for coord in generate_square_around_point(
                        end, update_radius, len(grid) - 1, len(grid[0]) - 1
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
                            # next_step_grid[coord[0]][coord[1]] = neighbour
            update_radius += 1
    # for row in min_distance_grid:
    #     print("".join("." if x == -1 else str(x % 10) for x in row))
    #
    # for row in next_step_grid:
    #     print("".join(f"{v}\t" for v in row))

    print(min_distance_grid[start[0]][start[1]])


if __name__ == "__main__":
    main()
