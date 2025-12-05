from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=4)
inp = puzzle.examples[0].input_data
# inp = puzzle.input_data


grid = [list(row) for row in inp.splitlines()]
HEIGHT = len(grid)
WIDTH = len(grid[0])

def get_valid_surrounding_square_indexes(x, y):
    # 123
    # 4X5
    # 678
    valid_locs = []
    if y > 0:
        if x > 0:
            valid_locs.append((x - 1, y - 1))  # 1
        valid_locs.append((x, y - 1))  # 2
        if x < WIDTH - 1:
            valid_locs.append((x + 1, y - 1))  # 3
    if x > 0:
        valid_locs.append((x - 1, y))  # 4
    if x < WIDTH - 1:
        valid_locs.append((x + 1, y))  # 5
    if y < HEIGHT - 1:
        if x > 0:
            valid_locs.append((x - 1, y + 1))  # 6
        valid_locs.append((x, y + 1))  # 7
        if x < WIDTH - 1:
            valid_locs.append((x + 1, y + 1))  # 8
    return valid_locs

def get_is_acccessible(x, y):
    num_adjacent_rolls = 0
    for loc in get_valid_surrounding_square_indexes(x, y):
        if grid[loc[1]][loc[0]] == "@":
            num_adjacent_rolls += 1
        if num_adjacent_rolls > 3:
            return False
    return True

roll_locs = []
for yy in range(HEIGHT):
    for xx in range(WIDTH):
        if grid[yy][xx] == "@":
            roll_locs.append((xx, yy))

num_accessible_rolls = 0
any_removed = True  # set true so first loop runs
while any_removed:
    any_removed = False
    to_remove = []
    for rl in roll_locs:
        if get_is_acccessible(rl[0], rl[1]):
            num_accessible_rolls += 1
            to_remove.append(rl)
            any_removed = True
    print(len(to_remove))
    for tr in to_remove:
        grid[tr[1]][tr[0]] = "."
        roll_locs.remove(tr)

print(num_accessible_rolls)


# num_accessible_rolls = 0
# to_remove = []
# for rl in roll_locs:
#     if get_is_acccessible(rl[0], rl[1]):
#         num_accessible_rolls += 1
#         to_remove.append(rl)
# print(num_accessible_rolls)

# for tr in to_remove:
#     grid[tr[1]][tr[0]] = "."
#     roll_locs.remove(tr)


# num_accessible_rolls = 0
# to_remove = []
# for rl in roll_locs:
#     if get_is_acccessible(rl[0], rl[1]):
#         num_accessible_rolls += 1
#         to_remove.append(rl)
# print(num_accessible_rolls)