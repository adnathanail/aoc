from itertools import chain, combinations

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

num_button_presses = 0
for machine in machines:
    number_of_lights = len(machine["desired_state"])
    # The powerset function returns subsets of increasing size,
    #   so the first one we find is automatically the shortest
    for buttons in powerset(machine["button_wirings"]):
        if run_buttons(number_of_lights, buttons) == machine["desired_state"]:
            break
    num_button_presses += len(buttons)

print(num_button_presses)
