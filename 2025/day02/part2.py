from aocd.models import Puzzle


# Possible lengths of repeated substrings within numbers of a given length
# Essentially the factors of the number except itself
FACTORS_LOOKUP = {
    1: (),
    2: (1,),
    3: (1,),
    4: (1, 2),
    5: (1, ),
    6: (1, 2, 3),
    7: (1, ),
    8: (1, 2, 4),
    9: (1, 3),
    10: (1, 2, 5),
}


puzzle = Puzzle(year=2025, day=2)
inp = puzzle.input_data.replace("\n", "")

def is_invalid(n_str: str):
    n_len = len(n_str)

    # For each possible length of repeat
    for rep_len in FACTORS_LOOKUP[n_len]:
        # Collect each substring of the given length
        n_chunks = set()
        for i in range(n_len // rep_len):
            n_chunks.add(n_str[rep_len*i:rep_len*(i + 1)])
        # If all the substrings of that length were the same length
        #   then the string was all repeats
        #   i.e. invalid
        if len(n_chunks) == 1:
            return True

    return False

tot_invalids = 0
for num_range in inp.split(","):
    from_num, to_num = [int(n) for n in num_range.split("-")]
    for num in range(from_num, to_num + 1):
        if is_invalid(str(num)):
            tot_invalids += num

print(tot_invalids)