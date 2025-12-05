from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=4)
inp = puzzle.examples[0].input_data
inp = puzzle.input_data


grid = inp.splitlines()
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

def get_surrounding_squares(x, y):
    out = []
    for loc in get_valid_surrounding_square_indexes(x, y):
        out.append(grid[loc[1]][loc[0]])
    return out

# # Generate map like the example, to check they match up
# accessible_rolls = []
# for yy in range(HEIGHT):
#     for xx in range(WIDTH):
#         if grid[yy][xx] == "@" and get_surrounding_squares(xx, yy).count("@") < 4:
#             accessible_rolls.append((xx, yy))

# for yy in range(HEIGHT):
#     for xx in range(WIDTH):
#         if (xx, yy) in accessible_rolls:
#             print("x", end="")
#         else:
#             print(grid[yy][xx], end="")
#     print()

num_accessible_rolls = 0
for yy in range(HEIGHT):
    for xx in range(WIDTH):
        if grid[yy][xx] == "@" and get_surrounding_squares(xx, yy).count("@") < 4:
            num_accessible_rolls += 1

print(num_accessible_rolls)

