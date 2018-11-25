from aocd import get_data
inp = get_data(day=11).split(',')

biggest = x = y = z = 0
for a in inp:
  if a == 'n':
    y += 1
    z -= 1
  elif a == 'ne':
    x += 1
    z -= 1
  elif a == 'nw':
    x -= 1
    y += 1
  elif a == 's':
    y -= 1
    z += 1
  elif a == 'sw':
    x -= 1
    z += 1
  elif a == 'se':
    x += 1
    y -= 1
  d = int(sum([abs(q) for q in [x,y,z]])/2)
  if d > biggest:
    biggest = d
print(biggest)