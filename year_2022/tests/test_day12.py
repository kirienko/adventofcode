import networkx as nx
import matplotlib.pyplot as plt
from year_2022.day_12 import read, draw_grid ,task1, task2

test_data = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""

def test_read(text=test_data):
    grid, source, end, pos = read(text)
    # for node in grid.nodes:
    #     if node == source: print("S:", end=' ')
    #     elif node == end: print("E:", end=' ')
    #     print(f"{node=}, {grid.nodes[node]['val']}")
    # for edge in grid.edges:
    #     print(edge)
    assert nx.has_path(grid, source, end)
    draw_grid(grid, pos)


def test_task1(data=test_data):
    expected = 31
    assert task1(data) == expected


# def test_task2(data=test_data):
#     expected = 2713310158
#     assert task2(data) == expected
