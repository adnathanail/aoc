import time
from aocd import get_data
inp = get_data(day=6, year=2018).split('\n')
start = time.time()

# Part 1
import string
ab = string.ascii_uppercase + string.ascii_lowercase
inp = {ab[x]: [int(y) for y in inp[x].split(', ')] for x in range(len(inp))}
w, h = max(map(lambda x: x[0], inp.values())),max(map(lambda x: x[1], inp.values()))
grid = [['' for j in range(w+1)] for i in range(h+1)]
for k in inp:
  x,y= inp[k]
  grid[y][x] = k
tally = {z: 0 for z in inp}
md = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
ep = set() # Edge pieces
topltot = 0 # Tally of places less that one thousand
for i in range(h+1):
  for j in range(w+1):
    cp = "" # Closest point
    cpd = h*w # Closest point distance - just so it's definitely bigger than any distance
    ds = []
    for p in inp:
      d = md(inp[p], [j,i])
      ds.append(d)
      if d < cpd:
        cpd = d
        cp = p
    if ds.count(cpd) == 1:
      tally[cp] += 1
    if i == 0 or j == 0 or i == h or j == w:
      ep.add(cp)
    if sum(ds) < 10000:
      topltot += 1
for n in ep:
  del tally[n]
print(max(tally.values()))

# Part 2
print(topltot)


end = time.time()
print(end - start)