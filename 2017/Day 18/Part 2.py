from aocd import get_data
inp = get_data(day=18, year=2017).split("\n")
inp = """snd 1
snd 2
snd p
rcv a
rcv b
rcv c
rcv d""".split("\n")

class Program:
  def __init__(self, name):
    self.regs = {}
    self.played = 0
    self.i = 0
    self.queue = []
    self.running = True
    self.sent = 0
    self.jftr = False
    self.name = name

  def ro(self): # Run operation
    self.jftr = False
    gv = lambda x : int(x) if x.lstrip('-').isdigit() else self.regs[x] # Get value
    o = inp[self.i]
    # print(o, self.regs)
    op = o[:3]
    if op in ["snd", "rcv"]:
      if op == "snd":
        self.sent += 1
        self.i += 1
        # print(self.name, "sent", gv(o[4:]))
        return gv(o[4:])
      else:
        try:
          self.regs[o[4:]] = self.queue.pop(0)
          # print(self.name, "recieved", self.regs[o[4:]])
          self.i += 1
        except:
          self.jftr = True
          pass
    else:
      v1,v2 = o[4:].split(" ")
      if v1 not in self.regs:
        self.regs[v1] = 0
      if not v2.lstrip('-').isdigit() and v2 not in self.regs:
        self.regs[v2] = 0
      v2 = gv(v2)
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
    if self.i < 0 or self.i >= len(inp):
      # print(self.i)
      self.running = False

p0 = Program('p0')
p0.regs['p'] = 0
p1 = Program('p1')
p1.regs['p'] = 1
while p1.running:
  if p0.running:
    v = p0.ro()
    if v is not None:
      p1.queue.append(v)
      # print('p1', p1.queue)
  if p1.running:
    v = p1.ro()
    if v is not None:
      p0.queue.append(v)
      # print('p0', p0.queue)
  if p0.jftr and p1.jftr:
    p0.running = p1.running = False
  if (not p1.sent % 1000):
    print(p1.sent)

print(p1.sent)