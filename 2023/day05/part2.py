import math

from aocd.models import Puzzle

from utils import combine_maps

puzzle = Puzzle(year=2023, day=5)

(
    seeds_split,
    seed_soil_split,
    soil_fert_split,
    fert_water_split,
    water_light_split,
    light_temp_split,
    temp_humid_split,
    humid_loc_split,
) = puzzle.input_data.split("\n\n")

seed_id_strs = seeds_split[7:].split(" ")

seed_ids = []

for i in range(int(len(seed_id_strs) / 2)):
    start_id = int(seed_id_strs[i * 2])
    range_len = int(seed_id_strs[i * 2 + 1])
    seed_ids.append([start_id, start_id + range_len, 0])


def proc_str_to_map(proc_str):
    mmap = []
    for item in proc_str.split("\n")[1:]:
        dest_start, source_start, size = [int(num) for num in item.split(" ")]
        mmap.append([source_start, source_start + size, dest_start - source_start])

    mmap_sorted = sorted(mmap, key=lambda x: x[0])

    n = 0
    mmap_ind = 0
    # Insert explicit 0 map for -infinity to 0
    out = [[-math.inf, 0, 0]]

    # Insert explicit 0 maps for missing regions
    while n < mmap_sorted[-1][1]:
        if n < mmap_sorted[mmap_ind][0]:
            out.append([n, mmap_sorted[mmap_ind][0], 0])
            n = mmap_sorted[mmap_ind][1]
            out.append(mmap_sorted[mmap_ind])
            mmap_ind += 1
        else:
            out.append(mmap_sorted[mmap_ind])
            n = mmap_sorted[mmap_ind][1]
            mmap_ind += 1

    # Insert explicit 0 map the last value to infinity
    out.append([out[-1][1], math.inf, 0])
    return out


seed_soil_map = proc_str_to_map(seed_soil_split)
soil_fert_map = proc_str_to_map(soil_fert_split)
fert_water_map = proc_str_to_map(fert_water_split)
water_light_map = proc_str_to_map(water_light_split)
light_temp_map = proc_str_to_map(light_temp_split)
temp_humid_map = proc_str_to_map(temp_humid_split)
humid_loc_map = proc_str_to_map(humid_loc_split)

seed_fert_map = combine_maps(seed_soil_map, soil_fert_map)
seed_water_map = combine_maps(seed_fert_map, fert_water_map)
seed_light_map = combine_maps(seed_water_map, water_light_map)
seed_temp_map = combine_maps(seed_light_map, light_temp_map)
seed_humid_map = combine_maps(seed_temp_map, temp_humid_map)
seed_loc_map = combine_maps(seed_humid_map, humid_loc_map)

locs = []

seed_id_loc_offset_map = combine_maps(seed_ids, seed_loc_map)

lowest_loc = math.inf

for m in seed_id_loc_offset_map:
    min_proc_value_in_range = m[0] + m[2]
    if min_proc_value_in_range < lowest_loc:
        lowest_loc = min_proc_value_in_range

print(lowest_loc)
