from aocd import get_data
inp = get_data(day=1, year=2017)
tot = 0
step = int(len(inp)/2)
for i in range(len(inp)):
    comp = i + step
    if comp >= len(inp): comp -= len(inp)
    if inp[i] == inp[comp]: tot += int(inp[i])
print(tot)
