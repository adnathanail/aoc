from copy import deepcopy
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=13)


def get_vertical_mirror_index(grid, ignore_num=-1):
    for split_point in range(1, len(grid[0])):
        is_mirror = True
        for row in grid:
            first_half, second_half = row[:split_point], row[split_point:]

            if len(first_half) > len(second_half):
                first_half = first_half[len(first_half) - len(second_half) :]
            elif len(second_half) > len(first_half):
                second_half = second_half[: len(first_half)]

            second_half = second_half[::-1]
            if first_half != second_half:
                is_mirror = False
                break
        if is_mirror and split_point != ignore_num:
            return split_point

    return None


def get_horizontal_mirror_index(grid, ignore_num=-1):
    for split_point in range(1, len(grid)):
        first_half = grid[:split_point]
        second_half = grid[split_point:]
        if len(first_half) > len(second_half):
            first_half = first_half[len(first_half) - len(second_half) :]
        elif len(second_half) > len(first_half):
            second_half = second_half[: len(first_half)]
        if first_half == second_half[::-1] and split_point != ignore_num:
            return split_point


def mutate_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            newgrid = deepcopy(grid)
            newgrid[i][j] = "#" if newgrid[i][j] == "." else "."
            yield newgrid


grids = puzzle.input_data.split("\n\n")


out = 0

for i in range(len(grids)):
    grid = grids[i]
    vid = get_vertical_mirror_index(grid.split("\n"))
    hid = get_horizontal_mirror_index(grid.split("\n"))
    done = False
    for g in mutate_grid([list(s) for s in grid.split("\n")]):
        newvid = get_vertical_mirror_index(g, vid)
        newhid = get_horizontal_mirror_index(g, hid)
        if newvid is not None:
            out += newvid
            done = True
            break
        elif newhid is not None:
            out += newhid * 100
            done = True
            break

print(out)
