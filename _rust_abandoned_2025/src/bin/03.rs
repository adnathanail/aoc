advent_of_code::solution!(3);

use advent_of_code::{get_number_length, get_substring_from_number};
use std::cmp::max;

fn get_largest_digit_in_number(num: u64) -> (u64, u32) {
    let mut largest = 0;
    let mut largest_index = 0;

    let mut curr = num;
    let mut i = 0;
    while curr > 0 {
        let digit = curr % 10;
        if digit >= largest {
            largest = digit;
            largest_index = i;
        }
        // println!("{} {}", curr, curr % 10);
        largest = max(largest, curr % 10);
        curr /= 10;
        i += 1;
    }
    // println!("{} {}", largest, largest_index);
    (largest, largest_index)
}

pub fn part_one(input: &str) -> Option<u64> {
    let mut total_joltage = 0;
    for row in input.strip_suffix("\n").unwrap().split("\n") {
        let num: u64 = row.parse().unwrap();
        let num_length: u32 = get_number_length(num);
        // println!("{} {}", num, get_number_length(num));
        // println!("{}", get_substring_from_number(num, 1, num_length));
        let (first_largest_digit, first_largest_digit_index) =
            get_largest_digit_in_number(get_substring_from_number(num, 1, num_length));
        // println!("{} {}", first_largest_digit, first_largest_digit_index);
        // println!(
        //     "{}",
        //     get_substring_from_number(num, 0, first_largest_digit_index + 1)
        // );
        let (second_largest_digit, _) = get_largest_digit_in_number(get_substring_from_number(
            num,
            0,
            first_largest_digit_index + 1,
        ));
        println!("{} {}", first_largest_digit, second_largest_digit);
        total_joltage += first_largest_digit * 10 + second_largest_digit;
        // println!("{:?}", get_largest_digit_in_number(get_substring_from_number(num, 1, num_length)));
        // break;
    }
    Some(total_joltage)
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
        assert_eq!(result, Some(357));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, None);
    }
}
