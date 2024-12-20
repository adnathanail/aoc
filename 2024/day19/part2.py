from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=19)
input_data = puzzle.input_data

towels_str, patterns_str = input_data.split("\n\n")

towels = towels_str.split(", ")
patterns = patterns_str.split("\n")


cache = {}


def match_pattern(pat, tows):
    if pat in cache:
        return cache[pat]
    num = 0
    for tow in tows:
        if tow == pat[: len(tow)]:
            if len(tow) == len(pat):
                num += 1
            else:
                num += match_pattern(pat[len(tow) :], tows)
    cache[pat] = num
    return num


num = 0
for pattern in patterns:
    num += match_pattern(pattern, towels)

print(num)
