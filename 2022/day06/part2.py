from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=6)

NUM_UNIQUE = 14

for i in range(NUM_UNIQUE - 1, len(puzzle.input_data)):
    if len(set(puzzle.input_data[i - NUM_UNIQUE : i])) == NUM_UNIQUE:
        print(i)
        break
