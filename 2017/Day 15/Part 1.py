from aocd import get_data
inp = get_data(day=15, year=2017)

a,b = [int(x[24:]) for x in inp.split('\n')]
x = 0
for i in range(40000000):
  a *= 16807
  a %= 2147483647
  b *= 48271
  b %= 2147483647
  if f'{a:0>32b}'[16:] == f'{b:0>32b}'[16:]:
    x += 1
print(x)