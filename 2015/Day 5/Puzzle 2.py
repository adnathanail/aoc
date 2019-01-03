from aocd import get_data
inputstring = get_data(day=5, year=2015)
split = inputstring.split()
nicecount = 0
for line in split:
    doubledouble = False
    for i in range(len(line)-1):
        if line.count(line[i:i+2]) > 1:
            doubledouble = True
            break
    doubleinmiddle = False
    for i in range(len(line)-2):
        if line[i:i+3][0] == line[i:i+3][2]:
            doubleinmiddle = True
            break
    if doubledouble and doubleinmiddle:
        nicecount += 1
print(nicecount)
