from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=15)


def HASH(st):
    curr = 0
    for char in st:
        curr += ord(char)
        curr *= 17
        curr %= 256

    return curr


tot = 0

for part in puzzle.input_data.split(","):
    tot += HASH(part)

print(tot)
