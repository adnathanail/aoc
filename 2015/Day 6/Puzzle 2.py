from aocd import get_data
inputstring = get_data(day=6, year=2015)
split = inputstring.split("\n")
grid = []
for i in range(1000):
    temp = []
    for i in range(1000):
        temp.append(0)
    grid.append(temp)
for line in split:
    linesplit = line.split()
    firstpoint = [int(x) for x in linesplit[-3].split(",")]
    lastpoint = [int(x) for x in linesplit[-1].split(",")]
    if linesplit[0] == "turn":
        if linesplit[1] == "on":
            for i in range(firstpoint[0],lastpoint[0]+1):
                for j in range(firstpoint[1],lastpoint[1]+1):
                    grid[i][j] += 1
        elif linesplit[1] == "off":
            for i in range(firstpoint[0],lastpoint[0]+1):
                for j in range(firstpoint[1],lastpoint[1]+1):
                    grid[i][j] -= 1
                    if grid[i][j] < 0:
                        grid[i][j] = 0
    elif linesplit[0] == "toggle":
        for i in range(firstpoint[0],lastpoint[0]+1):
            for j in range(firstpoint[1],lastpoint[1]+1):
                grid[i][j] += 2

total = 0
for rows in grid:
    total += sum(rows)
print(total)
