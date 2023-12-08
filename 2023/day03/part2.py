from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=3)


def scan_for_gear(grid, row, col):
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
            if grid[i][j] == "*":
                return (i, j)
    return None


input_data = puzzle.input_data.splitlines()

in_number = False
number_digits = ""
current_gear_coord = None

gear_numbers = {}

for i in range(len(input_data)):
    for j in range(len(input_data[i])):
        if input_data[i][j].isdigit():
            in_number = True
            number_digits += input_data[i][j]
            if current_gear_coord is None:
                current_gear_coord = scan_for_gear(input_data, i, j)
        elif in_number:
            if current_gear_coord is not None:
                if current_gear_coord not in gear_numbers:
                    gear_numbers[current_gear_coord] = []
                gear_numbers[current_gear_coord].append(int(number_digits))
            in_number = False
            current_gear_coord = None
            number_digits = ""

gear_ratio_sum = 0

for gear in gear_numbers:
    if len(gear_numbers[gear]) == 2:
        gear_ratio_sum += gear_numbers[gear][0] * gear_numbers[gear][1]

print(gear_ratio_sum)
