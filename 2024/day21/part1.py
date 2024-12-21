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
        return "^" * - yd
    else:
        return "v" * yd


def enter_code(key_poss, code):
    out = ""
    prev_loc = key_poss["A"]
    for char in code:
        char_loc = key_poss[char]
        x_delta, y_delta = char_loc[0] - prev_loc[0], char_loc[1] - prev_loc[1]
        out += x_delta_to_chars(x_delta)
        out += y_delta_to_chars(y_delta)
        out += "A"
        prev_loc = char_loc
    return out

number_key_pad = (
    ("7", "8", "9"),
    ("4", "5", "6"),
    ("1", "2", "3"),
    (None, "0", "A"),
)
number_key_pad_coord_lookup = generate_coord_lookup(number_key_pad)

robot_key_pad = (
    (None, "^", "A"),
    ("<", "v", ">")
)
robot_key_pad_coord_lookup = generate_coord_lookup(robot_key_pad)

codes = ["029A", "980A", "179A", "456A", "379A"]
# codes = ["179A"]
for code in codes:
    robot_1_instructions = enter_code(number_key_pad_coord_lookup, code)
    print(robot_1_instructions)
    robot_2_instructions = enter_code(robot_key_pad_coord_lookup, robot_1_instructions)
    print(robot_2_instructions)
    robot_3_instructions = enter_code(robot_key_pad_coord_lookup, robot_2_instructions)
    print(robot_3_instructions)
    print(len(robot_3_instructions))
    print(int(code[:-1]))
    print(len(robot_3_instructions) * int(code[:-1]))
    print()