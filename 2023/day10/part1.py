from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=10)

grid = []
for row in puzzle.input_data.splitlines():
    grid.append([char for char in row])

start = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)

def get_potential_nexts(loc):
    char = grid[loc[0]][loc[1]]

    if char == "|":
        return [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1])]
    elif char == "-":
        return [(loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]
    elif char == "L":
        return [(loc[0], loc[1] + 1), (loc[0] - 1, loc[1])]
    elif char == "J":
        return [(loc[0], loc[1] - 1), (loc[0] - 1, loc[1])]
    elif char == "7":
        return [(loc[0], loc[1] - 1), (loc[0] + 1, loc[1])]
    elif char == "F":
        return [(loc[0], loc[1] + 1), (loc[0] + 1, loc[1])]

    return []

def get_next_location(loc, prev_loc):
    potential_nexts = get_potential_nexts(loc)

    potential_nexts.remove(prev_loc)

    if len(potential_nexts) != 1:
        raise Exception(f"Invalid number of nexts: {potential_nexts}")

    return potential_nexts[0]

curr = start

# Looking in the 4 directions from the start, if one of them has the start as a potential prev(/next),
# then that is a valid next location from the start
for delt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    potential_next = (start[0] + delt[0], start[1] + delt[1])
    potential_next_potential_prevs = get_potential_nexts(potential_next)
    if start in potential_next_potential_prevs:
        curr = potential_next
        prev = start

n = 0
while grid[curr[0]][curr[1]] != "S":
    new = get_next_location(curr, prev)
    prev = curr
    curr = new
    n += 1

print((n // 2) + 1)