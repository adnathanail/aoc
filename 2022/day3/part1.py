from aocd.models import Puzzle
import string

puzzle = Puzzle(year=2022, day=3)

# Space so that character a has rank 1
character_ranking_string = " " + string.ascii_lowercase + string.ascii_uppercase.upper()

priorities_sum = 0
for row in puzzle.input_data.split("\n"):
    half_row_len = len(row) // 2
    intersection = set(row[:half_row_len]).intersection(set(row[half_row_len:]))
    for char in intersection:
        priorities_sum += character_ranking_string.index(char)

print(priorities_sum)
