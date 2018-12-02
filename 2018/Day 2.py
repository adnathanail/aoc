import time
from aocd import get_data
inp = get_data(day=2, year=2018).split('\n')
start = time.time()

# Part 1
from collections import Counter
twos = 0
threes = 0
for row in inp:
  c = Counter(dict(Counter(row)).values())
  twos += 1 if 2 in c else 0
  threes += 1 if 3 in c else 0
print(twos*threes)

# Part 2
def nocd(s1,s2): # Numbers of characters different
  x = 0
  for i in range(len(s1)):
    if s1[i] != s2[i]:
      x += 1
  return x
for i in range(len(inp)):
  for j in range(i+1,len(inp)):
    if nocd(inp[i], inp[j]) == 1:
      print(''.join([inp[i][x] for x in range(len(inp[i])) if inp[i][x] == inp[j][x]]))

end = time.time()
print(end - start)