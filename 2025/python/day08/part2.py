from math import sqrt, inf, prod
from scipy.cluster.hierarchy import DisjointSet

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=8)
inp = puzzle.input_data

# Extract list of coordinates for each junction box
junction_boxes = [[int(n) for n in row.split(",")] for row in inp.splitlines()]

# -- Cache distance between each pair of boxes --
def euc_dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

distance_lookup = {}

for i in range(len(junction_boxes) - 1):
    for j in range(i + 1, len(junction_boxes)):
        distance_lookup[(i, j)] = euc_dist(junction_boxes[i], junction_boxes[j])

# -- Form connected components --
# Sort the distance cache, so we can just run through it once,
#   instead of searching for the next closest pair every time
distances_in_increasing_order = sorted(distance_lookup.items(), key=lambda x: x[1])

# Create disjoint set, with every junction box in its own subset
connected_components = DisjointSet(list(range(len(junction_boxes))))

# Go through each pair of junction boxes, in order of increasing distance,
#   until there is just one connected component in the graph
i = -1
while len(connected_components.subsets()) > 1:
    i += 1
    connected_components.merge(*distances_in_increasing_order[i][0])

# Get the last connection made
last_connection = distances_in_increasing_order[i][0]

# Print the product of the x coordinates of the junction boxes of the last connection made
print(junction_boxes[last_connection[0]][0] * junction_boxes[last_connection[1]][0])
