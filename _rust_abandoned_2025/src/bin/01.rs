advent_of_code::solution!(1);

pub fn part_one(input: &str) -> Option<u64> {
    let mut curr_pos: i32 = 50;
    let mut num_zeroes: u64 = 0;
    for line in input.lines() {
        let n: i32 = line[1..].parse().expect("Should be integer");
        if line.starts_with('L') {
            curr_pos -= n;
        } else {
            curr_pos += n;
        }
        curr_pos %= 100;

        if curr_pos == 0 {
            num_zeroes += 1;
        }
    }
    Some(num_zeroes)
}

pub fn part_two(input: &str) -> Option<u64> {
    let mut curr_pos: i32 = 50;
    let mut num_zeroes: u64 = 0;
    let mut minus: bool;
    for line in input.lines() {
        let n: i32 = line[1..].parse().expect("Should be integer");
        minus = line.starts_with('L');
        for _ in 0..n {
            if minus {
                curr_pos -= 1;
            } else {
                curr_pos += 1;
            }
            if curr_pos % 100 == 0 {
                num_zeroes += 1;
            }
        }

    }
    Some(num_zeroes)
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
        assert_eq!(result, Some(6));
    }
}
