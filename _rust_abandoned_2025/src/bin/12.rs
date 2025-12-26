use std::{collections::HashSet, hash::Hash};

advent_of_code::solution!(12, 1);

const PRESENT_WIDTH_HEIGHT: usize = 3;
const NUM_PRESENTS: usize = 6;
type Coord = (usize, usize);
type PresentCoords = Vec<Coord>;
type Region = (usize, usize, [u64; NUM_PRESENTS]);

fn process_input(input: &str) -> (Vec<PresentCoords>, Vec<Region>) {
    let inp_split: Vec<&str> = input.strip_suffix("\n").unwrap().split("\n\n").collect();
    let present_coords: Vec<PresentCoords> = inp_split[0..inp_split.len() - 1]
        .iter()
        .map(|present_str| {
            let present_str_split: Vec<&str> = present_str.split("\n").collect();
            let mut out: PresentCoords = vec![];
            for y in 0..PRESENT_WIDTH_HEIGHT {
                for (x, val) in present_str_split[y + 1].chars().enumerate() {
                    if val == '#' {
                        out.push((x, y))
                    }
                }
            }
            out
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

fn rotate_present_right(present_coords: &PresentCoords) -> PresentCoords {
    present_coords
        .into_iter()
        .map(|coord| (2 - coord.1, coord.0))
        .collect()
}

fn flip_present_horizontally(present_coords: &PresentCoords) -> PresentCoords {
    present_coords
        .into_iter()
        .map(|coord| (2 - coord.0, coord.1))
        .collect()
}

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

fn offset_present(
    present_coords: &PresentCoords,
    x_offset: usize,
    y_offset: usize,
) -> PresentCoords {
    present_coords
        .into_iter()
        .map(|coord| (coord.0 + x_offset, coord.1 + y_offset))
        .collect()
}

type PresentPlacement = HashSet<Coord>;

fn attempt_placement(
    presents: &Vec<PresentCoords>,
    current_placement: PresentPlacement,
    region_width: usize,
    region_height: usize,
    present_ids_to_place: Vec<usize>,
) -> Option<PresentPlacement> {
    if present_ids_to_place.is_empty() {
        return Some(current_placement);
    }
    // # Short circuit when there aren't enough spaces left on the grid to place
    // if (len(current_placement) + sum(len(PRESS[pres_id]) for pres_id in present_ids_to_place)) > region_height * region_width:
    //     return False
    for present_coords in get_all_versions_of_present(&presents[present_ids_to_place[0]]) {
        for x_offset in 0..(region_width - PRESENT_WIDTH_HEIGHT + 1) {
            for y_offset in 0..(region_height - PRESENT_WIDTH_HEIGHT + 1) {
                let present_to_place = offset_present(&present_coords, x_offset, y_offset);
                // if present_to_place.diff current_placement == present_to_place {
                //     // maybe_working_arrangement = attempt_placement(current_placement.union(present_to_place), region_width, region_height, present_ids_to_place[1:])
                //     // if maybe_working_arrangement {
                //     //     return maybe_working_arrangement
                //     // }
                // }
            }
        }
    }
    None
}

pub fn part_one(input: &str) -> Option<u64> {
    let (present_coords, regions) = process_input(input);
    println!("{:?}", present_coords);
    println!("{:?}", regions);
    None
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
