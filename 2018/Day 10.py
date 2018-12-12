import time
from aocd import get_data
inp = get_data(day=10, year=2018).split("\n")
start = time.time()

# Part 1 & 2
import re
import plotly.graph_objs as go
import plotly.io as pio

class Position:
  def __init__(self, x, y, u, v):
    self.x = x
    self.y = y
    self.u = u
    self.v = v
  def __str__(self):
    return "%s,%s %s,%s" % (self.x, self.y, self.u, self.v)
  def tick(self, forward=True):
    self.x += self.u if forward else -self.u
    self.y += self.v if forward else -self.v

def print_ps(ps):
  x, y = list(map(lambda p: p.x, ps)), list(map(lambda p: p.y, ps))
  fig = go.Figure()
  fig.add_scatter(x=x,y=y,mode='markers')
  pio.write_image(fig, '2018/d10.png')

ps = []
for row in inp:
  x, y, u, v = [int(a) for a in re.match(r"position=<([- ]?\d+), ([- ]?\d+)> velocity=<([- ]?\d+), ([- ]?\d+)>", row).groups()]
  ps.append(Position(x,y,u,v))

lr = max(map(lambda p: p.x, ps)) - min(map(lambda p: p.x, ps))+1
i = 0
found = False
while not found:
  minx, maxx = min(map(lambda p: p.x, ps)), max(map(lambda p: p.x, ps))
  if (maxx-minx+1) > lr:
    for p in ps:
      p.tick(False)
    print_ps(ps)
    print(i-1)
    found = True
  else:
    lr = (maxx-minx+1)
    for p in ps:
      p.tick()
  i += 1

end = time.time()
print(end - start)
