from aocd import get_data
inp = get_data(day=14, year=2017)

def xor(l):
  tot = l[0]
  for x in l[1:]:
    tot ^= x
  return tot

def hash(inst): # In string
  ls = [ord(x) for x in inst] + [17, 31, 73, 47, 23] # Lengths
  l = [i for i in range(256)]
  i = 0
  skip = 0

  for q in range(64):
    for length in ls:
      if (i + length-1) < len(l):
        s = l[i:i+length]
        s.reverse()
        l[i:i+length] = s
      else:
        j = len(l) - i # Number of elements from i to end of list inclusive
        s = l[i:] + l[:length - j]
        s.reverse()
        l[-j:] = s[:j]
        l[:length-j] = s[j:]
      i += length + skip
      skip += 1
      while i >= len(l):
        i -= len(l)
  out = ""
  for i in range(0,len(l),16):
    out += '%02x' % xor(l[i:i+16])
  return out

def hextobin(h):
  h = int(h,16)
  return f'{h:0>128b}'

used = 0
grid = []
for i in range(128):
  grid.append([x for x in hextobin(hash("%s-%i" % (inp, i))).replace('0','.').replace('1','#')])

def uoo(grid, a, b, c): # Grid, number to be replaced, number to replace with, up to in i, up to in j
  for i in range(c+1):
    for j in range(len(grid[i])):
      if grid[i][j] == a:
        grid[i][j] = b
  return grid

k = 0
for i in range(len(grid)):
  for j in range(len(grid[i])):
    rc = False # Row changed
    cc = False # Column changed
    if grid[i][j] != '.':
      if i > 0 and grid[i-1][j] != '.':
        if grid[i-1][j] == '#':
          grid[i-1][j] = k
          grid[i][j] = k
        else:
          grid[i][j] = grid[i-1][j]
        rc = True
        k += 1
      if j > 0 and grid[i][j-1] != '.':
        if grid[i][j-1] == '#':
          grid[i][j-1] = k
          grid[i][j] = k
        else:
          grid[i][j] = grid[i][j-1]
        cc = True
        k += 1
      if rc and cc:
        grid = uoo(grid, grid[i-1][j], grid[i][j-1], i)
      if not rc and not cc:
        grid[i][j] = k
        k += 1

nums = set([])
for row in grid:
  for item in row:
    if item != '.':
      nums.add(item)

print(len(nums))