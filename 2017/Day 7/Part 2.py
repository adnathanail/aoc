from aocd import get_data
inp = {}
for p in get_data(day=7, year=2017).split('\n'):
    n = p.split(" ")[0]
    w = int(p.split("(")[1].split(")")[0])
    try:
        c = p.split(" -> ")[1].split(", ")
    except IndexError:
        c = []
    inp[n] = [w, c]

def getWeight(pid):
    p = inp[pid]
    if len(p[1]) == 0:
        return p[0]
    else:
        ws = [getWeight(x) for x in p[1]]
        if len(set(ws)) > 1:
            wp = p[1][ws.index(min(set(ws), key=ws.count))] # Program with incorrect weight
            bv = max(set(ws), key=ws.count) # Best value
            wv = min(set(ws), key=ws.count) # Worst value
            print(inp[wp][0] + (bv - wv)) # Add the diff between best and worst to incorrect weight
            for i in range(len(ws)):
                ws[i] = max(set(ws), key=ws.count)
        return sum(ws) + p[0]

getWeight('fbgguv') # From part 1