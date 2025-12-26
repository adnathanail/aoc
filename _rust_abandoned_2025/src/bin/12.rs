use std::collections::HashSet;

advent_of_code::solution!(12, 1);

const PRESENT_WIDTH_HEIGHT: usize = 3;
const NUM_PRESENTS: usize = 6;
const MAX_GRID_SIZE: usize = 50;

type Coord = (usize, usize);
type PresentCoords = ([Coord; PRESENT_WIDTH_HEIGHT * PRESENT_WIDTH_HEIGHT], usize);
type Region = (usize, usize, [u64; NUM_PRESENTS]);

fn process_input(input: &str) -> (Vec<PresentCoords>, Vec<Region>) {
    let inp_split: Vec<&str> = input.strip_suffix("\n").unwrap().split("\n\n").collect();
    let present_coords: Vec<PresentCoords> = inp_split[0..inp_split.len() - 1]
        .iter()
        .map(|present_str| {
            let present_str_split: Vec<&str> = present_str.split("\n").collect();
            let mut out = [(0, 0); PRESENT_WIDTH_HEIGHT * PRESENT_WIDTH_HEIGHT];
            let mut i = 0;
            for y in 0..PRESENT_WIDTH_HEIGHT {
                for (x, val) in present_str_split[y + 1].chars().enumerate() {
                    if val == '#' {
                        out[i] = (x, y);
                        i += 1;
                    }
                }
            }
            (out, i)
        })
        .collect();
    let regions: Vec<Region> = inp_split[inp_split.len() - 1]
        .split("\n")
        .map(|region_str| {
            let region_str_split: Vec<&str> = region_str.split(": ").collect();
            let dimensions_vec: Vec<&str> = region_str_split[0].split("x").collect();
            let tallies_vec: Vec<u64> = region_str_split[1]
                .split(" ")
                .map(|tally_str| tally_str.parse().unwrap())
                .collect();
            (
                dimensions_vec[0].parse().unwrap(),
                dimensions_vec[1].parse().unwrap(),
                tallies_vec.try_into().unwrap(),
            )
        })
        .collect();
    (present_coords, regions)
}

#[hotpath::measure]
fn rotate_present_right(present_coords: &PresentCoords) -> PresentCoords {
    let mut out = [(0, 0); PRESENT_WIDTH_HEIGHT * PRESENT_WIDTH_HEIGHT];
    for i in 0..present_coords.1 {
        out[i] = (2 - present_coords.0[i].1, present_coords.0[i].0)
    }
    (out, present_coords.1)
}

#[hotpath::measure]
fn flip_present_horizontally(present_coords: &PresentCoords) -> PresentCoords {
    let mut out = [(0, 0); PRESENT_WIDTH_HEIGHT * PRESENT_WIDTH_HEIGHT];
    for i in 0..present_coords.1 {
        out[i] = (2 - present_coords.0[i].0, present_coords.0[i].1)
    }
    (out, present_coords.1)
}

#[hotpath::measure]
fn get_all_versions_of_present(present_coords: &PresentCoords) -> HashSet<PresentCoords> {
    let mut out = HashSet::new();
    let mut present_coords_clone = *present_coords;
    for _ in 0..4 {
        present_coords_clone = rotate_present_right(&present_coords_clone);
        out.insert(present_coords_clone);
    }
    present_coords_clone = flip_present_horizontally(&present_coords_clone);
    out.insert(present_coords_clone);
    for _ in 0..3 {
        present_coords_clone = rotate_present_right(&present_coords_clone);
        out.insert(present_coords_clone);
    }
    out
}

#[inline]
fn coords_to_mask(present_coords: &PresentCoords, x_offset: usize, y_offset: usize) -> PresentMask {
    let mut mask: PresentMask = [(0, 0); PRESENT_WIDTH_HEIGHT];
    for i in 0..present_coords.1 {
        let x = present_coords.0[i].0 + x_offset;
        let y = present_coords.0[i].1 + y_offset;
        mask[y - y_offset].0 = y;
        mask[y - y_offset].1 |= 1u64 << x;
    }
    mask
}

// Precomputed masks for a single present: all versions × all offsets
type PrecomputedMasks = Vec<PresentMask>;

fn precompute_masks_for_present(
    all_versions: &HashSet<PresentCoords>,
    region_width: usize,
    region_height: usize,
) -> PrecomputedMasks {
    let mut masks = Vec::new();
    for present_coords in all_versions {
        for x_offset in 0..(region_width - PRESENT_WIDTH_HEIGHT + 1) {
            for y_offset in 0..(region_height - PRESENT_WIDTH_HEIGHT + 1) {
                masks.push(coords_to_mask(present_coords, x_offset, y_offset));
            }
        }
    }
    masks
}

#[inline]
fn no_crossover_mask(mask: &PresentMask, placement: &PresentPlacement) -> bool {
    mask.iter().all(|(row, bits)| (placement[*row] & bits) == 0)
}

// Row-based bitmask: one u64 per row (up to 50 bits used per row)
type PresentPlacement = [u64; MAX_GRID_SIZE];

// A present mask stored as array of (row_index, bits_in_that_row)
// Max 3 rows affected by a 3x3 present
type PresentMask = [(usize, u64); PRESENT_WIDTH_HEIGHT];

#[inline]
fn apply_mask(placement: &mut PresentPlacement, mask: &PresentMask) {
    for (row, bits) in mask {
        placement[*row] |= bits;
    }
}

fn attempt_placement(
    precomputed_masks: &[PrecomputedMasks],
    squares_per_present: &[usize],
    current_placement: PresentPlacement,
    current_count: usize,
    max_cells: usize,
    present_ids_to_place: &[usize],
) -> bool {
    if present_ids_to_place.is_empty() {
        return true;
    }
    // Short circuit when there aren't enough spaces left on the grid to place
    let squares_to_place: usize = present_ids_to_place
        .iter()
        .map(|pid| squares_per_present[*pid])
        .sum();
    if (current_count + squares_to_place) > max_cells {
        return false;
    }

    let pid = present_ids_to_place[0];
    for mask in &precomputed_masks[pid] {
        if no_crossover_mask(mask, &current_placement) {
            let mut new_placement = current_placement;
            apply_mask(&mut new_placement, mask);
            if attempt_placement(
                precomputed_masks,
                squares_per_present,
                new_placement,
                current_count + squares_per_present[pid],
                max_cells,
                &present_ids_to_place[1..],
            ) {
                return true;
            }
        }
    }
    false
}

pub fn part_one(input: &str) -> Option<u64> {
    let (presents, regions) = process_input(input);
    let all_present_versions: Vec<HashSet<PresentCoords>> =
        presents.iter().map(get_all_versions_of_present).collect();

    // Precompute squares per present (for pruning)
    let squares_per_present: Vec<usize> = presents.iter().map(|p| p.1).collect();

    let mut tot = 0;
    for region in regions {
        println!("{:?}", region);
        let (reg_width, reg_height, present_tallies) = region;

        // Precompute all masks for this region's dimensions
        let precomputed_masks: Vec<PrecomputedMasks> = all_present_versions
            .iter()
            .map(|versions| precompute_masks_for_present(versions, reg_width, reg_height))
            .collect();

        let mut pids_to_place_this_region: Vec<usize> = vec![];
        for (i, present_tally) in present_tallies.iter().enumerate() {
            for _ in 0..*present_tally {
                pids_to_place_this_region.push(i)
            }
        }

        let empty_placement: PresentPlacement = [0u64; MAX_GRID_SIZE];
        if attempt_placement(
            &precomputed_masks,
            &squares_per_present,
            empty_placement,
            0,
            reg_width * reg_height,
            &pids_to_place_this_region,
        ) {
            tot += 1
        }
    }
    Some(tot)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2));
    }
}
