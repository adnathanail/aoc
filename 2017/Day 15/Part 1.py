inp = """Generator A starts with 883
Generator B starts with 879"""
a,b = [int(x[24:]) for x in inp.split('\n')]
# a,b = 65,8921
x = 0
for i in range(40000000):
  a *= 16807
  a %= 2147483647
  b *= 48271
  b %= 2147483647
  if f'{a:0>32b}'[16:] == f'{b:0>32b}'[16:]:
    x += 1
print(x)