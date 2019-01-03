from aocd import get_data
inputstring = get_data(day=2, year=2015)
split1 = inputstring.split()
split2 = [x.split("x") for x in split1]
total = 0
for item in split2:
    side1 = int(item[0]) * int(item[1])
    side2 = int(item[1]) * int(item[2])
    side3 = int(item[2]) * int(item[0])
    paper = (2 * side1) + (2 * side2) + (2 * side3) + min(side1,side2,side3)
    total += paper
print(total)
