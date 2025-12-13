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
        presents.append(tuple(present_coords))

    regions = []
    for region in inp_split[-1].splitlines():
        size_str, present_tally_str = region.split(": ")
        regions.append((
            tuple(int(x) for x in size_str.split("x")),
            tuple(int(x) for x in present_tally_str.split(" "))
        ))

    return presents, regions

def print_present(present_coords):
    for y in range(PRESENT_WIDTH_HEIGHT):
        for x in range(PRESENT_WIDTH_HEIGHT):
            if (x, y) in present_coords:
                print("#", end="")
            else:
                print(".", end="")
        print()

def rotate_present_right(present_coords):
    return tuple((2-coord[1], coord[0]) for coord in present_coords)

def flip_present_horizontally(present_coords):
    return tuple((2-coord[0], coord[1]) for coord in present_coords)

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

pres, regs = process_input(inp)

for pres in get_all_versions_of_present(pres[2]):
    print_present(pres)
    print()
# print(pres)
# print(regs)

# # print(pres[0])
# # print(rotate_present_right(pres[0]))
# print_present(pres[0])
# print()
# print_present(flip_present_horizontally(pres[0]))
# # print()
# # print_present(rotate_present_right(rotate_present_right(pres[0])))