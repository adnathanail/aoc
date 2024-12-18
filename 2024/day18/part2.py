from aocd.models import Puzzle
import networkx as nx

puzzle = Puzzle(year=2024, day=18)
input_data = puzzle.input_data
# input_data = """5,4
# 4,2
# 4,5
# 3,0
# 2,1
# 6,3
# 2,4
# 1,5
# 0,6
# 3,3
# 2,6
# 5,1
# 1,2
# 5,5
# 2,5
# 6,5
# 1,4
# 0,4
# 6,4
# 1,1
# 6,1
# 1,0
# 0,5
# 1,6
# 2,0"""
inp_lines = input_data.splitlines()
grid_size = 70


def generate_grid(rows):
    out = [["." for _ in range(grid_size + 1)] for _ in range(grid_size + 1)]

    for row in rows:
        x, y = [int(x) for x in row.split(",")]
        out[y][x] = "#"

    return out


def generate_graph(in_grid):
    out = nx.Graph()
    for i in range(len(in_grid)):
        for j in range(len(in_grid[i])):
            if grid[i][j] != ".":
                continue
            out.add_node((j, i))
            dirs = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
            for newi, newj in dirs:
                if 0 <= newi < len(in_grid) and 0 <= newj < len(in_grid[j]):
                    if in_grid[newi][newj] == ".":
                        out.add_node((newj, newi))
                        out.add_edge((j, i), (newj, newi))

    return out


for i in range(len(inp_lines)):
    grid = generate_grid(inp_lines[:i])

    G = generate_graph(grid)

    try:
        nx.shortest_path_length(G, (0, 0), (grid_size, grid_size))
    except nx.NetworkXNoPath:
        print(inp_lines[i - 1])
        break
