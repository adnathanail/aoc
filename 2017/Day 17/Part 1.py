inp = 301
l = [0]
p = 0
for i in range(1,2017+1):
  p += inp
  while p >= len(l):
    p -= len(l)
  l.insert(p+1,i)
  p += 1
print(l[p+1])