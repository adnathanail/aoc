from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=1)

elf_totals = []
current_elf_total = 0
for line in puzzle.input_data.split("\n"):
    if line == "":
        elf_totals.append(current_elf_total)
        current_elf_total = 0
    else:
        current_elf_total += int(line)
elf_totals.append(current_elf_total)

print(sum(sorted(elf_totals)[-3:]))
