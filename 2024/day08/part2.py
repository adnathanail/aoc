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

            pot_node_1 = node_hash[char][i]
            while 0 <= pot_node_1[0] <= max_y and 0 <= pot_node_1[1] <= max_x:
                antinode_set.add(pot_node_1)
                pot_node_1 = (pot_node_1[0] + y_diff, pot_node_1[1] + x_diff)

            pot_node_2 = node_hash[char][j]
            while 0 <= pot_node_2[0] <= max_y and 0 <= pot_node_2[1] <= max_x:
                antinode_set.add(pot_node_2)
                pot_node_2 = (pot_node_2[0] - y_diff, pot_node_2[1] - x_diff)

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if (i, j) not in antinode_set:
#             print(grid[i][j], end="")
#         elif grid[i][j] != ".":
#             print(grid[i][j], end="")
#         else:
#             print("#", end="")
#     print()

print(len(antinode_set))
