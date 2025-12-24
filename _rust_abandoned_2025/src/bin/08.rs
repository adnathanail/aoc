use disjoint_sets::UnionFind;
use std::collections::HashMap;
use std::hash::Hash;
advent_of_code::solution!(8);

fn process_input(input: &str) -> Vec<Vec<i64>> {
    input
        .strip_suffix("\n")
        .unwrap()
        .split("\n")
        .map(|row| row.split(",").map(|x| x.parse().unwrap()).collect())
        .collect()
}

fn euc_dist(a: &[i64], b: &[i64]) -> f32 {
    (((a[0] - b[0]).pow(2) + (a[1] - b[1]).pow(2) + (a[2] - b[2]).pow(2)) as f32).sqrt()
}

fn tally_vec<T: Hash + Eq + Copy>(inp: &Vec<T>) -> HashMap<T, u64> {
    let mut out: HashMap<T, u64> = HashMap::new();
    for val in inp {
        out.insert(*val, out.get(val).unwrap_or(&0) + 1);
    }
    out
}

fn do_part_one(input: &str, num_iterations: u64) -> Option<u64> {
    let junction_boxes = process_input(input);
    let mut distance_lookup: HashMap<usize, HashMap<usize, f32>> = HashMap::new();
    for i in 0..(junction_boxes.len() - 1) {
        let mut i_distances: HashMap<usize, f32> = HashMap::new();
        for j in (i + 1)..junction_boxes.len() {
            i_distances.insert(j, euc_dist(&junction_boxes[i], &junction_boxes[j]));
        }
        distance_lookup.insert(i, i_distances);
    }
    let mut connected_components: UnionFind<usize> = UnionFind::new(junction_boxes.len());
    let mut connections: Vec<(usize, usize)> = vec![];
    for _ in 0..num_iterations {
        let mut closest_points: Option<(usize, usize)> = None;
        let mut shortest_distance: f32 = f32::MAX;
        for i in distance_lookup.keys() {
            for j in distance_lookup[i].keys() {
                if distance_lookup[i][j] < shortest_distance && !connections.contains(&(*i, *j)) {
                    shortest_distance = distance_lookup[i][j];
                    closest_points = Some((*i, *j));
                }
            }
        }
        connections.push(closest_points.unwrap());
        connected_components.union(closest_points.unwrap().0, closest_points.unwrap().1);
    }
    let mut tallies: Vec<u64> = tally_vec(&connected_components.to_vec())
        .values()
        .copied()
        .collect();
    tallies.sort();
    let blah: Vec<u64> = tallies.iter().rev().take(3).copied().collect();
    Some(blah.iter().product::<u64>())
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
        let result = do_part_one(&advent_of_code::template::read_file("examples", DAY), 100);
        assert_eq!(result, Some(40));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(25272));
    }
}
