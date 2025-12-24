use std::collections::{HashMap, HashSet};

advent_of_code::solution!(7);

fn process_input(input: &str) -> (Vec<Vec<usize>>, usize) {
    // List of splitter index locations on each row
    let mut splitter_indexes_by_row: Vec<Vec<usize>> = vec![];
    let mut start_index: Option<usize> = None;
    // Go through each row
    for row in input.strip_suffix("\n").unwrap().split("\n") {
        // List of splitter indexes for this row
        let mut row_splitter_indexes: Vec<usize> = vec![];
        for (i, char) in row.chars().enumerate() {
            // Get start index
            if char == 'S' {
                start_index = Some(i)
            } else if char == '^' {
                // Add index of splitter on this row
                row_splitter_indexes.push(i);
            }
        }
        // Don't both adding empty splitter rows
        if !row_splitter_indexes.is_empty() {
            splitter_indexes_by_row.push(row_splitter_indexes)
        }
    }
    (splitter_indexes_by_row, start_index.unwrap())
}

pub fn part_one(input: &str) -> Option<u64> {
    let (splitter_indexes_by_row, start_index) = process_input(input);
    // Set to keep track of beams
    let mut beams: HashSet<usize> = HashSet::new();
    // Add start index as initial beam
    beams.insert(start_index);

    let mut num_splits: u64 = 0;
    for splitter_row in &splitter_indexes_by_row {
        let mut new_beams: HashSet<usize> = HashSet::new();
        for beam_index in &beams {
            if splitter_row.contains(&beam_index) {
                new_beams.insert(beam_index - 1);
                new_beams.insert(beam_index + 1);
                num_splits += 1;
            } else {
                new_beams.insert(*beam_index);
            }
        }
        beams = new_beams;
    }
    Some(num_splits)
}

pub fn part_two(input: &str) -> Option<u64> {
    let (splitter_indexes_by_row, start_index) = process_input(input);
    // Dictionary to keep track of the number of beams at each index
    let mut beams: HashMap<usize, u64> = HashMap::new();
    beams.insert(start_index, 1);
    for splitter_row in splitter_indexes_by_row {
        let mut new_beams: HashMap<usize, u64> = HashMap::new();
        for beam_index in beams.keys() {
            if splitter_row.contains(beam_index) {
                if !new_beams.contains_key(&((*beam_index) - 1)) {
                    new_beams.insert(beam_index - 1, 0);
                }
                if !new_beams.contains_key(&((*beam_index) + 1)) {
                    new_beams.insert(beam_index + 1, 0);
                }
                new_beams.insert(
                    beam_index - 1,
                    new_beams.get(&(beam_index - 1)).unwrap() + beams.get(beam_index).unwrap(),
                );
                new_beams.insert(
                    beam_index + 1,
                    new_beams.get(&(beam_index + 1)).unwrap() + beams.get(beam_index).unwrap(),
                );
            } else {
                if !new_beams.contains_key(beam_index) {
                    new_beams.insert(*beam_index, 0);
                }
                new_beams.insert(
                    *beam_index,
                    new_beams.get(beam_index).unwrap() + beams.get(beam_index).unwrap(),
                );
            }
        }
        beams = new_beams;
    }
    Some(beams.values().sum::<u64>())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(21));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(40));
    }
}
