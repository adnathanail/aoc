advent_of_code::solution!(6);

pub fn part_one(input: &str) -> Option<u64> {
    let mut vals: Vec<Vec<u64>> = vec![];
    let mut grand_total = 0;
    for (i, row) in input.split("\n").enumerate() {
        for (j, val_str) in row.split(" ").filter(|x| *x != "").enumerate() {
            if i == 0 {
                vals.push(vec![]);
            }
            if let Ok(val) = val_str.parse::<u64>() {
                vals[j].push(val);
            } else {
                if val_str == "+" {
                    grand_total += vals[j].iter().sum::<u64>();
                } else {
                    grand_total += vals[j].iter().product::<u64>();
                }
            }
        }
    }
    Some(grand_total)
}

fn get_column_widths(operands_row: &str) -> Vec<u64> {
    // Given the row of operands, extract the width of each column
    //   as a list of integers
    let mut out: Vec<u64> = vec![];
    let mut n = 0;
    for char in operands_row[1..operands_row.len()].chars() {
        n += 1;
        if char != ' ' {
            out.push(n);
            n = 0;
        }
    }
    n += 1;
    out.push(n);
    return out;
}

fn split_out_puzzles<'a>(
    number_rows: &Vec<&'a str>,
    column_widths: &Vec<u64>,
) -> Vec<Vec<&'a str>> {
    // Given all the number rows, and the width of each column
    //   extract the numbers for each column, maintaining the
    //   number alignment
    // Returns a list of strings
    let mut out: Vec<Vec<&str>> = vec![];
    // # Create empty lists for each column
    for _ in column_widths {
        out.push(vec![])
    }

    for row in number_rows {
        let mut ind: usize = 0;
        // Go through each column width for each row
        for (cwi, cw) in column_widths.iter().enumerate() {
            let mut end_ind = ind + (*cw as usize);
            if cwi < (column_widths.len() - 1) {
                // Remove extra space on each column except the last column
                end_ind -= 1;
            }
            out[cwi].push(&row[ind..end_ind]);
            ind += *cw as usize;
        }
    }
    return out;
}

fn transpose_puzzle(puzz: &Vec<&str>) -> Vec<u64> {
    // Given a single puzzle (list of numbers as strings with
    //   space alignments) read the numbers vertically
    //   and parse them into a list of integers
    let mut out_strs: Vec<Vec<char>> = vec![];
    for (i, row) in puzz.iter().enumerate() {
        for (j, char) in row.chars().enumerate() {
            if i == 0 {
                out_strs.push(vec![])
            }
            if char != ' ' {
                out_strs[j].push(char);
            }
        }
    }
    out_strs
        .iter()
        .map(|x| x.iter().collect::<String>().parse::<u64>().unwrap())
        .collect()
}

pub fn part_two(input: &str) -> Option<u64> {
    // Parse input
    let rows: Vec<&str> = input.strip_suffix("\n").unwrap().split("\n").collect();
    let column_widths = get_column_widths(rows[rows.len() - 1]);
    let operands: Vec<char> = rows[rows.len() - 1].chars().filter(|x| *x != ' ').collect();
    // Split out "columns" into puzzle groups
    let untransposed_puzzles = split_out_puzzles(&rows[0..rows.len() - 1].into(), &column_widths);
    // Do the maths
    let mut grand_total = 0;
    for (i, puzzle) in untransposed_puzzles.iter().enumerate() {
        if operands[i] == '+' {
            grand_total += transpose_puzzle(puzzle).iter().sum::<u64>();
        } else {
            grand_total += transpose_puzzle(puzzle).iter().product::<u64>();
        }
    }
    Some(grand_total)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_part_one() {
        let result = part_one(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(4277556));
    }

    #[test]
    fn test_part_two() {
        let result = part_two(&advent_of_code::template::read_file("examples", DAY));
        assert_eq!(result, Some(3263827));
    }
}
