advent_of_code::solution!(12, 1);

const PRESENT_WIDTH_HEIGHT: usize = 3;
const NUM_PRESENTS: usize = 6;
type Present = [[u32; PRESENT_WIDTH_HEIGHT]; PRESENT_WIDTH_HEIGHT];
type Region = (usize, usize, [u32; NUM_PRESENTS]);

// fn process_presents_str(presents_str: &str) {}

fn process_input(input: &str) {
    let inp_split: Vec<&str> = input.strip_suffix("\n").unwrap().split("\n\n").collect();
    let presents: Vec<Present> = inp_split[0..inp_split.len() - 1]
        .iter()
        .map(|present_str| {
            let present_str_split: Vec<&str> = present_str.split("\n").collect();
            present_str_split[1..present_str_split.len()]
                .iter()
                .map(|p_row| {
                    p_row
                        .chars()
                        .map(|x| if x == '#' { 1 } else { 0 })
                        .collect::<Vec<u32>>()
                        .try_into()
                        .unwrap()
                })
                .collect::<Vec<[u32; PRESENT_WIDTH_HEIGHT]>>()
                .try_into()
                .unwrap()
        })
        .collect();
    let regions: Vec<Region> = inp_split[inp_split.len() - 1]
        .split("\n")
        .map(|region_str| {
            let region_str_split: Vec<&str> = region_str.split(": ").collect();
            let dimensions_vec: Vec<&str> = region_str_split[0].split("x").collect();
            let tallies_vec: Vec<u32> = region_str_split[1]
                .split(" ")
                .map(|tally_str| tally_str.parse().unwrap())
                .collect();
            (
                dimensions_vec[0].parse().unwrap(),
                dimensions_vec[1].parse().unwrap(),
                tallies_vec.try_into().unwrap(),
            )
        })
        .collect();
    println!("{:?}", presents);
    println!("{:?}", regions);
}

pub fn part_one(input: &str) -> Option<u64> {
    process_input(input);
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(2));
    }
}
