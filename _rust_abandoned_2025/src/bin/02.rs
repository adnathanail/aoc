advent_of_code::solution!(2);

fn is_invalid(num: u64) -> bool {
    // Number of characters in number is log10(num) + 1
    let num_length = num.ilog10() + 1;
    //If the length of the string isn't even, then it can't be equally cut in half
    if num_length % 2 == 1 {
        return false;
    }
    // 10^(num_length / 2)
    let ten_to_half_num_length = (10 as u64).pow(num_length / 2);
    // Get first half of the number by integer dividing it by 10^(num_length / 2)
    let first_half = num / ten_to_half_num_length;
    // Get second half of the number by subtracting first_half * 10^(num_length / 2)
    let second_half = num - (first_half * ten_to_half_num_length);
    // If the first half equals the second half then the string is invalid
    first_half == second_half
}

pub fn part_one(input: &str) -> Option<u64> {
    let mut tot_invalids = 0;
    for num_range in input.strip_suffix("\n").unwrap().split(",") {
        let num_range_split = num_range.split("-").collect::<Vec<&str>>();
        let from_num: u64 = num_range_split[0].parse().unwrap();
        let to_num: u64 = num_range_split[1].parse().unwrap();
        for num in from_num..(to_num + 1) {
            if is_invalid(num) {
                tot_invalids += num;
            }
        }
    }
    Some(tot_invalids)
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
        assert_eq!(result, Some(1227775554));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4174379265));
    }
}
