from aocd import get_data
inp = get_data(day=2)
tot = 0
for row in inp.split("\n"):
    procrow = [int(x) for x in row.split("\t")]
    tot += max(procrow) - min(procrow)
print(tot)