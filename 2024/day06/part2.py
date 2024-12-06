from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=6)
input_data = puzzle.input_data


def find_guard(gr):
    for i in range(len(gr)):
        for j in range(len(gr[i])):
            if gr[i][j] == "^":
                return (i, j)
    raise Exception("Not found")


def get_new_loc(loc, loc_dir):
    if loc_dir == 1:
        return (loc[0] - 1, loc[1])
    elif loc_dir == 2:
        return (loc[0], loc[1] + 1)
    elif loc_dir == 3:
        return (loc[0] + 1, loc[1])
    elif loc_dir == 4:
        return (loc[0], loc[1] - 1)


def move(gr, loc, loc_dir):
    new_loc = get_new_loc(loc, loc_dir)
    if new_loc[0] < 0 or new_loc[0] >= len(gr) or new_loc[1] < 0 or new_loc[1] >= len(gr[new_loc[0]]):
        return None, None
    elif gr[new_loc[0]][new_loc[1]] in [".", "^"]:
        return new_loc, loc_dir
    else:
        new_dir = loc_dir + 1
        if new_dir > 4:
            new_dir -= 4
        return move(gr, loc, new_dir)


class LoopException(Exception):
    pass


def get_grid_path(gr):
    guard = find_guard(gr)
    guard_dir = 1
    path = []
    while guard is not None:
        guard, guard_dir = move(gr, guard, guard_dir)
        if (guard, guard_dir) in path:
            raise LoopException
        if guard is not None:
            path.append((guard, guard_dir))
    return path


original_grid = input_data.split("\n")
original_path = get_grid_path(original_grid)

num = 0
loop_locs = set()

for loc, loc_dir in original_path:
    print(loc)
    if original_grid[loc[0]][loc[1]] == "^":
        continue
    grid = [[cell for cell in row] for row in input_data.split("\n")]
    grid[loc[0]][loc[1]] = "O"
    try:
        get_grid_path(grid)
    except LoopException:
        loop_locs.add(loc)


print(len(loop_locs))
