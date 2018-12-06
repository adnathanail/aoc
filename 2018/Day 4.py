import time
from aocd import get_data
inp = get_data(day=4, year=2018).split('\n')
start = time.time()

import datetime, operator, re

inp = sorted(inp, key = lambda x: re.match(r"\[1518\-(\d+)\-(\d+) (\d+):(\d+).*", x).groups()) # Sort by month, date, hour, minute
guards = {}
for row in inp:
  if "Guard" in row:
    current_guard = re.match(".*#(\d+).*",row).groups()[0]
  else:
    dt = datetime.datetime.strptime(re.match('\[(.*)\].*', row).groups()[0], '%Y-%m-%d %H:%M')
    if 'falls asleep' in row:
      fallen_asleep = dt
    else:
      if current_guard not in guards:
        guards[current_guard] = {}
      m = fallen_asleep.minute
      for i in range(m, m+int((dt-fallen_asleep).seconds/60)):
        if i not in guards[current_guard]:
          guards[current_guard][i] = 0
        guards[current_guard][i] += 1

# Part 1
tots = {g:sum(guards[g].values()) for g in guards} # Total sleeping times for each guard
sg = max(tots.items(), key=operator.itemgetter(1))[0] # Sleepiest guard
sgst = max(guards[sg].items(), key=operator.itemgetter(1))[0] # Sleepiest guard sleepiest time
print(int(sg) * int(sgst))

# Part 2
mhfeg = {} # Max hours for each guard
for gid in guards:
  mhfeg[gid] = max(guards[gid].values())
gwmh = max(mhfeg.items(), key=operator.itemgetter(1))[0] # Guard with max hours
print(max(guards[gwmh].items(), key=operator.itemgetter(1))[0] * int(gwmh))

end = time.time()
print(end - start)