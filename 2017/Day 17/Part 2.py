from aocd import get_data
inp = int(get_data(day=17, year=2017))

p = 0
x = 0
for i in range(1,50000000+1):
  p += inp
  p %= i
  if p == 0:
    x = i
  p += 1
print(x)