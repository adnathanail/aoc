from typing import Generator

from aocd.models import Puzzle  # type: ignore[import]

from utils import *


def coord_list_generator(
        grid_height: int, grid_width: int, treehouse_location: tuple[int, int]
) -> Generator[list[tuple[int, int]], None, None]:
    # Down
    yield [(i, treehouse_location[1]) for i in range(treehouse_location[0] + 1, grid_height)]
    # Up
    yield [(i, treehouse_location[1]) for i in range(treehouse_location[0] - 1, -1, -1)]
    # Right
    yield [(treehouse_location[0], i) for i in range(treehouse_location[1] + 1, grid_width)]
    # Left
    yield [(treehouse_location[0], i) for i in range(treehouse_location[1] - 1, -1, -1)]


def calculate_scenic_score(tree_height_grid: list[list[int]], coord: tuple[int, int]):
    score = 1
    for cl in coord_list_generator(len(tree_height_grid), len(tree_height_grid[0]), coord):
        x = check_tree_visibility(tree_height_grid, cl, True, tree_height_grid[coord[0]][coord[1]])
        # print(sorted([a[0] for a in x]))
        print(x)
        score *= len(x)
    return score


def main() -> None:
    inp = """30373
25512
65332
33549
35390"""
    grid: list[list[int]] = [[int(cell) for cell in row] for row in inp.split("\n")]
    puzzle = Puzzle(year=2022, day=8)
    grid: list[list[int]] = [[int(cell) for cell in row] for row in puzzle.input_data.split("\n")]
    print(grid[63][23], grid[63][24], grid[63][25], grid[63][26], grid[63][27])
    print(grid[63][25])
    print(calculate_scenic_score(grid, (63, 25)))
    # max_score = 0
    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         max_score = max(max_score, calculate_scenic_score(grid, (i, j)))
    #         print(max_score, i, j)
    # print(max_score)


if __name__ == "__main__":
    main()
