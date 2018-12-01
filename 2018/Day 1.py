import time
from aocd import get_data
inp = get_data(day=1, year=2018).split('\n')
start = time.time()

# Part 1
print(sum([int(x) for x in inp]))

# Part 2
seen = []
i = 0 # Index in list of numbers
x = 0 # Running total
while x not in seen:
  seen.append(x)
  x += int(inp[i])
  i += 1
  if i >= len(inp):
    i -= len(inp)
print(x)


end = time.time()
print(end - start)