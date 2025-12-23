advent_of_code::solution!(4);

type Grid = Vec<Vec<bool>>;

fn print_grid(grid: &Grid) {
    for yy in 0..grid.len() {
        for xx in 0..grid[yy].len() {
            if grid[yy][xx] {
                print!("@");
            } else {
                print!(".");
            }
        }
        println!();
    }
}

fn get_valid_surrounding_square_indexes(
    height: u64,
    width: u64,
    x: u64,
    y: u64,
) -> Vec<(u64, u64)> {
    // Given a coordinate, return all the surrounding coordinates that exist
    //   i.e. ones that don't cause IndexErrors
    // Numbers below match comments on the lines which deal with each potential valid location
    // 123
    // 4X5
    // 678
    let mut out: Vec<(u64, u64)> = vec![];
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

fn get_num_adjacent_rolls(grid: &Grid, height: u64, width: u64, x: u64, y: u64) -> u64 {
    println!(
        "bbb {} {} aa {} {} {:?}",
        height,
        width,
        x,
        y,
        get_valid_surrounding_square_indexes(height, width, x, y)
    );
    // Get the values in every square surrounding the given coordinate
    let mut out = 0;
    for loc in get_valid_surrounding_square_indexes(height, width, x, y) {
        if grid[loc.1 as usize][loc.0 as usize] {
            out += 1;
        }
    }
    out
}

pub fn part_one(input: &str) -> Option<u64> {
    let grid: Grid = input
        .strip_suffix("\n")
        .unwrap()
        .split("\n")
        .into_iter()
        .map(|x| x.chars().map(|ch| ch == '@').collect())
        .collect();
    let height = (&grid).len();
    let width = (&grid[0]).len();
    let mut num_accessible_rolls = 0;
    for yy in 0..height {
        for xx in 0..width {
            if grid[yy][xx]
                && (get_num_adjacent_rolls(
                    &grid,
                    height as u64,
                    width as u64,
                    xx as u64,
                    yy as u64,
                ) < 4)
            {
                num_accessible_rolls += 1
            }
        }
    }
    Some(num_accessible_rolls)
}

pub fn part_two(input: &str) -> Option<u64> {
    None
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
