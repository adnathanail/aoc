from typing import Generator, Optional

from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=10)
inp = puzzle.input_data

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
    """Parse input string to 2D array of characters"""
    out: Grid = []
    for row in inp_str.splitlines():
        out.append([char for char in row])
    return out


def find_start(grid: Grid) -> Coord:
    """Get coordinate of start character 'S'"""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                return (i, j)
    raise Exception("Start not found!")


def get_potential_nexts(grid: Grid, loc: Coord) -> list[Coord]:
    """Find adjacent pipe characters, based on the current character"""
    char = grid[loc[0]][loc[1]]
    if char == ".":
        return []
    pipe_char_delts = pipe_char_delta_lookup[char]
    return [(loc[0] + delt[0], loc[1] + delt[1]) for delt in pipe_char_delts]


def get_next_location(grid: Grid, loc: Coord, prev_loc: Optional[Coord]) -> Coord:
    """
    Given the current location and previous location, we can decide
      which of the 2 locations adjacent to the current location should
      be the "next" location
    """
    potential_nexts = get_potential_nexts(grid, loc)

    if prev_loc is None:  # Pick random direction, if we have no previous_loc
        return potential_nexts[0]

    potential_nexts.remove(prev_loc)

    if len(potential_nexts) != 1:
        raise Exception(f"Invalid number of nexts: {potential_nexts}")

    return potential_nexts[0]


def get_surrounding_squares(
    point: Coord, max_y: int, max_x: int
) -> Generator[tuple[Coord, Coord], None, None]:
    for delt in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        out = (point[0] + delt[0], point[1] + delt[1])
        if max_y > out[0] >= 0 and max_x > out[1] >= 0:  # Prevent going out of bounds
            yield out, delt


def detect_start_type(grid: Grid, start: Coord, max_y: int, max_x: int) -> str:
    available_dirs = []
    for potential_next, delt in get_surrounding_squares(start, max_y, max_x):
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


def print_grid(height: int, width: int, pipes: set[Coord], insides: set[Coord]):
    for y in range(height):
        for x in range(width):
            if (y, x) in pipes:
                print("P", end="")
            elif (y, x) in insides:
                print("X", end="")
            else:
                print(".", end="")
        print()


def pipe_to_virtual_pipe(pipe_char: str, coord: Coord) -> list[Coord]:
    center = (coord[0] * 3 + 1, coord[1] * 3 + 1)
    pipe_char_delts = pipe_char_delta_lookup[pipe_char]
    return [
        (center[0] + pipe_char_delts[0][0], center[1] + pipe_char_delts[0][1]),
        (center),
        (center[0] + pipe_char_delts[1][0], center[1] + pipe_char_delts[1][1]),
    ]


def flood_fill(pipes: set[Coord], start: Coord, max_y: int, max_x: int) -> set[Coord]:
    to_check = {start}
    out = set()
    while to_check:
        next = to_check.pop()
        out.add(next)
        for potential, _delta in get_surrounding_squares(next, max_y, max_x):
            if (
                potential not in pipes
                and potential not in out
                and potential not in to_check
            ):
                to_check.add(potential)
    return out


def get_pipe_coords(grid: Grid) -> set[Coord]:
    start = find_start(grid)
    grid[start[0]][start[1]] = detect_start_type(grid, start, len(grid), len(grid[0]))

    return {element for element in get_path(grid, start)}


def find_empty_point(max_y, max_x, pipes_coords: set[Coord]) -> Coord:
    for y in range(max_y):
        for x in range(max_x):
            if (y, x) not in pipes_coords:
                return (y, x)
    raise Exception("Couldn't find an empty point!")


def get_contiguous_points(
    grid: Grid, pipes_coords: set[Coord], fill_from_point: Coord
) -> set[Coord]:
    virtual_pipes_unflat: list[list[Coord]] = [
        pipe_to_virtual_pipe(grid[pipe[0]][pipe[1]], pipe) for pipe in pipes_coords
    ]
    virtual_pipes: set[Coord] = {x for xs in virtual_pipes_unflat for x in xs}
    insides = flood_fill(
        virtual_pipes,
        (fill_from_point[0] * 3 + 1, fill_from_point[1] * 3 + 1),
        len(grid) * 3,
        len(grid[0]) * 3,
    )

    actual_insides = set()
    for item in insides:
        if (item[0] - 1) % 3 == 0 and (item[1] - 1) % 3 == 0:
            actual_insides.add(((item[0] - 1) // 3, (item[1] - 1) // 3))
    return actual_insides


def main():
    # Parse grid
    grid = get_grid(inp)
    grid_height, grid_width = len(grid), len(grid[0])
    pipes_coords = get_pipe_coords(grid)

    # Pick a random empty point
    fill_from_point = find_empty_point(grid_height, grid_width, pipes_coords)
    # Fill all adjacent squares from that point (using virtual grid expansion, to allow "paint" to pass through adjacent parallel walls)
    filled_points = get_contiguous_points(grid, pipes_coords, fill_from_point)
    # How many points did we fill?
    print(len(filled_points))

    # The original empty point may have been outside the line, so find another empty point, not painted by the first attempt
    new_fill_from_point = find_empty_point(
        grid_height, grid_width, pipes_coords.union(filled_points)
    )
    # Fill all adjacent squares from the new point
    new_filled_points = get_contiguous_points(grid, pipes_coords, new_fill_from_point)
    # How many points this time?
    print(len(new_filled_points))

    # One of those answers will be correct
    print("Try both above (the smaller one is probably correct)")


main()
