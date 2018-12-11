import time
from aocd import get_data
inp = get_data(day=9, year=2018)
start = time.time()

import re
from collections import deque
nop, mm = [int(x) for x in re.match(r"(\d+) players; last marble is worth (\d+) points", inp).groups()] # Number of players, Max marble

def ms(nop, mm): # Max score
  l = deque([1,0])
  pss = [0 for _ in range(nop)] # Player scores
  cp = 0 # Current player
  for n in range(2,1+mm):
    if n % 23:
      l.append(n)
      l.rotate(-1)
    else:
      l.rotate(8)
      pss[cp] += n + l.pop()
      l.rotate(-2)
    cp += 1
    if cp >= len(pss):
      cp -= len(pss)
  return max(pss)

# Part 1
print(ms(nop,mm))

# Part 2
print(ms(nop,mm*100))

end = time.time()
print(end - start)
