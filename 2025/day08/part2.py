from math import sqrt, inf, prod
from scipy.cluster.hierarchy import DisjointSet

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=8)
inp = puzzle.input_data
num_rounds = 1000

junction_boxes = [[int(n) for n in row.split(",")] for row in inp.splitlines()]

def euc_dist(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2 + (a[2] - b[2])**2)

distance_lookup = {}

for i in range(len(junction_boxes) - 1):
    distance_lookup[i] = {}
    for j in range(i + 1, len(junction_boxes)):
        distance_lookup[i][j] = euc_dist(junction_boxes[i], junction_boxes[j])

connections = []
connected_components = DisjointSet(list(range(len(junction_boxes))))

for fdh in range(num_rounds):
    closest_points = None
    shortest_distance = inf
    for i in distance_lookup:
        for j in distance_lookup[i]:
            if distance_lookup[i][j] < shortest_distance and (i, j) not in connections:
                shortest_distance = distance_lookup[i][j]
                closest_points = (i, j)

    connections.append(closest_points)
    connected_components.merge(closest_points[0], closest_points[1])

print(prod(sorted([len(cc) for cc in connected_components.subsets()])[-3:]))