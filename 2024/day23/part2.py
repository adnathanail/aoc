from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=23)
input_data = puzzle.input_data
cons_list = input_data.splitlines()


nodes = set()
edge_lookup = {}

clique_3 = []
for con in cons_list:
    f, t = con.split("-")
    nodes.add(f)
    nodes.add(t)
    if f not in edge_lookup:
        edge_lookup[f] = set()
    edge_lookup[f].add(t)
    if t not in edge_lookup:
        edge_lookup[t] = set()
    edge_lookup[t].add(f)
    for inter in edge_lookup[f].intersection(edge_lookup[t]):
        clique_3.append((f, t, inter))


n = 3
clique_n = clique_3
while clique_n is None or len(clique_n) > 0:
    clique_nm_1 = clique_n
    clique_n = set()
    for cl in clique_nm_1:
        for node in nodes:
            if all(cln in edge_lookup[node] for cln in cl):
                clique_n.add(tuple(sorted(cl + (node,))))
    n += 1

print(",".join(sorted(list(clique_nm_1)[0])))
