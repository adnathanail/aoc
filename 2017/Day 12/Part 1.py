from aocd import get_data
inp = get_data(day=12, year=2017).split('\n')
dic = {}
for r in inp:
  pid, cs = r.split(" <-> ") # Program id, childs (children)
  dic[pid] = cs.split(", ")

def cig(pid, ps): # Count in group
  ps.add(pid)
  for p in dic[pid]:
    if p not in ps:
      ps = ps.union(cig(p, ps))
  return ps

print(len(cig('0',set([]))))