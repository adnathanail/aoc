from aocd import get_data
import re

inp = get_data(day=9, year=2017)
inp = re.sub('!.', '', inp)
inp = re.sub('<[^>]*>', '', inp)
inp = re.sub(',', '', inp)
# print(inp)
tot = 0
depth = 0
for char in inp:
  if char == "{":
    depth += 1
  else:
    tot += depth
    depth -= 1
print(tot)