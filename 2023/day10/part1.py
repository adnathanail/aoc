from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=10)
inp = puzzle.input_data

def get_grid(inp_str):
    out = []
    for row in inp_str.splitlines():
        out.append([char for char in row])
    return out

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return (i, j)
    raise Exception("Start not found!")


def get_potential_nexts(grid, loc):
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


def get_next_location(grid, loc, prev_loc):
    potential_nexts = get_potential_nexts(grid, loc)

    potential_nexts.remove(prev_loc)

    if len(potential_nexts) != 1:
        raise Exception(f"Invalid number of nexts: {potential_nexts}")

    return potential_nexts[0]


def get_next_after_start(grid, start):
    for delt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        potential_next = (start[0] + delt[0], start[1] + delt[1])
        potential_next_potential_prevs = get_potential_nexts(grid, potential_next)
        if start in potential_next_potential_prevs:
            return potential_next


def get_path(grid):
    prev = find_start(grid)
    curr = get_next_after_start(grid, prev)
    while grid[curr[0]][curr[1]] != "S":
        yield curr
        new = get_next_location(grid, curr, prev)
        prev = curr
        curr = new
    yield curr


def main():
    grid = get_grid(inp)

    n = 0
    for element in get_path(grid):
        n += 1

    print(max(n // 2, (n+1) // 2))  # I.e. 8 -> 4, 9 -> 5, 10 -> 5, etc.

main()
