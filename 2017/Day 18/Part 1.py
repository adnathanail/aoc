from aocd import get_data
inp = get_data(day=18).split("\n")

class Program:
  regs = {}
  played = 0
  i = 0

  def ro(self): # Run operation
    gv = lambda x : int(x) if x.lstrip('-').isdigit() else self.regs[x] # Get value
    o = inp[self.i]
    op = o[:3]
    if op in ["snd", "rcv"]:
      v = gv(o[4:])
      if op == "snd":
        self.played = v
      elif v != 0:
        return False
    else:
      v1,v2 = o[4:].split(" ")
      v2 = gv(v2)
      if v1 not in self.regs:
        self.regs[v1] = 0
      if op == "jgz" and self.regs[v1] != 0:
        self.i += v2 -1
      elif op == "set":
        self.regs[v1] = v2
      elif op == "add":
        self.regs[v1] += v2
      elif op == "mul":
        self.regs[v1] *= v2
      elif op == "mod":
        self.regs[v1] %= v2
    self.i += 1
    return True
  def run(self):
    while self.i >= 0 and self.i < len(inp) and self.ro():
      pass
    print(self.played)

p = Program()
p.run()