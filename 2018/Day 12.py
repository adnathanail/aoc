import time
from aocd import get_data
inp = get_data(day=12, year=2018).split('\n')
start = time.time()
# inp = """initial state: #..#.#..##......###...###

# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #""".split('\n')

# Part 1
plants = [x for x in inp[0][15:]]
rules = [(x[:5],x[9]) for x in inp[2:]]
i = 0
def ars(ps):
  ps = ['.','.','.','.'] + ps + ['.','.','.','.']
  newps = []
  for j in range(3,len(ps)-1):
    f = False
    for rule in rules:
      test,nv = rule
      if ''.join(ps[j-3:j+2]) == test:
        newps.append(nv)
        f = True
        break
    if not f:
      newps.append('.')
  return newps

for i in range(20):
  plants = ars(plants)
  t = 0
  for k in range(len(plants)):
    if plants[k] == "#":
      t += k - 2*(i+1)
  print(t)

# Part 2


end = time.time()
print(end - start)
