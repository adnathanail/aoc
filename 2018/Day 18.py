import time
from aocd import get_data
inp = get_data(day=18, year=2018).split('\n')
start = time.time()

def procLCA(area): # Process lumber collection area
  newarea = []
  for i in range(len(area)):
    newrow = []
    for j in range(len(area[0])):
      if area[i][j] == ".":
        trees = 0
        for k in range(i-1,i+2):
          for l in range(j-1,j+2):
            try:
              if k >= 0 and l >= 0 and area[k][l] == "|":
                trees += 1
            except IndexError:
              pass
        if trees >= 3:
          newrow.append("|")
        else:
          newrow.append(".")
      elif area[i][j] == "|":
        lumberyards = 0
        for k in range(i-1,i+2):
          for l in range(j-1,j+2):
            try:
              if k >= 0 and l >= 0 and area[k][l] == "#":
                lumberyards += 1
            except IndexError:
              pass
        if lumberyards >= 3:
          newrow.append("#")
        else:
          newrow.append("|")
      elif area[i][j] == "#":
        lumberyards = 0
        trees = 0
        for k in range(i-1,i+2):
          for l in range(j-1,j+2):
            try:
              if k >= 0 and l >= 0 and not (k == i and l == j):
                if area[k][l] == "#":
                  lumberyards += 1
                elif area[k][l] == "|":
                  trees += 1
            except IndexError:
              pass
        if lumberyards >= 1 and trees >= 1:
          newrow.append("#")
        else:
          newrow.append(".")
    newarea.append(newrow)
  return newarea

def resourceValue(area):
  trees = 0
  lumberyards = 0
  for row in area:
    trees += row.count("|")
    lumberyards += row.count("#")
  return trees * lumberyards

# Part 1
forest = inp
for i in range(10):
  forest = procLCA(forest)

print(resourceValue(forest))

# Part 2
forest = inp
forests = []
for i in range(1000):
  forest = procLCA(forest)
  sv = ''.join([''.join(row) for row in forest])
  if sv not in forests:
    forests.append(sv)
  else:
    x, y, z = forests.index(sv), i, 1000000000-1
    break

print(resourceValue(forests[(z-x)%(y-x)+x]))

end = time.time()
print(end - start)
