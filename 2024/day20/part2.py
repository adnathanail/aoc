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


def generate_grid():
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


def generate_graph():
    out = nx.Graph()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                continue
            out.add_node((j, i))
            dirs = [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]
            for newi, newj in dirs:
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[j]):
                    if grid[newi][newj] == ".":
                        out.add_node((newj, newi))
                        out.add_edge((j, i), (newj, newi))

    return out


def list_cheats():
    cheats = []
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != ".":
                continue
            potential_jump_dirs = [(1, 0), (0, 1)]
            for pjd in potential_jump_dirs:
                no_jump = (j, i)
                one_jump = (j + pjd[0], i + pjd[1])
                two_jump = (j + pjd[0] * 2, i + pjd[1] * 2)
                three_jump = (j + pjd[0] * 3, i + pjd[1] * 3)
                if 0 <= two_jump[0] < width and 0 <= two_jump[1] < height:
                    if grid[one_jump[1]][one_jump[0]] == "#":
                        if grid[two_jump[1]][two_jump[0]] == ".":
                            if (no_jump, two_jump) not in cheats and (two_jump, no_jump) not in cheats:
                                cheats.append((no_jump, two_jump))
                        if 0 <= three_jump[0] < width and 0 <= three_jump[1] < height:
                            if grid[two_jump[1]][two_jump[0]] == "#" and grid[three_jump[1]][three_jump[0]] == ".":
                                if (no_jump, three_jump) not in cheats and (three_jump, no_jump) not in cheats:
                                    cheats.append((no_jump, three_jump))
    return cheats

start_time = time.time()

print("Generating grid")
grid, start, end = generate_grid()
height = len(grid)
width = len(grid[0])

print("Generating graph")
graph = generate_graph()

print("Finding cheats")
cheats = list_cheats()
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