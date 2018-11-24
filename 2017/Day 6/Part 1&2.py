from aocd import get_data
inp = [int(x) for x in get_data(day=6).split('\t')]
l = inp

prevs = []
tally = 0
while str(l) not in prevs:
    prevs.append(str(l))
    i = l.index(max(l))
    x = l[i]
    l[i] = 0
    while x > 0:
        i += 1
        if i >= len(l):
            i = 0
        l[i] += 1
        x -= 1
    tally += 1
print(tally)

print(tally - prevs.index(str(l)))