from typing import Generator

from aocd.models import Puzzle  # type: ignore[import]


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


def calculate_scenic_score(tree_height_grid: list[list[int]], tree_coord: tuple[int, int]):
    score = 1
    for cl in coord_list_generator(len(tree_height_grid), len(tree_height_grid[0]), tree_coord):
        viewing_distance = 0
        for c in cl:
            viewing_distance += 1
            if tree_height_grid[c[0]][c[1]] >= tree_height_grid[tree_coord[0]][tree_coord[1]]:
                break
        score *= viewing_distance
    return score


def main() -> None:
    puzzle = Puzzle(year=2022, day=8)
    grid: list[list[int]] = [[int(cell) for cell in row] for row in puzzle.input_data.split("\n")]
    max_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            max_score = max(max_score, calculate_scenic_score(grid, (i, j)))
    print(max_score)


if __name__ == "__main__":
    main()
