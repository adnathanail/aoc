from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=8)
input_data = puzzle.input_data
grid = input_data.split("\n")

max_y = len(grid) - 1
max_x = len(grid[0]) - 1


node_hash = {}


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] != ".":
            if grid[i][j] not in node_hash:
                node_hash[grid[i][j]] = []
            node_hash[grid[i][j]].append((i, j))

antinode_set = set()

for char in node_hash:
    for i in range(len(node_hash[char])):
        for j in range(i + 1, len(node_hash[char])):
            y_diff = node_hash[char][i][0] - node_hash[char][j][0]
            x_diff = node_hash[char][i][1] - node_hash[char][j][1]
            antinode_set.add((node_hash[char][i][0] + y_diff, node_hash[char][i][1] + x_diff))
            antinode_set.add((node_hash[char][j][0] - y_diff, node_hash[char][j][1] - x_diff))

print(len([an for an in antinode_set if 0 <= an[0] <= max_y and 0 <= an[1] <= max_x]))
