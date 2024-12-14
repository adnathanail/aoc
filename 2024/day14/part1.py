import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=14)
input_data = puzzle.input_data
width = 101
height = 103
steps = 100


def move_n_steps(x, y, dx, dy, steps):
    return ((x + dx * steps) % width, (y + dy * steps) % height)


end_positions = []
for row in input_data.splitlines():
    pos_str, vel_str = row.split(" ")
    pos = [int(a) for a in pos_str[2:].split(",")]
    vel = [int(a) for a in vel_str[2:].split(",")]
    end_positions.append(move_n_steps(pos[0], pos[1], vel[0], vel[1], steps))


x_ranges = ((0, (width // 2) - 1), ((width // 2) + 1, width - 1))
y_ranges = ((0, (height // 2) - 1), ((height // 2) + 1, height - 1))


q_mul = 1
for xr in x_ranges:
    for yr in y_ranges:
        q = 0
        for pos in end_positions:
            if (xr[0] <= pos[0] <= xr[1]) and (yr[0] <= pos[1] <= yr[1]):
                q += 1
        q_mul *= q

print(q_mul)
