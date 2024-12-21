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

the_path = generate_path(start)

print("Finding cheats")
cheats = list_cheats()
print(len(cheats), "found")

print("Testing cheats")
num_good_cheats = 0
for cheat in cheats:
    time_saved = abs(the_path.index(cheat[0]) - the_path.index(cheat[1])) - 2
    if time_saved >= 100:
        num_good_cheats += 1

print(num_good_cheats)

print("Time taken", time.time() - start_time)


# for c in cheats:
#     for i in range(len(grid)):
#         for j in range(len(grid)):
#             if (j, i) in c:
#                 print("C", end="")
#             else:
#                 print(grid[i][j], end="")
#         print()
#     input()