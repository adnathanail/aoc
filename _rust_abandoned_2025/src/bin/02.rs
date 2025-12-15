advent_of_code::solution!(2);

fn is_invalid_part_one(num: u64) -> bool {
    // Number of characters in number is log10(num) + 1
    let num_length = num.ilog10() + 1;
    //If the length of the string isn't even, then it can't be equally cut in half
    if num_length % 2 == 1 {
        return false;
    }
    // 10^(num_length / 2)
    let ten_to_half_num_length = 10_u64.pow(num_length / 2);
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
            if is_invalid_part_one(num) {
                tot_invalids += num;
            }
        }
    }
    Some(tot_invalids)
}

// const FACTORS_LOOKUP: Vec<Vec<u32>> = vec![vec![1, 2, 3]];
// const FACTORS_LOOKUP: [[u32; 3]; 10] = [[], [1, 2, 3]];
type FactorLookup = Vec<Vec<u32>>;

fn get_substring_from_number(num: u64, a: u32, b: u32) -> u64 {
    let ten_to_a = 10_u64.pow(a);
    let ten_to_b = 10_u64.pow(b);
    (num - ((num / ten_to_b) * ten_to_b)) / ten_to_a
}

fn is_invalid_part_two(num: u64, factors_lookup: &FactorLookup) -> bool {
    // Number of characters in number is log10(num) + 1
    let num_length = num.ilog10() + 1;

    for rep_length in &factors_lookup[num_length as usize] {
        println!("{}", rep_length);
        let mut first_chunk: Option<u64> = None;
        let mut chunks_different = false;
        for i in 0..(num_length / rep_length) {
            // let ten_to_rep_length: u64 = 10_u64.pow((i + 1) * (*rep_length));
            // let ten_to_i_plus_one: u64 = 10_u64.pow(i * (*rep_length));
            // println!(
            //     "  {} {} {} {} {}",
            //     i,
            //     (num / ten_to_rep_length) * ten_to_rep_length,
            //     num - ((num / ten_to_rep_length) * ten_to_rep_length),
            //     (num - ((num / ten_to_rep_length) * ten_to_rep_length)) / ten_to_i_plus_one,
            //     get_substring_from_number(num, i * (*rep_length), (i + 1) * (*rep_length))
            // );
            let subs = get_substring_from_number(num, i * (*rep_length), (i + 1) * (*rep_length));
            println!(
                " {} {} {}",
                i * (*rep_length),
                (i + 1) * (*rep_length),
                subs
            );
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
    // //If the length of the string isn't even, then it can't be equally cut in half
    // if num_length % 2 == 1 {
    //     return false;
    // }
    // // 10^(num_length / 2)
    // let ten_to_half_num_length = 10_u64.pow(num_length / 2);
    // // Get first half of the number by integer dividing it by 10^(num_length / 2)
    // let first_half = num / ten_to_half_num_length;
    // // Get second half of the number by subtracting first_half * 10^(num_length / 2)
    // let second_half = num - (first_half * ten_to_half_num_length);
    // // If the first half equals the second half then the string is invalid
    // first_half == second_half
}

pub fn part_two(input: &str) -> Option<u64> {
    let FACTORS_LOOKUP: FactorLookup = vec![
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
    // println!("{}", is_invalid_part_two(474747, &FACTORS_LOOKUP));
    // println!("{}", (423 / 100) * 100);
    let mut tot_invalids = 0;
    for num_range in input.strip_suffix("\n").unwrap().split(",") {
        let num_range_split = num_range.split("-").collect::<Vec<&str>>();
        let from_num: u64 = num_range_split[0].parse().unwrap();
        let to_num: u64 = num_range_split[1].parse().unwrap();
        for num in from_num..(to_num + 1) {
            if is_invalid_part_two(num, &FACTORS_LOOKUP) {
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
