from typing import Optional

from aocd.models import Puzzle  # type: ignore[import]

from utils import find_character, generate_square_around_point, generate_movements_around_point, generate_grid, \
    can_reach_square, show_grid_path


def main() -> None:
    puzzle = Puzzle(year=2022, day=12)
    grid = puzzle.input_data.split("\n")

    start_point = find_character(grid, "S")
    end_end_point = find_character(grid, "E")

    # 2D array with same dimensions as the grid, holding the current known minimum number of steps to E
    #  initialise to width * height as this is theoretically the longest possible trail
    min_distance_grid: list[list[int]] = generate_grid(len(grid), len(grid[0]), len(grid) * len(grid[0]))
    min_distance_grid[end_end_point[0]][end_end_point[1]] = 0  # The end square is 0 steps away from itself

    next_step_grid: list[list[Optional[tuple[int, int]]]] = generate_grid(
        len(grid), len(grid[0]), None
    )

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
                        end_end_point, update_radius, len(grid) - 1, len(grid[0]) - 1
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

    distances_from_a_to_E = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "a":
                distances_from_a_to_E.add(min_distance_grid[i][j])
    print(distances_from_a_to_E)
    print(min(distances_from_a_to_E))


if __name__ == "__main__":
    main()
