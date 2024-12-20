import time
from aocd.models import Puzzle
import networkx as nx

puzzle = Puzzle(year=2024, day=20)
input_data = puzzle.input_data
# input_data = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""


def generate_grid(inp):
    input_lines = input_data.splitlines()

    grid_arr = []
    start_loc = None
    end_loc = None
    for i in range(len(input_lines)):
        row = []
        for j in range(len(input_lines[i])):
            if input_lines[i][j] == "#":
                row.append("#")
            elif input_lines[i][j] == ".":
                row.append(".")
            elif input_lines[i][j] in ["S", "E"]:
                if input_lines[i][j] == "S":
                    start_loc = (j, i)
                else:
                    end_loc = (j, i)
                row.append(".")
        grid_arr.append(row)

    return grid_arr, start_loc, end_loc


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


def list_cheats(in_grid):
    cheats = []
    for i in range(len(in_grid)):
        for j in range(len(in_grid[i])):
            if in_grid[i][j] != ".":
                continue
            potential_jump_dirs = [(1, 0), (0, 1)]
            for pjd in potential_jump_dirs:
                no_jump = (j, i)
                one_jump = (j + pjd[0], i + pjd[1])
                two_jump = (j + pjd[0] * 2, i + pjd[1] * 2)
                three_jump = (j + pjd[0] * 3, i + pjd[1] * 3)
                if 0 <= one_jump[0] < len(in_grid[i]) and 0 <= one_jump[1] < len(in_grid) and 0 <= two_jump[0] < len(in_grid[i]) and 0 <= two_jump[1] < len(in_grid):
                    if in_grid[one_jump[1]][one_jump[0]] == "#":
                        if in_grid[two_jump[1]][two_jump[0]] == ".":
                            if (no_jump, two_jump) not in cheats and (two_jump, no_jump) not in cheats:
                                cheats.append((no_jump, two_jump))
                        if 0 <= three_jump[0] < len(in_grid[i]) and 0 <= three_jump[1] < len(in_grid):
                            if in_grid[two_jump[1]][two_jump[0]] == "#" and in_grid[three_jump[1]][three_jump[0]] == ".":
                                if (no_jump, three_jump) not in cheats and (three_jump, no_jump) not in cheats:
                                    cheats.append((no_jump, three_jump))
    return cheats

start_time = time.time()

print("Generating grid")
grid, start, end = generate_grid(input_data)

print("Generating graph")
graph = generate_graph(grid)

print("Finding cheats")
cheats = list_cheats(grid)
print(len(cheats), "found")

print("Testing cheats")
shortest_path_no_cheats = nx.shortest_path_length(graph, start, end)
num_good_cheats = 0
for cheat in cheats:
    time_saved = nx.shortest_path_length(graph, cheat[0], cheat[1]) - 2
    if time_saved >= 100:
        num_good_cheats += 1

print(num_good_cheats)

print("Time taken", time.time() - start_time)