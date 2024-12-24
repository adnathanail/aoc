import math
import networkx as nx
import time
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=21)
input_data = puzzle.input_data
codes = input_data.splitlines()


def generate_keypad_map(keypad):
    keypad_graph = nx.Graph()
    keypad_coord_lookup = {}

    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if keypad[i][j] is not None:
                keypad_graph.add_node(keypad[i][j])
                keypad_coord_lookup[keypad[i][j]] = (j, i)

    for i in range(len(keypad)):
        for j in range(len(keypad[i])):
            if keypad[i][j] is None:
                continue
            if i + 1 < len(keypad) and keypad[i + 1][j] is not None:
                keypad_graph.add_edge(keypad[i][j], keypad[i + 1][j])
            if j + 1 < len(keypad[i]) and keypad[i][j + 1] is not None:
                keypad_graph.add_edge(keypad[i][j], keypad[i][j + 1])

    def node_path_to_instructions(path):
        out = ""
        for i in range(len(path) - 1):
            node_a_coord = keypad_coord_lookup[path[i]]
            node_b_coord = keypad_coord_lookup[path[i + 1]]
            delta = (node_b_coord[0] - node_a_coord[0], node_b_coord[1] - node_a_coord[1])
            if delta == (1, 0):
                out += ">"
            elif delta == (0, 1):
                out += "v"
            if delta == (-1, 0):
                out += "<"
            elif delta == (0, -1):
                out += "^"
        return out

    def instructions_between_nodes(a, b):
        return [node_path_to_instructions(path) for path in nx.all_shortest_paths(keypad_graph, a, b)]

    keypad_map = {}

    for a in keypad_graph.nodes:
        keypad_map[a] = {}
        for b in keypad_graph.nodes:
            keypad_map[a][b] = instructions_between_nodes(a, b)

    return keypad_map


number_keypad = (
    ("7", "8", "9"),
    ("4", "5", "6"),
    ("1", "2", "3"),
    (None, "0", "A"),
)
number_keypad_map = generate_keypad_map(number_keypad)
robot_keypad = (
    (None, "^", "A"),
    ("<", "v", ">"),
)
robot_keypad_map = generate_keypad_map(robot_keypad)


def get_valid_instructions(code, previous="A", *, keypad_map):
    if len(code) == 1:
        return [chunk + "A" for chunk in keypad_map[previous][code[0]]]
    out = []
    for path in get_valid_instructions(code[1:], code[0], keypad_map=keypad_map):
        for chunk in keypad_map[previous][code[0]]:
            out.append(chunk + "A" + path)
    return out


shortest_instruction_length_cache = {}


def shortest_instruction_length(keys, depth):
    if depth == 0:
        return len(keys)
    if (keys, depth) in shortest_instruction_length_cache:
        return shortest_instruction_length_cache[(keys, depth)]

    total = 0
    for subKey in keys.split("A")[:-1]:
        subKey += "A"
        shortest_thing = math.inf
        for sequence in get_valid_instructions(subKey, keypad_map=robot_keypad_map):
            shortest_thing = min(shortest_instruction_length(sequence, depth - 1), shortest_thing)
        total += shortest_thing
    shortest_instruction_length_cache[(keys, depth)] = total
    return total


start_time = time.time()

intermediate_robots = 25

tot = 0
for keys in codes:
    shortest_thing = math.inf
    for sequence in get_valid_instructions(keys, keypad_map=number_keypad_map):
        shortest_thing = min(shortest_instruction_length(sequence, intermediate_robots), shortest_thing)
    tot += shortest_thing * int(keys[:-1])

print(tot)

print("Time", time.time() - start_time)
