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

from aocd.models import Puzzle  # type: ignore[import]

from utils import find_character, show_grid_path, traverse_grid


def main() -> None:
    puzzle = Puzzle(year=2022, day=12)
    grid = puzzle.input_data.split("\n")

    start_point = find_character(grid, "S")
    end_point = find_character(grid, "E")

    min_distance_grid, next_step_grid = traverse_grid(grid, end_point)

    show_grid_path(grid, next_step_grid, start_point, end_point)
    print(min_distance_grid[start_point[0]][start_point[1]])


if __name__ == "__main__":
    main()
