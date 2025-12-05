from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=5)
inp = puzzle.input_data

ranges_str, numbers_str = inp.split("\n\n")

ranges = [tuple(int(v) for v in r.split("-")) for r in ranges_str.splitlines()]

def is_in_ranges(n):
    for range in ranges:
        if n >= range[0] and n <= range[1]:
            return True
    return False

fresh_ingredients = 0
for n_str in numbers_str.splitlines():
    if is_in_ranges(int(n_str)):
        fresh_ingredients += 1

print(fresh_ingredients)