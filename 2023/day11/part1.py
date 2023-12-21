from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=11)


def expand_universe(lines):
    rows_to_be_doubled = []

    for i in range(len(lines)):
        if all([ch == "." for ch in lines[i]]):
            rows_to_be_doubled.append(i)

    cols_to_be_doubled = []

    for j in range(len(lines[0])):
        if all([lines[i][j] == "." for i in range(len(lines[j]))]):
            cols_to_be_doubled.append(j)

    out = []
    for i in range(len(lines)):
        for _ in range(2 if i in rows_to_be_doubled else 1):
            tem = []
            for j in range(len(lines[i])):
                if j in cols_to_be_doubled:
                    tem.append(".")
                tem.append(lines[i][j])
            out.append(tem)
    return out


def find_galaxies(universe):
    galaxies = []
    for i in range(len(universe)):
        for j in range(len(universe[i])):
            if universe[i][j] == "#":
                galaxies.append((i, j))
    return galaxies


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


universe = expand_universe(puzzle.input_data.split("\n"))

galaxies = find_galaxies(universe)

dist_sum = 0

for i in range(len(galaxies)):
    for j in range(i + 1, len(galaxies)):
        dist_sum += manhattan_distance(galaxies[i], galaxies[j])

print(dist_sum)
