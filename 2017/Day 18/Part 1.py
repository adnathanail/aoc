from aocd import get_data
inp = get_data(day=18).split("\n")
# inp = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2""".split("\n")

def gv(x): # Get value
  try:
    return int(x)
  except ValueError:
    return regs[x]

regs = {}
played = 0
i = 0
done = False
while i >= 0 and i < len(inp) and not done:
  row = inp[i]
  print(row)
  op = row[:3]
  if op in ["snd", "rcv"]:
    v = gv(row[4:])
    if op == "snd":
      played = v
    elif v != 0:
      done = True
  else:
    v1,v2 = row[4:].split(" ")
    v2 = gv(v2)
    if v1 not in regs:
      regs[v1] = 0
    if op == "jgz" and regs[v1] != 0:
      i += v2 -1
    elif op == "set":
      regs[v1] = v2
    elif op == "add":
      regs[v1] += v2
    elif op == "mul":
      regs[v1] *= v2
    elif op == "mod":
      regs[v1] %= v2
  i += 1

print(played)
