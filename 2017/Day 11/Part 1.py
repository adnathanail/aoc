from aocd import get_data
inp = get_data(day=11).split(',')

done = False
while not done:
  if 'n' in inp and 's' in inp:
    inp.remove('n')
    inp.remove('s')
  elif 'n' in inp:
    if 'sw' in inp:
      inp.remove('n')
      inp[inp.index('sw')] = 'nw'
    elif 'se' in inp:
      inp.remove('n')
      inp[inp.index('se')] = 'ne'
  elif 's' in inp:
    if 'nw' in inp:
      inp.remove('s')
      inp[inp.index('nw')] = 'sw'
    elif 'ne' in inp:
      inp.remove('s')
      inp[inp.index('ne')] = 'se'
  elif 'ne' in inp and 'sw' in inp:
    inp.remove('ne')
    inp.remove('sw')
  elif 'nw' in inp and 'se' in inp:
    inp.remove('nw')
    inp.remove('se')
  else:
    done = True

print(len(inp))