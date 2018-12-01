from aocd import get_data
inp = get_data(day=1).split('\n')

print(sum([int(x) for x in inp]))

seen = []
i = 0
x = 0
while x not in seen:
  # print(x, len(seen))
  seen.append(x)
  x += int(inp[i])
  i += 1
  if i >= len(inp):
    i -= len(inp)
print(x)