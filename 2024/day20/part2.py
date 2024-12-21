import time
from aocd.models import Puzzle

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


def generate_path(start):
    out = [start]
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_delta = None
    for delta in deltas:
        nnext = (start[0] + delta[0], start[1] + delta[1])
        if grid[nnext[1]][nnext[0]] == ".":
            current_delta = delta
            break
    if current_delta is None:
        raise Exception("No path from start")
    current = start
    over = False
    while not over:
        nnext = (current[0] + delta[0], current[1] + delta[1])
        if grid[nnext[1]][nnext[0]] == ".":
            current = nnext
            out.append(nnext)
        else:
            rotated_delta = (abs(current_delta[1]), abs(current_delta[0]))
            deltas_to_try = [rotated_delta, (-rotated_delta[0], -rotated_delta[1])]
            current_delta = None
            for delta in deltas_to_try:
                nnext = (current[0] + delta[0], current[1] + delta[1])
                if grid[nnext[1]][nnext[0]] == ".":
                    current_delta = delta
                    break
            if current_delta is None:
                over = True
    return out


def list_cheats():
    cheats = []
    for i in range(height):
        for j in range(width):
            if grid[i][j] != ".":
                continue
            no_jump = (j, i)
            potential_jump_dirs = [(1, 0), (0, 1)]
            for pjd in potential_jump_dirs:
                one_jump = (j + pjd[0], i + pjd[1])
                two_jump = (j + pjd[0] * 2, i + pjd[1] * 2)
                if 0 <= two_jump[0] < width and 0 <= two_jump[1] < height:
                    if grid[one_jump[1]][one_jump[0]] == "." and grid[two_jump[1]][two_jump[0]] == ".":
                        if (no_jump, two_jump) not in cheats and (two_jump, no_jump) not in cheats:
                            cheats.append((no_jump, two_jump))
    return cheats


def manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def cheat_time_saved(ch):
    return abs(the_path.index(ch[0]) - the_path.index(ch[1])) - manhattan(ch[0], ch[1])


start_time = time.time()

print("Generating grid")
grid, start, end = generate_grid()
height = len(grid)
width = len(grid[0])

print("Generating path")
the_path = generate_path(start)

print("Finding cheats")
cheats = list_cheats()
print(len(cheats), "found")

print("Testing cheats")
num_good_cheats = 0
for cheat in cheats:
    if cheat_time_saved(cheat) >= 100:
        num_good_cheats += 1

print(num_good_cheats)

print("Time taken", time.time() - start_time)
