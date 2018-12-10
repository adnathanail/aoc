import time
from aocd import get_data
inp = get_data(day=7, year=2018).split('\n')
start = time.time()

import re

required = {x: [] for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
for row in inp:
  l1, l2 = re.match("Step (.) must be finished before step (.) can begin.", row).groups()
  required[l2].append(l1)

class Worker:
  def __init__(self):
    self.current_letter = ""
    self.time_left = 0
  def tick_clock(self):
    global completed, working, required, o
    if self.time_left <= 0:
      if self.current_letter != "":
        completed.add(self.current_letter)
      if self.current_letter not in o:
        o += self.current_letter
      for l1 in sorted(required.keys()):
        allowed = True
        for l2 in required[l1]:
          if l2 not in completed:
            allowed = False
        if allowed and l1 not in completed and l1 not in working:
          working.append(l1)
          self.current_letter = l1
          self.time_left = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(l1)+1+60
          break
    self.time_left -= 1

# Part 1
completed = set()
working = []
o = ""
w = Worker()
x = 0
while len(completed) < len(required.keys()):
  x += 1
  w.tick_clock()
print(o)

# Part 2
completed = set()
working = []
o = ""
ws = [Worker(), Worker(), Worker(), Worker(), Worker()]
x = 0
while len(completed) < len(required.keys()):
  x += 1
  for w in ws:
    w.tick_clock()
print(x-1)

end = time.time()
print(end - start)
