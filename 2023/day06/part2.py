from math import ceil, floor

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=6)

sp = puzzle.input_data.split("\n")
time = int("".join(x for x in sp[0].split(" ")[1:] if x != ""))
distance = int("".join(x for x in sp[1].split(" ")[1:] if x != ""))


def quad_form(a, b, c):
    pm = (b**2 - 4 * a * c) ** 0.5
    return [(-b + pm) / (2 * a), (-b - pm) / (2 * a)]


# Get the bounds of the quadratic formula
a1, a2 = quad_form(1, -time, distance)
# Sort the bounds to numerical order
lb, ub = min(a1, a2), max(a1, a2)
# Round the bounds correctly
least_ms, most_ms = floor(lb) + 1, ceil(ub) - 1
ways_to_beat = most_ms - least_ms + 1

print(ways_to_beat)
