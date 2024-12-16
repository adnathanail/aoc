import math
from aocd.models import Puzzle
import networkx as nx

puzzle = Puzzle(year=2024, day=16)
input_data = puzzle.input_data

grid = input_data.split("\n")


def find_char(char):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == char:
                return (j, i)
    raise Exception(f"Couldn't find '{char}'")


OPPOS = (("U", "D"), ("L", "R"))


def build_graph():

    G = nx.Graph()

    start_vec = (find_char("S"), "R")
    end_pos = find_char("E")

    G.add_node(start_vec)

    added = set()
    adding = [start_vec]

    while adding:
        s = adding.pop(0)

        if s in added:
            continue
        added.add(s)

        dirs = {
            "R": (s[0][0] + 1, s[0][1]),
            "D": (s[0][0], s[0][1] + 1),
            "L": (s[0][0] - 1, s[0][1]),
            "U": (s[0][0], s[0][1] - 1),
        }
        s_next_no_turn = dirs[s[1]]
        if grid[s_next_no_turn[1]][s_next_no_turn[0]] in [".", "E"]:
            G.add_node((s_next_no_turn, s[1]))
            G.add_edge(s, (s_next_no_turn, s[1]), weight=1)
            adding.append((s_next_no_turn, s[1]))

        for ddir in dirs:
            if ddir == s[1] or (ddir, s[1]) in OPPOS or (s[1], ddir) in OPPOS:
                continue
            ddir_next = dirs[ddir]
            if grid[ddir_next[1]][ddir_next[0]] in [".", "E"]:
                G.add_node((s[0], ddir))
                G.add_edge(s, (s[0], ddir), weight=1000)
                adding.append((s[0], ddir))

    G.add_node(end_pos)
    G.add_edge((end_pos, "R"), end_pos, weight=0)
    G.add_edge((end_pos, "U"), end_pos, weight=0)
    G.add_edge((end_pos, "D"), end_pos, weight=0)
    G.add_edge((end_pos, "L"), end_pos, weight=0)

    return G, start_vec, end_pos


gra, st, en = build_graph()


def build_dists_dict(focus):
    visited = set()
    to_visit = [focus]
    dists = {focus: 0}
    while to_visit:
        from_node = None
        from_node_dist = math.inf
        for node in to_visit:
            if dists[node] < from_node_dist:
                from_node = node
                from_node_dist = dists[node]
        to_visit.remove(from_node)
        for to_node in nx.all_neighbors(gra, from_node):
            if to_node not in dists:
                dists[to_node] = math.inf
            dists[to_node] = min(dists[to_node], dists[from_node] + nx.path_weight(gra, [from_node, to_node], weight="weight"))
            if to_node not in visited and to_node not in to_visit:
                to_visit.append(to_node)
        visited.add(from_node)
    return dists


st_dists = build_dists_dict(st)
en_dists = build_dists_dict(en)


points = set()
target_length = nx.shortest_path_length(gra, st, en, "weight")
i = 0
for node in gra.nodes:
    if type(node[0]) is not tuple:
        continue
    node_via = st_dists[node] + en_dists[node]
    if node_via == target_length:
        points.add(node[0])
    i += 1

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if (j, i) in points:
#             print("O", end="")
#         else:
#             print(grid[i][j], end="")
#     print()


print(len(points))
