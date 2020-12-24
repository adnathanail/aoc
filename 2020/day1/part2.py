from itertools import combinations

from aocd import get_data

# TODO implement combinations myself

inp = get_data(day=1, year=2020)

nums = [int(x) for x in inp.split("\n")]

for com in list(combinations(nums, 3)):
  if com[0] + com[1] + com[2] == 2020:
    print(com[0] * com[1] * com[2])
    break
