from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=1)

NUMBER_STRINGS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

total = 0


def find_num_string(line):
    current_num_index = None
    current_num = None
    for index, num in enumerate(NUMBER_STRINGS):
        if (num_index := line.find(num)) != -1:
            if current_num_index is None or num_index < current_num_index:
                current_num_index = num_index
                current_num = str(index + 1)
    return current_num


def find_num_string_reverse(line):
    current_num_index = None
    current_num = None
    for index, num in enumerate(NUMBER_STRINGS):
        if (num_index := line.rfind(num)) != -1:
            if current_num_index is None or num_index > current_num_index:
                current_num_index = num_index
                current_num = str(index + 1)
    return current_num


for line in puzzle.input_data.splitlines():
    first_num = last_num = last_num_index = None
    for index, char in enumerate(line):
        if char.isdigit():
            if first_num is None:
                first_num = char
                if (str_num := find_num_string(line[:index])) is not None:
                    first_num = str_num
            last_num = char
            last_num_index = index
    if (str_num := find_num_string_reverse(line[last_num_index + 1 :])) is not None:
        last_num = str_num
    total += int(first_num + last_num)

print(total)
