import time
from aocd import get_data
inp = get_data(day=2, year=2018).split('\n')
start = time.time()

# Part 1
from collections import Counter

tt = [[1 if 2 in c else 0, 1 if 3 in c else 0] for c in (Counter(dict(Counter(row)).values()) for row in inp)]
print(sum([z[0] for z in tt]) * sum([z[1] for z in tt]))

# Part 2
nocd = lambda s1,s2: sum([1 for i in range(len(s1)) if s1[i] != s2[i]]) # Numbers of characters different
i,j = next(k[0] for k in ([[i,j] for j in range(i+1,len(inp)) if nocd(inp[i], inp[j]) == 1] for i in range(len(inp))) if k)
print(''.join([inp[i][x] for x in range(len(inp[i])) if inp[i][x] == inp[j][x]]))

end = time.time()
print(end - start)