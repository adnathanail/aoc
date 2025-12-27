from math import prod

from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=6)
inp = puzzle.input_data

rows = inp.splitlines()

def get_column_widths(operands_row):
    """
    Given the row of operands, extract the width of each column
    as a list of integers
    """
    out = []
    n = 0
    for char in operands_row[1:]:
        n += 1
        if char != " ":
            out.append(n)
            n = 0

    n += 1
    out.append(n)
    return out

def split_out_puzzles(number_rows, column_widths):
    """
    Given all the number rows, and the width of each column
    extract the numbers for each column, maintaining the
    number alignment
    Returns a list of strings
    """
    out = []
    # Create empty lists for each column
    for _ in column_widths:
        out.append([])
    
    for row in number_rows:
        ind = 0
        # Go through each column width for each row
        for cwi in range(len(column_widths)):
            cw = column_widths[cwi]
            end_ind = ind+cw
            if cwi < (len(column_widths) - 1):
                # Remove extra space on each column except the last column
                end_ind -= 1
            out[cwi].append(row[ind:end_ind])
            ind += cw
    
    return out

def transpose_puzzle(puzz):
    """
    Given a single puzzle (list of numbers as strings with
    space alignments) read the numbers vertically
    and parse them into a list of integers
    """
    out = []
    for i in range(len(puzz[0])):
        acc = ""
        for row in puzz:
            if row[i] == "":
                break
            acc += row[i]
        out.append(int(acc))

    return out


operands = [val for val in inp.splitlines()[-1].split(" ") if val]
untransposed_puzzles = split_out_puzzles(rows[:-1], get_column_widths(rows[-1]))

grand_total = 0
for i in range(len(operands)):
    transposed_puzzle = transpose_puzzle(untransposed_puzzles[i])
    if operands[i] == "+":
        grand_total += sum(transposed_puzzle)
    else:
        grand_total +=  prod(transposed_puzzle)

print(grand_total)