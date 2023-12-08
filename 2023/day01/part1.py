from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=1)

total = 0

for line in puzzle.input_data.splitlines():
    first_num = last_num = None
    for char in line:
        if char.isdigit():
            if first_num is None:
                first_num = char
            last_num = char
    total += int(first_num + last_num)

print(total)
