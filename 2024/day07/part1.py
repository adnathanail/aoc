from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=7)
input_data = puzzle.input_data

eqs = []
for row in input_data.split("\n"):
    target, num_str = row.split(": ")
    nums = num_str.split(" ")
    eqs.append((int(target), [int(x) for x in nums]))


def create_guesses(nums):
    if len(nums) == 1:
        return nums

    out = []
    out.extend(create_guesses([nums[0] + nums[1]] + nums[2:]))
    out.extend(create_guesses([nums[0] * nums[1]] + nums[2:]))

    return out


tot = 0
for eq in eqs:
    if eq[0] in create_guesses(eq[1]):
        tot += eq[0]

print(tot)
