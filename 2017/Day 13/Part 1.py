from aocd import get_data
inp = get_data(day=13).split("\n")

fw = {}
for row in inp:
  d,r = row.split(": ") # Depth, Range
  fw[d] = ['' for x in range(int(r)+1)]
  fw[d][0] = 'S'
  fw[d][-1] = 'D'

def move_scanners(fw):
  for k in list(fw):
    i = fw[k].index('S')
    if fw[k][-1] == 'D':
      newi = i + 1
      if newi >= (len(fw[k]) - 1):
        newi -= 2
        fw[k][-1] = 'U'
    elif fw[k][-1] == 'U':
      newi = i - 1
      if newi <= -1:
        newi += 2
        fw[k][-1] = 'D'
    fw[k][i] = ''
    fw[k][newi] = 'S'
  return fw

x = 0
s = 0 # Severity total
while x <= max([int(x) for x in list(fw)]):
  if str(x) in fw and fw[str(x)][0] == "S":
    s += x * (len(fw[str(x)])-1)
  fw = move_scanners(fw)
  x += 1
print(s)