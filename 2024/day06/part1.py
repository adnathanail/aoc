from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=6)
input_data = puzzle.input_data

grid = input_data.split("\n")


def find_guard(gr):
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] == "^":
                return (i, j)
    raise Exception("Not found")


def get_new_loc(loc, dir):
    if dir == 1:
        return (loc[0] - 1, loc[1])
    elif dir == 2:
        return (loc[0], loc[1] + 1)
    elif dir == 3:
        return (loc[0] + 1, loc[1])
    elif dir == 4:
        return (loc[0], loc[1] - 1)


def move(gr, loc, dir):
    new_loc = get_new_loc(loc, dir)
    if new_loc[0] < 0 or new_loc[0] >= len(gr) or new_loc[0] < 0 or new_loc[1] >= len(gr[new_loc[0]]):
        return None, None
    elif gr[new_loc[0]][new_loc[1]] in [".", "^"]:
        return new_loc, dir
    else:
        new_dir = dir + 1
        if new_dir > 4:
            new_dir -= 4
        return loc, new_dir


guard = find_guard(grid)
guard_dir = 1

unique_locs = {guard}
while guard is not None:
    guard, guard_dir = move(grid, guard, guard_dir)
    if guard is not None:
        unique_locs.add(guard)

print(len(unique_locs))
