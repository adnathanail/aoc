from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=11)
inp = puzzle.input_data

cables = {}
for row in inp.splitlines():
    cable_from, cable_to_str = row.split(": ")
    cables[cable_from] = cable_to_str.split(" ")

def follow_cables(start_cable, end_cable):
    out = 0
    for c in cables[start_cable]:
        if c == end_cable:
            out += 1
        else:
            out += follow_cables(c, end_cable)
    return out

print(follow_cables("you", "out"))