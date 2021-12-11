"""
I decided to leave that fancy colored output here,
just for the future re-usage.
"""
import networkx as nx

with open('./data/day_11.txt') as fd:
    data = fd.read().split()

rows, cols = len(data), len(data[0])


class color:
    # https://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
    GREEN = '\033[92m'
    RED = '\033[91m'
    END = '\033[0m'


def print_grid(G: nx.Graph, nr: int, nc: int):
    for i in range(nr):
        line = ''
        for j in range(nc):
            val = G.nodes[i * nc + j]['val']
            if val in range(1, 9):
                line += str(val)
            elif val == 9:
                line += color.RED + str(val) + color.END
            else:
                line += color.GREEN + '0' + color.END
        print(line)


def if_superflash(G: nx.Graph) -> bool:
    return not any(G.nodes[n]['val'] for n in G.nodes)


grid = nx.Graph()
# create a grid with values on the nodes
for i in range(rows):
    for j in range(cols):
        node = i * cols + j
        val_ij = int(data[i][j])
        grid.add_node(node, val=val_ij)
        if j != cols - 1:   # horizontal edges
            grid.add_edge(node, node + 1)
        if i != rows - 1:   # vertical edges
            grid.add_edge(node, node + cols)
            if j != cols - 1:   # diagonal edges
                grid.add_edge(node, node + cols + 1)
                grid.add_edge(node + cols, node + 1)

print(grid)
print_grid(grid, rows, cols)

flashes = 0
for step in range(1000):
    ready_to_flash = set()
    for node in grid.nodes:
        # increase each node value by 1:
        grid.nodes[node]['val'] += 1
        if grid.nodes[node]['val'] > 9:
            ready_to_flash.add(node)
    flashed = set()     # set of nodes that have fired already
    while ready_to_flash:
        node = ready_to_flash.pop()
        flashed.add(node)
        for n in grid.neighbors(node):
            grid.nodes[n]['val'] += 1
            if grid.nodes[n]['val'] > 9 and n not in flashed:
                ready_to_flash.add(n)
    for node in grid.nodes:
        # zeroing flashed nodes
        if grid.nodes[node]['val'] > 9:
            grid.nodes[node]['val'] = 0
            if step < 100:
                flashes += 1
    if step + 1 in (1, 2, 3, 4, 5, 10, 20, 30, 90, 100):
        print(f"\nAfter step {step + 1}:")
        print_grid(grid, rows, cols)
    if if_superflash(grid):
        break

print(f"Answer 1: {flashes}")
print(f"Answer 2: {step + 1}")
