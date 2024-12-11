import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=11)
input_data = puzzle.input_data
stones = [int(x) for x in input_data.split(" ")]


def blink(inp):
    out = []
    for stone in inp:
        if stone == 0:
            out.append(1)
        elif (num_length := math.floor(math.log10(stone)) + 1) % 2 == 0:
            lh_divisor = 10 ** (num_length // 2)
            left_half = stone // lh_divisor
            right_half = stone - (left_half * lh_divisor)
            out += [left_half, right_half]
        else:
            out.append(stone * 2024)
    return out


for i in range(25):
    stones = blink(stones)
print(len(stones))
