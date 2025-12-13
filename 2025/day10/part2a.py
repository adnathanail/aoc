from itertools import chain, combinations
import math

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=10)
# inp = puzzle.examples[0].input_data
inp = puzzle.input_data

# Parse machine data
machines = []
for row in inp.splitlines():
    row_split = row.split(" ")
    machines.append({
        "desired_state": [char == "#" for char in row_split[0][1:-1]],
        "button_wirings": [[int(v) for v in button[1:-1].split(",")] for button in row_split[1:-1]],
        "joltages": [int(j) for j in row_split[-1][1:-1].split(",")]
    })

# Helper function https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def run_buttons(num_lights, buttons_to_push):
    """
    Simulate a list of button presses
    """
    out = [False for _ in range(num_lights)]
    for but in buttons_to_push:
        for i in but:
            out[i] = not out[i]
    return out

def get_possible_buttons_for_desired_state(button_wirings, desired_state):
    number_of_lights = len(desired_state)
    # The powerset function returns subsets of increasing size,
    #   so the first one we find is automatically the shortest
    for buttons in powerset(button_wirings):
        if run_buttons(number_of_lights, buttons) == desired_state:
            yield buttons

def get_num_button_presses_for_joltages(button_wirings, joltages):
    if any([jolt < 0 for jolt in joltages]):
        return math.inf
    if set(joltages) == {0}:
        return 0
    odd_joltages = [bool(jolt % 2) for jolt in joltages]
    possible_buttons_for_even_joltages = get_possible_buttons_for_desired_state(button_wirings, odd_joltages)
    least_buttons = math.inf
    for buttons in possible_buttons_for_even_joltages:
        new_joltages = joltages.copy()
        for button in buttons:
            for wire in button:
                new_joltages[wire] -= 1
        for i in range(len(new_joltages)):
            new_joltages[i] = new_joltages[i] // 2
        least_buttons = min(least_buttons, len(buttons) + (2 * get_num_button_presses_for_joltages(button_wirings, new_joltages)))
    return least_buttons

num_button_presses = 0
for machine in machines:
    print(machine)
    num_button_presses += get_num_button_presses_for_joltages(machine["button_wirings"], machine["joltages"])

print(num_button_presses)
