use std::collections::HashMap;

advent_of_code::solution!(11);

type Cables<'a> = HashMap<&'a str, Vec<&'a str>>;

fn get_cables<'a>(input: &'a str) -> Cables<'a> {
    let mut out = HashMap::new();
    for row in input.strip_suffix("\n").unwrap().split("\n") {
        let row_split: Vec<&str> = row.split(": ").collect();
        out.insert(row_split[0], row_split[1].split(" ").collect());
    }
    out
}

fn follow_cables(cables: &Cables, start_cable: &str, end_cable: &str) -> u64 {
    let mut out = 0;
    for c in cables[start_cable].iter() {
        if *c == end_cable {
            out += 1;
        } else {
            out += follow_cables(cables, c, end_cable)
        }
    }
    out
}

pub fn part_one(input: &str) -> Option<u64> {
    let cables = get_cables(input);
    Some(follow_cables(&cables, "you", "out"))
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
        assert_eq!(result, Some(5));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2));
    }
}
