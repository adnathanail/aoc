from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=1)
inp = puzzle.input_data

curr_pos = 50
num_zeroes = 0
for line in inp.splitlines():
    n = int(line[1:])
    if line[0] == "L":
        curr_pos -= n
    else:
        curr_pos += n
    curr_pos = curr_pos % 100

    if curr_pos == 0:
        num_zeroes += 1

print(num_zeroes)