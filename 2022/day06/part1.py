from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=6)

for i in range(3, len(puzzle.input_data)):
    if len(set(puzzle.input_data[i - 4 : i])) == 4:
        print(i)
        break
