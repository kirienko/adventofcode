import networkx as nx
import matplotlib.pyplot as plt

with open('./test/day_09.txt') as fd:
    raw = fd.read()

data = raw.split('\n')
rows, cols = len(data), len(data[0])
# print(data)
print(rows, cols)

grid = nx.Graph()
# create a grid with values on the nodes
for i in range(rows):
    for j in range(cols):
        grid.add_node(i * cols + j, val=int(data[i][j]))
        if j != cols - 1:
            grid.add_edge(i * cols + j, i * cols + j + 1)
        if i != rows - 1:
            grid.add_edge(i * cols + j, (i + 1) * cols + j)
print(grid)


def min_adj(G: nx.graph, elem: int) -> bool:
    """ True if the point is lower than all its adjacent """
    return G.nodes[elem]['val'] < min(G.nodes[x]['val'] for x in G.neighbors(elem))


risk_level = 0
# basin_dict = nx.Graph()
for i in range(rows):
    for j in range(cols):
        node = i * cols + j
        if min_adj(grid, node):
            risk_level += 1 + grid.nodes[node]['val']

print(f"Answer 1: {risk_level}")
