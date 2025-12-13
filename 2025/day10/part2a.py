from itertools import chain, combinations

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=10)
inp = puzzle.examples[0].input_data

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

def get_button_presses_for_desired_state(button_wirings, desired_state):
    number_of_lights = len(desired_state)
    # The powerset function returns subsets of increasing size,
    #   so the first one we find is automatically the shortest
    for buttons in powerset(button_wirings):
        if run_buttons(number_of_lights, buttons) == desired_state:
            return buttons

def get_num_button_presses_for_joltages(button_wirings, joltages):
    if set(joltages) == {0}:
        return 0
    # print(joltages)
    odd_joltages = [bool(jolt % 2) for jolt in joltages]
    button_pushes_to_get_even_joltages = get_button_presses_for_desired_state(button_wirings, odd_joltages)
    print(button_pushes_to_get_even_joltages)
    for button in button_pushes_to_get_even_joltages:
        for wire in button:
            joltages[wire] -= 1
    # print(joltages)
    for i in range(len(joltages)):
        joltages[i] = joltages[i] // 2
    # print(joltages)
    print()
    return len(button_pushes_to_get_even_joltages) + (2 * get_num_button_presses_for_joltages(button_wirings, joltages))

num_button_presses = 0
for machine in machines[-1:]:
    print(get_num_button_presses_for_joltages(machine["button_wirings"], machine["joltages"]))
    num_button_presses += get_num_button_presses_for_joltages(machine["button_wirings"], machine["joltages"])
    # break

print(num_button_presses)
