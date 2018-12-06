import time
from aocd import get_data
inp = get_data(day=5, year=2018)
start = time.time()

import re
s = ""
for l in "abcdefghijklmnopqrstuvwxyz":
  s += l+l.upper() + "|" + l.upper()+l + "|"
rx = "(" + s[:-1] + ")+" # (aA|Aa|bB|Bb|cC|Cc|dD|Dd|eE|Ee|fF|Ff|gG|Gg|hH|Hh|iI|Ii|jJ|Jj|kK|Kk|lL|Ll|mM|Mm|nN|Nn|oO|Oo|pP|Pp|qQ|Qq|rR|Rr|sS|Ss|tT|Tt|uU|Uu|vV|Vv|wW|Ww|xX|Xx|yY|Yy|zZ|Zz)+

def lorp(pol): # Length of reacted polymer
  repd = 1 # Anything been replaced this run?
  while repd:
    pol, repd = re.subn(rx,"",pol)
  return len(pol)

# Part 1
print(lorp(inp))

# Part 2
bl = 0 # Best length
bc = "" # Best character
for char in set([x.lower() for x in set(inp)]):
  l = lorp(re.sub("(" + char + "|" + char.upper() + ")+","",inp))
  if l > bl:
    bl = l
    bc = char
print(bl)

end = time.time()
print(end - start)