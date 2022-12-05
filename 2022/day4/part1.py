from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=4)


def fullycovers(elfa, elfb):
    elfastart, elfaend = elfa.split("-")
    elfbstart, elfbend = elfb.split("-")
    return int(elfastart) <= int(elfbstart) and int(elfaend) >= int(elfbend)


total = 0
for row in puzzle.input_data.split("\n"):
    elf1, elf2 = row.split(",")
    if fullycovers(elf1, elf2) or fullycovers(elf2, elf1):
        total += 1

print(total)
