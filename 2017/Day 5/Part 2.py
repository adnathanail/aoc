from aocd import get_data
inp = [int(x) for x in get_data(day=5, year=2017).split('\n')]
l = inp

i = 0
tally = 0
while i >= 0 and i < len(l):
    newi = i + l[i]
    if l[i] >= 3:
        l[i] -= 1
    else:
        l[i] += 1
    i = newi
    tally += 1
print(tally)
