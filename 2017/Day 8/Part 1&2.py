from aocd import get_data
inp = get_data(day=8, year=2017).split('\n')

regs = {}
highest = 0
for row in inp:
  # o dec -427 if wnh < -1
  r1, op1, v1, _, r2, op2, v2 = row.split()
  if r1 not in regs:
    regs[r1] = 0
  if r2 not in regs:
    regs[r2] = 0
  if eval(str(regs[r2]) + op2 + v2):
    v1 = int(v1)
    if op1 == "dec":
      v1 = -v1
    regs[r1] += v1
    if regs[r1] > highest:
      highest = regs[r1]
print(max(regs.values())) # Part 1
print(highest) # Part 2