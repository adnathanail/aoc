from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=3)
inp = puzzle.input_data

# To find the largest N digit number,
#   we just find the largest first digit with at least N-1 more digits after it
#   then the next largest digit with N-2 digits after it
#   etc.

def find_largest_number_in_string(string_to_search, *, start_offset, end_offset):
    """
    Given a string and offsets from either end,
    return the left-most location of the highest digit
    with the start and end range
    """
    for i in range(9, -1, -1):
        if str(i) in string_to_search:
            i_index = string_to_search.find(str(i), start_offset, len(row) - end_offset)
            if i_index != -1:
                return i_index


# looking for numbers of length N
N = 12
total_joltage = 0

for row in inp.splitlines():
    inds = []  # indexes of each digit found so far
    vals = []  # values of each digit found so far
    for j in range(N, 0, -1):
        ind = find_largest_number_in_string(
            row,
            start_offset=(inds[-1] + 1) if inds else 0,  # restrict the start to the index of the previous number
            end_offset=j - 1  # restrict the end to the number of digits left to find after this one
        )
        inds.append(ind)
        vals.append(row[ind])
    total_joltage += int("".join(vals))

print(total_joltage)