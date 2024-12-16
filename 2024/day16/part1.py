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


G = nx.Graph()

start_vec = (find_char("S"), "R")
end_pos = find_char("E")

G.add_node(start_vec)

added = set()

adding = [start_vec]

oppos = (("U", "D"), ("L", "R"))

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
        if ddir == s[1] or (ddir, s[1]) in oppos or (s[1], ddir) in oppos:
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


print(nx.shortest_path_length(G, start_vec, end_pos, "weight"))
