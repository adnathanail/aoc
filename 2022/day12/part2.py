from aocd.models import Puzzle  # type: ignore[import]

from utils import find_character, traverse_grid


def main() -> None:
    puzzle = Puzzle(year=2022, day=12)
    grid = puzzle.input_data.split("\n")

    end_point = find_character(grid, "E")

    min_distance_grid, next_step_grid = traverse_grid(grid, end_point)

    distances_from_a_to_E = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "a":
                distances_from_a_to_E.add(min_distance_grid[i][j])

    print(min(distances_from_a_to_E))


if __name__ == "__main__":
    main()
