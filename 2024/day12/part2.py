import math
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=12)
input_data = puzzle.input_data
grid = input_data.splitlines()


def get_potential_locations_from_loc(loc):
    """
    Given a loc, return the 4 surrounding locs (left, right, up, down)
    """
    return [(loc[0] - 1, loc[1]), (loc[0] + 1, loc[1]), (loc[0], loc[1] - 1), (loc[0], loc[1] + 1)]


def location_valid(loc):
    """
    Given a loc, return whether it is within the bounds of the grid or not
    """
    return 0 <= loc[0] < len(grid[0]) and 0 <= loc[1] < len(grid)


def explore(loc, current_block_locs):
    """
    Given a loc, recursively look in all directions for any contiguous locs containing the same character
    Also add any locs with different characters yet to be explored to the to_explore set
    And keep track of which locs have been explored by adding them to the explored set
    And ignoring any locs already explored
    """
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


def get_perimeter_locs(region):
    """
    Given a region (set of locs), return a set of locs of the perimeter of the region
    Floats are used to represent the spaces between grid rows/cols
    Perimeters hug tightly to their regions, so a loc of (1.4, 4) means a perimeter between x values of 1 and 2 on row 4,
      and the region is found on the left hand side of the perimeter (because 1.4 is closer to 1 than 2)
    """
    perimeter = set()
    for loc in region:
        for new_loc in get_potential_locations_from_loc(loc):
            if loc[0] == new_loc[0]:
                per_loc_x = loc[0]
            else:
                per_loc_x = (loc[0] + new_loc[0]) / 2
                # Make perimeter hug region
                if loc[0] < new_loc[0]:
                    per_loc_x -= 0.1
                else:
                    per_loc_x += 0.1
            if loc[1] == new_loc[1]:
                per_loc_y = loc[1]
            else:
                per_loc_y = (loc[1] + new_loc[1]) / 2
                # Make perimeter hug region
                if loc[1] < new_loc[1]:
                    per_loc_y -= 0.1
                else:
                    per_loc_y += 0.1

            if location_valid(new_loc):
                if grid[loc[1]][loc[0]] != grid[new_loc[1]][new_loc[0]]:
                    perimeter.add((per_loc_x, per_loc_y))
            else:
                perimeter.add((per_loc_x, per_loc_y))
    return perimeter


def count_contiguous_nums(nums):
    """
    Given a list of numbers, return how many separate contiguous sets of numbers there are
    E.g. 1,2,3,6,7,10 contains 3 separate contiguous sets: 1,2,3 and 6,7 and 10
    """
    sorted_nums = sorted(nums)
    out = 0
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i] + 1 != sorted_nums[i + 1]:
            out += 1
    return out + 1


def get_perimeter(region):
    """
    Given a region, calculate the length of the perimeter
    """
    locs = get_perimeter_locs(region)
    x_vals = set([x for (x, _) in locs if isinstance(x, float)])
    y_vals = set([y for (_, y) in locs if isinstance(y, float)])

    out = 0
    for x in x_vals:
        out += count_contiguous_nums([loc[1] for loc in locs if loc[0] == x])

    for y in y_vals:
        out += count_contiguous_nums([loc[0] for loc in locs if loc[1] == y])

    return out


def get_area(region):
    """
    Given a region, calculate the area
    """
    return len(region)


explored = set()
to_explore = {(0, 0)}

tot = 0
while to_explore:
    region = explore(to_explore.pop(), set())
    tot += get_perimeter(region) * get_area(region)

print(tot)
