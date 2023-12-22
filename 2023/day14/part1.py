from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=14)


def roll_north(rocks):
    for i in range(len(rocks)):
        for j in range(len(rocks[i])):
            if rocks[i][j] == ".":
                for i2 in range(i + 1, len(rocks)):
                    if rocks[i2][j] == "O":
                        rocks[i][j] = "O"
                        rocks[i2][j] = "."
                        break
                    elif rocks[i2][j] == "#":
                        break


grid = [list(r) for r in puzzle.input_data.split("\n")]

roll_north(grid)

total_load = 0

for i in range(len(grid)):
    row_load = len(grid) - i
    num_rocks = len([1 for item in grid[i] if item == "O"])
    total_load += row_load * num_rocks

print(total_load)
