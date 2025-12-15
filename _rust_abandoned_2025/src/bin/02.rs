advent_of_code::solution!(2);

fn get_substring_from_number(num: u64, a: u32, b: u32) -> u64 {
    // Indexing out "substrings" of a number, without converting to a string
    let ten_to_a = 10_u64.pow(a);
    let ten_to_b = 10_u64.pow(b);
    (num - ((num / ten_to_b) * ten_to_b)) / ten_to_a
}

fn is_invalid_part_one(num: u64) -> bool {
    // Number of characters in number is log10(num) + 1
    let num_length = num.ilog10() + 1;
    //If the length of the string isn't even, then it can't be equally cut in half
    if num_length % 2 == 1 {
        return false;
    }
    // If the first half equals the second half then the string is invalid
    get_substring_from_number(num, 0, num_length / 2)
        == get_substring_from_number(num, num_length / 2, num_length)
}

pub fn part_one(input: &str) -> Option<u64> {
    let mut tot_invalids = 0;
    for num_range in input.strip_suffix("\n").unwrap().split(",") {
        let num_range_split = num_range.split("-").collect::<Vec<&str>>();
        let from_num: u64 = num_range_split[0].parse().unwrap();
        let to_num: u64 = num_range_split[1].parse().unwrap();
        for num in from_num..(to_num + 1) {
            if is_invalid_part_one(num) {
                tot_invalids += num;
            }
        }
    }
    Some(tot_invalids)
}

type FactorLookup = Vec<Vec<u32>>;

fn is_invalid_part_two(num: u64) -> bool {
    let factors_lookup: FactorLookup = vec![
        vec![],
        vec![],
        vec![1],
        vec![1],
        vec![1, 2],
        vec![1],
        vec![1, 2, 3],
        vec![1],
        vec![1, 2, 4],
        vec![1, 3],
        vec![1, 2, 5],
    ];

    // Number of characters in number is log10(num) + 1
    let num_length = num.ilog10() + 1;

    for rep_length in &factors_lookup[num_length as usize] {
        let mut first_chunk: Option<u64> = None;
        let mut chunks_different = false;
        for i in 0..(num_length / rep_length) {
            let subs = get_substring_from_number(num, i * rep_length, (i + 1) * rep_length);
            if first_chunk == None {
                first_chunk = Some(subs);
            } else if first_chunk != Some(subs) {
                chunks_different = true;
                break;
            }
        }
        if chunks_different == false {
            return true;
        }
    }
    return false;
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut tot_invalids = 0;
    for num_range in input.strip_suffix("\n").unwrap().split(",") {
        let num_range_split = num_range.split("-").collect::<Vec<&str>>();
        let from_num: u64 = num_range_split[0].parse().unwrap();
        let to_num: u64 = num_range_split[1].parse().unwrap();
        for num in from_num..(to_num + 1) {
            if is_invalid_part_two(num) {
                tot_invalids += num;
            }
        }
    }
    Some(tot_invalids)
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
