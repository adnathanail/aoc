from aocd import get_data
inp = get_data(day=12).split('\n')
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

i = 0
while len(list(dic)) > 0:
  for id in cig(list(dic)[0],set([])):
    del dic[id]
  i += 1

print(i)