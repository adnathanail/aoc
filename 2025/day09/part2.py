from math import sqrt, inf, prod
from scipy.cluster.hierarchy import DisjointSet

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=9)
inp = puzzle.input_data

red_tile_coords = [tuple(int(v) for v in row.split(",")) for row in inp.splitlines()]

def get_horizontal_and_vertical_lines(rtcs):
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
    xs = sorted((a[0], b[0]))
    ys = sorted((a[1], b[1]))
    for vert in verts:
        if xs[0] < vert < xs[1]:
            # print(vert, verts[vert])
            if verts[vert][0] <= ys[0] and verts[vert][1] > ys[0]:
                # print("1")
                return False
            elif verts[vert][0] < ys[1] and verts[vert][1] >= ys[1]:
                # print("2")
                return False
    
    for hori in horis:
        if ys[0] < hori < ys[1]:
            if horis[hori][0] <= xs[0] and horis[hori][1] > xs[0]:
                # print("1")
                return False
            elif horis[hori][0] < xs[1] and horis[hori][1] >= xs[1]:
                # print("2")
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

# 7,1 2,3
# 9,7 2,5