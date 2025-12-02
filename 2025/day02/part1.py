from aocd.models import Puzzle

puzzle = Puzzle(year=2025, day=2)
inp = puzzle.input_data.replace("\n", "")

def is_invalid(n_str: str):
    # If the length of the string isn't even, then it can't be equally cut in half
    if len(n_str) % 2 != 0:
        return False

    # If the first half equals the second half then the string is invalid
    return n_str[:len(n_str)//2] == n_str[len(n_str)//2:]

tot_invalids = 0
for num_range in inp.split(","):
    from_num, to_num = [int(n) for n in num_range.split("-")]
    for num in range(from_num, to_num + 1):
        if is_invalid(str(num)):
            tot_invalids += num

print(tot_invalids)