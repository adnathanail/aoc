from aocd import get_data
inp = list(get_data(day=10).encode()) + [17, 31, 73, 47, 23]

l = [i for i in range(256)]
i = 0
skip = 0

for q in range(64):
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

def xor(l):
  tot = l[0]
  for x in l[1:]:
    tot ^= x
  return tot

out = ""
for i in range(0,len(l),16):
  out += '%02x' % xor(l[i:i+16])
print(out)