from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=15)
input_data = puzzle.input_data

grid_str, ins_strs = input_data.split("\n\n")
grid = [[char for char in row] for row in grid_str.split("\n")]
ins = ins_strs.replace("\n", "")


def find_rob():
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "@":
                return (j, i)


rob = find_rob()


def try_to_move(loc, delta):
    new_loc = (loc[0] + delta[0], loc[1] + delta[1])

    if grid[new_loc[1]][new_loc[0]] == "O":
        try_to_move(new_loc, delta)

    if grid[new_loc[1]][new_loc[0]] == ".":
        grid[new_loc[1]][new_loc[0]] = grid[loc[1]][loc[0]]
        grid[loc[1]][loc[0]] = "."
        return new_loc

    return loc


for struc in ins:
    if struc == "<":
        rob = try_to_move(rob, (-1, 0))
    elif struc == "^":
        rob = try_to_move(rob, (0, -1))
    if struc == ">":
        rob = try_to_move(rob, (1, 0))
    elif struc == "v":
        rob = try_to_move(rob, (0, 1))


tot = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "O":
            tot += i * 100 + j

print(tot)
