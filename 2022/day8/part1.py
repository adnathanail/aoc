from typing import Generator

from aocd.models import Puzzle  # type: ignore[import]

from utils import *


def coord_list_generator(
        row_min: int, row_max: int, row_step: int, col_min: int, col_max: int, col_step: int,
        reverse: bool
) -> Generator[list[tuple[int, int]], None, None]:
    for i in range(row_min, row_max, row_step):
        yield [((j, i) if reverse else (i, j)) for j in range(col_min, col_max, col_step)]


def main() -> None:
    puzzle = Puzzle(year=2022, day=8)
    grid: list[list[int]] = [[int(cell) for cell in row] for row in puzzle.input_data.split("\n")]
    coord_generators = [
        coord_list_generator(0, len(grid), 1, 0, len(grid[0]), 1, False),
        coord_list_generator(0, len(grid), 1, len(grid[0]) - 1, -1, -1, False),
        coord_list_generator(0, len(grid), 1, 0, len(grid[0]), 1, True),
        coord_list_generator(0, len(grid), 1, len(grid[0]) - 1, -1, -1, True)
    ]
    visible_trees: set[tuple[int, int]] = set()
    for cg in coord_generators:
        for coords in cg:
            visible_trees = visible_trees.union(check_tree_visibility(grid, coords))
    print(len(visible_trees))


if __name__ == "__main__":
    main()
