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
    for (digit, digit_char) in DIGITS {
        if let Some(index) = num.find(digit_char) {
            return Some((digit, index));
        }
    }
    None
}

pub fn part_one(input: &str) -> Option<u64> {
    let mut total_joltage = 0;
    for row in input.strip_suffix("\n").unwrap().split("\n") {
        // Get largest digit in number (excluding the last digit)
        let (first_largest_digit, first_largest_digit_index) =
            get_largest_digit_in_number(&row[0..row.len() - 1]).unwrap();
        // Get largest digit to the right of first largest digit
        let (second_largest_digit, _) =
            get_largest_digit_in_number(&row[first_largest_digit_index + 1..]).unwrap();
        total_joltage += first_largest_digit * 10 + second_largest_digit;
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
