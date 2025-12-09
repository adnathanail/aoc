from math import sqrt, inf, prod
from scipy.cluster.hierarchy import DisjointSet

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=9)
inp = puzzle.examples[0].input_data

def get_green_tile_coords(rtcs):
    out = []
    for n in range(0, len(rtcs)):
        m = (n + 1) % len(rtcs)
        n_rtc = rtcs[n]
        m_rtc = rtcs[m]
        if n_rtc[0] == m_rtc[0]:
            # x-vals same -> vertical
            y_vals = sorted([n_rtc[1], m_rtc[1]])
            out.extend([(n_rtc[0], y) for y in range(y_vals[0] + 1, y_vals[1])])
        elif n_rtc[1] == m_rtc[1]:
            # y-vals same -> horizontal
            x_vals = sorted([n_rtc[0], m_rtc[0]])
            out.extend([(x, n_rtc[1]) for x in range(x_vals[0] + 1, x_vals[1])])
        else:
            raise Exception(f"Cannot make line between coords {n_rtc} and {m_rtc}")
    return out

def find_internal_point(per, *, max_x, max_y):
    out = []
    for j in range(max_y + 1):
        inside = False
        for i in range(max_x + 1):
            if inside:
                if (i, j) in per:
                    inside = False
                else:
                    return (i, j)
            else:
                if (i, j) in per:
                    inside = True

    return out

def get_coordinates_for_each_direction(coord):
    return [
        (coord[0], coord[1] + 1),
        (coord[0], coord[1] - 1),
        (coord[0] + 1, coord[1]),
        (coord[0] - 1, coord[1]),
    ]

def flood_fill(per, start_x, start_y):
    checklist = [(start_x, start_y)]
    checked = []
    out = []
    while checklist:
        to_check = checklist.pop()
        if to_check not in per:
            out.append(to_check)
        checked.append(to_check)
        for dir_co in get_coordinates_for_each_direction(to_check):
            if dir_co not in per and dir_co not in checked:
                checklist.append(dir_co)
    return out

def print_grid(rtcs, gtcs, *, max_x, max_y, x_padding=2, y_padding=1):
    for j in range(max_y + 1 + y_padding):
        for i in range(max_x + 1 + x_padding):
            if (i, j) in rtcs:
                print("#", end="")
            elif (i, j) in gtcs:
                print("X", end="")
            else:
                print(".", end="")
        print()

red_tile_coords = [tuple(int(v) for v in row.split(",")) for row in inp.splitlines()]
green_tile_coords = get_green_tile_coords(red_tile_coords)

maximum_x = max(t[0] for t in red_tile_coords)
maximum_y = max(t[1] for t in red_tile_coords)

perimeter = red_tile_coords + green_tile_coords

start_point = find_internal_point(perimeter, max_x=maximum_x, max_y=maximum_y)
green_tile_coords.extend(flood_fill(perimeter, start_point[0], start_point[1]))

print_grid(red_tile_coords, green_tile_coords, max_x=maximum_x, max_y=maximum_y)

# def get_square_size(c1, c2):
#     return (abs(c1[0] - c2[0]) + 1) * (abs(c1[1] - c2[1]) + 1)


# largest_square_size = 0
# for i in range(len(red_tile_coords) - 1):
#     for j in range(i + 1, len(red_tile_coords)):
#         largest_square_size = max(largest_square_size, get_square_size(red_tile_coords[i], red_tile_coords[j]))

# print(largest_square_size)