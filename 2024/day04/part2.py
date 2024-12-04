from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=4)
input_data = puzzle.input_data


def get_substr_from_xy_range(puz, ymin, ymax, xmin, xmax):
    yrange = abs(ymax - ymin)
    ystep = 1 if ymin < ymax else -1
    xrange = abs(xmax - xmin)
    xstep = 1 if xmin < xmax else -1
    if yrange > 0 and xrange > 0 and yrange != xrange:
        raise Exception("X and Y ranges must be equal length, or 0")
    if yrange == 0:
        coords = [(ymin, x) for x in range(xmin, xmax, xstep)]
    elif xrange == 0:
        coords = [(y, xmin) for y in range(ymin, ymax, ystep)]
    else:
        coords = [(y, x) for (y, x) in zip(range(ymin, ymax, ystep), range(xmin, xmax, xstep))]

    return "".join(puz[y][x] for (y, x) in coords if y >= 0 and y < len(puz) and x >= 0 and x < len(puz[y]))


def x_mas_at_point(puz, y, x):
    return get_substr_from_xy_range(puz, y - 1, y + 2, x - 1, x + 2) in ["MAS", "SAM"] and get_substr_from_xy_range(puz, y + 1, y - 2, x - 1, x + 2) in [
        "MAS",
        "SAM",
    ]


def count_xmas_in_puzzle(puz):
    tot = 0
    for i in range(len(puz)):
        for j in range(len(puz[i])):
            if puz[i][j] == "A" and x_mas_at_point(puz, i, j):
                tot += 1
    return tot


print(count_xmas_in_puzzle(input_data.split("\n")))
