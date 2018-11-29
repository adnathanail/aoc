from aocd import get_data
import itertools

inp = get_data(day=13).split("\n")
fw = {}
for row in inp:
  d,r = row.split(": ") # Depth, Range
  fw[int(d)] = int(r)

def score(o):
  return [i*fw[i] for i in fw if (i+o)%(2*fw[i]-2) == 0]

print(next(d for d in itertools.count(0) if score(d) == []))