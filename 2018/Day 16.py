import time
from aocd import get_data
inp = get_data(day=16, year=2018).split('\n')
start = time.time()

bef = []
ins = ""
aft = []
lowb = False # Last one was blank
rd = False # Runs done

runs = []
testp = []
for row in inp:
  if not rd:
    try:
      if row[0] == "B":
        bef = [int(e) for e in row[9:19].split(', ')]
      elif row[0] in [str(q) for q in range(10)]:
        ins = row
      elif row[0] == "A":
        aft = [int(e) for e in row[9:19].split(', ')]
    except:
      if lowb:
        rd = True
      else:
        lowb = True
        runs.append([bef, ins, aft])
        continue
    lowb = False # Will not get here if was blank because either break-ed or continue-ed
  else:
    testp.append(row)

addr = lambda A, B, regs: regs[A] + regs[B]
addi = lambda A, B, regs: regs[A] + B
mulr = lambda A, B, regs: regs[A] * regs[B]
muli = lambda A, B, regs: regs[A] * B
banr = lambda A, B, regs: regs[A] & regs[B]
bani = lambda A, B, regs: regs[A] & B
borr = lambda A, B, regs: regs[A] | regs[B]
bori = lambda A, B, regs: regs[A] | B
setr = lambda A, B, regs: regs[A]
seti = lambda A, B, regs: A
gtir = lambda A, B, regs: 1 if A > regs[B] else 0
gtri = lambda A, B, regs: 1 if regs[A] > B else 0
gtrr = lambda A, B, regs: 1 if regs[A] > regs[B] else 0
eqir = lambda A, B, regs: 1 if A == regs[B] else 0
eqri = lambda A, B, regs: 1 if regs[A] == B else 0
eqrr = lambda A, B, regs: 1 if regs[A] == regs[B] else 0

ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

# Part 1
def noos(before, instruction, after): # Number of opcodes
  _, A, B, C = [int(x) for x in instruction.split()]
  z = 0
  for op in ops:
    tem = before[:]
    # print(A, B, tem)
    tem[C] = op(A, B, tem)
    if tem == after:
      z += 1
  return z

n = 0
for r in runs:
  if noos(r[0], r[1], r[2]) >= 3:
    n += 1
print(n)

# Part 2

end = time.time()
print(end - start)
