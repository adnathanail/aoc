from fractions import Fraction

from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=13)
input_data = puzzle.input_data


def solve(a_x, a_y, b_x, b_y, prize_x, prize_y):
    b = (Fraction(prize_x, a_x) - Fraction(prize_y, a_y)) / (Fraction(b_x, a_x) - Fraction(b_y, a_y))
    a = Fraction(prize_x, a_x) - (Fraction(b_x, a_x) * b)
    if a.denominator == 1 and b.denominator == 1:
        return (int(a), int(b))
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
    prize_x, prize_y = int(prize_x_str[2:]) + 10000000000000, int(prize_y_str[2:]) + 10000000000000
    sol = solve(a_x, a_y, b_x, b_y, prize_x, prize_y)
    if sol is not None:
        tot += sol[0] * 3 + sol[1]


print(tot)
