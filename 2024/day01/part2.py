from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=1)

# Parse the input data into 2 lists of ints
list_a = []
list_b = []
for row in puzzle.input_data.splitlines():
    a, b = row.split("   ")
    list_a.append(int(a))
    list_b.append(int(b))

# Tally up the occurrences of each number in list b
list_b_tallies = {}
for x in list_b:
    if x not in list_b_tallies:
        list_b_tallies[x] = 0
    list_b_tallies[x] += 1

# Go through each number in list a, look up its list b tally, and add the product to the total
tot = 0
for y in list_a:
    tot += y * list_b_tallies.get(y, 0)

print(tot)