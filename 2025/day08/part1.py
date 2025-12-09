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
    distance_lookup[i] = {}
    for j in range(i + 1, len(junction_boxes)):
        distance_lookup[i][j] = euc_dist(junction_boxes[i], junction_boxes[j])

# -- Form connected components --
# Create disjoint set, with every junction box in its own subset
#   a disjoint set provides a neat abstraction for creating groupings within a set
connected_components = DisjointSet(list(range(len(junction_boxes))))
# If a is merged with b, then b is merged with c, then according to the disjoint set a is linked to c
#   but, for this algorithm, we want to know if two junction boxes were explicitly wired together
#   so we also keep track of a list of every wire
connections = []

for _ in range(1000):
    # Find the next closest pair of junction boxes
    closest_points = None
    shortest_distance = inf
    for i in distance_lookup:
        for j in distance_lookup[i]:
            if distance_lookup[i][j] < shortest_distance and (i, j) not in connections:
                shortest_distance = distance_lookup[i][j]
                closest_points = (i, j)

    # Wire them up
    connections.append(closest_points)
    connected_components.merge(closest_points[0], closest_points[1])

connected_component_lengths = [len(cc) for cc in connected_components.subsets()]
# Print product of the sizes of the largest 3 connected components
print(prod(sorted(connected_component_lengths)[-3:]))