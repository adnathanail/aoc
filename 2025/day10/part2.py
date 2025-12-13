from itertools import chain, combinations

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=10)
inp = puzzle.examples[0].input_data
# inp = puzzle.input_data
inp = "[#....#...#] (1,2,3,4,6,7,8) (4,9) (2,3,6,7,9) (0,3,7,8) (0,3,5,8) (0,4,5,6) (4,5,6,8) (1,2,4,6,7,9) {29,3,15,31,45,32,44,31,38,28}"

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

def compare_tuples(t1, t2):
    for i in range(len(t1)):
        if t1[i] > t2[i]:
            return False
    return True

def find_smallest_presses(button_wirings, desired_joltages):
    start_state = tuple(0 for _ in desired_joltages)
    states_to_visit = set([start_state])
    states = {start_state: 0}
    button_tuples = [button_wiring_to_tuple(button, len(desired_joltages)) for button in button_wirings]
    while desired_joltages not in states:
        new_states_to_visit = set()
        for state in states_to_visit:
            for bt in button_tuples:
                potential_state = add_tuples(state, bt)
                if compare_tuples(potential_state, desired_joltages):
                    if potential_state not in states:
                        states[potential_state] = states[state] + 1
                        new_states_to_visit.add(potential_state)

        states_to_visit = new_states_to_visit
    return states[desired_joltages]


num_button_presses = 0
for machine in machines:
    num_button_presses += find_smallest_presses(machine["button_wirings"], machine["joltages"])

print(num_button_presses)
