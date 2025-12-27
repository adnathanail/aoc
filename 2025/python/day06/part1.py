from math import prod

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=6)
inp = puzzle.input_data

# Parse input string into grid of values
inp_split = [[val for val in line.split(" ") if val] for line in inp.splitlines()]

WIDTH = len(inp_split[0])

# Accumulator lists for each column
vals = [[] for _ in range(WIDTH)]

# Collect values from each row for each column
for row in inp_split[:-1]:
    for i in range(WIDTH):
        vals[i].append(int(row[i]))

# Do the sums
grand_total = 0
for i in range(WIDTH):
    if inp_split[-1][i] == "+":
        grand_total += sum(vals[i])
    else:
        grand_total += prod(vals[i])

print(grand_total)
