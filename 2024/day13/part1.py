import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=13)
input_data = puzzle.input_data


def custom_round(number):
    return math.floor(number + 0.5)


EPSILON = 0.00001


def fix_number(number):
    rounded = custom_round(number)
    if abs(rounded - number) < EPSILON:
        return rounded
    return number


def solve(a_x, a_y, b_x, b_y, prize_x, prize_y):
    """
    Created some dodgy little equations by manually rearranging simultaneous equations by hand
    Hack around floating point division precision by defining an "epsilon-closeness"
    """
    b = fix_number(((prize_x / a_x) - (prize_y / a_y)) / ((b_x / a_x) - (b_y / a_y)))
    a = fix_number((prize_x / a_x) - ((b_x / a_x) * b))
    if isinstance(a, int) and isinstance(b, int):
        return (a, b)
    else:
        return None


tot = 0
for s in input_data.split("\n\n"):
    a_row, b_row, prize_row = s.splitlines()
    a_x_str, a_y_str = a_row[10:].split(", ")
    a_x, a_y = int(a_x_str[1:]), int(a_y_str[1:])

    b_x_str, b_y_str = b_row[10:].split(", ")
    b_x, b_y = int(b_x_str[1:]), int(b_y_str[1:])

    prize_x_str, prize_y_str = prize_row[7:].split(", ")
    prize_x, prize_y = int(prize_x_str[2:]), int(prize_y_str[2:])
    sol = solve(a_x, a_y, b_x, b_y, prize_x, prize_y)
    if sol is not None:
        tot += sol[0] * 3 + sol[1]


print(tot)
