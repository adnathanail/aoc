use std::cmp::max;
use std::collections::HashMap;

advent_of_code::solution!(9);

fn get_red_tile_coords(input: &str) -> Vec<[u32; 2]> {
    let mut out: Vec<[u32; 2]> = Vec::new();
    for line in input.lines() {
        let coord: Vec<u32> = line.split(",").map(|x| x.parse::<u32>().unwrap()).collect();
        out.push([coord[0], coord[1]]);
    }
    out
}

fn get_square_size(c1: [u32; 2], c2: [u32; 2]) -> u64 {
    let width = ((c1[0] as i64) - (c2[0] as i64)).abs() + 1;
    let height = ((c1[1] as i64) - (c2[1] as i64)).abs() + 1;
    (width * height) as u64
}

pub fn part_one(input: &str) -> Option<u64> {
    let red_tile_coords = get_red_tile_coords(input);
    let mut largest_square_size = 0;
    for i in 0..(red_tile_coords.len() - 1) {
        for j in (i + 1)..red_tile_coords.len() {
            largest_square_size = max(
                largest_square_size,
                get_square_size(red_tile_coords[i], red_tile_coords[j]),
            )
        }
    }
    Some(largest_square_size)
}

fn sort_ints_to_array(a: u32, b: u32) -> [u32; 2] {
    if a <= b { [a, b] } else { [b, a] }
}

type TilingLineMap = HashMap<u32, [u32; 2]>;

fn get_horizontal_and_vertical_lines(rtcs: &[[u32; 2]]) -> (TilingLineMap, TilingLineMap) {
    let mut verts = HashMap::new();
    let mut horis = HashMap::new();
    for i in 0..rtcs.len() {
        let a = rtcs[i];
        let b = rtcs[(i + 1) % rtcs.len()];
        if a[0] == b[0] {
            verts.insert(a[0], sort_ints_to_array(a[1], b[1]));
        } else if a[1] == b[1] {
            horis.insert(a[1], sort_ints_to_array(a[0], b[0]));
        } else {
            panic!("Invalid line: {:?} {:?}", a, b);
        }
    }
    (verts, horis)
}

fn is_valid_square(a: [u32; 2], b: [u32; 2], verts: &TilingLineMap, horis: &TilingLineMap) -> bool {
    let xs: [u32; 2] = sort_ints_to_array(a[0], b[0]);
    let ys: [u32; 2] = sort_ints_to_array(a[1], b[1]);
    for (vert_x, vert_ys) in verts {
        if xs[0] < *vert_x && *vert_x < xs[1] {
            if vert_ys[0] <= ys[0] && vert_ys[1] > ys[0] {
                return false;
            }
            if vert_ys[0] < ys[1] && vert_ys[1] >= ys[1] {
                return false;
            }
        }
    }
    for (hori_y, hori_xs) in horis {
        if ys[0] < *hori_y && *hori_y < ys[1] {
            if hori_xs[0] <= xs[0] && hori_xs[1] > xs[0] {
                return false;
            }
            if hori_xs[0] < xs[1] && hori_xs[1] >= xs[1] {
                return false;
            }
        }
    }
    true
}

pub fn part_two(input: &str) -> Option<u64> {
    let red_tile_coords = get_red_tile_coords(input);
    let (vertical_lines, horizontal_lines) = get_horizontal_and_vertical_lines(&red_tile_coords);
    let mut largest_square_size = 0;
    for i in 0..(red_tile_coords.len() - 1) {
        for j in (i + 1)..red_tile_coords.len() {
            if is_valid_square(
                red_tile_coords[i],
                red_tile_coords[j],
                &vertical_lines,
                &horizontal_lines,
            ) {
                largest_square_size = max(
                    largest_square_size,
                    get_square_size(red_tile_coords[i], red_tile_coords[j]),
                )
            }
        }
    }
    Some(largest_square_size)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(50));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(24));
    }
}
