use std::collections::HashSet;

advent_of_code::solution!(12, 1);

const PRESENT_WIDTH_HEIGHT: usize = 3;
const NUM_PRESENTS: usize = 6;
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
    let mut present_coords_clone = present_coords.clone();
    for _ in 0..4 {
        present_coords_clone = rotate_present_right(&present_coords_clone);
        out.insert(present_coords_clone.clone());
    }
    present_coords_clone = flip_present_horizontally(&present_coords_clone);
    out.insert(present_coords_clone.clone());
    for _ in 0..3 {
        present_coords_clone = rotate_present_right(&present_coords_clone);
        out.insert(present_coords_clone.clone());
    }
    out
}

#[hotpath::measure]
fn offset_present(
    present_coords: &PresentCoords,
    x_offset: usize,
    y_offset: usize,
) -> PresentCoords {
    let mut out = [(0, 0); PRESENT_WIDTH_HEIGHT * PRESENT_WIDTH_HEIGHT];
    for i in 0..present_coords.1 {
        out[i] = (
            present_coords.0[i].0 + x_offset,
            present_coords.0[i].1 + y_offset,
        )
    }
    (out, present_coords.1)
}

#[hotpath::measure]
fn no_crossover(present_coords: &PresentCoords, present_placement: &PresentPlacement) -> bool {
    for i in 0..present_coords.1 {
        if present_placement.contains(&present_coords.0[i]) {
            return false;
        }
    }
    true
}

type PresentPlacement = HashSet<Coord>;

#[hotpath::measure]
fn attempt_placement(
    presents: &Vec<PresentCoords>,
    all_present_versions: &Vec<HashSet<PresentCoords>>,
    current_placement: PresentPlacement,
    region_width: usize,
    region_height: usize,
    present_ids_to_place: &[usize],
) -> Option<PresentPlacement> {
    if present_ids_to_place.is_empty() {
        return Some(current_placement);
    }
    // Short circuit when there aren't enough spaces left on the grid to place
    let squares_to_place: usize = present_ids_to_place
        .iter()
        .map(|pid| presents[*pid].1)
        .sum();
    if (current_placement.len() + squares_to_place) > region_height * region_width {
        return None;
    }
    for present_coords in &all_present_versions[present_ids_to_place[0]] {
        for x_offset in 0..(region_width - PRESENT_WIDTH_HEIGHT + 1) {
            for y_offset in 0..(region_height - PRESENT_WIDTH_HEIGHT + 1) {
                let present_to_place = offset_present(&present_coords, x_offset, y_offset);
                if no_crossover(&present_to_place, &current_placement) {
                    let ptp_set: PresentPlacement = present_to_place.0.into_iter().collect();
                    let current_placement_plus_ptp: PresentPlacement =
                        current_placement.union(&ptp_set).copied().collect();
                    if let Some(maybe_working_arrangement) = attempt_placement(
                        presents,
                        all_present_versions,
                        current_placement_plus_ptp,
                        region_width,
                        region_height,
                        &present_ids_to_place[1..],
                    ) {
                        return Some(maybe_working_arrangement);
                    }
                }
            }
        }
    }
    None
}

pub fn part_one(input: &str) -> Option<u64> {
    let (presents, regions) = process_input(input);
    let all_present_versions: Vec<HashSet<PresentCoords>> = presents
        .iter()
        .map(|present_coords| get_all_versions_of_present(&present_coords))
        .collect();
    let mut tot = 0;
    for region in regions {
        println!("{:?}", region);
        let (reg_width, reg_height, present_tallies) = region;
        let mut pids_to_place_this_region: Vec<usize> = vec![];
        for (i, present_tally) in present_tallies.iter().enumerate() {
            for _ in 0..*present_tally {
                pids_to_place_this_region.push(i)
            }
        }
        if attempt_placement(
            &presents,
            &all_present_versions,
            HashSet::new(),
            reg_width,
            reg_height,
            &pids_to_place_this_region,
        )
        .is_some()
        {
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
