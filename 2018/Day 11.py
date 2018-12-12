import time
from aocd import get_data
inp = int(get_data(day=11, year=2018)) # 8199
start = time.time()

def cpl(X, Y): # Calculate power level
  rid = X + 10 # Rack ID
  pl = rid * Y # Power level
  pl += inp
  pl *= rid
  return int(("00" + str(pl))[-3]) - 5

grid = []
for i in range(1,301): # Y
  tem = []
  for j in range(1,301): # X
    # tem.append(("+"+str(cpl(j,i)))[-2:])
    tem.append((cpl(j,i)))
  grid.append(tem)

def gmpgs(size): # Get max power given size
  maxv = 0 # Max value
  maxc = (0,0) # Max value coordinates
  for i in range(1,300-(size-1)): # Y
    for j in range(1,300-(size-1)): # X
      v = sum([sum(grid[x][i:i+size]) for x in range(j,j+size)])
      if v > maxv:
        maxv = v
        maxc = (i+1,j+1)
  return maxc, maxv

# Part 1
p1 = gmpgs(3)
print("%i,%i" % (p1[0][0], p1[0][1]))

# Part 2
maxv = 0
maxc = (0,0)
maxi = 0
for i in range(1,301):
  c, v = gmpgs(i)
  if v > maxv:
    maxv = v
    maxc = c
    maxi = i
print("%i,%i,%i" % (maxc[0], maxc[1], maxi))

end = time.time()
print(end - start)
