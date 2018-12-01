from aocd import get_data
inp = get_data(day=16, year=2017).split(",")

def spin(l,x):
  return l [-x:] + l [:-x]

def exchange(l, a, b):
  c = l[a]
  l[a] = l[b]
  l[b] = c
  return l

def partner(l, a, b):
  i = l.index(a)
  j = l.index(b)
  c = l[i]
  l[i] = l[j]
  l[j] = c
  return l

def dance(l):
  for c in inp: # Command
    if c[0] == "s":
      l = spin(l,int(c[1:]))
    elif c[0] == "x":
      a,b = [int(x) for x in c[1:].split('/')]
      l = exchange(l, a, b)
    elif c[0] == "p":
      a,b = c[1:].split('/')
      l = partner(l, a, b)
  return l

l = list("abcdefghijklmnop")
x = 0
while l != list("abcdefghijklmnop") or x == 0:
  l = dance(l)
  x += 1

for i in range(1000000000%x):
  l = dance(l)
print(''.join(l))