"""
This is not necessarily an optimal approach, we just run the same greedy algorithm repeatedly until nothing is changed
In fact, there are 2 nested greedy loops!

This could have been mapped onto Dijkstra and solved (probably?) quicker

But this solution is completely original, and also raises the interesting question of what the worst case path could
  look like

For the inner loop, going round a square of radius X repeatedly, I think the worst case path would be a clockwise
  spiral, because we search clockwise

e.g.
.....
.>>v.
.>.v.
.^<<.
.....

1st pass

.....
.....
.10..
.....
.....

2nd pass

.....
.....
.10..
.2...
.....

3rd pass

.....
.....
.10..
.23..
.....

etc.

Then for the outer loop, because we resolve from the inside out, paths heading from the outside in would be very slow
  to resolve
So a path that goes all the way from S to near E, then back near S, then near E etc. would take a long time
"""
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
        # print("Iteration")
        distances_changed_this_iteration = False
        update_radius = 1
        squares_checked_this_radius = True
        while squares_checked_this_radius:
            # print(f"\tUpdate radius {update_radius}")
            squares_checked_this_radius = False
            distances_changed_this_square = True
            while distances_changed_this_square:
                # print("\t\tSquare")
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

    # show_grid_path(grid, next_step_grid, start_point, end_end_point)
    print(min_distance_grid[start_point[0]][start_point[1]])


if __name__ == "__main__":
    main()
