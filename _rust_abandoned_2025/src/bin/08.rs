use disjoint::DisjointSet;
use ordered_float::OrderedFloat;
use priority_queue::PriorityQueue;
use std::cmp::Reverse;
advent_of_code::solution!(8);

fn process_input(input: &str) -> Vec<Vec<i64>> {
    // Convert input string into a vector of 3-vectors of coordinates
    input
        .strip_suffix("\n")
        .unwrap()
        .split("\n")
        .map(|row| row.split(",").map(|x| x.parse().unwrap()).collect())
        .collect()
}

fn get_boxes_to_join_in_order(
    junction_boxes: &[Vec<i64>],
) -> PriorityQueue<(usize, usize), Reverse<OrderedFloat<f32>>> {
    // Cache all pairs of junction boxes into a priority queue, sorted
    //   by the distance between each paid
    // OrderedFloat is a wrapper around floats provided by a library, giving floats
    //   the Ord trait, required by the priority queue from another library..!
    let mut pq = PriorityQueue::new();
    for i in 0..(junction_boxes.len() - 1) {
        for j in (i + 1)..junction_boxes.len() {
            pq.push(
                (i, j),
                Reverse(euc_dist(&junction_boxes[i], &junction_boxes[j])),
            );
        }
    }
    pq
}

fn euc_dist(a: &[i64], b: &[i64]) -> OrderedFloat<f32> {
    // Get the 3D euclidean distance between two points as a float
    OrderedFloat(
        (((a[0] - b[0]).pow(2) + (a[1] - b[1]).pow(2) + (a[2] - b[2]).pow(2)) as f32).sqrt(),
    )
}

fn do_part_one(input: &str, num_iterations: u64) -> Option<u64> {
    let junction_boxes = process_input(input);
    let pq = get_boxes_to_join_in_order(&junction_boxes);
    // Go through the queue in increasing order of distance,
    //   joining up the connections up to num_iterations
    // "DisjointSet" is a way of keeping track of connected components
    //   you tell it how many elements you have, then you can join any
    //   elements together, and it keeps track of all the elements that
    //   are connected to each other
    let mut connected_components = DisjointSet::with_len(junction_boxes.len());
    for (pair, _) in pq.into_sorted_iter().take(num_iterations as usize) {
        connected_components.join(pair.0, pair.1);
    }
    let mut set_lengths: Vec<u64> = connected_components
        .sets()
        .into_iter()
        .map(|set| set.len() as u64)
        .collect();
    // Get the product of the sizes of the 3 largest connected components
    set_lengths.sort();
    Some(set_lengths.iter().rev().take(3).product())
}

pub fn part_one(input: &str) -> Option<u64> {
    do_part_one(input, 1000)
}

pub fn part_two(input: &str) -> Option<u64> {
    let junction_boxes = process_input(input);
    let mut pq = get_boxes_to_join_in_order(&junction_boxes);
    let mut connected_components = DisjointSet::with_len(junction_boxes.len());
    let mut pair: (usize, usize) = (0, 0);
    while connected_components.sets().len() > 1 {
        (pair, _) = pq.pop().unwrap();
        connected_components.join(pair.0, pair.1);
    }
    Some((junction_boxes[pair.0][0] * junction_boxes[pair.1][0]) as u64)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = do_part_one(&advent_of_code::template::read_file("examples", DAY), 10);
        assert_eq!(result, Some(40));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(25272));
    }
}
