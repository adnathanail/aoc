from math import lcm

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=8)

inp_split = puzzle.input_data.splitlines()

instructions = inp_split[0]

node_map = {}
for line in inp_split[2:]:
    node_map[line[:3]] = (line[7:10], line[12:15])


def get_num_steps(current_node):
    current_instruction_index = 0
    n = 0
    while current_node[2] != "Z":
        if instructions[current_instruction_index] == "L":
            current_node = node_map[current_node][0]
        elif instructions[current_instruction_index] == "R":
            current_node = node_map[current_node][1]
        else:
            raise Exception("Invalid character")
        n += 1
        current_instruction_index += 1
        if current_instruction_index == len(instructions):
            current_instruction_index = 0

    return n


print(lcm(*[get_num_steps(n) for n in node_map.keys() if n[2] == "A"]))
