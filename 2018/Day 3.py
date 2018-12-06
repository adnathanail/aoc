import time
from aocd import get_data
inp = get_data(day=3, year=2018).split('\n')
start = time.time()

import re

grid = []
for i in range(1000):
  tem = []
  for j in range(1000):
    tem.append('')
  grid.append(tem)

cids = set()
overlapped = set()
for row in inp:
  cid, left, top, width, height = [int(x) for x in re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", row).groups()]
  cids.add(str(cid))
  for x in range(left, left+width):
    for y in range(top, top+height):
      if grid[x][y] == '':
        grid[x][y] = str(cid)
      else:
        if grid[x][y] != 'X':
          overlapped.add(grid[x][y])
          grid[x][y] = 'X'
        overlapped.add(str(cid))

# Part 1
t = 0
for i in range(1000):
  for j in range(1000):
    if grid[i][j] == 'X':
      t += 1
print(t)

# Part 2
print(cids.difference(overlapped))

end = time.time()
print(end - start)