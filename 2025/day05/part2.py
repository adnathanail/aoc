from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=5)
inp = puzzle.input_data

ranges_str, numbers_str = inp.split("\n\n")

ranges = [tuple(int(v) for v in r.split("-")) for r in ranges_str.splitlines()]

def can_merge_ranges(a1, a2, b1, b2):
    """
    Check if two ranges overlap
    """
    if a1 <= b2 <= a2:
        return True
    if b1 <= a2 <= b2:
        return True
    return False

def find_ranges_indexes_to_merge():
    """
    Find the next set of mergeable ranges
    """
    for i in range(len(ranges) - 1):
        for j in range(i + 1, len(ranges)):
            if can_merge_ranges(*ranges[i], *ranges[j]):
                return (i, j)
    return None

# Go through every pair of ranges
#   if they are overlap, merge them
#   then reset and keep looking for another merge,
#   until none of the ranges overlap
while True:
    itm = find_ranges_indexes_to_merge()
    if itm is None:
        break

    rtm1 = ranges[itm[0]]
    rtm2 = ranges[itm[1]]

    new_ranges = [(min(rtm1[0], rtm2[0]), max(rtm1[1], rtm2[1]))]
    for i in range(len(ranges)):
        if i not in itm:
            new_ranges.append(ranges[i])
    ranges = new_ranges

# Once none of the ranges overlap, the number of 
#   fresh ingredients is just the sum of the size
#   of every range
fresh_ingredients = 0
for rr in ranges:
    fresh_ingredients += rr[1] - rr[0] + 1

print(fresh_ingredients)