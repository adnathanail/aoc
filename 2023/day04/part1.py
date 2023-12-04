from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=4)

point_total = 0

for row in puzzle.input_data.splitlines():
    winning_num_str, got_num_str = row.split(":")[1].split(" | ")
    winning_nums = {int(num) for num in winning_num_str.split(" ") if num != ""}
    got_nums = {int(num) for num in got_num_str.split(" ") if num != ""}
    matching_nums = winning_nums.intersection(got_nums)
    if matching_nums:
        point_total += 2 ** (len(matching_nums) - 1)

print(point_total)