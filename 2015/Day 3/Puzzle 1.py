from aocd import get_data
inputstring = get_data(day=3, year=2015)
x=0
y=0
coords = [[0,0]]
for char in inputstring:
    if char == "^":
        y += 1
    elif char == "v":
        y -= 1
    elif char == ">":
        x += 1
    else:
        x -= 1
    coords.append([x,y])
newcoords = []
for coord in coords:
    if coord not in newcoords:
        newcoords.append(coord)
print(len(newcoords))
