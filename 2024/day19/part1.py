from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=19)
input_data = puzzle.input_data

towels_str, patterns_str = input_data.split("\n\n")

towels = towels_str.split(", ")
patterns = patterns_str.split("\n")


def match_pattern(pat, tows):
    for tow in tows:
        if tow == pat[: len(tow)]:
            if len(tow) == len(pat):
                return True
            elif match_pattern(pat[len(tow) :], tows):
                return True
    return False


num = 0
for pattern in patterns:
    if match_pattern(pattern, towels):
        num += 1

print(num)
