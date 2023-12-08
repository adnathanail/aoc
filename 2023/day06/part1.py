from math import ceil, floor

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=6)

sp = puzzle.input_data.split("\n")
times = [int(x) for x in sp[0].split(" ")[1:] if x != ""]
distances = [int(x) for x in sp[1].split(" ")[1:] if x != ""]
races = list(zip(times, distances))


# Analysis
# Let t be the total time available for the race
# Let d be the current farthest distance
# Let x be the number of milliseconds the button is held
# Then the travel time for the boat is (t - x)
# The speed is also x, so the distance travelled is (t - x)x
# We want to know when this function meets the current record
# d = (t - x)x
# This is a quadratic formula
# x^2 - tx + d = 0


def quad_form(a, b, c):
    pm = (b ** 2 - 4 * a * c) ** 0.5
    return [(-b + pm) / (2 * a), (-b - pm) / (2 * a)]


out = 1

for race in races:
    # Get the bounds of the quadratic formula
    a1, a2 = quad_form(1, -race[0], race[1])
    # Sort the bounds to numerical order
    lb, ub = min(a1, a2), max(a1, a2)
    # Round the bounds correctly
    least_ms, most_ms = floor(lb) + 1, ceil(ub) - 1
    ways_to_beat = most_ms - least_ms + 1
    out *= ways_to_beat

print(out)
