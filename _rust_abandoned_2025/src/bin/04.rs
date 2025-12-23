advent_of_code::solution!(4);

type Grid = Vec<Vec<bool>>;

// fn print_grid(grid: &Grid) {
//     for yy in 0..grid.len() {
//         for xx in 0..grid[yy].len() {
//             if grid[yy][xx] {
//                 print!("@");
//             } else {
//                 print!(".");
//             }
//         }
//         println!();
//     }
// }

fn get_valid_surrounding_square_indexes(
    height: usize,
    width: usize,
    x: usize,
    y: usize,
) -> Vec<(usize, usize)> {
    // Given a coordinate, return all the surrounding coordinates that exist
    //   i.e. ones that don't cause IndexErrors
    // Numbers below match comments on the lines which deal with each potential valid location
    // 123
    // 4X5
    // 678
    let mut out: Vec<(usize, usize)> = vec![];
    if y > 0 {
        if x > 0 {
            out.push((x - 1, y - 1)); // 1
        }
        out.push((x, y - 1)); // 2
        if x < width - 1 {
            out.push((x + 1, y - 1)); // 3
        }
    }
    if x > 0 {
        out.push((x - 1, y)); // 4
    }
    if x < width - 1 {
        out.push((x + 1, y)); // 5
    }
    if y < height - 1 {
        if x > 0 {
            out.push((x - 1, y + 1)); // 6
        }
        out.push((x, y + 1)); // 7
        if x < width - 1 {
            out.push((x + 1, y + 1)); // 8
        }
    }
    out
}

fn get_num_adjacent_rolls(grid: &Grid, height: usize, width: usize, x: usize, y: usize) -> u64 {
    // Get the values in every square surrounding the given coordinate
    let mut out = 0;
    for loc in get_valid_surrounding_square_indexes(height, width, x, y) {
        if grid[loc.1][loc.0] {
            out += 1;
        }
    }
    out
}

fn parse_grid(input: &str) -> Grid {
    // Convert input string into a 2D vec of booleans,
    //   where true means a roll, and false otherwise
    input
        .strip_suffix("\n")
        .unwrap()
        .split("\n")
        .into_iter()
        .map(|x| x.chars().map(|ch| ch == '@').collect())
        .collect()
}

pub fn part_one(input: &str) -> Option<u64> {
    let grid: Grid = parse_grid(input);
    // Get width and height
    let height = (&grid).len();
    let width = (&grid[0]).len();
    // Accumulator
    let mut num_accessible_rolls = 0;
    // Go through grid
    for y in 0..height {
        for x in 0..width {
            // If there is a roll there, and it is accessible (less than 4 neighbours)
            if grid[y][x] && (get_num_adjacent_rolls(&grid, height, width, x, y) < 4) {
                num_accessible_rolls += 1
            }
        }
    }
    Some(num_accessible_rolls)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut grid: Grid = parse_grid(input);
    // Get width and height
    let height = (&grid).len();
    let width = (&grid[0]).len();
    // Get a list of the locations of every rolls
    let mut roll_locs: Vec<(usize, usize)> = vec![];
    for y in 0..height {
        for x in 0..width {
            if grid[y][x] {
                roll_locs.push((x, y));
            }
        }
    }
    let mut num_accessible_rolls = 0;
    let mut indexes_to_remove: Vec<usize> = vec![];
    while num_accessible_rolls == 0 || indexes_to_remove.len() > 0 {
        indexes_to_remove = vec![];
        for (index, rl) in roll_locs.iter().enumerate() {
            if get_num_adjacent_rolls(&grid, height, width, rl.0, rl.1) < 4 {
                num_accessible_rolls += 1;
                grid[rl.1][rl.0] = false;
                indexes_to_remove.push(index);
            }
        }
        for index in (&indexes_to_remove).iter().rev() {
            roll_locs.remove(*index);
        }
    }
    Some(num_accessible_rolls)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(13));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(43));
    }
}
