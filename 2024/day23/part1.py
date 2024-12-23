from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=23)
input_data = puzzle.input_data


cons = {}

intersections = []
for con in input_data.splitlines():
    f, t = con.split("-")
    if f not in cons:
        cons[f] = set()
    cons[f].add(t)
    if t not in cons:
        cons[t] = set()
    cons[t].add(f)
    for inter in cons[f].intersection(cons[t]):
        intersections.append((f, t, inter))

intersections_with_ts = [inter for inter in intersections if any([x[0] == "t" for x in inter])]

print(len(intersections_with_ts))
