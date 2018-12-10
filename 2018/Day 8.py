import time
from aocd import get_data
inp = [int(x) for x in get_data(day=8, year=2018).split(' ')]
start = time.time()

# Part 1
def som(l): # Sum of metadata
  c = l[0] # number of children
  m = l[1] # number of metadata
  if c == 0:
    return sum(l[2:2+m]),l[2+m:]
  else:
    l = l[2:]
    tot = 0
    for _ in range(c):
      q = som(l)
      tot += q[0]
      l = q[1]
    return tot+sum(l[:m]),l[m:]
print(som(inp)[0])

# Part 2
def cnt(l): # Child node tally
  c = l[0] # number of children
  m = l[1] # number of metadata
  if c == 0:
    return sum(l[2:2+m]),l[2+m:]
  else:
    l = l[2:]
    vs = []
    for _ in range(c):
      q = cnt(l)
      vs.append(q[0])
      l = q[1]
    tot = 0
    for x in l[:m]:
      try:
        tot += vs[x-1]
      except:
        continue
    return tot,l[m:]
print(cnt(inp)[0])

end = time.time()
print(end - start)
