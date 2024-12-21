import time
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=21)
input_data = puzzle.input_data
codes = input_data.splitlines()


def generate_coord_lookup(key_pad):
    """
    Given a keypad grid, return a dictionary mapping a key's text to its coord on the keypad
    """
    coord_lookup = {}
    for i in range(len(key_pad)):
        for j in range(len(key_pad[i])):
            coord_lookup[key_pad[i][j]] = (j, i)
    return coord_lookup


def delta_to_chars(delta, negative_char, positive_char):
    """
    Given a delta and the corresponding characters for its positive and negative values, return a string telling a robot how to enter that delta
    E.g. moving left 3 spaces: (-3, "<", ">") gives "<<<"
    """
    if delta < 0:
        return negative_char * -delta
    else:
        return positive_char * delta


def part_options_to_full_strs(options):
    """
    Given a list of lists, where each member list is a series of options of strings that could appear there, return a list of all possible strings resulting from all combinations
    E.g. [["a", "b"], ["c", "d"]] gives ["ac", "ad", "bc", "bd"]
    """
    if not options:
        return []

    results = options[0]

    # Iterate through remaining sets of options
    for option_set in options[1:]:
        new_results = []
        # For each existing partial result
        for partial in results:
            # Combine it with each new option
            for option in option_set:
                new_results.append(partial + option)
        results = new_results

    return results


def enter_code(key_poss, code):
    """
    Given a key label to coord lookup map, and a desired sequence of key presses, return all possible direct robot instructions that achieve this
        this function can return instructions that cross the empty key (i.e. invalid instructions)
        a "direct" robot instruction is one that doesn't backtrack, e.g. to go 1 space right it wouldn't return "^>v", it would just return "v"
    """
    out_part_options = []
    prev_loc = key_poss["A"]
    for char in code:
        char_loc = key_poss[char]
        x_delta, y_delta = char_loc[0] - prev_loc[0], char_loc[1] - prev_loc[1]
        x_chars, y_chars = delta_to_chars(x_delta, "<", ">"), delta_to_chars(y_delta, "^", "v")
        if y_delta == 0:
            out_part_options.append([x_chars + "A"])
        elif x_delta == 0:
            out_part_options.append([y_chars + "A"])
        else:
            out_part_options.append([x_chars + y_chars + "A", y_chars + x_chars + "A"])
        prev_loc = char_loc
    return part_options_to_full_strs(out_part_options)


def check_instructions_dont_cross_bad_key(coord_lookup, code):
    """
    Given a series of instructions, and the relevant keypad, check the path given doesn't cross the empty key
    """
    x, y = coord_lookup["A"]
    bad_key_poss = coord_lookup[None]

    for char in code:
        if char == ">":
            x += 1
        elif char == "v":
            y += 1
        elif char == "<":
            x -= 1
        elif char == "^":
            y -= 1
        if (x, y) == bad_key_poss:
            return False
    return True


def get_valid_instructions(coord_lookup, code):
    """
    Given a list of codes to attempt to input and a coord lookup, return all possible instructions to input this code
    """
    return [inst for inst in enter_code(coord_lookup, code) if check_instructions_dont_cross_bad_key(coord_lookup, inst)]


rc_cache = {}
def enter_robot_code(code):
    """
    Enter a code specifically to the robot key pads
        caches code chunks
    """
    code_chunks = code.split("A")
    out = ""
    for i in range(len(code_chunks) - 1):
        chunk = code_chunks[i] + "A"
        # print(chunk)
        if chunk in rc_cache:
            out += rc_cache[chunk]
        else:
            ch = get_valid_instructions(robot_key_pad_coord_lookup, chunk)[0]
            rc_cache[chunk] = ch
            out += ch
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
    ("<", "v", ">"),
)
robot_key_pad_coord_lookup = generate_coord_lookup(robot_key_pad)


start_time = time.time()

intermediate_robots = 2

tot = 0
for code in codes:
    robot_instruction_options = get_valid_instructions(number_key_pad_coord_lookup, code)

    for i in range(intermediate_robots):
        new_options = []
        for opt in robot_instruction_options:
            new_options.append(enter_robot_code(opt))
        robot_instruction_options = new_options

    tot += min([len(r3) for r3 in robot_instruction_options]) * int(code[:-1])

print(tot)

print("Time", time.time() - start_time)
