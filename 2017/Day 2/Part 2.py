from aocd import get_data
inp = get_data(day=2)
tot = 0
for row in inp.split("\n"):
    procrow = [int(x) for x in row.split("\t")]
    for i in range(len(procrow)):
        for j in range(i+1,len(procrow)):
            if procrow[i] % procrow[j] == 0:
                tot += int(procrow[i] / procrow[j])
            elif procrow[j] % procrow[i] == 0:
                tot += int(procrow[j] / procrow[i])
print(tot)