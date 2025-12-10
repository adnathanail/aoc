use std::cmp::max;

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
            largest_square_size = max(largest_square_size, get_square_size(red_tile_coords[i], red_tile_coords[j]))
        }
    }
    Some(largest_square_size)
}

pub fn part_two(input: &str) -> Option<u64> {
    let red_tile_coords = get_red_tile_coords(input);
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
