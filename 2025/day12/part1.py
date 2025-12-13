from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=12)
inp = puzzle.examples[0].input_data

PRESENT_WIDTH_HEIGHT = 3

def process_input(inpp):
    inp_split = inpp.split("\n\n")

    present_shapes_str = inp_split[:-1]
    presents = []
    for pss in present_shapes_str:
        present_lines = pss.split("\n")[1:]
        present_coords = []
        for y in range(PRESENT_WIDTH_HEIGHT):
            for x in range(PRESENT_WIDTH_HEIGHT):
                if present_lines[y][x] == "#":
                    present_coords.append((x, y))
        presents.append(frozenset(present_coords))

    regions = []
    for region in inp_split[-1].splitlines():
        size_str, present_tally_str = region.split(": ")
        regions.append((
            tuple(int(x) for x in size_str.split("x")),
            tuple(int(x) for x in present_tally_str.split(" "))
        ))

    return presents, regions

def print_grid(present_coords, *, width=PRESENT_WIDTH_HEIGHT, height=PRESENT_WIDTH_HEIGHT):
    for y in range(height):
        for x in range(width):
            if (x, y) in present_coords:
                print("#", end="")
            else:
                print(".", end="")
        print()

def rotate_present_right(present_coords):
    return frozenset((2-coord[1], coord[0]) for coord in present_coords)

def flip_present_horizontally(present_coords):
    return frozenset((2-coord[0], coord[1]) for coord in present_coords)

def get_all_versions_of_present(present_coords):
    flipped_present = flip_present_horizontally(present_coords)
    out = set([present_coords, flipped_present])
    for _ in range(3):
        present_coords = rotate_present_right(present_coords)
        out.add(present_coords)
    for _ in range(3):
        flipped_present = rotate_present_right(flipped_present)
        out.add(flipped_present)
    return out

press, regs = process_input(inp)

# for pres in get_all_versions_of_present(press[3]):
#     print_grid(pres)
#     print()

def offset_present(present_coords, x_offset, y_offset):
    return frozenset((coord[0] + x_offset, coord[1] + y_offset) for coord in present_coords)

# def attempt_placement(current_placement, presents, region_width, region_height, placement_tally):
#     if placement_tally == 0:
#         return #current_placement
#     # print_grid(current_placement.union(presents[0]), width=region_width, height=region_height)
#     for x_offset in range(0, region_width - PRESENT_WIDTH_HEIGHT + 1):
#         for y_offset in range(0, region_width - PRESENT_WIDTH_HEIGHT + 1):
#             new_placement = current_placement.union(offset_present(presents[0], x_offset, y_offset))
#             print_grid(new_placement, width=region_width, height=region_height)
#             print()
#             print(new_placement.intersection(offset_present(rotate_present_right(rotate_present_right(presents[0])), 1, 1)))
#             break
#             attempt_placement(new_placement, presents, region_width, region_height, placement_tally - 1)
#             # new_placement = current_placement.union(offset_present(presents[0], x_offset, y_offset))
#             # print_grid(current_placement.union(offset_present(presents[0], x_offset, y_offset)), width=region_width, height=region_height)
#         break

# def attempt_placement(current_placement, presents, region_width, region_height, placement_tally):
#     if placement_tally == 0:
#         return current_placement
#     # print_grid(current_placement.union(presents[0]), width=region_width, height=region_height)
#     print_grid(current_placement, width=region_width, height=region_height)
#     for present_coords in get_all_versions_of_present(presents[0]):
#         for x_offset in range(0, region_width - PRESENT_WIDTH_HEIGHT + 1):
#             for y_offset in range(0, region_width - PRESENT_WIDTH_HEIGHT + 1):
#                 present_to_place = offset_present(present_coords, x_offset, y_offset)
#                 if current_placement.intersection(present_to_place) == set():
#                     maybe_working_arrangement = attempt_placement(current_placement.union(present_to_place), presents, region_width, region_height, placement_tally - 1)
#                     print(maybe_working_arrangement)
#                     if maybe_working_arrangement:
#                         return maybe_working_arrangement
#                     # if working_arrangement := attempt_placement(current_placement.union(present_to_place), presents, region_width, region_height, placement_tally - 1):
#                     #     return working_arrangement
#                 # new_placement = current_placement.union(offset_present(present_coords, x_offset, y_offset))
#                 # print_grid(new_placement, width=region_width, height=region_height)
#                 # print()
#                 # print(new_placement.intersection(offset_present(rotate_present_right(rotate_present_right(presents[0])), 1, 1)))
#                 # break
#                 # attempt_placement(new_placement, presents, region_width, region_height, placement_tally - 1)
#                 # # new_placement = current_placement.union(offset_present(presents[0], x_offset, y_offset))
#                 # # print_grid(current_placement.union(offset_present(presents[0], x_offset, y_offset)), width=region_width, height=region_height)
#     return False

def attempt_placement(current_placement, presents, region_width, region_height, placement_tally):
    if placement_tally == 0:
        return current_placement
    print_grid(current_placement, width=region_width, height=region_height)
    for present_coords in get_all_versions_of_present(presents[4]):
        for x_offset in range(0, region_width - PRESENT_WIDTH_HEIGHT + 1):
            for y_offset in range(0, region_width - PRESENT_WIDTH_HEIGHT + 1):
                present_to_place = offset_present(present_coords, x_offset, y_offset)
                if current_placement.intersection(present_to_place) == set():
                    maybe_working_arrangement = attempt_placement(current_placement.union(present_to_place), presents, region_width, region_height, placement_tally - 1)
                    if maybe_working_arrangement:
                        print(11, placement_tally, present_coords)
                        return maybe_working_arrangement
    return False


for region in regs:
    wh, pts = region
    # region_width, region_height = wh
    print_grid(attempt_placement(set(), press, wh[0], wh[1], 2), width=wh[0], height=wh[1])
    # region_placements = set()
    # region_placements = region_placements.union(press[0])
    # print_grid(region_placements, width=region_width, height=region_height)
    break
# region = set()
# print(press[0])
# print(region.union(press[0]))