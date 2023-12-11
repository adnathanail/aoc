from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=10)

inp = """.....
.S-7.
.|.|.
.L-J.
....."""

# inp = """-L|F7
# 7S-7|
# L|7||
# -L-J|
# L|-JF"""

# inp = """7-F7-
# .FJ|7
# SJLL7
# |F--J
# LJ.LJ"""

inp = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""

inp = """..........
.S------7.
.|F----7|.
.||OOOO||.
.||OOOO||.
.|L-7F-J|.
.|II||II|.
.L--JL--J.
.........."""

grid = []
for row in inp.splitlines():
    grid.append([char for char in row])

start = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)

def get_potential_nexts(loc):
    char = grid[loc[0]][loc[1]]

    if char == "|":
        return [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1])]
    elif char == "-":
        return [(loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]
    elif char == "L":
        return [(loc[0], loc[1] + 1), (loc[0] - 1, loc[1])]
    elif char == "J":
        return [(loc[0], loc[1] - 1), (loc[0] - 1, loc[1])]
    elif char == "7":
        return [(loc[0], loc[1] - 1), (loc[0] + 1, loc[1])]
    elif char == "F":
        return [(loc[0], loc[1] + 1), (loc[0] + 1, loc[1])]

    return []

def get_next_location(loc, prev_loc):
    potential_nexts = get_potential_nexts(loc)

    potential_nexts.remove(prev_loc)

    if len(potential_nexts) != 1:
        raise Exception(f"Invalid number of nexts: {potential_nexts}")

    return potential_nexts[0]

curr = start

# Looking in the 4 directions from the start, if one of them has the start as a potential prev(/next),
# then that is a valid next location from the start
for delt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    potential_next = (start[0] + delt[0], start[1] + delt[1])
    potential_next_potential_prevs = get_potential_nexts(potential_next)
    if start in potential_next_potential_prevs:
        curr = potential_next
        prev = start

path = [start]

n = 0
while grid[curr[0]][curr[1]] != "S":
    # print("prev", prev)
    # print("curr", curr)
    path.append(curr)
    new = get_next_location(curr, prev)
    prev = curr
    curr = new
    n += 1
    # print(curr, grid[curr[0]][curr[1]], n)

for loc in path:
    print(loc, grid[loc[0]][loc[1]])

def is_on_segment(p, q, r):
    """
    Check if point q lies on line segment 'pr'
    """
    if (q[0] <= max(p[0], r[0]) and q[0] >= min(p[0], r[0]) and
       q[1] <= max(p[1], r[1]) and q[1] >= min(p[1], r[1])):
        return True
    return False

def orientation(p, q, r):
    """
    Find orientation of ordered triplet (p, q, r).
    Returns 0 --> p, q and r are colinear
            1 --> Clockwise
            2 --> Counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0  # colinear
    elif val > 0:
        return 1  # clockwise
    else:
        return 2  # counterclockwise

def do_intersect(p1, q1, p2, q2):
    """
    Check if two line segments 'p1q1' and 'p2q2' intersect.
    """
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)

    # General case
    if (o1 != o2 and o3 != o4):
        return True

    # Special Cases
    if (o1 == 0 and is_on_segment(p1, p2, q1)):
        return True
    if (o2 == 0 and is_on_segment(p1, q2, q1)):
        return True
    if (o3 == 0 and is_on_segment(p2, p1, q2)):
        return True
    if (o4 == 0 and is_on_segment(p2, q1, q2)):
        return True

    return False


def count_inside_points(loop, grid_height, grid_width):
    inside_count = 0

    for y in range(grid_height):
        intersections = []
        for i in range(len(loop) - 1):
            if do_intersect((0, y), (grid_width, y), loop[i], loop[i + 1]):
                # Calculate the intersection points
                if loop[i][1] == loop[i + 1][1]: # Horizontal line segment
                    intersections.extend([loop[i][0], loop[i + 1][0]])
                elif loop[i][0] == loop[i + 1][0]: # Vertical line segment
                    intersections.append(loop[i][0])
                else: # Diagonal line segment
                    intersections.append(loop[i][0])

        intersections = list(set(intersections)) # Remove duplicates
        intersections.sort()
        for i in range(0, len(intersections), 2):
            if i + 1 < len(intersections):
                # Count the grid points between each pair of intersections
                inside_count += sum(1 for x in range(intersections[i], intersections[i + 1]) if (x, y) not in loop)

    return inside_count

# New loop
loop = path  # Example loop
loop.append(path[0])

# Calculate points inside
points_inside = count_inside_points(loop, len(grid), len(grid[0]))
print(points_inside)

