from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=3)
inp = puzzle.input_data

# To find the largest 2 digit number, we just need the largest number overall
#   and then the largest number to the right of that
#   (ensuring that the first number has at least one number to the right of it)

def find_largest_number_in_string(string_to_search):
    for i in range(9, -1, -1):
        if str(i) in string_to_search:
            return string_to_search.index(str(i))


total_joltage = 0
for row in inp.splitlines():
    # Largest digit in first n-1 chars of n length string
    first_digit_index = find_largest_number_in_string(row[:len(row) - 1])
    # Largest digit after first digit
    second_digit_index = first_digit_index + find_largest_number_in_string(row[first_digit_index + 1:]) + 1
    total_joltage += int(row[first_digit_index] + row[second_digit_index])

print(total_joltage)