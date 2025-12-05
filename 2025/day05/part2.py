from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=5)
inp = puzzle.input_data
inp = puzzle.examples[0].input_data

ranges_str, numbers_str = inp.split("\n\n")

ranges = [tuple(int(v) for v in r.split("-")) for r in ranges_str.splitlines()]

def merge_ranges(a1, a2, b1, b2):
    if a1 < b2 < a2:
        return True
    if b1 < a2 < b2:
        return True
    return False

def find_ranges_indexes_to_merge():
    for i in range(len(ranges) - 1):
        for j in range(i + 1, len(ranges)):
            if merge_ranges(*ranges[i], *ranges[j]):
                return (i, j)

itm = find_ranges_indexes_to_merge()

rtm1 = ranges[itm[0]]
rtm2 = ranges[itm[1]]
# print(rtm1, rtm2)
# print(min(rtm1[0], rtm2[0]), max(rtm1[1], rtm2[1]))

new_ranges = [(min(rtm1[0], rtm2[0]), max(rtm1[1], rtm2[1]))]
for i in range(len(ranges)):
    if i not in itm:
        new_ranges.append(ranges[i])

print(new_ranges)

# print(merge_ranges(10,14,12,18))
# print(merge_ranges(10,20,14,16))