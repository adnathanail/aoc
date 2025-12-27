use std::collections::HashMap;
use std::sync::{LazyLock, Mutex};
advent_of_code::solution!(11);

type Cables = HashMap<usize, Vec<usize>>;
type CableNames<'a> = Vec<&'a str>;

fn get_cable_index(cable_names: &Vec<&str>, val: &str) -> usize {
    // Give a vector cable names, and a specific cable name
    //   get the index of that cable name in the vector
    cable_names.iter().position(|x| *x == val).unwrap()
}

fn get_cables<'a>(input: &'a str) -> (CableNames<'a>, Cables) {
    // Convert the input into a vector of cable names
    //   and a HashMap of cable indexes to the vectors of
    //   cable indexes
    let mut out = HashMap::new();
    // Extract the cable names into a vector
    let mut cable_names: Vec<&str> = input
        .strip_suffix("\n")
        .unwrap()
        .split("\n")
        .map(|x| x.split(": ").collect::<Vec<&str>>()[0])
        .collect();
    // Add the "out" cable, because it won't be on the "from" side
    //   that is processed above
    cable_names.push("out");
    // Go through each row (one per cable)
    //   and split out all the cables connected to it
    //   and add the indexes to the output HashMap
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

type FollowCablesInput = (usize, usize, Option<usize>, Option<usize>);
// Cache for the follow_cables_function
static FOLLOW_CABLES_CACHE: LazyLock<Mutex<HashMap<FollowCablesInput, u64>>> =
    LazyLock::new(|| Mutex::new(HashMap::new()));

fn follow_cables(
    cables: &Cables,
    start_cable: usize,
    end_cable: usize,
    fft_cable: Option<usize>, // If this is Some(xyz), then we still need to visit xyd
    dac_cable: Option<usize>, // ^same
) -> u64 {
    // Check the cache
    if let Some(&result) =
        FOLLOW_CABLES_CACHE
            .lock()
            .unwrap()
            .get(&(start_cable, end_cable, fft_cable, dac_cable))
    {
        return result;
    }

    let mut out = 0;
    // Go through all the cables connected to this one
    for c in cables[&start_cable].iter() {
        // If one of the connected cables is the desired end cable
        if *c == end_cable {
            // If we've visited the FFT and DAC cables
            if fft_cable.is_none() && dac_cable.is_none() {
                out += 1;
            }
        } else {
            // Keep tracing until we get to the next end
            out += follow_cables(
                cables,
                *c,
                end_cable,
                // If the current cable was the fft_cable, then
                //   replace fft_cable with None
                if Some(*c) == fft_cable {
                    None
                } else {
                    fft_cable
                },
                if Some(*c) == dac_cable {
                    None
                } else {
                    dac_cable
                },
            )
        }
    }
    // Store the value in the cache
    FOLLOW_CABLES_CACHE
        .lock()
        .unwrap()
        .insert((start_cable, end_cable, fft_cable, dac_cable), out);
    out
}

pub fn part_one(input: &str) -> Option<u64> {
    let (cable_names, cables) = get_cables(input);
    // Get the number of paths from 'you' to 'out'
    Some(follow_cables(
        &cables,
        get_cable_index(&cable_names, "you"),
        get_cable_index(&cable_names, "out"),
        // Don't set fft/dac cables as they are only for part 1
        None,
        None,
    ))
}

pub fn part_two(input: &str) -> Option<u64> {
    let (cable_names, cables) = get_cables(input);
    // Get the number of paths from 'svr' to 'out' via 'fft' and 'dac'
    Some(follow_cables(
        &cables,
        get_cable_index(&cable_names, "svr"),
        get_cable_index(&cable_names, "out"),
        Some(get_cable_index(&cable_names, "fft")),
        Some(get_cable_index(&cable_names, "dac")),
    ))
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
        let result = part_two(&advent_of_code::template::read_file_part(
            "examples", DAY, 2,
        ));
        assert_eq!(result, Some(2));
    }
}
