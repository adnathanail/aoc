advent_of_code::solution!(5);

fn is_in_ranges(ranges: &Vec<(u64, u64)>, n: u64) -> bool {
    for range in ranges {
        if n >= range.0 && n <= range.1 {
            return true;
        }
    }
    false
}

pub fn part_one(input: &str) -> Option<u64> {
    let input_parts: Vec<&str> = input.strip_suffix("\n").unwrap().split("\n\n").collect();
    let ranges: Vec<(u64, u64)> = input_parts[0]
        .split("\n")
        .map(|range_str| {
            let range_parts: Vec<&str> = range_str.split("-").collect();
            (
                range_parts[0].parse().unwrap(),
                range_parts[1].parse().unwrap(),
            )
        })
        .collect();

    let mut fresh_ingredients = 0;
    for n in input_parts[1].split("\n") {
        if is_in_ranges(&ranges, n.parse().unwrap()) {
            fresh_ingredients += 1;
        }
    }
    Some(fresh_ingredients)
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
        assert_eq!(result, Some(3));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(14));
    }
}
