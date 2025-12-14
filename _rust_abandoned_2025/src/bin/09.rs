use std::cmp::{max, min};
use std::collections::HashMap;

advent_of_code::solution!(9);

fn get_red_tile_coords(input: &str) -> Vec<[i32; 2]> {
    let mut out: Vec<[i32; 2]> = Vec::new();
    for line in input.lines() {
        let coord: Vec<i32> = line.split(",").map(|x| x.parse::<i32>().unwrap()).collect();
        out.push([coord[0], coord[1]]);
    }
    out
}

fn get_square_size(c1: [i32; 2], c2: [i32; 2]) -> i32 {
    ((c1[0] - c2[0]).abs() + 1) * ((c1[1] - c2[1]).abs() + 1)
}

pub fn part_one(input: &str) -> Option<i32> {
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

fn get_horizontal_and_vertical_lines(
    rtcs: &[[i32; 2]],
) -> (HashMap<i32, (i32, i32)>, HashMap<i32, (i32, i32)>) {
    let mut verts = HashMap::new();
    let mut horis = HashMap::new();
    for i in 0..rtcs.len() {
        let a = rtcs[i];
        let b = rtcs[(i + 1) % rtcs.len()];
        if a[0] == b[0] {
            verts.insert(a[0], (min(a[1], b[1]), max(a[1], b[1])));
        } else if a[1] == b[1] {
            horis.insert(a[1], (min(a[0], b[0]), max(a[0], b[0])));
        } else {
            panic!("Invalid line: {:?} {:?}", a, b);
        }
    }
    (verts, horis)
}

pub fn part_two(input: &str) -> Option<u64> {
    let red_tile_coords = get_red_tile_coords(input);
    let (vertical_lines, horizontal_lines) = get_horizontal_and_vertical_lines(&red_tile_coords);
    println!("{:?}", vertical_lines);
    println!("{:?}", horizontal_lines);
    None
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
