from aocd.models import Puzzle


"""
Optimisation based on the idea that if we just draw straight lines down from each horizontal line,
    stopping when we hit another horizontal line, we will count all the squares.
When we're travelling right, the lines below us are inside the pool, when we're travelling left, they're outside.
Instead of storing the entire grid, instead we store a list of the horizontal line segments we're going to hit.
Then, given a point, we look for the first line we will hit, and find the distance from the point to the line.
"""


DIR_MAP = ("R", "D", "L", "U")


def process_instructions(inp):
    out = []
    for row in inp.split("\n"):
        _, _, col = row.split(" ")
        out.append((DIR_MAP[int(col[-2])], int(col[2:-2], 16)))
    return out


def check_instructions_alternate_x_y(instructions):
    direc = None

    for instr in instructions:
        last_direc = direc
        direc, _ = instr
        if last_direc is not None:
            if last_direc in ["L", "R"]:
                assert direc in ["U", "D"]
            else:
                assert direc in ["L", "R"]


def get_horizontal_lines(instructions):
    loc = (0, 0)
    out = []

    for instr in instructions:
        direc, num = instr
        num = int(num)

        last_loc = loc

        match direc:
            case "R":
                loc = (loc[0], loc[1] + num)
            case "L":
                loc = (loc[0], loc[1] - num)
            case "U":
                loc = (loc[0] - num, loc[1])
            case "D":
                loc = (loc[0] + num, loc[1])

        if direc == "R":
            out.append((last_loc, loc))
        elif direc == "L":
            out.append((loc, last_loc))

    return sorted(out, key=lambda l: l[0][0])


def get_trench_length(instructions):
    out = 0
    for instr in instructions:
        _, num = instr
        out += int(num)
    return out


def dist_to_line(lines, location):
    for line in lines:
        if line[0][0] > location[0] and (line[0][1] <= location[1] <= line[1][1]):
            break
    return line[0][0] - location[0] - 1


puzzle = Puzzle(year=2023, day=18)

instrs = process_instructions(puzzle.input_data)

check_instructions_alternate_x_y(instrs)

ls = get_horizontal_lines(instrs)

loc = (0, 0)

filled = 0

for x in range(len(instrs)):
    print(instrs[x])
    direc, num = instrs[x]

    if direc == "R" and x > 0 and instrs[x - 1][0] == "D":
        print("\t", loc, dist_to_line(ls, loc))
        filled += dist_to_line(ls, loc)

    for i in range(num):
        match direc:
            case "R":
                loc = (loc[0], loc[1] + 1)
                if i < num - 1:
                    print("\t", loc, dist_to_line(ls, loc))
                    filled += dist_to_line(ls, loc)
                if i == num - 1 and instrs[x + 1][0] == "U":
                    print("\t", loc, dist_to_line(ls, loc))
                    filled += dist_to_line(ls, loc)
            case "L":
                loc = (loc[0], loc[1] - 1)
            case "U":
                loc = (loc[0] - 1, loc[1])
            case "D":
                loc = (loc[0] + 1, loc[1])

print(filled + get_trench_length(instrs))
