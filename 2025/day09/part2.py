from math import sqrt, inf, prod
from scipy.cluster.hierarchy import DisjointSet

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=9)
inp = puzzle.input_data

red_tile_coords = [tuple(int(v) for v in row.split(",")) for row in inp.splitlines()]

def get_horizontal_and_vertical_lines(rtcs):
    """
    Given a list of red tile coordinates
    Joins each pair of adjacent points into a line, and organises them
      into two dictionaries, of horizontal and vertical lines, where
      the key of the dictionary is the shared coordinate (x for verticals, and
      y for horizontals) and the value of the dict is the range of the other coordinate
    """
    verts = {}
    horis = {}
    for i in range(len(rtcs)):
        a, b = rtcs[i], rtcs[(i + 1) % len(rtcs)]
        if a[0] == b[0]:
            verts[a[0]] = sorted((a[1], b[1]))
        elif a[1] == b[1]:
            horis[a[1]] = sorted((a[0], b[0]))
        else:
            raise Exception(f"Invalid line: {a} {b}")
    return verts, horis

def is_valid_square(a, b, verts, horis):
    """
    Given two coordinates, and dictionaries of horizontal and vertical
      lines, determines whether any of the lines fall within the ranges
      of the square defined by the two coordinates
    """
    xs = sorted((a[0], b[0]))
    ys = sorted((a[1], b[1]))
    for vert in verts:
        # Vertical line falls within horizontal range of the square
        if xs[0] < vert < xs[1]:
            # Vertical line crossing top edge of square
            if verts[vert][0] <= ys[0] and verts[vert][1] > ys[0]:
                return False
            # Vertical line crossing bottom edge of square
            elif verts[vert][0] < ys[1] and verts[vert][1] >= ys[1]:
                return False
    
    for hori in horis:
        # Horizontal line falls between vertical range of the square
        if ys[0] < hori < ys[1]:
            # Horizontal line crossing left edge of square
            if horis[hori][0] <= xs[0] and horis[hori][1] > xs[0]:
                return False
            # Horizontal line crossing right edge of square
            elif horis[hori][0] < xs[1] and horis[hori][1] >= xs[1]:
                return False
    return True


vertical_lines, horizontal_lines = get_horizontal_and_vertical_lines(red_tile_coords)

def get_square_size(c1, c2):
    return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


largest_square_size = 0
for i in range(len(red_tile_coords) - 1):
    for j in range(i + 1, len(red_tile_coords)):
        if is_valid_square(red_tile_coords[i], red_tile_coords[j], vertical_lines, horizontal_lines):
            largest_square_size = max(largest_square_size, get_square_size(red_tile_coords[i], red_tile_coords[j]))

print(largest_square_size)

# Squares from example, incorrectly marked as valid,
#   due to not correctly dealing with being "inside" vs "outside" the shape
# 7,1 2,3
# 9,7 2,5