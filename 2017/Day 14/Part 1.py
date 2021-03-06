from aocd import get_data
inp = get_data(day=14, year=2017)

def xor(l):
  tot = l[0]
  for x in l[1:]:
    tot ^= x
  return tot

def hash(inst): # In string
  ls = [ord(x) for x in inst] + [17, 31, 73, 47, 23] # Lengths
  l = [i for i in range(256)]
  i = 0
  skip = 0

  for q in range(64):
    for length in ls:
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
  out = ""
  for i in range(0,len(l),16):
    out += '%02x' % xor(l[i:i+16])
  return out

def hextobin(h):
  h = int(h,16)
  return f'{h:0>128b}'

used = 0
for i in range(128):
  # print(hextobin(hash("%s-%i" % (inp, i))).replace('0','.').replace('1','#'))
  for char in hextobin(hash("%s-%i" % (inp, i))):
    if char == '1':
      used += 1

print(used)