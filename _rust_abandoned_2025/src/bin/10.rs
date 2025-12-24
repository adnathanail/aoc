use itertools::Itertools;
advent_of_code::solution!(10);

type LightingState = Vec<bool>;
type ButtonWirings = Vec<Vec<u64>>;
type Joltages = Vec<u64>;
type Machine = (LightingState, ButtonWirings, Joltages);

fn parse_input(input: &str) -> Vec<Machine> {
    let mut out = vec![];
    for row in input.strip_suffix("\n").unwrap().split("\n") {
        let row_split: Vec<&str> = row.split(" ").collect();
        let desired_state: LightingState = row_split[0]
            .chars()
            .filter(|x| *x != '[' && *x != ']')
            .map(|x| x == '#')
            .collect();
        let button_wirings_str = (&row_split[1..row_split.len() - 1]).to_vec();
        let button_wirings: ButtonWirings = button_wirings_str
            .into_iter()
            .map(|x| {
                (&x[1..x.len() - 1])
                    .split(",")
                    .map(|x| x.parse().unwrap())
                    .collect()
            })
            .collect();
        let joltages_str = row_split[row_split.len() - 1];
        let joltages: Joltages = (&joltages_str[1..joltages_str.len() - 1])
            .split(",")
            .map(|x| x.parse::<u64>().unwrap())
            .collect();
        out.push((desired_state, button_wirings, joltages));
    }
    out
}

fn run_buttons(num_lights: usize, buttons_to_push: &Vec<&Vec<u64>>) -> LightingState {
    let mut out = vec![false; num_lights];
    for but in buttons_to_push {
        for i in *but {
            out[*i as usize] = !out[*i as usize];
        }
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

pub fn part_two(input: &str) -> Option<u64> {
    None
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
