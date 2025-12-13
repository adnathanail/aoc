from itertools import chain, combinations

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=10)
inp = puzzle.examples[0].input_data
# inp = puzzle.input_data

# Parse machine data
machines = []
for row in inp.splitlines():
    row_split = row.split(" ")
    machines.append({
        "desired_state": tuple(char == "#" for char in row_split[0][1:-1]),
        "button_wirings": [tuple(int(v) for v in button[1:-1].split(",")) for button in row_split[1:-1]],
        "joltages": tuple(int(j) for j in row_split[-1][1:-1].split(","))
    })

def button_wiring_to_tuple(buttons, num_lights):
    return tuple(1 if i in buttons else 0 for i in range(num_lights))


def add_tuples(t1, t2):
    return tuple(sum(t) for t in zip(t1, t2))

def find_smallest_presses(button_wirings, desired_joltages):
    states = [tuple(0 for _ in desired_joltages)]
    button_tuples = [button_wiring_to_tuple(button, len(desired_joltages)) for button in button_wirings]
    print(button_tuples)
    # print(button_wiring_to_tuple(button_wirings, len(desired_joltages)))
    for state in states:
        for bt in button_tuples:

    return 0


num_button_presses = 0
for machine in machines:
    num_button_presses += find_smallest_presses(machine["button_wirings"], machine["joltages"])
    break

print(num_button_presses)
