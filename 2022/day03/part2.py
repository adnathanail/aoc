from aocd.models import Puzzle
import string

puzzle = Puzzle(year=2022, day=3)

# Space so that character a has rank 1
character_ranking_string = " " + string.ascii_lowercase + string.ascii_uppercase.upper()


input_data_lines = puzzle.input_data.split("\n")
input_len = len(input_data_lines)

priorities_sum = 0
i = 0
while i < input_len // 3:
    elf1, elf2, elf3 = input_data_lines[i * 3 : (i + 1) * 3]
    shared_character = set(elf1).intersection(set(elf2)).intersection(set(elf3))
    priorities_sum += character_ranking_string.index(list(shared_character)[0])
    i += 1

print(priorities_sum)
