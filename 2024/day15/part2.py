import copy
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=15)
input_data = puzzle.input_data

grid_str, ins_strs = input_data.split("\n\n")
grid = []
for row_str in grid_str.split("\n"):
    row = []
    for char in row_str:
        if char == "#":
            row.append("#")
            row.append("#")
        if char == "O":
            row.append("[")
            row.append("]")
        if char == ".":
            row.append(".")
            row.append(".")
        if char == "@":
            row.append("@")
            row.append(".")
    grid.append(row)
ins = ins_strs.replace("\n", "")


def find_rob():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                return (j, i)


rob = find_rob()


def try_to_move(loc, delta):
    global grid

    new_loc = (loc[0] + delta[0], loc[1] + delta[1])
    other_new_loc = None
    if delta[1] != 0:
        if grid[new_loc[1]][new_loc[0]] == "[":
            other_new_loc = (new_loc[0] + 1, new_loc[1])
        elif grid[new_loc[1]][new_loc[0]] == "]":
            other_new_loc = (new_loc[0] - 1, new_loc[1])

    grid_checkpoint = copy.deepcopy(grid)

    first_moved = False
    if grid[new_loc[1]][new_loc[0]] in ["[", "]"]:
        _, first_moved = try_to_move(new_loc, delta)

    if first_moved:
        if other_new_loc is not None and grid[other_new_loc[1]][other_new_loc[0]] in ["[", "]"]:
            _, second_moved = try_to_move(other_new_loc, delta)
            if not second_moved:
                grid = grid_checkpoint

    if grid[new_loc[1]][new_loc[0]] == "." and (other_new_loc is None or grid[other_new_loc[1]][other_new_loc[0]] == "."):
        grid[new_loc[1]][new_loc[0]] = grid[loc[1]][loc[0]]
        grid[loc[1]][loc[0]] = "."
        if other_new_loc is not None:
            grid[other_new_loc[1]][other_new_loc[0]] = grid[loc[1]][loc[0]]
        return new_loc, True

    return loc, False


for struc in ins:
    if struc == "<":
        rob, _ = try_to_move(rob, (-1, 0))
    elif struc == "^":
        rob, _ = try_to_move(rob, (0, -1))
    if struc == ">":
        rob, _ = try_to_move(rob, (1, 0))
    elif struc == "v":
        rob, _ = try_to_move(rob, (0, 1))

tot = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "[":
            tot += i * 100 + j

print(tot)
