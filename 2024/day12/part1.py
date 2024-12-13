import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=12)
input_data = puzzle.input_data
grid = input_data.splitlines()


def get_potential_locations_from_loc(loc):
    return [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]


def location_valid(loc):
    return 0 <= loc[0] < len(grid[0]) and 0 <= loc[1] < len(grid)


def explore(loc, current_block_locs):
    if loc in explored:
        return current_block_locs

    explored.add(loc)
    if loc in to_explore:
        to_explore.remove(loc)
    current_block_locs.add(loc)

    locations = [pl for pl in get_potential_locations_from_loc(loc) if location_valid(pl)]

    loc_val = grid[loc[1]][loc[0]]

    for new_loc in locations:
        if new_loc in explored:
            continue
        if grid[new_loc[1]][new_loc[0]] == loc_val:
            current_block_locs.add(new_loc)
            explore(new_loc, current_block_locs)
        else:
            to_explore.add(new_loc)
    return current_block_locs


def get_perimeter(region):
    perimeter = 0
    for loc in region:
        for new_loc in get_potential_locations_from_loc(loc):
            if location_valid(new_loc):
                if grid[loc[1]][loc[0]] != grid[new_loc[1]][new_loc[0]]:
                    perimeter += 1
            else:
                perimeter += 1
    return perimeter


def get_area(region):
    return len(region)


explored = set()
to_explore = {(0, 0)}

tot = 0
while to_explore:
    region = explore(to_explore.pop(), set())
    tot += get_perimeter(region) * get_area(region)

print(tot)
