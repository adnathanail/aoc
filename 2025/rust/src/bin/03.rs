advent_of_code::solution!(3);

const DIGITS: [(u64, char); 10] = [
    (9, '9'),
    (8, '8'),
    (7, '7'),
    (6, '6'),
    (5, '5'),
    (4, '4'),
    (3, '3'),
    (2, '2'),
    (1, '1'),
    (0, '0'),
];

fn get_largest_digit_in_number(num: &str) -> Option<(u64, usize)> {
    // Given a string of digits, find the left-most occurrence of the largest
    //   digit in the string
    // Go through each digit (and its char representation) in descending order
    for (digit, digit_char) in DIGITS {
        // If the digit is in the string, return the index
        if let Some(index) = num.find(digit_char) {
            return Some((digit, index));
        }
    }
    None
}

fn get_largest_n_digit_substring(num: &str, n: u64) -> u64 {
    // Given a string of digits, and the desired length of the result
    //   find the "substring" (as an integer) with the largest value
    //   formed just by removing digits from the string
    // Keep track of the substring we are searching in with 2 pointers
    // The left is limited by the index of the previously found largest number
    let mut left_offset = 0;
    // The right is limited by the number of digits we still have to find
    //   (so we are guaranteed to find an n-digit string)
    let mut right_offset = n as usize;
    // Accumulator
    let mut out = 0;

    // i is used to get powers of 10, to construct the number, so we go from 12 - 0
    for i in (0..n).rev() {
        right_offset -= 1;
        let (digit, index) =
            get_largest_digit_in_number(&num[left_offset..num.len() - right_offset]).unwrap();
        // Build output by multiplying digits by powers of 10, so that the output is
        //   a number as opposed to a string, for ease of addition later
        out += digit * 10_u64.pow(i as u32);
        left_offset += index + 1;
    }
    out
}

fn solve_problem_for_n(input: &str, n: u64) -> Option<u64> {
    // Given a full input string, split it by rows
    //   and find the largest "substring" for each row
    //   returning the sum of these "substrings" as numbers
    let mut total_joltage = 0;
    for row in input.strip_suffix("\n").unwrap().split("\n") {
        total_joltage += get_largest_n_digit_substring(row, n);
    }
    Some(total_joltage)
}

pub fn part_one(input: &str) -> Option<u64> {
    solve_problem_for_n(input, 2)
}

pub fn part_two(input: &str) -> Option<u64> {
    solve_problem_for_n(input, 12)
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
        assert_eq!(result, Some(3121910778619));
    }
}
