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
        x_first_bad = False
        simulating_path_loc = prev_loc
        for _ in range(abs(x_delta)):
            simulating_path_loc = (simulating_path_loc[0] + (-1 if x_delta < 0 else 1), simulating_path_loc[1])
            if simulating_path_loc == key_poss[None]:
                x_first_bad = True
        # for _ in range(abs(y_delta)):
        #     simulating_path_loc = (simulating_path_loc[0], simulating_path_loc[1] + (-1 if y_delta < 0 else 1))
        #     if simulating_path_loc == key_poss[None]:
        #         print(code, char)
        #         raise Exception("Can't cross the blank key!")
        if x_first_bad:
            out += y_delta_to_chars(y_delta)
            out += x_delta_to_chars(x_delta)
        else:
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
            raise Exception("Can't cross the bad key")

codes = ["029A", "980A", "179A", "456A", "379A"]
tot = 0
for code in codes:
    # print(code)
    robot_1_instructions = enter_code(number_key_pad_coord_lookup, code)
    # print("R1", robot_1_instructions)
    check_instructions_dont_cross_bad_key(number_key_pad_coord_lookup, robot_1_instructions)
    robot_2_instructions = enter_code(robot_key_pad_coord_lookup, robot_1_instructions)
    # print("R2", robot_2_instructions)
    check_instructions_dont_cross_bad_key(robot_key_pad_coord_lookup, robot_2_instructions)
    robot_3_instructions = enter_code(robot_key_pad_coord_lookup, robot_2_instructions)
    check_instructions_dont_cross_bad_key(robot_key_pad_coord_lookup, robot_3_instructions)
    # print("R3", robot_3_instructions)
    print(len(robot_3_instructions), int(code[:-1]), len(robot_3_instructions) * int(code[:-1]))
    print()
    tot += len(robot_3_instructions) * int(code[:-1])

print(tot)
# 189174 too high