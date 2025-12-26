use itertools::Itertools;
use std::cmp::min;
advent_of_code::solution!(10);

type ButtonWiring = Vec<i64>;
type Joltages = Vec<i64>;
type Machine = (Joltages, Vec<ButtonWiring>, Joltages);

fn process_desired_state_str(desired_state_str: &str) -> Joltages {
    // Process lighting state string into a vector of 1s and 0s
    //   to make them basically match the format of joltages
    //   so both part 1 and part 2 can share the same code
    // E.g. "[.##.]" -> [0, 1, 1, 0]
    desired_state_str
        .chars()
        .filter(|ch| *ch != '[' && *ch != ']')
        .map(|ch| if ch == '#' { 1 } else { 0 })
        .collect()
}

fn process_button_wirings_str(
    button_wirings_strs: Vec<&str>,
    num_lights: usize,
) -> Vec<ButtonWiring> {
    // Process vector of button wiring strings into vector of vectors of 1s and 0s
    //   e.g. ["(2)", "(0, 1)"] -> [[0, 0, 1], [1, 1, 0]]
    button_wirings_strs
        .into_iter()
        .map(|but_str| {
            let button_indexes: Vec<u64> = but_str[1..but_str.len() - 1]
                .split(",")
                .map(|num_str| num_str.parse().unwrap())
                .collect();
            (0..num_lights)
                .map(|i| {
                    if button_indexes.contains(&(i as u64)) {
                        1
                    } else {
                        0
                    }
                })
                .collect()
        })
        .collect()
}

fn process_joltages_str(joltages_str: &str) -> Joltages {
    // Process joltages string into a vector of numbers
    // E.g. "{3,5,4,7}" -> [3, 5, 4, 7]
    joltages_str[1..joltages_str.len() - 1]
        .split(",")
        .map(|j_str| j_str.parse::<i64>().unwrap())
        .collect()
}

fn parse_input(input: &str) -> Vec<Machine> {
    // Process input into list of machines
    //   Each machine containing
    //   - a desired state vector
    //   - a vector of button wiring vectors
    //   - a joltages vector
    input
        .strip_suffix("\n")
        .unwrap()
        .split("\n")
        .map(|row| {
            let row_split: Vec<&str> = row.split(" ").collect();
            let desired_state = process_desired_state_str(row_split[0]);
            let num_lights = desired_state.len();
            (
                desired_state,
                process_button_wirings_str(row_split[1..row_split.len() - 1].to_vec(), num_lights),
                process_joltages_str(row_split[row_split.len() - 1]),
            )
        })
        .collect()
}

fn run_buttons(num_lights: usize, button_tuples_to_use: &Vec<&ButtonWiring>) -> Joltages {
    // Simulate a list of button presses
    let mut out: Vec<i64> = vec![0; num_lights];
    for but in button_tuples_to_use {
        out = add_tuples(&out, but, 2)
    }
    out
}

pub fn part_one(input: &str) -> Option<u64> {
    let machines = parse_input(input);
    let mut num_button_presses = 0;
    for machine in machines {
        let number_of_lights = machine.0.len();
        for buttons in machine.1.iter().powerset() {
            if run_buttons(number_of_lights, &buttons) == machine.0 {
                num_button_presses += buttons.len();
                break;
            }
        }
    }
    Some(num_button_presses as u64)
}

fn add_tuples(t1: &[i64], t2: &[i64], m: i64) -> Vec<i64> {
    t1.iter().zip(t2).map(|(x, y)| (x + y) % m).collect()
}

fn subtract_tuples(t1: &[i64], t2: &[i64]) -> Vec<i64> {
    t1.iter().zip(t2).map(|(x, y)| x - y).collect()
}

fn int_divide_tuple(t1: &[i64], s: i64) -> Vec<i64> {
    // Integer-divide a tuple by a scalar, elementwise
    t1.iter().map(|x| x / s).collect()
}

fn get_possible_buttons_for_desired_state(
    button_tuples: &[ButtonWiring],
    binary_desired_state: &Joltages,
) -> Vec<Vec<ButtonWiring>> {
    // Given a list of button tuples, and a desired state (consisting of only 0's and 1's)
    //   returns all possible button presses that reach that desired state
    let number_of_lights = binary_desired_state.len();
    let mut out = vec![];
    for buttons in button_tuples.iter().powerset() {
        if run_buttons(number_of_lights, &buttons) == *binary_desired_state {
            out.push(buttons.into_iter().cloned().collect())
        }
    }
    out
}

fn get_num_button_presses_for_joltages(
    button_tuples: &Vec<ButtonWiring>,
    joltages: &Joltages,
) -> u64 {
    // For given lists of button tuples and joltages, return the minimum number of button presses
    //   required to achieve the desired joltages
    // Can't have negative joltages
    for jolt in joltages {
        if *jolt < 0 {
            return u64::MAX;
        }
    }
    // If the joltages are all 0, we don't need to press any buttons
    let mut all_zero = true;
    for jolt in joltages {
        if *jolt != 0 {
            all_zero = false;
            break;
        }
    }
    if all_zero {
        return 0;
    }
    // To find all button presses required to make all the joltage numbers even,
    //   get a list of the "parity" (0 for even 1 for odd) of the joltages
    let joltage_parities: Joltages = joltages.iter().map(|x| x % 2).collect();
    let mut least_buttons = u64::MAX;
    // Find all the button presses that make our joltages even
    for buttons in get_possible_buttons_for_desired_state(button_tuples, &joltage_parities) {
        // Apply the button presses to the joltages
        let mut new_joltages: Joltages = joltages.clone();
        for button in &buttons {
            new_joltages = subtract_tuples(&new_joltages, button)
        }
        // Divide the new joltages by 2, to obtain a new set of target joltages, potentially with new odd joltages
        new_joltages = int_divide_tuple(&new_joltages, 2);
        // - Find the number of button presses required to make the new joltages
        // - Multiply it by 2, to account for the fact that we halved the targets
        // - And add the number of button presses we used, to make the joltages even
        let nbpfj = get_num_button_presses_for_joltages(button_tuples, &new_joltages);
        if nbpfj < u64::MAX {
            least_buttons = min(least_buttons, (buttons.len() as u64) + (2 * nbpfj))
        }
    }
    least_buttons
}

pub fn part_two(input: &str) -> Option<u64> {
    let machines = parse_input(input);
    let mut num_button_presses = 0;
    for machine in machines {
        num_button_presses += get_num_button_presses_for_joltages(&machine.1, &machine.2);
    }
    Some(num_button_presses)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(7));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(33));
    }
}
