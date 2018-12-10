import time
from aocd import get_data
inp = get_data(day=9, year=2018)
start = time.time()

import re
nop, mm = [int(x) for x in re.match("(\d+) players; last marble is worth (\d+) points", inp).groups()] # Number of players, Max marble

def ms(nop, mm): # Max score
  l = [0,1]
  i = 1
  pss = [0 for _ in range(nop)] # Player scores
  cp = 0 # Current player
  for n in range(2,1+mm):
    if n % 23:
      i += 2
      if i > len(l):
        i -= len(l)
      l.insert(i,n)
    else:
      i -= 7
      if i < 0:
        i += len(l)
      pss[cp] += n + l[i]
      del l[i]
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
