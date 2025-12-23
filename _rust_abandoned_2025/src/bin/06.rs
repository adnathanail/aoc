advent_of_code::solution!(6);

pub fn part_one(input: &str) -> Option<u64> {
    let mut vals: Vec<Vec<u64>> = vec![];
    let mut grand_total = 0;
    for (i, row) in input.split("\n").enumerate() {
        for (j, val_str) in row.split(" ").filter(|x| *x != "").enumerate() {
            if i == 0 {
                vals.push(vec![]);
            }
            if let Ok(val) = val_str.parse::<u64>() {
                vals[j].push(val);
            } else {
                if val_str == "+" {
                    grand_total += vals[j].iter().sum::<u64>();
                } else {
                    grand_total += vals[j].iter().product::<u64>();
                }
            }
        }
    }
    Some(grand_total)
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
        assert_eq!(result, Some(4277556));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3263827));
    }
}
