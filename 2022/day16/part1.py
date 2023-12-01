import re

from aocd.models import Puzzle  # type: ignore[import]
import networkx as nx
import matplotlib.pyplot as plt


def dfs(g, node, visited=None):
    print(visited)
    if visited is None:
        visited = []
    visited.append(node)
    for n in g.adj[node]:
        if n not in visited:
            dfs(g, n, visited)
    return visited


def main() -> None:
    puzzle = Puzzle(year=2022, day=16)

    inp = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II"""
    # inp = puzzle.input_data

    patt = re.compile(
        r"Valve (\w\w) has flow rate=(\d+); tunnels? leads? to valves? ((?:\w\w, )*\w\w)"
    )

    G = nx.Graph()

    for row in inp.split("\n"):
        valve, flow_rate, tunnels = re.match(patt, row).groups()
        for tunnel in tunnels.split(", "):
            G.add_edge(valve, tunnel)

    print(len(G.nodes))

    dfs(G, "AA")

    nx.draw(G, with_labels=True, font_weight='bold')
    plt.savefig("graph.png")


if __name__ == "__main__":
    main()
