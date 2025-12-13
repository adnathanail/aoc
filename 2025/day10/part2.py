from heapq import heappush, heappop

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=10)
inp = puzzle.examples[0].input_data
# inp = puzzle.input_data
# inp = "[#....#...#] (1,2,3,4,6,7,8) (4,9) (2,3,6,7,9) (0,3,7,8) (0,3,5,8) (0,4,5,6) (4,5,6,8) (1,2,4,6,7,9) {29,3,15,31,45,32,44,31,38,28}"
inp = "[##.#] (0,1,3) (0,2) {25,12,13,12}"

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
    """ Sum of 2 equal-length tuples, elementwise """
    return tuple(sum(t) for t in zip(t1, t2))

def compare_tuples(t_smaller, t_larger):
    """ Check that every element of 1 tuple is less than or equal to the other """
    for i in range(len(t_smaller)):
        if t_smaller[i] > t_larger[i]:
            return False
    return True

def tuple_distance(t_smaller, t_larger):
    """ Get the total distance between each pair of elements across 2 tuples """
    out = 0
    for i in range(len(t_smaller)):
        out += t_larger[i] - t_smaller[i]
    return out

def find_smallest_presses(button_wirings, desired_joltages):
    start_state = tuple(0 for _ in desired_joltages)
    button_tuples = [button_wiring_to_tuple(button, len(desired_joltages)) for button in button_wirings]
    # Priority queue, ordered by "manhattan-distance" between state and desired_joltages
    states_to_visit = []
    heappush(states_to_visit, (0, start_state))
    # Dictionary of states to number of buttons to reach that state
    states = {start_state: 0}
    while desired_joltages not in states:
        # Get next state to explore
        _priority, state = heappop(states_to_visit)
        for bt in button_tuples:
            # Try all button press options
            potential_state = add_tuples(state, bt)
            # If the button press hasn't knocked us over desired_joltages
            if compare_tuples(potential_state, desired_joltages):
                # If we've already seen this state
                if potential_state in states:
                    # If the new route to it was better
                    if states[potential_state] > (states[state] + 1):
                        # Update new shorter option
                        states[potential_state] = states[state] + 1
                # If we've never seen it before
                else:
                    # Add state to dictionary
                    states[potential_state] = states[state] + 1
                    # Add state to priority queue, ordered by distance to end state
                    heappush(states_to_visit, (tuple_distance(potential_state, desired_joltages), potential_state))

    return states[desired_joltages]

num_button_presses = 0
for machine in machines:
    num_button_presses += find_smallest_presses(machine["button_wirings"], machine["joltages"])

print(num_button_presses)

# Not certain if there is potentail for shorter paths to be ignored, due to the priority queue meaning we no longer explore states in order