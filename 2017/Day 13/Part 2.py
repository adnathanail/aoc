from aocd import get_data
import itertools

inp = get_data(day=13, year=2017).split("\n")
fw = {int(row.split(": ")[0]):int(row.split(": ")[1]) for row in inp}

def score(o):
  return [i*fw[i] for i in fw if (i+o)%(2*fw[i]-2) == 0]

print(next(d for d in itertools.count(0) if score(d) == []))