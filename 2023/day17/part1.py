import networkx as nx
from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=17)
inp = puzzle.input_data

GRID = [[int(x) for x in row] for row in inp.splitlines()]
GRID_HEIGHT = len(GRID)
GRID_WIDTH = len(GRID[0])
END = (GRID_WIDTH - 1, GRID_HEIGHT - 1)


Coord = tuple[int, int]


def get_surrounding_squares(coord: Coord) -> list[tuple[Coord, str]]:
    """
    Given a coordinate (x, y)
    Return a list of valid surrounding coordinates, with the corresponding direction
      character >v<^
    """
    out = []
    if coord[0] > 0:
        out.append(((coord[0] - 1, coord[1]), "<"))
    if coord[0] < (GRID_WIDTH - 1):
        out.append(((coord[0] + 1, coord[1]), ">"))
    if coord[1] > 0:
        out.append(((coord[0], coord[1] - 1), "^"))
    if coord[1] < (GRID_HEIGHT - 1):
        out.append(((coord[0], coord[1] + 1), "v"))
    return out


# Create a directed graph
#   each node in the graph (except the origin) contains:
#   - coordinate (x, y)
#   - the previous direction we were going in
#   - how many steps we've been going in that direction
#   then each node is only linked up if the coordinates are adjacent, and the
#     implied path would be valid,
#   e.g. (3, 4, ">", 2) -> (4, 4, ">", 3)
#   but not (4, 4, ">", 3) -> (5, 4, ">", 4)
G = nx.DiGraph()
# Link up adjacent square in grid in graph
for y in range(GRID_HEIGHT):
    for x in range(GRID_WIDTH):
        # Don't link up the origin (we'll do this manually)
        if (x, y) == (0, 0):
            continue
        # Get every possible direction from the current position
        for next_coord, next_dir_char in get_surrounding_squares((x, y)):
            # If we're going to go left or right next
            if next_dir_char in ["<", ">"]:
                # We can have been going up or down, 1-3 times
                for prev_dir_char in ["^", "v"]:
                    for prev_dir_tally in (1, 2, 3):
                        G.add_edge(
                            (x, y, prev_dir_char, prev_dir_tally),
                            (next_coord[0], next_coord[1], next_dir_char, 1),
                            weight=GRID[next_coord[1]][next_coord[0]],
                        )
            # If we're going to go up or down next
            if next_dir_char in ["^", "v"]:
                # We can have been going left or right, 1-3 times
                for prev_dir_char in ["<", ">"]:
                    for prev_dir_tally in (1, 2, 3):
                        G.add_edge(
                            (x, y, prev_dir_char, prev_dir_tally),
                            (next_coord[0], next_coord[1], next_dir_char, 1),
                            weight=GRID[next_coord[1]][next_coord[0]],
                        )
            # For previous direction tallies of 1-2, we can keep going in that direction
            for prev_dir_tally in (1, 2):
                G.add_edge(
                    (x, y, next_dir_char, prev_dir_tally),
                    (next_coord[0], next_coord[1], next_dir_char, prev_dir_tally + 1),
                    weight=GRID[next_coord[1]][next_coord[0]],
                )

# Link up a special origin node to the only 2 places it can possible go (right and down)
G.add_edge((0, 0), (0, 1, "v", 1), weight=GRID[1][0])
G.add_edge((0, 0), (1, 0, ">", 1), weight=GRID[0][1])
# Link up every possible node representing the end point, to a special end node
#   with 0 weight
for dir_char in ["^", "v", ">", "<"]:
    for dir_tally in (1, 2, 3):
        G.add_edge(
            (END[0], END[1], dir_char, dir_tally),
            END,
            weight=0,
        )

# Find the shortest path from the origin to the end
print(nx.shortest_path_length(G, (0, 0), END, weight="weight"))
