from aocd import get_data
inputstring = get_data(day=3, year=2015)
santa = ""
robotsanta = ""
index = 0
for char in inputstring:
    index += 1
    if not index % 2:
        santa += char
    else:
        robotsanta += char
def countHouses(inputstring):
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
    return coords
coords = countHouses(santa) + countHouses(robotsanta)
newcoords = []
for coord in coords:
    if coord not in newcoords:
        newcoords.append(coord)
print(len(newcoords))
