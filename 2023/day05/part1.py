from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=5)

seeds_split, seed_soil_split, soil_fert_split, fert_water_split, water_light_split, light_temp_split, temp_humid_split, humid_loc_split = puzzle.input_data.split("\n\n")

seed_ids = [int(sid) for sid in seeds_split[7:].split(" ")]

def proc_str_to_map(proc_str):
    mmap = []
    for item in proc_str.split("\n")[1:]:
        dest_start, source_start, size = [int(num) for num in item.split(" ")]
        mmap.append([source_start, source_start + size, dest_start - source_start])

    return mmap

seed_soil_map = proc_str_to_map(seed_soil_split)
soil_fert_map = proc_str_to_map(soil_fert_split)
fert_water_map = proc_str_to_map(fert_water_split)
water_light_map = proc_str_to_map(water_light_split)
light_temp_map = proc_str_to_map(light_temp_split)
temp_humid_map = proc_str_to_map(temp_humid_split)
humid_loc_map = proc_str_to_map(humid_loc_split)

def do_map_lookup(mmap, key):
    for m in mmap:
        if m[0] <= key < m[1]:
            return key + m[2]
    return key

locs = []

for seed in seed_ids:
    soil = do_map_lookup(seed_soil_map, seed)
    fert = do_map_lookup(soil_fert_map, soil)
    water = do_map_lookup(fert_water_map, fert)
    light = do_map_lookup(water_light_map, water)
    temp = do_map_lookup(light_temp_map, light)
    humid = do_map_lookup(temp_humid_map, temp)
    loc = do_map_lookup(humid_loc_map, humid)
    locs.append(loc)

print(min(locs))