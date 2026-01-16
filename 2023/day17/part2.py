import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=17)
inp = puzzle.input_data

GRID = [[int(x) for x in row] for row in inp.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])
END = (GRID_WIDTH - 1, GRID_HEIGHT - 1)

START = (0, 0)
MIN_JUMP = 4
MAX_JUMP = 10

Coord = tuple[int, int]


def get_squares_in_direction_in_range(
    coord: Coord, dir: str, min_dist: int, max_dist: int
) -> list[tuple[int, int, int]]:
    """
    Given
    - a coordinate (x, y)
    - a direction >v<^
    - min and max distance allowed to travel
    Return a list of valid coordinates in that direction, within the specified
      range, along with the weight of each coordinate
      (x, y, weight)
    """
    if dir == ">":
        return [
            (x, coord[1], GRID[coord[1]][x])
            for x in range(
                coord[0] + min_dist, min(coord[0] + max_dist + 1, GRID_WIDTH)
            )
        ]
    elif dir == "<":
        return [
            (x, coord[1], GRID[coord[1]][x])
            for x in range(coord[0] - min_dist, max(coord[0] - max_dist - 1, -1), -1)
        ]
    elif dir == "v":
        return [
            (coord[0], y, GRID[y][coord[0]])
            for y in range(
                coord[1] + min_dist, min(coord[1] + max_dist + 1, GRID_HEIGHT)
            )
        ]
    elif dir == "^":
        return [
            (coord[0], y, GRID[y][coord[0]])
            for y in range(coord[1] - min_dist, max(coord[1] - max_dist - 1, -1), -1)
        ]
    raise Exception(f"Invalid dir '{dir}'")


# Create a directed graph
#   each node in the graph contains:
#   - coordinate (x, y)
#   - the direction it's going in next
#   then each node is only linked up if the coordinates are within range
#     and the directions are valid
#   e.g. (3, 4, ">") -> (4, 4, "^") (4, 4, "v") (5, 4, "^") (5, 4, "v") (6, 4, "^") (6, 4, "v")
G = nx.DiGraph()
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        # Go through each possible direction we can go in
        for dir_char in [">", "v", "<", "^"]:
            # Accumulate total weights, for each step in this direction
            tot_weight = sum(
                d[2]
                for d in get_squares_in_direction_in_range(
                    (x, y), dir_char, 1, MIN_JUMP - 1
                )
            )
            for dest_x, dest_y, dest_weight in get_squares_in_direction_in_range(
                (x, y), dir_char, MIN_JUMP, MAX_JUMP
            ):
                tot_weight += dest_weight
                if dir_char in [">", "<"]:
                    G.add_edge(
                        (x, y, dir_char), (dest_x, dest_y, "^"), weight=tot_weight
                    )
                    G.add_edge(
                        (x, y, dir_char), (dest_x, dest_y, "v"), weight=tot_weight
                    )
                if dir_char in ["^", "v"]:
                    G.add_edge(
                        (x, y, dir_char), (dest_x, dest_y, ">"), weight=tot_weight
                    )
                    G.add_edge(
                        (x, y, dir_char), (dest_x, dest_y, "<"), weight=tot_weight
                    )

# Link up the origin and destination to each of the 4 direction nodes representing it (with weight 0)
for dir_char in ["^", "v", ">", "<"]:
    G.add_edge(START, (START[0], START[1], dir_char), weight=0)
    G.add_edge((END[0], END[1], dir_char), END, weight=0)

# Find the shortest path from the origin to the end
print(nx.shortest_path_length(G, (0, 0), END, weight="weight"))
