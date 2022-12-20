from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=4)


def partiallycovers(elfa, elfb):
    elfastart, elfaend = elfa.split("-")
    elfbstart, elfbend = elfb.split("-")
    return (int(elfbstart) <= int(elfastart) <= int(elfbend)) or (
        int(elfbstart) <= int(elfaend) <= int(elfbend)
    )


total = 0
for row in puzzle.input_data.split("\n"):
    elf1, elf2 = row.split(",")
    if partiallycovers(elf1, elf2) or partiallycovers(elf2, elf1):
        total += 1

print(total)
