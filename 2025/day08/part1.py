from math import sqrt, inf

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=8)
inp = puzzle.examples[0].input_data
# inp = puzzle.input_data

junction_boxes = [[int(n) for n in row.split(",")] for row in inp.splitlines()]

def euc_dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

distance_lookup = {}

for i in range(len(junction_boxes) - 1):
    distance_lookup[i] = {}
    for j in range(i + 1, len(junction_boxes)):
        distance_lookup[i][j] = euc_dist(junction_boxes[i], junction_boxes[j])

# jb_component_index_lookup = {}
# connected_components = []

closest_points = None
shortest_distance = inf
for i in distance_lookup:
    for j in distance_lookup[i]:
        print(i, j, distance_lookup[i][j])
        if distance_lookup[i][j] < shortest_distance:
            shortest_distance = distance_lookup[i][j]
            closest_points = (i, j)
# if closest_points[0] in jb_component_index_lookup:
#     if closest_points[1] in jb_component_index_lookup:

print(closest_points)
print(junction_boxes[closest_points[0]], junction_boxes[closest_points[1]])