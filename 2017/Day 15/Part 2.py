from aocd import get_data
inp = get_data(day=15, year=2017)

a,b = [int(x[24:]) for x in inp.split('\n')]

def judge(a,b):
  return f'{a:0>32b}'[16:] == f'{b:0>32b}'[16:]

judged = 0
x = 0
while judged < 5000000:
  if a % 4: # If a is not divisble by 4, because if it is then % will return 0 which is falsy
    a *= 16807
    a %= 2147483647
  if b % 8:
    b *= 48271
    b %= 2147483647
  if (not a % 4) and (not b % 8):
    judged += 1
    if judge(a,b):
      x += 1
    a *= 16807
    a %= 2147483647
    b *= 48271
    b %= 2147483647
print(x)