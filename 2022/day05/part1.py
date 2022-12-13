import re

from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=5)

rows = puzzle.input_data.split("\n")

stacks: dict[int, list[str]] = {}

i = 0
# Loop until the line " 1   2   3 " etc.
while rows[i][1] != "1":
    # If there are n crates
    #   each crate takes 3 chars and there are (n - 1) spaces
    #   so there are 4n - 1 chars in a line
    # E.g. for 3 crates there are 11 chars in a line
    # So to go from line length (l) to n
    #   n = (l + 1) // 4      (where a // b is integer division)
    for j in range((len(rows[i]) + 1) // 4):
        # Don't add blanks to the stacks
        if rows[i][4 * j + 1] != " ":
            # If this is the first time we are adding an item to this stack, initialise it to an empty array
            if j + 1 not in stacks:
                stacks[j + 1] = []
            # Insert the item at the start of the list, so the stack ends up with the top item at the end (feels neater)
            stacks[j + 1].insert(0, rows[i][4 * j + 1])
    i += 1

# Skip to the move instructions
i += 2

# Compile the regex once outside the loop to save executions
pattern = re.compile(r"move (\d+) from (\d+) to (\d+)")

while i < len(rows):
    # Extract the useful numbers from the text with regex
    regex_result = re.search(pattern, rows[i])
    how_many = int(regex_result.groups()[0])
    from_where = int(regex_result.groups()[1])
    to_where = int(regex_result.groups()[2])
    for _ in range(how_many):
        # Remove item from 1 stack and add it to the other
        stacks[to_where].append(stacks[from_where].pop())
    i += 1

out = ""
# Sort the keys of the dictionary numerically, so the output is in the right order
for stack_id in sorted(stacks.keys()):
    out += stacks[stack_id][-1]

print(out)
