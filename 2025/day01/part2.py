import time
from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=1)
inp = puzzle.input_data

s = time.time()

curr_pos = 50
num_zeroes = 0
for row in inp.splitlines():
    n = int(row[1:])
    minus = row[0] == "L"
    for _ in range(n):
        if minus:
            curr_pos -= 1
        else:
            curr_pos += 1

        if curr_pos % 100 == 0:
            num_zeroes += 1

print(num_zeroes)
print(time.time() - s)