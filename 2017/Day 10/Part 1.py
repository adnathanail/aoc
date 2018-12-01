from aocd import get_data
inp = [int(x) for x in get_data(day=10, year=2017).split(',')]

l = [i for i in range(256)]
i = 0
skip = 0

for length in inp:
  if (i + length-1) < len(l):
    s = l[i:i+length]
    s.reverse()
    l[i:i+length] = s
  else:
    j = len(l) - i # Number of elements from i to end of list inclusive
    s = l[i:] + l[:length - j]
    s.reverse()
    l[-j:] = s[:j]
    l[:length-j] = s[j:]
  i += length + skip
  skip += 1
  while i >= len(l):
    i -= len(l)

print(l[0]*l[1])
