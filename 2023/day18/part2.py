from aocd.models import Puzzle


def check_instructions_alternate_x_y(instructions):
    direc = None

    for row in instructions:
        last_direc = direc
        direc, num, col = row.split(" ")
        if last_direc is not None:
            if last_direc in ["L", "R"]:
                assert direc in ["U", "D"]
            else:
                assert direc in ["L", "R"]


def get_horizontal_lines(instructions):
    loc = (0, 0)
    out = []

    for row in instructions:
        direc, num, _col = row.split(" ")
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
    for row in instructions:
        _direc, num, _col = row.split(" ")
        out += int(num)
    return out


def dist_to_line(lines, location):
    for line in lines:
        if line[0][0] > location[0] and (line[0][1] <= location[1] <= line[1][1]):
            break
    return line[0][0] - location[0] - 1


puzzle = Puzzle(year=2023, day=18)

inp = puzzle.input_data
instrs = inp.split("\n")

check_instructions_alternate_x_y(instrs)

ls = get_horizontal_lines(instrs)

loc = (0, 0)

filled = 0

for x in range(len(instrs)):
    print(instrs[x])
    direc, num, col = instrs[x].split(" ")
    num = int(num)

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
