from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=10)
input_data = puzzle.input_data
rows = [[(int(cell) if cell.isnumeric() else cell) for cell in row] for row in input_data.splitlines()]


def follow_trail(grid, curr_point, prev_point=None):
    if grid[curr_point[1]][curr_point[0]] == 9:
        return 1
    potential_next_points = [
        (curr_point[0] + 1, curr_point[1]),
        (curr_point[0] - 1, curr_point[1]),
        (curr_point[0], curr_point[1] + 1),
        (curr_point[0], curr_point[1] - 1),
    ]
    tot = 0
    for p in potential_next_points:
        if p == prev_point:
            continue
        if 0 <= p[0] < len(grid[0]) and 0 <= p[1] < len(grid):
            if grid[p[1]][p[0]] == (grid[curr_point[1]][curr_point[0]] + 1):
                tot += follow_trail(grid, p, curr_point)
    return tot


tot = 0
for i in range(len(rows)):
    for j in range(len(rows[i])):
        if rows[i][j] == 0:
            rating = follow_trail(rows, (j, i))
            tot += rating

print(tot)
