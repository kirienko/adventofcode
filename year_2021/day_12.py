import networkx as nx
from matplotlib import pyplot as plt

with open('./test/day_12.txt') as fd:
    data = fd.read().split()

G = nx.Graph()
for line in data:
    a, b =line.split('-')
    G.add_edge(a, b)

# print(G)
# print(G.edges)

# nx.draw_networkx(G)
# plt.show()
# for p in nx.algorithms.all_simple_paths(G, 'start', 'end'):
#     print(p)


def silly_bfs(graph: nx.Graph, start: str, end: str):
    visited = {n: 0 for n in graph.nodes}
    queue = [start]
    visited[start] = 1
    paths = [[start]]
    while queue:
        node = queue.pop()
        print(f"{node}", end='->')
        if node == end:
            continue
        for n in graph.neighbors(node):
            if n.islower() and visited[n] == 1:
                continue
            else:
                paths += [paths[-1] + [node]]
                queue += [n]
                visited[n] = 1
                for p in paths:
                    p += [n]
    return paths

for p in silly_bfs(G, 'start', 'end'):
    print(p)
