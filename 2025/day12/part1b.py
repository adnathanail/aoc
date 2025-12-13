from functools import lru_cache
from functools import cache
from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=12)
inp = puzzle.input_data

PRESENT_WIDTH_HEIGHT = 3

def process_input(inpp):
    inp_split = inpp.split("\n\n")

    present_shapes_str = inp_split[:-1]
    presents = []
    for pss in present_shapes_str:
        present_lines = pss.split("\n")[1:]
        present_coords = []
        for y in range(PRESENT_WIDTH_HEIGHT):
            for x in range(PRESENT_WIDTH_HEIGHT):
                if present_lines[y][x] == "#":
                    present_coords.append((x, y))
        presents.append(frozenset(present_coords))

    regions = []
    for region in inp_split[-1].splitlines():
        size_str, present_tally_str = region.split(": ")
        regions.append((
            tuple(int(x) for x in size_str.split("x")),
            tuple(int(x) for x in present_tally_str.split(" "))
        ))

    return presents, regions

PRESS, REGS = process_input(inp)

tot = 0
for region in REGS:
    wh, pts = region
    if sum(pts) * 9 <= wh[0] * wh[1]:
        tot += 1
print(tot)
