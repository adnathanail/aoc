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


def find_points_with_manhattan_distance(point, dist):
    if dist == 0:
        return []
    out = []
    for i in range(dist + 1):
        a, b = i, dist - i
        out.append((point[0] + a, point[1] + b))
        out.append((point[0] + a, point[1] - b))
        out.append((point[0] - a, point[1] + b))
        out.append((point[0] - a, point[1] - b))
    out += find_points_with_manhattan_distance(point, dist - 1)
    return out


def list_cheats():
    cheats = set()
    for i in range(height):
        for j in range(width):
            if grid[i][j] != ".":
                continue
            no_jump = (j, i)
            for jump in find_points_with_manhattan_distance(no_jump, 20):
                if 0 <= jump[0] < width and 0 <= jump[1] < height:
                    if grid[jump[1]][jump[0]] == ".":
                        cheats.add(tuple(sorted([no_jump, jump])))
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


# points = find_points_with_manhattan_distance((25, 25), 20)
# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if (j, i) in points:
#             print("X", end="")
#         else:
#             print(grid[i][j], end="")
#     print()