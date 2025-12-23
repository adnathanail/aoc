use std::cmp::{max, min};

advent_of_code::solution!(5);

fn is_in_ranges(ranges: &Ranges, n: usize) -> bool {
    for range in ranges {
        if n >= range.0 && n <= range.1 {
            return true;
        }
    }
    false
}

type Ranges = Vec<(usize, usize)>;

fn parse_input(input: &str) -> (Ranges, Vec<&str>) {
    let input_parts: Vec<&str> = input.strip_suffix("\n").unwrap().split("\n\n").collect();
    let ranges: Ranges = input_parts[0]
        .split("\n")
        .map(|range_str| {
            let range_parts: Vec<&str> = range_str.split("-").collect();
            (
                range_parts[0].parse().unwrap(),
                range_parts[1].parse().unwrap(),
            )
        })
        .collect();
    let numbers: Vec<&str> = input_parts[1].split("\n").collect();
    (ranges, numbers)
}

pub fn part_one(input: &str) -> Option<u64> {
    let (ranges, numbers) = parse_input(input);

    let mut fresh_ingredients = 0;
    for n in numbers {
        if is_in_ranges(&ranges, n.parse().unwrap()) {
            fresh_ingredients += 1;
        }
    }
    Some(fresh_ingredients)
}

fn can_merge_ranges(a1: usize, a2: usize, b1: usize, b2: usize) -> bool {
    // Check if two ranges overlap
    if a1 <= b2 && b2 <= a2 {
        return true;
    }
    if b1 <= a2 && a2 <= b2 {
        return true;
    }
    false
}

fn find_ranges_indexes_to_merge(ranges: &Ranges) -> Option<(usize, usize)> {
    // Find the next set of mergeable ranges
    for i in 0..(ranges.len() - 1) {
        for j in (i + 1)..ranges.len() {
            if can_merge_ranges(ranges[i].0, ranges[i].1, ranges[j].0, ranges[j].1) {
                return Some((i, j));
            }
        }
    }
    None
}

pub fn part_two(input: &str) -> Option<u64> {
    let (mut ranges, _) = parse_input(input);
    loop {
        let itm = find_ranges_indexes_to_merge(&ranges);
        if let Some((rtm1_index, rtm2_index)) = itm {
            let rtm1 = ranges[rtm1_index];
            let rtm2 = ranges[rtm2_index];
            let mut new_ranges: Ranges = vec![(min(rtm1.0, rtm2.0), max(rtm1.1, rtm2.1))];
            for (i, range) in ranges.iter().enumerate() {
                if i != rtm1_index && i != rtm2_index {
                    new_ranges.push(*range)
                }
            }
            ranges = new_ranges;
        } else {
            break;
        }
    }
    let mut fresh_ingredients = 0;
    for (r1, r2) in ranges {
        fresh_ingredients += (r2 as i64) - (r1 as i64) + 1
    }
    Some(fresh_ingredients as u64)
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
