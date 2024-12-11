import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=11)
input_data = puzzle.input_data
num_steps = 75
stones = [(int(x), num_steps) for x in input_data.split(" ")]


cache = {}


def map_stones(stone, steps, history=None):
    if history is None:
        history = tuple()

    if steps == 0:
        return 1

    if stone in cache:
        if steps in cache[stone]:
            return cache[stone][steps]

    if stone == 0:
        out = map_stones(1, steps - 1, history + (stone,))
    elif (num_length := math.floor(math.log10(stone)) + 1) % 2 == 0:
        lh_divisor = 10 ** (num_length // 2)
        left_half = stone // lh_divisor
        right_half = stone - (left_half * lh_divisor)
        out = map_stones(left_half, steps - 1, history + (stone,)) + map_stones(right_half, steps - 1, history + (stone,))
    else:
        out = map_stones(stone * 2024, steps - 1, history + (stone,))

    if stone not in cache:
        cache[stone] = {}

    cache[stone][steps] = out
    return out


out = 0
for stone in stones:
    out += map_stones(stone[0], stone[1])

print(out)
