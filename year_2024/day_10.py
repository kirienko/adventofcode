import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def parse_map(text: str):
    lines = text.strip().split("\n")
    matrix = np.array(
        [[int(char) for char in line]
            for line in lines])

    rows, cols = matrix.shape   # dimensions
    assert rows == cols         # it's a square grid
    n = rows

    graph = nx.DiGraph()

    for i in range(rows):
        for j in range(cols):
            current_value = matrix[i, j]

            neighbors = [
                (i - 1, j),  # Up
                (i + 1, j),  # Down
                (i, j - 1),  # Left
                (i, j + 1)   # Right
            ]

            for ni, nj in neighbors:
                if 0 <= ni < rows and 0 <= nj < cols:  # Check boundaries
                    neighbor_value = matrix[ni, nj]
                    if neighbor_value == current_value + 1:
                        # Add directed edge if the neighbor's value is exactly one greater
                        graph.add_edge((i, j), (ni, nj))

    start_nodes = [(i, j) for i in range(n) for j in range(n) if matrix[i, j] == 0]
    end_nodes = [(i, j) for i in range(n) for j in range(n) if matrix[i, j] == 9]

    return graph, matrix, start_nodes, end_nodes


def part_1(graph: nx.DiGraph, start_nodes, end_nodes) -> int:
    reachable = {}
    for start in start_nodes:
        reachable_from_start = set()
        for end in end_nodes:
            if nx.has_path(graph, source=start, target=end):
                reachable_from_start.add(end)
        reachable[start] = len(reachable_from_start)
    return sum(v for v in reachable.values())

def part_2(graph: nx.DiGraph, start_nodes, end_nodes) -> int:
    all_paths = []
    for start in start_nodes:
        for end in end_nodes:
            paths = list(nx.all_simple_paths(graph, source=start, target=end))
            all_paths.extend(paths)

    return len(all_paths)

def visualise(graph: nx.DiGraph, matrix) -> None:
    rows, cols = matrix.shape
    pos = {(i, j): (j, -i) for i in range(rows) for j in range(cols)}
    labels = {(i, j): str(matrix[i, j]) for i in range(rows) for j in range(cols)}  # Use original one-digit labels
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=500, font_size=8, font_color="black", arrowsize=10)
    plt.show()


if __name__ == "__main__":
    with open('data/data_10.txt') as f:
        data = f.read()

    G, _, start, end = parse_map(data)
    print(part_1(G, start, end))
    print(part_2(G, start, end))
