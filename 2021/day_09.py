import networkx as nx

with open('./data/day_09.txt') as fd:
    raw = fd.read()

data = raw.split('\n')
rows, cols = len(data), len(data[0])

grid = nx.Graph()
# create a grid with values on the nodes
for i in range(rows):
    for j in range(cols):
        node = i * cols + j
        val_ij = int(data[i][j])
        grid.add_node(node, val=val_ij)
        if j != cols - 1:
            grid.add_edge(node, node + 1)
        if i != rows - 1:
            grid.add_edge(node, node + cols)


def min_adj(G: nx.graph, elem: int) -> bool:
    """ True if the point is lower than all its adjacent """
    return G.nodes[elem]['val'] < min(G.nodes[x]['val'] for x in G.neighbors(elem))

risk_level = 0
for i in range(rows):
    for j in range(cols):
        node = i * cols + j
        if min_adj(grid, node):
            risk_level += 1 + grid.nodes[node]['val']

print(f"Answer 1: {risk_level}")

""" This solution exploits a particular property of the basins' generation algorithm:
_all_ nodes with values less than 9 belong to a basin. This observation was made
from [this insanely beautiful visualisation](https://static.aperiodic.net/aoc/2021/09.png), 
from [reddit](https://www.reddit.com/r/adventofcode/comments/rcszzx/2021_day_9_cave_floor_relief_map/).
That means that if we simply remove the nines from the grid and then count the connected components,
it will deliver the answer!
"""
basins = grid.copy()
for n in grid.nodes:
    if basins.nodes[n]["val"] == 9:
        basins.remove_node(n)

bas_sizes = [len(graph) for graph in nx.algorithms.connected_components(basins)]
a, b, c = sorted(bas_sizes, reverse=True)[:3]
print(f"Answer 2: {a*b*c} = {a} x {b} x {c}")
