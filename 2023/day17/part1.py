import heapq
import sys
from typing import Literal

import networkx as nx
from aocd.models import Puzzle
from networkx.drawing.nx_pydot import write_dot

puzzle = Puzzle(year=2023, day=17)
inp = puzzle.input_data

# inp = """2413432311323
# 3215453535623"""

inp = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533"""

# inp = """1234
# 5678"""

GRID = [[int(x) for x in row] for row in inp.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])


Coord = tuple[int, int]


def get_surrounding_squares(coord: Coord) -> list[tuple[Coord, str]]:
    out = []
    if coord[0] > 0:
        out.append(((coord[0] - 1, coord[1]), "<"))
    if coord[0] < (GRID_WIDTH - 1):
        out.append(((coord[0] + 1, coord[1]), ">"))
    if coord[1] > 0:
        out.append(((coord[0], coord[1] - 1), "^"))
    if coord[1] < (GRID_HEIGHT - 1):
        out.append(((coord[0], coord[1] + 1), "v"))
    return out


G = nx.DiGraph()

# END = (8, 1)
END = (GRID_WIDTH - 1, GRID_HEIGHT - 1)
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        if (x, y) == (0, 0):
            continue
        print(x, y)
        for next_coord, next_dir_char in get_surrounding_squares((x, y)):
            print("\t", next_coord, next_dir_char)
            # G.add_edge((x, y), next_coord)
            # If we're going to go left or right next
            if next_dir_char in ["<", ">"]:
                # We can have been going up or down, 1-3 times
                for prev_dir_char in ["^", "v"]:
                    for prev_dir_tally in (1, 2, 3):
                        G.add_edge(
                            (x, y, prev_dir_char, prev_dir_tally),
                            (next_coord[0], next_coord[1], next_dir_char, 1),
                            weight=GRID[next_coord[1]][next_coord[0]],
                        )
            # If we're going to go up or down next
            if next_dir_char in ["^", "v"]:
                # We can have been going left or right, 1-3 times
                for prev_dir_char in ["<", ">"]:
                    for prev_dir_tally in (1, 2, 3):
                        G.add_edge(
                            (x, y, prev_dir_char, prev_dir_tally),
                            (next_coord[0], next_coord[1], next_dir_char, 1),
                            weight=GRID[next_coord[1]][next_coord[0]],
                        )
            # For previous direction tallies of 1-2, we can keep going in that direction
            for prev_dir_tally in (1, 2):
                G.add_edge(
                    (x, y, next_dir_char, prev_dir_tally),
                    (next_coord[0], next_coord[1], next_dir_char, prev_dir_tally + 1),
                    weight=GRID[next_coord[1]][next_coord[0]],
                )

G.add_edge((0, 0), (0, 1, "v", 1), weight=GRID[1][0])
G.add_edge((0, 0), (1, 0, ">", 1), weight=GRID[0][1])
for dir_char in ["^", "v", ">", "<"]:
    for dir_tally in (1, 2, 3):
        G.add_edge(
            (END[0], END[1], dir_char, dir_tally),
            END,
            weight=0,
        )

# write_dot(G, "file.dot")

print(nx.shortest_path_length(G, (0, 0), END, weight="weight"))
# outp = nx.shortest_path(G, (0, 0), END, weight="weight")
# path_coords = [(p[0], p[1]) for p in outp]

# for y in range(GRID_HEIGHT):
#     for x in range(GRID_WIDTH):
#         if (x, y) in path_coords:
#             print("p", end="")
#             # print(path[path_coords.index((x, y))], end="")
#         else:
#             print(GRID[y][x], end="")
#     print()
