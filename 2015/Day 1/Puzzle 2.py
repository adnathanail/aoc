from aocd import get_data
inputstring = get_data(day=1, year=2015)
index = 0
count = 0
for char in inputstring:
    index +=1
    if char == "(":
        count += 1
    else:
        count -= 1
    if count <= -1:
        break
print(index)
