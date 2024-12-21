from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=21)
input_data = puzzle.input_data
codes = input_data.splitlines()


def generate_coord_lookup(key_pad):
    coord_lookup = {}
    for i in range(len(key_pad)):
        for j in range(len(key_pad[i])):
            coord_lookup[key_pad[i][j]] = (j, i)
    return coord_lookup


def x_delta_to_chars(xd):
    if xd < 0:
        return "<" * -xd
    else:
        return ">" * xd


def y_delta_to_chars(yd):
    if yd < 0:
        return "^" * -yd
    else:
        return "v" * yd


def part_options_to_full_strs(options):
    if len(options) == 1:
        return options[0]
    out = []
    for item in options[0]:
        for end_str in part_options_to_full_strs(options[1:]):
            out.append(item + end_str)
    return out


def enter_code(key_poss, code):
    out_part_options = []
    prev_loc = key_poss["A"]
    for char in code:
        char_loc = key_poss[char]
        x_delta, y_delta = char_loc[0] - prev_loc[0], char_loc[1] - prev_loc[1]
        x_chars, y_chars = x_delta_to_chars(x_delta), y_delta_to_chars(y_delta)
        if y_delta == 0:
            out_part_options.append([x_chars + "A"])
        elif x_delta == 0:
            out_part_options.append([y_chars + "A"])
        else:
            out_part_options.append([x_chars + y_chars + "A", y_chars + x_chars + "A"])
        prev_loc = char_loc
    return part_options_to_full_strs(out_part_options)


number_key_pad = (
    ("7", "8", "9"),
    ("4", "5", "6"),
    ("1", "2", "3"),
    (None, "0", "A"),
)
number_key_pad_coord_lookup = generate_coord_lookup(number_key_pad)

robot_key_pad = ((None, "^", "A"), ("<", "v", ">"))
robot_key_pad_coord_lookup = generate_coord_lookup(robot_key_pad)


def check_instructions_dont_cross_bad_key(key_poss, code):
    loc = key_poss["A"]
    for char in code:
        if char == ">":
            loc = (loc[0] + 1, loc[1])
        elif char == "v":
            loc = (loc[0], loc[1] + 1)
        elif char == "<":
            loc = (loc[0] - 1, loc[1])
        elif char == "^":
            loc = (loc[0], loc[1] - 1)
        if loc == key_poss[None]:
            return False
    return True


# codes = ["029A", "980A", "179A", "456A", "379A"]
tot = 0
for code in codes:
    robot_1_instruction_options = [
        r1 for r1 in enter_code(number_key_pad_coord_lookup, code) if check_instructions_dont_cross_bad_key(number_key_pad_coord_lookup, r1)
    ]

    robot_2_instruction_options = []
    for r1 in robot_1_instruction_options:
        robot_2_instruction_options += [
            r2 for r2 in enter_code(robot_key_pad_coord_lookup, r1) if check_instructions_dont_cross_bad_key(robot_key_pad_coord_lookup, r2)
        ]

    robot_3_instruction_options = []
    for r2 in robot_2_instruction_options:
        robot_3_instruction_options += [
            r3 for r3 in enter_code(robot_key_pad_coord_lookup, r2) if check_instructions_dont_cross_bad_key(robot_key_pad_coord_lookup, r3)
        ]

    tot += min([len(r3) for r3 in robot_3_instruction_options]) * int(code[:-1])

print(tot)
# 189174 too high
