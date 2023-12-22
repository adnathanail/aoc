from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=13)


def get_vertical_mirror_index(grid):
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
        if is_mirror:
            return split_point

    return None


def get_horizontal_mirror_index(grid):
    for split_point in range(1, len(grid)):
        first_half = grid[:split_point]
        second_half = grid[split_point:]
        if len(first_half) > len(second_half):
            first_half = first_half[len(first_half) - len(second_half) :]
        elif len(second_half) > len(first_half):
            second_half = second_half[: len(first_half)]
        if first_half == second_half[::-1]:
            return split_point


grids = puzzle.input_data.split("\n\n")

out = 0

for grid in grids:
    vid = get_vertical_mirror_index(grid.split("\n"))
    hid = get_horizontal_mirror_index(grid.split("\n"))
    if vid is not None:
        out += vid
    if hid is not None:
        out += hid * 100

print(out)
