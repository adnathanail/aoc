import heapq
import sys
from typing import Literal

import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=17)
inp = puzzle.input_data

inp = """2413432311323
3215453535623"""

GRID = [[int(x) for x in row] for row in inp.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])


# def get_surrounding_squares(coord: Coord) -> list[tuple[Coord, str]]:
#     out = []
#     if coord[0] > 0:
#         out.append(((coord[0] - 1, coord[1]), "<"))
#     if coord[0] < (GRID_WIDTH - 1):
#         out.append(((coord[0] + 1, coord[1]), ">"))
#     if coord[1] > 0:
#         out.append(((coord[0], coord[1] - 1), "^"))
#     if coord[1] < (GRID_HEIGHT - 1):
#         out.append(((coord[0], coord[1] + 1), "v"))
#     return out


G = nx.Graph()

for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        if x > 0:
            G.add_edge((x, y), (x - 1, y), weight=GRID[y][x])
        if y > 0:
            G.add_edge((x, y), (x, y - 1), weight=GRID[y][x])

# print(len(G.nodes))
# print(len(G.edges))
print(G.nodes)

path_coords = nx.shortest_path(G, (0, 0), (12, 1), weight="weight")

for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        if (x, y) in path_coords:
            print("p", end="")
            # print(path[path_coords.index((x, y))], end="")
        else:
            print(GRID[y][x], end="")
    print()
