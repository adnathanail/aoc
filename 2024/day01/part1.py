from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=1)

# Parse the input data into 2 lists of ints
list_a = []
list_b = []
for row in puzzle.input_data.splitlines():
    a, b = row.split("   ")
    list_a.append(int(a))
    list_b.append(int(b))

# Sort the 2 lists so we can easily pair up the nth smallest number in each list
list_a_sorted = sorted(list_a)
list_b_sorted = sorted(list_b)

# Get the distance between each index in each list and add to total
tot = 0
for i in range(len(list_a_sorted)):
    tot += abs(list_a_sorted[i] - list_b_sorted[i])

print(tot)
