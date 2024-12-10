from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=10)
input_data = puzzle.input_data
rows = [[(int(cell) if cell.isnumeric() else cell) for cell in row] for row in input_data.splitlines()]


def follow_trail(grid, curr_point, prev_point=None):
    if grid[curr_point[1]][curr_point[0]] == 9:
        return set([curr_point])
    potential_next_points = [
        (curr_point[0] + 1, curr_point[1]),
        (curr_point[0] - 1, curr_point[1]),
        (curr_point[0], curr_point[1] + 1),
        (curr_point[0], curr_point[1] - 1),
    ]
    ends = set()
    for p in potential_next_points:
        if p == prev_point:
            continue
        if 0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid):
            if grid[p[1]][p[0]] == (grid[curr_point[1]][curr_point[0]] + 1):
                ends = ends.union(follow_trail(grid, p, curr_point))
    return ends


tot = 0
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == 0:
            tot += len(follow_trail(rows, (j, i)))

print(tot)
