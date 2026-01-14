from typing import Generator, Optional

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=10)
inp = puzzle.input_data
# inp = """.....
# .S-7.
# .|.|.
# .L-J.
# ....."""
inp = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

pipe_char_delta_lookup = {
    "|": ((-1, 0), (1, 0)),
    "-": ((0, -1), (0, 1)),
    "L": ((0, 1), (-1, 0)),
    "J": ((0, -1), (-1, 0)),
    "7": ((0, -1), (1, 0)),
    "F": ((0, 1), (1, 0)),
}

delta_pipe_char_lookup = {
    delta: pipe_char for (pipe_char, delta) in pipe_char_delta_lookup.items()
}

type Grid = list[list[str]]
type Coord = tuple[int, int]


def get_grid(inp_str: str) -> Grid:
    out: Grid = []
    for row in inp_str.splitlines():
        out.append([char for char in row])
    return out


def find_start(grid: Grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return (i, j)
    raise Exception("Start not found!")


def get_potential_nexts(grid: Grid, loc: Coord) -> list[Coord]:
    char = grid[loc[0]][loc[1]]
    if char == ".":
        return []
    pipe_char_delts = pipe_char_delta_lookup[char]
    return [(loc[0] + delt[0], loc[1] + delt[1]) for delt in pipe_char_delts]


def get_next_location(grid: Grid, loc: Coord, prev_loc: Optional[Coord]) -> Coord:
    potential_nexts = get_potential_nexts(grid, loc)

    if prev_loc is None:  # Pick random direction, if we have no previous_loc
        return potential_nexts[0]

    potential_nexts.remove(prev_loc)

    if len(potential_nexts) != 1:
        raise Exception(f"Invalid number of nexts: {potential_nexts}")

    return potential_nexts[0]


def detect_start_type(grid: Grid, start: Coord) -> str:
    available_dirs = []
    for delt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        potential_next = (start[0] + delt[0], start[1] + delt[1])
        potential_next_potential_prevs = get_potential_nexts(grid, potential_next)
        if start in potential_next_potential_prevs:
            available_dirs.append(delt)
    return delta_pipe_char_lookup[tuple(available_dirs)]


def get_path(grid: Grid, start: Coord) -> Generator[Coord, None, None]:
    prev: Optional[Coord] = None
    curr: Coord = start
    while curr != start or prev is None:
        yield curr
        new = get_next_location(grid, curr, prev)
        prev = curr
        curr = new
    yield curr


def print_grid(height: int, width: int, pipes: list[Coord]):
    for y in range(height):
        for x in range(width):
            if (y, x) in pipes:
                print("P", end="")
            else:
                print(".", end="")
        print()


def main():
    grid = get_grid(inp)
    start = find_start(grid)
    grid[start[0]][start[1]] = detect_start_type(grid, start)

    pipes = [element for element in get_path(grid, start)]

    print_grid(len(grid), len(grid[0]), pipes)


main()
