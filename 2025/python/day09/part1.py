from math import sqrt, inf, prod
from scipy.cluster.hierarchy import DisjointSet

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=9)
inp = puzzle.input_data

red_tile_coords = [[int(v) for v in row.split(",")] for row in inp.splitlines()]

def get_square_size(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


largest_square_size = 0
for i in range(len(red_tile_coords) - 1):
    for j in range(i + 1, len(red_tile_coords)):
        largest_square_size = max(largest_square_size, get_square_size(red_tile_coords[i], red_tile_coords[j]))

print(largest_square_size)