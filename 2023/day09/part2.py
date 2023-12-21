from aocd.models import Puzzle

puzzle = Puzzle(year=2023, day=9)

extrapolated_values_sum = 0

for line in puzzle.input_data.splitlines():
    pat = [int(x) for x in line.split(" ")]
    sequences = [pat]
    while set(sequences[-1]) != {0}:
        new_seq = []
        for i in range(len(sequences[-1]) - 1):
            new_seq.append(sequences[-1][i + 1] - sequences[-1][i])
        sequences.append(new_seq)

    while len(sequences) != 1:
        seq = sequences.pop()
        sequences[-1].insert(0, sequences[-1][0] - seq[0])

    extrapolated_values_sum += sequences[-1][0]

print(extrapolated_values_sum)
