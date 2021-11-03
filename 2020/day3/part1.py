from aocd import get_data

inp = get_data(day=3, year=2020)

rows = inp.split("\n")
rowlen = len(rows[0])

treetally = 0
i = 0
for row in inp.split("\n"):
  if row[i % rowlen] == "#":
    treetally += 1
  i += 3

print(treetally)
