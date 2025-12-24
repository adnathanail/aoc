use disjoint_sets::UnionFind;
use priq::PriorityQueue;
use std::collections::HashMap;
use std::hash::Hash;
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

fn euc_dist(a: &[i64], b: &[i64]) -> f32 {
    // Get the 3D euclidean distance between two points as a float
    (((a[0] - b[0]).pow(2) + (a[1] - b[1]).pow(2) + (a[2] - b[2]).pow(2)) as f32).sqrt()
}

fn tally_vec<T: Hash + Eq + Copy>(inp: &Vec<T>) -> HashMap<T, u64> {
    // Given a vector of values, count how many occurrences of each value there are
    let mut out: HashMap<T, u64> = HashMap::new();
    for val in inp {
        out.insert(*val, out.get(val).unwrap_or(&0) + 1);
    }
    out
}

fn do_part_one(input: &str, num_iterations: u64) -> Option<u64> {
    let junction_boxes = process_input(input);
    let mut pq: PriorityQueue<f32, (usize, usize)> = PriorityQueue::new();
    // Cache distances between all pairs of junction boxes
    let mut distance_lookup: HashMap<(usize, usize), f32> = HashMap::new();
    for i in 0..(junction_boxes.len() - 1) {
        for j in (i + 1)..junction_boxes.len() {
            pq.put(euc_dist(&junction_boxes[i], &junction_boxes[j]), (i, j));
        }
    }
    // Join up the connections in increasing order of distance up to num_iterations
    let mut connected_components: UnionFind<usize> = UnionFind::new(junction_boxes.len());
    for _ in 0..num_iterations {
        let pair = pq.pop().unwrap().1;
        connected_components.union(pair.0, pair.1);
    }
    // Count how many junction boxes are in each connected component
    let mut tallies: Vec<u64> = tally_vec(&connected_components.to_vec())
        .values()
        .copied()
        .collect();
    // Get the product of the sizes of the 3 largest connected components
    tallies.sort();
    Some(tallies.iter().rev().take(3).product())
}

pub fn part_one(input: &str) -> Option<u64> {
    do_part_one(input, 1000)
}

pub fn part_two(input: &str) -> Option<u64> {
    None
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
