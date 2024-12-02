from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=2)
input_data = puzzle.input_data

reports = [[int(l) for l in r.split(" ")] for r in input_data.splitlines()]

safe_reports = 0

for r in reports:
    diffs = set()
    for i in range(len(r) - 1):
        diffs.add(r[i + 1] - r[i])
    if diffs.difference({1, 2, 3}) == set() or diffs.difference({-1, -2, -3}) == set():
        safe_reports += 1

print(safe_reports)