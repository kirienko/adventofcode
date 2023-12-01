import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

from string import ascii_lowercase as abc


def read(text: str) -> ((nx.MultiDiGraph), int, int, dict):
    """ Create a grid with values on the nodes    """

    data = text.strip().split('\n')
    rows, cols = len(data), len(data[0])
    print(f"Grid size: {rows=}, {cols=}")
    grid = nx.MultiDiGraph()
    pos = {}
    for i in range(rows):
        for j in range(cols):
            node = i * cols + j
            pos[node] = (i, -j)
            # print(f"{data[i][j]=}")
            # val_ij = abc.index(data[i][j])  # 'a' -> 0, ... 'z' -> 27
            if data[i][j] == 'S':
                grid.add_node(node, val=0)
                source = node
            elif data[i][j] == 'E':
                grid.add_node(node, val=26)
                end = node
            else:
                grid.add_node(node, val=abc.index(data[i][j]))
    for i in range(rows):
        for j in range(cols):
            node = i * cols + j
            if j != cols - 1:
                # if grid.nodes[node + 1]['val'] - grid.nodes[node]['val'] in (0, 1):
                if grid.nodes[node + 1]['val'] - grid.nodes[node]['val'] <= 1:
                    grid.add_edge(node, node + 1)
                if grid.nodes[node + 1]['val'] - grid.nodes[node]['val'] >= -1:
                    grid.add_edge(node + 1, node)
            if i != rows - 1:
                if grid.nodes[node + cols]['val'] - grid.nodes[node]['val'] <= 1:
                    grid.add_edge(node, node + cols)
                if grid.nodes[node + cols]['val'] - grid.nodes[node]['val'] >= -1:
                    grid.add_edge(node + cols, node)
    return grid, source, end, pos

def draw_grid(G, pos):
    options = {
        "font_size": 14,
        "node_size": 500,
        "node_color": "white",
        "edgecolors": "black",
        "linewidths": 1,
        "width": 3,
    }
    nx.draw_networkx(G, pos, **options)
    ax = plt.gca()
    plt.show()


def task1(text: str) -> int:
    grid, source, target, pos = read(text)
    print(f"{source=}, {target=}")
    # draw_grid(grid,pos)
    assert nx.has_path(grid, source, target)
    return nx.shortest_path_length(grid, source, target, weight=1, method='bellman-ford')
    # nx.shortest_simple_paths(grid, source=)


def task2(text: str) -> int:
    return 1


if __name__ == "__main__":
    with open('data/day_12.txt') as fd:
        data = fd.read()

    print(task1(data))
    # print(task2(data))
