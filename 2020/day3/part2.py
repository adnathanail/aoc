from aocd import get_data

inp = get_data(day=3, year=2020)

rows = inp.split("\n")
rowlen = len(rows[0])


def tallytrees(right, down):
  treetally = 0
  x = 0
  for y in range(0, len(rows), down):
    if rows[y][x % rowlen] == "#":
      treetally += 1
    x += right
  return treetally


acc = 1
for paths in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
  acc *= tallytrees(paths[0], paths[1])

print(acc)
