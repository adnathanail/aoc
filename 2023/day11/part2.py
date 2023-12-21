from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=11)


def find_empty_rows_and_cols(lines):
    rows = []

    for i in range(len(lines)):
        if all([ch == "." for ch in lines[i]]):
            rows.append(i)

    cols = []

    for j in range(len(lines[0])):
        if all([lines[i][j] == "." for i in range(len(lines[j]))]):
            cols.append(j)

    return rows, cols


def find_galaxies(universe):
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                galaxies.append((i, j))
    return galaxies


def galaxy_distance(a, b, rows, cols):
    EXPANSION_FACTOR = 1000000

    out = abs(a[0] - b[0]) + abs(a[1] - b[1])
    for row in rows:
        if a[0] < row < b[0] or b[0] < row < a[0]:
            out += EXPANSION_FACTOR - 1
    for col in cols:
        if a[1] < col < b[1] or b[1] < col < a[1]:
            out += EXPANSION_FACTOR - 1
    return out


universe = puzzle.input_data.split("\n")

empty_rows, empty_cols = find_empty_rows_and_cols(universe)
galaxies = find_galaxies(universe)

dist_sum = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        dist_sum += galaxy_distance(galaxies[i], galaxies[j], empty_rows, empty_cols)

print(dist_sum)
