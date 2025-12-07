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

# Map of all beam locations to number of beams in that location
beams = {
    rows[0].index("S"): 1  # Get location of first beam
}

def add_beam_to_dict(beams_dict, new_beam_index, new_beam_value):
    """
    If an index is already in the dictionary, we want to add it's value to the current value instead of overwriting
    """
    if new_beam_index not in beams_dict:
        beams_dict[new_beam_index] = 0
    beams_dict[new_beam_index] += new_beam_value

for splitter_row in splitter_indexes:
    new_beams = {}
    for beam_index in beams:
        if beam_index in splitter_row:
            add_beam_to_dict(new_beams, beam_index -1, beams[beam_index])
            add_beam_to_dict(new_beams, beam_index +1, beams[beam_index])
        else:
            add_beam_to_dict(new_beams, beam_index, beams[beam_index])
    beams = new_beams

print(sum(beams.values()))