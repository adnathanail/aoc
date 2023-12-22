from typing import Literal
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=14)


def next_cell(i, j, direction):
    if direction == "north":
        return i + 1, j
    elif direction == "south":
        return i - 1, j
    elif direction == "east":
        return i, j - 1
    elif direction == "west":
        return i, j + 1


def roll_rock(rocks, i, j, direction):
    if rocks[i][j] == ".":
        i2, j2 = i, j
        while True:
            i2, j2 = next_cell(i2, j2, direction)
            if 0 <= i2 < len(rocks) and 0 <= j2 < len(rocks[0]):
                if rocks[i2][j2] == "O":
                    rocks[i][j] = "O"
                    rocks[i2][j2] = "."
                    break
                elif rocks[i2][j2] == "#":
                    break
            else:
                break


def roll_rocks(rocks, direction: Literal["north", "south", "east", "west"]):
    height = len(rocks)
    width = len(rocks[0])

    if direction == "north":
        for i in range(height):
            for j in range(width):
                roll_rock(rocks, i, j, direction)
    elif direction == "east":
        for j in range(width - 1, -1, -1):
            for i in range(height):
                roll_rock(rocks, i, j, direction)
    elif direction == "south":
        for i in range(height - 1, -1, -1):
            for j in range(width - 1, -1, -1):
                roll_rock(rocks, i, j, direction)
    elif direction == "west":
        for j in range(width):
            for i in range(height - 1, -1, -1):
                roll_rock(rocks, i, j, direction)


def run_cycle(rocks):
    roll_rocks(rocks, "north")
    roll_rocks(rocks, "west")
    roll_rocks(rocks, "south")
    roll_rocks(rocks, "east")


def get_total_load(grid):
    out = 0

    for i in range(len(grid)):
        row_load = len(grid) - i
        num_rocks = len([1 for item in grid[i] if item == "O"])
        out += row_load * num_rocks

    return out


def hash_grid(grid):
    return "".join("".join(row) for row in grid)


def loop_til_seen(grid):
    out = 0
    seen = set()

    while True:
        run_cycle(grid)
        if hash_grid(grid) in seen:
            break
        seen.add(hash_grid(grid))
        out += 1

    return out


inp = puzzle.input_data

grid = [list(r) for r in inp.split("\n")]

n = loop_til_seen(grid)

m = loop_til_seen(grid)

x = (1000000000 - n) % m

for i in range(x - 2):
    run_cycle(grid)

print(get_total_load(grid))
