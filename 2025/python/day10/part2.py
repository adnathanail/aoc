# Credit to this post for a beautiful idea
# https://www.reddit.com/r/adventofcode/comments/1pk87hl/2025_day_10_part_2_bifurcate_your_way_to_victory/

from itertools import chain, combinations
from functools import cache
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

@cache
def add_tuples(t1, t2, m):
    """ Sum of 2 equal-length tuples modulo m, elementwise """
    return tuple(sum(t) % m for t in zip(t1, t2))

@cache
def run_buttons(num_lights, button_tuples_to_use):
    """
    Simulate a list of button presses
    """
    out = tuple(0 for _ in range(num_lights))
    for but in button_tuples_to_use:
        out = add_tuples(out, but, 2)
    return out

@cache
def get_possible_buttons_for_desired_state(button_tuples, binary_desired_state):
    """
    Given a list of button tuples, and a desired state (consisting of only 0's and 1's)
      returns all possible button presses that reach that desired state
    """
    number_of_lights = len(binary_desired_state)
    return [
        # The powerset function returns subsets of increasing size, so the first one we find is automatically the shortest
        buttons for buttons in powerset(button_tuples)
        if run_buttons(number_of_lights, buttons) == binary_desired_state
    ]

@cache
def subtract_tuples(t1, t2):
    """
    Subtract one tuple from another, equal-length, tuple, elementwise
    """
    return tuple(t[0] - t[1] for t in zip(t1, t2))

def int_divide_tuple(t, s):
    """
    Integer-divide a tuple by a scalar, elementwise
    """
    return tuple(item // s for item in t)

def get_num_button_presses_for_joltages(button_tuples, joltages):
    """
    For given lists of button tuples and joltages, return the minimum number of button presses
      required to achieve the desired joltages
    """
    # Can't have negative joltages
    if any([jolt < 0 for jolt in joltages]):
        return math.inf
    # If the joltages are all 0, we don't need to press any buttons
    if set(joltages) == {0}:
        return 0
    # To find all button presses required to make all the joltage numbers even,
    #   get a list of the "parity" (0 for even 1 for odd) of the joltages
    joltage_parities = tuple(jolt % 2 for jolt in joltages)
    least_buttons = math.inf
    # Find all the button presses that make our joltages even
    for buttons in get_possible_buttons_for_desired_state(button_tuples, joltage_parities):
        # Apply the button presses to the joltages
        new_joltages = joltages
        for button in buttons:
            new_joltages = subtract_tuples(new_joltages, button)
        # Divide the new joltages by 2, to obtain a new set of target joltages, potentially with new odd joltages
        new_joltages = int_divide_tuple(new_joltages, 2)
        # - Find the number of button presses required to make the new joltages
        # - Multiply it by 2, to account for the fact that we halved the targets
        # - And add the number of button presses we used, to make the joltages even
        least_buttons = min(least_buttons, len(buttons) + (2 * get_num_button_presses_for_joltages(button_tuples, new_joltages)))
    return least_buttons

def button_wiring_to_tuple(buttons, num_lights):
    """
    Convert a list of button indexes, to a tuple representing that button
    E.g.
    buttons=[0, 2], num=lights=4 -> (1, 0, 1, 0)
    """
    return tuple(1 if i in buttons else 0 for i in range(num_lights))

num_button_presses = 0
for machine in machines:
    # print(machine)
    num_button_presses += get_num_button_presses_for_joltages(tuple(button_wiring_to_tuple(wiring, len(machine["joltages"])) for wiring in machine["button_wirings"]), machine["joltages"])

print(num_button_presses)
