import networkx as nx

with open('./data/day_15.txt') as fd:
    data = fd.read().split()

rows, cols = len(data), len(data[0])
print(rows, cols)

grid = nx.Graph()
# create a grid with values on the nodes
N = 5
for i in range(rows * N):
    for j in range(cols * N):
        node = i * cols * N + j
        val_ij = (int(data[i % rows][j % cols]) + i // rows + j // cols) % 9 or 9
        grid.add_node(node, val=val_ij)
        if j != cols * N - 1:
            grid.add_edge(node, node + 1)
        if i != rows * N - 1:
            grid.add_edge(node, node + cols * N)

print(grid)

# add weights to the edges of the existing graph
for v1, v2 in grid.edges:
    grid.remove_edge(v1, v2)
    grid.add_edge(v1, v2, weight=grid.nodes[v1]['val'] + grid.nodes[v2]['val'])


path = nx.algorithms.shortest_path(grid, source=0, target=rows * cols * N * N - 1, weight='weight')
print(sum(grid.nodes[p]['val'] for p in path) - grid.nodes[0]['val'])
