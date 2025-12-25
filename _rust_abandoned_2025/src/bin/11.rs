use std::collections::HashMap;
// use std::sync::{LazyLock, Mutex};
advent_of_code::solution!(11);

type Cables = HashMap<usize, Vec<usize>>;
type CableNames<'a> = Vec<&'a str>;

fn get_cable_index(cable_names: &Vec<&str>, val: &str) -> usize {
    println!("{}", val);
    cable_names.iter().position(|x| *x == val).unwrap()
}

fn get_cables<'a>(input: &'a str) -> (CableNames<'a>, Cables) {
    let mut out = HashMap::new();
    let mut cable_names: Vec<&str> = input
        .strip_suffix("\n")
        .unwrap()
        .split("\n")
        .map(|x| x.split(": ").collect::<Vec<&str>>()[0])
        .collect();
    cable_names.push("out");
    for row in input.strip_suffix("\n").unwrap().split("\n") {
        let row_split: Vec<&str> = row.split(": ").collect();
        out.insert(
            get_cable_index(&cable_names, row_split[0]),
            row_split[1]
                .split(" ")
                .map(|x| get_cable_index(&cable_names, x))
                .collect::<Vec<usize>>(),
        );
    }
    (cable_names, out)
}

// static FOLLOW_CABLES_CACHE: LazyLock<Mutex<HashMap<(&str, &str), u64>>> =
//     LazyLock::new(|| Mutex::new(HashMap::new()));

fn follow_cables(cables: &Cables, start_cable: &usize, end_cable: &usize) -> u64 {
    // if let Some(&result) = FOLLOW_CABLES_CACHE
    //     .lock()
    //     .unwrap()
    //     .get(&(start_cable, end_cable))
    // {
    //     return result;
    // }

    let mut out = 0;
    for c in cables[start_cable].iter() {
        if c == end_cable {
            out += 1;
        } else {
            out += follow_cables(cables, c, end_cable)
        }
    }
    // FOLLOW_CABLES_CACHE
    //     .lock()
    //     .unwrap()
    //     .insert((start_cable, end_cable), out);
    out
}

pub fn part_one(input: &str) -> Option<u64> {
    let (cable_names, cables) = get_cables(input);
    Some(follow_cables(
        &cables,
        &get_cable_index(&cable_names, "you"),
        &get_cable_index(&cable_names, "out"),
    ))
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
