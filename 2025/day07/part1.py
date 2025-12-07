from math import prod

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=7)
inp = puzzle.input_data

rows = inp.splitlines()

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

# Get list of splitter index locations on each row
# (the fancy := "walrus" operator part allows us to just ignore rows with no splitters)
splitter_indexes = [
    splitters
    for row in rows[1:]
    if (splitters := find(row, "^"))
]

# Set of all current beam indexes
beams = {rows[0].index("S")}  # Get location of first beam

num_splits = 0
for splitter_row in splitter_indexes:
    new_beams = set()
    for beam_index in beams:
        if beam_index in splitter_row:
            new_beams.add(beam_index - 1)
            new_beams.add(beam_index + 1)
            num_splits += 1
        else:
            new_beams.add(beam_index)
    beams = new_beams

print(num_splits)