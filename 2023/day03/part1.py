from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=3)

def is_symbol(char):
    return (not char.isdigit()) and char != "."

def scan_for_symbols(grid, row, col):
    minx = maxx = row
    miny = maxy = col
    if row > 0:
        minx = row - 1
    if row < len(grid) - 1:
        maxx = row + 1
    if col > 0:
        miny = col - 1
    if col < len(grid[row]) - 1:
        maxy = col + 1
    for i in range(minx, maxx + 1):
        for j in range(miny, maxy + 1):
            if is_symbol(grid[i][j]):
                return True
    return False

input_data = puzzle.input_data.splitlines()

in_number = False
number_digits = ""
is_part_number = False

part_number_sum = 0

for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        if input_data[i][j].isdigit():
            in_number = True
            number_digits += input_data[i][j]
            if scan_for_symbols(input_data, i, j):
                is_part_number = True
        elif in_number:
            if is_part_number:
                part_number_sum += int(number_digits)
            in_number = False
            is_part_number = False
            number_digits = ""

print(part_number_sum)