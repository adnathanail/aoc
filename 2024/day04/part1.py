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


def count_xmas_from_point(puz, y, x):
    possible_xmas_matches = []
    possible_xmas_matches.append(get_substr_from_xy_range(puz, y, y, x, x + 4))  # Right
    possible_xmas_matches.append(get_substr_from_xy_range(puz, y, y, x - 3, x + 1))  # Left
    possible_xmas_matches.append(get_substr_from_xy_range(puz, y, y + 4, x, x))  # Down
    possible_xmas_matches.append(get_substr_from_xy_range(puz, y - 3, y + 1, x, x))  # Up

    possible_xmas_matches.append(get_substr_from_xy_range(puz, y, y + 4, x, x + 4))  # Bottom right
    possible_xmas_matches.append(get_substr_from_xy_range(puz, y, y + 4, x, x - 4))  # Bottom left
    possible_xmas_matches.append(get_substr_from_xy_range(puz, y, y - 4, x, x + 4))  # Top right
    possible_xmas_matches.append(get_substr_from_xy_range(puz, y, y - 4, x, x - 4))  # Top left
    return possible_xmas_matches.count("XMAS") + possible_xmas_matches.count("SAMX")


def count_xmas_in_puzzle(puz):
    tot = 0
    for i in range(len(puz)):
        for j in range(len(puz[i])):
            if puz[i][j] == "X":
                tot += count_xmas_from_point(puz, i, j)
    return tot


print(count_xmas_in_puzzle(input_data.split("\n")))
