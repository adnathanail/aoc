from itertools import chain, combinations
import math

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=10)
inp = puzzle.input_data

# Parse machine data
machines = []
for row in inp.splitlines():
    row_split = row.split(" ")
    machines.append({
        "desired_state": [char == "#" for char in row_split[0][1:-1]],
        "button_wirings": [[int(v) for v in button[1:-1].split(",")] for button in row_split[1:-1]],
        "joltages": tuple(int(j) for j in row_split[-1][1:-1].split(","))
    })

# Helper function https://docs.python.org/3/library/itertools.html#itertools-recipes
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def add_tuples(t1, t2, m):
    """ Sum of 2 equal-length tuples modulo m, elementwise """
    return tuple(sum(t) % m for t in zip(t1, t2))

def run_buttons(num_lights, button_tuples_to_use):
    """
    Simulate a list of button presses
    """
    out = tuple(0 for _ in range(num_lights))
    for but in button_tuples_to_use:
        out = add_tuples(out, but, 2)
    return out

# print(run_buttons(4, [(0, 1, 0, 0), (1, 0, 1, 0)]))

def get_possible_buttons_for_desired_state(button_tuples, desired_state):
    number_of_lights = len(desired_state)
    # The powerset function returns subsets of increasing size,
    #   so the first one we find is automatically the shortest
    for buttons in powerset(button_tuples):
        if run_buttons(number_of_lights, buttons) == desired_state:
            yield buttons

# print(list(get_possible_buttons_for_desired_state([(0, 0, 1, 0), (1, 0, 1, 0), (0, 1, 0, 0)], (0, 1, 1, 0))))

def subtract_tuples(t1, t2):
    # """ Sum of 2 equal-length tuples, elementwise """
    return tuple(t[0] - t[1] for t in zip(t1, t2))

def divide_tuple(t, s):
    return [item // s for item in t]

def get_num_button_presses_for_joltages(button_tuples, joltages):
    if any([jolt < 0 for jolt in joltages]):
        return math.inf
    if set(joltages) == {0}:
        return 0
    joltage_parities = tuple(jolt % 2 for jolt in joltages)
    least_buttons = math.inf
    for buttons in get_possible_buttons_for_desired_state(button_tuples, joltage_parities):
        new_joltages = joltages
        for button in buttons:
            new_joltages = subtract_tuples(new_joltages, button)
        new_joltages = divide_tuple(new_joltages, 2)
        least_buttons = min(least_buttons, len(buttons) + (2 * get_num_button_presses_for_joltages(button_tuples, new_joltages)))
    return least_buttons

def button_wiring_to_tuple(buttons, num_lights):
    return tuple(1 if i in buttons else 0 for i in range(num_lights))

num_button_presses = 0
for machine in machines:
    print(machine)
    num_button_presses += get_num_button_presses_for_joltages([button_wiring_to_tuple(wiring, len(machine["joltages"])) for wiring in machine["button_wirings"]], machine["joltages"])

print(num_button_presses)
