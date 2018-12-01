from aocd import get_data
inp = []
for p in get_data(day=7, year=2017).split('\n'):
    n = p.split(" ")[0]
    w = int(p.split("(")[1].split(")")[0])
    try:
        c = p.split(" -> ")[1].split(", ")
    except IndexError:
        c = []
    inp.append([n, w, c])

ps = []
for p in inp:
    ps = ps + p[2]
for p in inp:
    if p[0] in ps:
        ps.remove(p[0])
    else:
        print(p[0])